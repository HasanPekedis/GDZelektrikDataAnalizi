import pandas as pd
import datetime

AVG_YEAR = 1845.3666195685175

MONTH_8_AVG = 2209.5902674072577



filepath = "sample_submission.csv"
filepath1 = "0-24(saat).csv"
filepath2 = "1-7(haftalık).csv"
filepath3 = "1-30(Gun).csv"

df = pd.read_csv(filepath)
saatlik = pd.read_csv(filepath1)
haftalik = pd.read_csv(filepath2)
aylik = pd.read_csv(filepath3)

df['Tarih'] = pd.to_datetime(df['Tarih'])

# Yıl bilgisi
df['Yıl'] = df['Tarih'].dt.year

# Ay bilgisi
df['Ay'] = df['Tarih'].dt.month

# Gün bilgisi
df['Gün'] = df['Tarih'].dt.day

# Saat bilgisi
df['Saat'] = df['Tarih'].dt.hour

# Veriyi seçme
ikinci_eleman = df.iloc[1]

# Saat değerine erişme
saat = ikinci_eleman['Tarih'].hour

i=0
for i in range(744):
    # Veriyi seçme  
    ikinci_eleman = df.iloc[i]

    # Saat değerine erişme
    gun = ikinci_eleman['Tarih'].day
    saat = ikinci_eleman['Tarih'].hour
    haftagunu = ikinci_eleman['Tarih'].strftime('%A')
    haftalik_gun_degeri = haftalik.loc[haftalik['HaftaninGunu'] == haftagunu, "Dağıtılan Enerji (MWh)"].values[0]
    #print(aylik.iloc[gun-1]['Dağıtılan Enerji (MWh)'])
    #print("-----------------------------------")
    #print(saatlik.iloc[saat]['Dağıtılan Enerji (MWh)'])
    #print("-----------------------------------")
    
    #print(haftalik_gun_degeri)
    #print("***********************************")

    total = aylik.iloc[gun-1]['Dağıtılan Enerji (MWh)']+saatlik.iloc[saat]['Dağıtılan Enerji (MWh)']+haftalik_gun_degeri
    total = total + AVG_YEAR + MONTH_8_AVG

    result = total/5

    print(result)

    i = i+1

