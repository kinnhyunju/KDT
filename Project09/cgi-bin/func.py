# 모듈 로딩
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchinfo import summary
from classes import CancerModel

import pandas as pd


def prerocessing(text):
    lungDF = pd.DataFrame([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],columns=['age', 'gender', 'diagnosis_date', 'cancer_stage', 'beginning_of_treatment_date',  'family_history', 
 'smoking_status', 'bmi', 'cholesterol_level', 'hypertension', 'asthma', 'cirrhosis', 'other_cancer', 'treatment_type', 'end_treatment_date'])
    data = text.split(',')
    lungDF.loc[0] = data
    lungDF['age'] = (lungDF['age'].astype('float64')).astype('int')
    lungDF['bmi'] = lungDF['bmi'].astype('float64')
    lungDF['cholesterol_level'] = lungDF['cholesterol_level'].astype('int64')
    lungDF['hypertension'] = lungDF['hypertension'].astype('int64')
    lungDF['asthma'] = lungDF['asthma'].astype('int64')
    lungDF['cirrhosis'] = lungDF['cirrhosis'].astype('int64')
    lungDF['other_cancer'] = lungDF['other_cancer'].astype('int64')
    lungDF['beginning_of_treatment_date'] = pd.to_datetime(lungDF['beginning_of_treatment_date'])
    lungDF['end_treatment_date'] = pd.to_datetime(lungDF['end_treatment_date'])
    lungDF['diagnosis_date'] = pd.to_datetime(lungDF['diagnosis_date'])
    lungDF['cancer_stage'] = lungDF['cancer_stage'].replace({'Stage I':1,'Stage II':2, 'Stage III':3, 'Stage IV':4})
    lungDF['gender'] = lungDF['gender'].replace({'Male':0, 'Female':1})
    lungDF['family_history'] = lungDF['family_history'].replace({'No':0, 'Yes':1})
    lungDF['smoking_status'] = lungDF['smoking_status'].replace({'Never Smoked':0,'Passive Smoker':1,'Former Smoker':2,'Current Smoker':3})
    lungDF['treatment_type'] = lungDF['treatment_type'].replace({'Chemotherapy':0,'Combined':1,'Radiation':2,'Surgery':3})
    lungDF['start_days'] = (lungDF['beginning_of_treatment_date']-lungDF['diagnosis_date']).dt.days
    lungDF['treatment_days'] = (lungDF['end_treatment_date'] - lungDF['beginning_of_treatment_date']).dt.days
    cancerDF = lungDF.drop(['diagnosis_date','beginning_of_treatment_date','end_treatment_date'], axis=1)

    return cancerDF.loc[0].to_list()

def detecting(text):
    cancerModel = CancerModel()
    data = prerocessing(text)
    dataTS = torch.FloatTensor(data).reshape(1,-1)

    cancerModel.eval()

    with torch.no_grad():
        pre_val = cancerModel(dataTS)

    result = 'Survived : True' if (pre_val>0.22).item() else 'Survived : False'
    return result
