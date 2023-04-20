#THIS CODE FOR AVARAGE MONTH CALC.

import pandas as pd

# Veri setini yükle
data = pd.read_csv('train.csv', parse_dates=['Tarih'])

# Yıl ve ay sütunlarını oluştur
data['yil'] = data['Tarih'].dt.year
data['ay'] = data['Tarih'].dt.month

# Yalnızca 8. aylara ait verileri seç
aggregated_data = data[data['ay'] == 8]

aggregated_data.to_csv('yeni_veriseti.csv', index=False)
Sum = aggregated_data['Dağıtılan Enerji (MWh)'].sum()

print(Sum/len(aggregated_data))