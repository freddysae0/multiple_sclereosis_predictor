# Predicción de Esclerosis Múltiple

Este proyecto es una aplicación de inteligencia artificial diseñada para predecir la esclerosis múltiple basándose en los parámetros proporcionados por el usuario.

## Clonar el proyecto

Para comenzar a trabajar con este proyecto, sigue estos pasos:

1. Clona el repositorio en tu máquina local utilizando Git:
   ```
   git clone https://github.com/freddysae0/multiple_sclereosis_predictor.git
   ```
2. Navega al directorio del proyecto:
   ```
   cd multiple_sclereosis_predictor
   ```

## Requisitos

Antes de comenzar, asegúrate de tener instalado Python y las siguientes bibliotecas:

- Flask
- Pandas
- Scikit-learn
- Joblib

Puedes instalar estas bibliotecas utilizando pip:

```bash
pip install flask pandas scikit-learn joblib
```

## Uso

Para utilizar el modelo de predicción, sigue estos pasos:

1.  Inicia la API de predicción:
    ```
    python3 ./api/startApi.py
    ```
    o
    ```
    python ./api/startApi.py
    ```
2.  Llama al endpoint /predict (POST). Ingresa los parámetros solicitados por el script en formato json.

        'age'
        'gender'
        'breastfeeding'
        'varicella'
        'initial_symptoms'
        'llssep'
        'ulssep'
        'vep'
        'baep'
        'periventricular_mri'
        'cortical_mri'
        'initial_edss'
        'final_edss'

## Example Input 1

```json
{
  "age": "22",
  "gender": "1",
  "breastfeeding": "1",
  "varicella": "0",
  "initial_symptoms": "8",
  "llssep": "0",
  "ulssep": "0",
  "vep": "0",
  "baep": "0",
  "periventricular_mri": "0",
  "cortical_mri": "0",
  "initial_edss": null,
  "final_edss": null
}
```

## Example Output 1

```json
{
  "group": "non-CDMS",
  "prediction": [2.0]
}
```

## Example Input 2

```json
{
  "age": "22",
  "gender": "1",
  "breastfeeding": "1",
  "varicella": "0",
  "initial_symptoms": "8",
  "llssep": "1",
  "ulssep": "1",
  "vep": "1",
  "baep": "1",
  "periventricular_mri": "1",
  "cortical_mri": "0",
  "initial_edss": "0",
  "final_edss": "0"
}
```

## Example Output 2

```json
{
  "group": "CDMS",
  "prediction": [1.0]
}
```
