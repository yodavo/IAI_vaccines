# Instalar paquetes no disponibles
!pip install squarify

# Para importar la data
import os

# Importar para manipulacion de datos
import numpy as np
import pandas as pd
from statistics import *

# Importar para Visualizacion 
import matplotlib.pyplot as plt
import missingno as msno
import seaborn as sns
plt.style.use('seaborn-whitegrid')
import warnings # para evitar warnings
warnings.filterwarnings('ignore')
import textwrap
from textwrap import wrap
import squarify
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

# Importar Dependencias
%matplotlib inline
%load_ext google.colab.data_table


from google.colab import drive
drive.mount('/content/drive')

# Carga de datos
os.chdir('/content/drive/MyDrive/DIPLOMADO BIGDATA/MODULO V/COVID-19 World Adverse Reactions/')
print(os.listdir())
data = pd.read_csv('2021VAERSDATA.csv', index_col=0, encoding='latin-1')
symptom = pd.read_csv('2021VAERSSYMPTOMS.csv', index_col=0, encoding='latin-1')
vax = pd.read_csv('2021VAERSVAX.csv', index_col=0, encoding='latin-1')

# combinando datasets en un solo dataframe
df = pd.merge(data, symptom, on='VAERS_ID')
df = pd.merge(df, vax, on='VAERS_ID')

# separando el dataset de vacunas de covid19
dataset_covid = dataset[(dataset['VAX_TYPE'] == 'COVID19')]

### OBSERVACIONES SIN EDAD, SIN INFORMACIÓN DE HOSPITALIZACIÓN O DÍAS HOSPITALIZADOS.
dataset_hospitalizados=dataset_covid.copy()
dataset_hospitalizados=dataset_hospitalizados[dataset_hospitalizados['AGE_YRS'].notna()]
dataset_hospitalizados=dataset_hospitalizados[dataset_hospitalizados['HOSPDAYS'].notna()]
dataset_hospitalizados=dataset_hospitalizados[dataset_hospitalizados['HOSPITAL'].notna()]
dataset_hospitalizados=dataset_hospitalizados[dataset_hospitalizados['STATE'].notna()]
###OBSERVACIONES SIN SINTOMAS:
dataset_hospitalizados=dataset_hospitalizados[dataset_hospitalizados['SYMPTOM1'].notna()]
dataset_hospitalizados=dataset_hospitalizados[dataset_hospitalizados['SYMPTOM2'].notna()]
dataset_hospitalizados=dataset_hospitalizados[dataset_hospitalizados['SYMPTOM3'].notna()]
dataset_hospitalizados=dataset_hospitalizados[dataset_hospitalizados['SYMPTOM4'].notna()]
dataset_hospitalizados=dataset_hospitalizados[dataset_hospitalizados['SYMPTOM5'].notna()]
### OBSERVACIONES SIN NÚMERO DE DOSIS ADMINISTRADA CONOCIDA
dataset_hospitalizados=dataset_hospitalizados[dataset_hospitalizados['VAX_DOSE_SERIES'].notna()]
dataset_hospitalizados=dataset_hospitalizados[dataset_hospitalizados['VAX_SITE'].notna()]
dataset_hospitalizados=dataset_hospitalizados[dataset_hospitalizados['VAX_ROUTE'].notna()]
dataset_hospitalizados=dataset_hospitalizados[dataset_hospitalizados['VAX_DATE'].notna()]
dataset_hospitalizados=dataset_hospitalizados[dataset_hospitalizados['NUMDAYS'].notna()]
### observaciones incompletas:
#dataset_hospitalizados=dataset_hospitalizados[dataset_hospitalizados['ALLERGIES'].notna()]
dataset_hospitalizados=dataset_hospitalizados[dataset_hospitalizados['LAB_DATA'].notna()]
### ELIMINACIÓN DE COLUMNAS SIN VALOR INFORMATIVO:
dataset_hospitalizados.drop(['CAGE_YR', 'CAGE_MO','RPT_DATE','V_FUNDBY','ER_VISIT', 'X_STAY',  'RECOVD',
       'OTHER_MEDS', 'CUR_ILL', 'HISTORY', 'PRIOR_VAX', 'SPLTTYPE','TODAYS_DATE', 'BIRTH_DEFECT', 'OFC_VISIT', 'ER_ED_VISIT',
       'ALLERGIES', 'VAX_LOT','DATEDIED'],axis=1, inplace=True)

### SEGÚN VAERS : • Died (DIED): If the vaccine recipient died a "Y" is used; otherwise the field will be blank.
dataset_hospitalizados['DIED']=dataset_hospitalizados['DIED'].apply(lambda x : 1 if x is 'Y' else 0)
### Life Threatening (L_THREAT): If the vaccine recipient had a lifethreatening event associated with the vaccination a "Y" is placed is used; otherwise the field will be blank.
dataset_hospitalizados['L_THREAT']=dataset_hospitalizados['L_THREAT'].apply(lambda x : 1 if x is 'Y' else 0)
### Disability (DISABLE): If the vaccine recipient was disabled as a result of the vaccination a "Y" is placed in this field; otherwise the field will be blank.
dataset_hospitalizados['DISABLE']=dataset_hospitalizados['DISABLE'].apply(lambda x : 1 if x is 'Y' else 0)
