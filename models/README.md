# Modelos

Modelo final de la fase 4, generado por `notebooks/03_ajuste_y_evaluacion.ipynb`:

- `modelo_v1.ubj`: modelo XGBoost en formato nativo, que no depende de la versión de Python ni de scikit-learn.
- `modelo_v1.json`: versión, hiperparámetros, umbral de decisión y métricas (validación cruzada y prueba).

Ambos archivos se copian a `exoplanetas-api/modelos/`, donde el servicio de IA los carga como versión inicial.
