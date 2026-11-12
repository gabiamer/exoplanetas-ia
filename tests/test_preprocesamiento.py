import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from preprocesamiento import (N_MEDICIONES, espectro_fourier, limpiar_curvas,  # noqa: E402
                              preparar, recodificar_etiqueta)

rng = np.random.default_rng(0)


def curva_con_transitos(periodo=400, profundidad=50.0):
    t = np.arange(N_MEDICIONES)
    x = 1000 + 30 * np.sin(t / 500) + rng.normal(0, 2, N_MEDICIONES)
    x[(t % periodo) < 6] -= profundidad
    return x


def test_recodificar_etiqueta():
    assert recodificar_etiqueta([2, 1, 1, 2]).tolist() == [1, 0, 0, 1]


def test_formas_de_salida():
    X = np.stack([curva_con_transitos() for _ in range(4)])
    Z, F = preparar(X)
    assert Z.shape == (4, N_MEDICIONES)
    assert F.shape == (4, N_MEDICIONES // 2)


def test_curva_limpia_normalizada():
    Z = limpiar_curvas(curva_con_transitos())
    assert abs(Z.mean()) < 1e-3
    assert abs(Z.std() - 1) < 1e-2


def test_cada_estrella_se_procesa_por_separado():
    """El resultado de una estrella no depende de las demás (sin fuga de datos)."""
    a, b = curva_con_transitos(), curva_con_transitos(periodo=250) * 1e4
    solo = limpiar_curvas(a)
    juntas = limpiar_curvas(np.stack([a, b]))
    np.testing.assert_allclose(solo[0], juntas[0], atol=1e-5)


def test_los_transitos_siguen_siendo_caidas():
    t = np.arange(N_MEDICIONES)
    Z = limpiar_curvas(curva_con_transitos())[0]
    assert Z[(t % 400) < 6].mean() < -2


def test_espectro_entre_0_y_1():
    F = espectro_fourier(limpiar_curvas(curva_con_transitos()))
    assert F.min() >= 0 and np.isclose(F.max(), 1, atol=1e-5)


def test_rechaza_longitud_incorrecta():
    with pytest.raises(ValueError):
        limpiar_curvas(np.zeros((1, 100)))


def test_rechaza_valores_vacios():
    x = curva_con_transitos()
    x[10] = np.nan
    with pytest.raises(ValueError):
        limpiar_curvas(x)
