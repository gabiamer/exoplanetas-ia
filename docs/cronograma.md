# Cronograma CRISP-ML(Q)

El cronograma va del 10 al 23 de noviembre de 2026. Cada fase cierra con un control de calidad (QA) antes de pasar a la siguiente.

| Fase | Fechas | Actividades | Entregable y control de calidad |
|---|---|---|---|
| 1. Comprensión del negocio y de los datos | 10 nov | Objetivo y criterios de éxito (recall ≥ 0,8 y F1 ≥ 0,6). Análisis exploratorio. | Ficha del problema y reporte exploratorio. **QA:** datos etiquetados y suficientes. |
| 2. Preparación de datos | 11 – 13 nov | Recodificar LABEL, normalizar, recortar picos, quitar tendencia, suavizar, transformada de Fourier, SMOTE solo en entrenamiento. | Pipeline reproducible en `src/`. **QA:** sin fuga de datos. |
| 3. Ingeniería del modelo | 14 – 17 nov | Regresión logística (base), Random Forest, XGBoost y CNN 1D, con validación cruzada estratificada. | Modelos y tabla comparativa. **QA:** superar al modelo base, sin sobreajuste. |
| 4. Evaluación del modelo | 18 – 19 nov | Recall, precisión, F1 y matriz de confusión en exoTest. Ajuste del umbral. | Modelo final guardado. **QA:** cumplir los criterios de la fase 1. |
| 5. Despliegue | 19 – 21 nov | 19: backend. 20: API REST (`POST /predict`, `GET /historial`). 21: frontend. | Sistema funcionando. **QA:** la API da la misma predicción que el notebook. |
| 6. Monitoreo y mantenimiento | 21 – 22 nov | Registro de predicciones, pruebas del sistema completo, criterio de reentrenamiento. | Historial activo. **QA:** se guardan todas las solicitudes. |
| Cierre | 22 – 23 nov | Documentación y ensayo. | Presentación el 23 nov. |
