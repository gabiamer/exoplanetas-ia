"""Preprocesamiento de curvas de luz de Kepler.

Cada función procesa cada estrella (fila) por separado y no aprende parámetros
del conjunto de datos. Por eso se puede aplicar igual al entrenamiento, a la prueba
y a cada curva que llegue por la API, sin fuga de datos.
"""
import numpy as np
from scipy.ndimage import gaussian_filter1d, median_filter

N_MEDICIONES = 3197


def recodificar_etiqueta(label):
    """LABEL original (2 = con planeta, 1 = sin planeta) -> 1 / 0."""
    return (np.asarray(label) == 2).astype(int)


def limpiar_curvas(X, recorte=3.0, ventana=101, sigma=2):
    """Limpia un arreglo de curvas de forma (n_estrellas, 3197).

    1. Normaliza cada curva (media 0, desviación 1).
    2. Recorta los picos hacia arriba (los tránsitos son caídas, no subidas).
    3. Quita la tendencia lenta restando una mediana móvil.
    4. Suaviza con un filtro gaussiano.
    5. Vuelve a normalizar.
    """
    X = np.atleast_2d(np.asarray(X, dtype=np.float64))
    if X.shape[1] != N_MEDICIONES:
        raise ValueError(f"Cada curva debe tener {N_MEDICIONES} mediciones; llegaron {X.shape[1]}.")
    if not np.isfinite(X).all():
        raise ValueError("La curva contiene valores vacíos o infinitos.")
    Z = (X - X.mean(1, keepdims=True)) / (X.std(1, keepdims=True) + 1e-8)
    Z = np.minimum(Z, recorte)
    Z = Z - median_filter(Z, size=(1, ventana), mode="nearest")
    Z = gaussian_filter1d(Z, sigma=sigma, axis=1)
    Z = (Z - Z.mean(1, keepdims=True)) / (Z.std(1, keepdims=True) + 1e-8)
    return Z.astype(np.float32)


def espectro_fourier(Z):
    """Magnitud del espectro de Fourier de cada curva, sin la componente constante,
    normalizada por estrella. Devuelve (n_estrellas, 1598)."""
    F = np.abs(np.fft.rfft(Z, axis=1))[:, 1:]
    return (F / (F.max(1, keepdims=True) + 1e-8)).astype(np.float32)


def preparar(X):
    """Pipeline completo: curvas crudas -> (curvas limpias, espectro de Fourier)."""
    Z = limpiar_curvas(X)
    return Z, espectro_fourier(Z)
