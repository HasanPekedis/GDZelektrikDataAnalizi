import pandas as pd

# Veri setini yükle
data = pd.read_csv('train.csv')

# Tarih ve saat sütunlarını birleştir
data['Tarih'] = pd.to_datetime(data['Tarih'])
data['Saat'] = data['Tarih'].apply(lambda x: x.hour)

# Her bir saat için toplam dağıtılan enerjiyi hesapla
saatlik_toplam = data.groupby(['Saat'])['Dağıtılan Enerji (MWh)'].sum()



s_new = saatlik_toplam / 1673

s_new.to_csv("0-24(saat).csv",index=True)