# Detección de exoplanetas con IA

Sistema inteligente que predice si una estrella tiene un exoplaneta a partir de su **curva de luz** (brillo en el tiempo), usando datos reales del telescopio espacial Kepler de la NASA.

Proyecto final de la materia **Taller de Sistemas Inteligentes** — 8vo semestre de Ingeniería de Sistemas.

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
├── models/        Modelos entrenados (no se suben a Git)
├── backend/       API REST para predicciones e historial
├── frontend/      Interfaz web
└── docs/          Cronograma y documentación
```

## Avance (CRISP-ML(Q))

| Fase | Fechas | Estado |
|---|---|---|
| 1. Comprensión del negocio y de los datos | 10 nov | Completa |
| 2. Preparación de datos | 11 – 13 nov | En curso |
| 3. Ingeniería del modelo | 14 – 17 nov | Pendiente |
| 4. Evaluación del modelo | 18 – 19 nov | Pendiente |
| 5. Despliegue: backend, API REST y frontend | 19 – 21 nov | Pendiente |
| 6. Monitoreo y mantenimiento | 21 – 22 nov | Pendiente |
| Presentación | 23 nov | Pendiente |

El detalle está en [docs/cronograma.md](docs/cronograma.md).

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
