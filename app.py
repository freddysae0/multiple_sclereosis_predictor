import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from joblib import dump

data =  pd.read_csv("./dataset.csv")
features  = [ "Age", "Gender" , "Breastfeeding" ,"Varicella" , "Initial_Symptoms" , "LLSSEP", "ULSSEP" , "VEP" , "BAEP" , "Periventricular_MRI" , "Cortical_MRI" , "Initial_EDSS" ,"Final_EDSS"]
y = data.group
X = data[features]

model = DecisionTreeRegressor(random_state=1)
model.fit(X,y)

dump(model, 'api/multiple_sclereosis.joblib')
