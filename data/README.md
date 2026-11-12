# Datos

Los CSV no se suben al repositorio: `exoTrain.csv` pesa unos 260 MB y GitHub no acepta archivos de más de 100 MB.

**Origen:** [Kepler Labelled Time Series Data (Kaggle)](https://www.kaggle.com/datasets/keplersmachines/kepler-labelled-time-series-data)

**Descarga automática:**

```python
import kagglehub
ruta = kagglehub.dataset_download('keplersmachines/kepler-labelled-time-series-data')
```

**Descarga manual:** baja el ZIP desde Kaggle y coloca `exoTrain.csv` y `exoTest.csv` en esta carpeta.

| Archivo | Estrellas | Con planeta |
|---|---|---|
| exoTrain.csv | 5.087 | 37 |
| exoTest.csv | 570 | 5 |
