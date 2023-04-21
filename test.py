import pandas as pd

filepath4 = "sonuc.csv"

sonuc = pd.read_csv(filepath4)


sonuc.at[2, 'Dağıtılan Enerji (MWh)'] = 100

sonuc.to_csv("sonuc.csv",index=False)