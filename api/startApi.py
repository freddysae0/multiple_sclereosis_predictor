
""" 
Docs in 
https://www.kaggle.com/datasets/desalegngeb/conversion-predictors-of-cis-to-multiple-sclerosis
"""
from flask import Flask, request, jsonify
from joblib import load


app = Flask(__name__)
# Cargar el modelo
model = load('api/multiple_sclereosis.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos del cuerpo de la solicitud
    data = request.get_json()
    
    # Preparar los datos para el modelo
    features = [
        data['age'],
        data['gender'],
        data['breastfeeding'],
        data['varicella'],
        data['initial_symptoms'],
        data['llssep'],
        data['ulssep'],
        data['vep'],
        data['baep'],
        data['periventricular_mri'],
        data['cortical_mri'],
        data['initial_edss'],
        data['final_edss']
    ]
    
    # Hacer la predicción
    prediction = model.predict([features])
    
    # Devolver la predicción como respuesta JSON
    return jsonify({'prediction': prediction.tolist() , "group": "CDMS" if int(prediction.tolist()[0]) == 1 else "non-CDMS" } )

if __name__ == '__main__':
    app.run(debug=True)