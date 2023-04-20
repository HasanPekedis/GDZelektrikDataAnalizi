import pandas as pd
from datetime import datetime

# Veri setini yükle
data = pd.read_csv('train.csv')

# Tarih sütununu datetime formatına dönüştür
data['Tarih'] = pd.to_datetime(data['Tarih'])

# Her bir tarihin hangi ayın hangi gününe denk geldiğini belirle
data['Gun'] = data['Tarih'].apply(lambda x: x.day)

# Her bir gün için toplam dağıtılan enerjiyi hesapla
gunluk_toplam = data.groupby('Gun')['Dağıtılan Enerji (MWh)'].sum()

s_new = gunluk_toplam/ 1295

s_new.to_csv('1-30(Gun).csv',index=True)