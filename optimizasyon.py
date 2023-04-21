import pandas as pd

filepath = "ornek.csv"
filepath2 = "sonuc.csv"

ornek = pd.read_csv(filepath)
sonuc = pd.read_csv(filepath2)

TOPLAM_HATA_ENDEKSI = 0

i = 0
for i in range(744):
    fark = ornek.at[i, 'Dağıtılan Enerji (MWh)'] - \
        sonuc.at[i, 'Dağıtılan Enerji (MWh)']
    if (fark < 0):
        fark = fark*-1

    oran = fark/sonuc.at[i, 'Dağıtılan Enerji (MWh)']
    oran = oran*100

    TOPLAM_HATA_ENDEKSI = TOPLAM_HATA_ENDEKSI + oran

    i = i+1

print("TOPLAM HATA ENDEKSİ:  " +str(TOPLAM_HATA_ENDEKSI))
