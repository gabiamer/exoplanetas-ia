# Backend y API REST

Se desarrolla en la fase 5:

- **19 nov:** backend que carga el modelo guardado y la base de datos del historial (SQLite).
- **20 nov:** API REST.
  - `POST /predict`: recibe una curva de luz (3.197 valores) y devuelve la predicción y su probabilidad.
  - `GET /historial`: devuelve las predicciones anteriores, con los datos enviados y el resultado.
