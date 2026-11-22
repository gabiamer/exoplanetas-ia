# Detección de exoplanetas con IA

Sistema inteligente que predice si una estrella tiene un exoplaneta a partir de su **curva de luz** (brillo en el tiempo), usando datos reales del telescopio espacial Kepler de la NASA.

Proyecto final de la materia **Taller de Sistemas Inteligentes** — 8vo semestre de Ingeniería de Sistemas.

El proyecto se divide en tres repositorios:

| Repositorio | Contenido |
|---|---|
| **exoplanetas-ia** (este) | Entrenamiento del modelo: notebooks de las fases 1 a 4 de CRISP-ML(Q) y módulo de preprocesamiento |
| [exoplanetas-api](https://github.com/gabiamer/exoplanetas-api) | Servicio de IA: API REST, base de datos y modelo en producción (fases 5 y 6) |
| [exoplanetas-web](https://github.com/gabiamer/exoplanetas-web) | Aplicación web que consume todos los endpoints del servicio |

## Problema

Cuando un planeta pasa delante de su estrella, el brillo baja un poco y de forma periódica (método de tránsito). El modelo aprende a reconocer ese patrón.

- **Tipo de tarea:** aprendizaje supervisado, clasificación binaria (1 = tiene planeta, 0 = no tiene).
- **Dataset:** [Kepler Labelled Time Series Data](https://www.kaggle.com/datasets/keplersmachines/kepler-labelled-time-series-data). Tiene 5.087 estrellas de entrenamiento (37 con planeta) y 570 de prueba (5 con planeta), con 3.197 mediciones de brillo cada una.
- **Criterios de éxito:** recall ≥ 0,8 y F1 ≥ 0,6 en la clase "con planeta".
- **Metodología:** CRISP-ML(Q).

## Estructura del repositorio

```
exoplanetas-ia/
├── data/          Datos (no se suben a Git; ver data/README.md)
├── notebooks/     Análisis exploratorio, preparación y entrenamiento
├── src/           Código reutilizable (preprocesamiento, modelo)
├── tests/         Pruebas automáticas
├── models/        Modelo final exportado (modelo_v1.ubj + métricas en modelo_v1.json)
└── docs/          Cronograma, resultados y documentación
```

## Avance (CRISP-ML(Q))

| Fase | Fechas | Estado |
|---|---|---|
| 1. Comprensión del negocio y de los datos | 10 nov | Completa |
| 2. Preparación de datos | 11 – 13 nov | Completa |
| 3. Ingeniería del modelo | 14 – 17 nov | Completa: XGBoost con profundidad 2, AP 0,74 en validación cruzada |
| 4. Evaluación del modelo | 18 – 19 nov | Completa: recall 0,80, precisión 0,67 y F1 0,73 en exoTest |
| 5. Despliegue: backend, API REST y frontend | 19 – 21 nov | En [exoplanetas-api](https://github.com/gabiamer/exoplanetas-api) y [exoplanetas-web](https://github.com/gabiamer/exoplanetas-web) |
| 6. Monitoreo y mantenimiento | 21 – 22 nov | En exoplanetas-api: historial, métricas en uso, reentrenamiento y rollback |
| Presentación | 23 nov | Pendiente |

El detalle está en [docs/cronograma.md](docs/cronograma.md).

## Notebooks

| Notebook | Fases | Contenido |
|---|---|---|
| `01_exploracion_y_preparacion.ipynb` | 1 y 2 | Ficha del problema, análisis exploratorio y pipeline de limpieza |
| `02_modelado.ipynb` | 2 (cierre) y 3 | Validación de parámetros y comparación de 4 modelos con validación cruzada |
| `03_ajuste_y_evaluacion.ipynb` | 3 (cierre) y 4 | Ajuste de XGBoost, elección del umbral, evaluación en exoTest y exportación del modelo |

## Modelo final

| | Validación cruzada | Prueba (exoTest) |
|---|---|---|
| Recall | 0,68 | 0,80 (4 de 5 planetas) |
| Precisión | 0,78 | 0,67 |
| F1 | 0,72 | 0,73 |
| AP | 0,74 | 0,67 |

XGBoost (400 árboles, profundidad 2) sobre el espectro de Fourier de la curva limpia, con umbral de decisión 0,10. El modelo se exporta a `models/modelo_v1.ubj` y se usa en [exoplanetas-api](https://github.com/gabiamer/exoplanetas-api).

## Cómo ejecutarlo

```bash
pip install -r requirements.txt
pytest                     # pruebas del preprocesamiento
```

Los notebooks se pueden abrir directamente en Google Colab: descargan el dataset de Kaggle con `kagglehub`.

## Control de versiones

- `main`: versiones estables, una por fase terminada (con etiqueta, por ejemplo `fase-1`).
- `develop`: integración del trabajo en curso.
- `feature/<nombre>`: una rama por tarea, que se une a `develop` al terminarla.
- Los commits siguen el formato *Conventional Commits*: `feat:`, `fix:`, `docs:`, `test:`, `chore:`.
