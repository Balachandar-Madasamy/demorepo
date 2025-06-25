import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import auc,roc_curve,confusion_matrix,classification_report
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.metrics import f1_score
import seaborn as sns



def feature_selection(df):
    X = df.drop(['starttime','endtime','insider'],axis=True)
    y = df['insider']
    return X,y

df = '/bala/sample/repo'