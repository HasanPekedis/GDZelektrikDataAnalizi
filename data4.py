import pandas as pd
from datetime import datetime

# Veri setini yükle
data = pd.read_csv('train.csv')

# Tarih sütununu datetime formatına dönüştür
data['Tarih'] = pd.to_datetime(data['Tarih'])

# Her satırın hangi haftanın hangi gününe denk geldiğini belirle
data['HaftaninGunu'] = data['Tarih'].apply(lambda x: datetime.strftime(x, '%A'))

# Her haftanın günlerine göre böl ve toplam dağıtılan enerjiyi hesapla
haftalik_toplam = data.groupby('HaftaninGunu')['Dağıtılan Enerji (MWh)'].sum()

s_new = haftalik_toplam/ 5736

print(s_new)

s_new.to_csv('1-7(haftalık).csv',index=True)


