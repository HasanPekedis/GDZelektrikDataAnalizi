#THIS CODE FOR AVARAGE YEAR CALC.

import pandas as pd
import datetime

filepath = "train.csv"

df = pd.read_csv(filepath)

# Convert the "date" column to a datetime object
df['Tarih'] = pd.to_datetime(df['Tarih'])

# Filter the data for only the year 2018
data_2018 = df[(df['Tarih'].dt.year == 2018)]

sum2018 = data_2018['Dağıtılan Enerji (MWh)'].sum()

avg2018 = sum2018/8760

#----------------------------------------------------------------------------

data_2019 = df[(df['Tarih'].dt.year == 2019)]

sum2019 = data_2019['Dağıtılan Enerji (MWh)'].sum()

avg2019 = sum2019/8760

#----------------------------------------------------------------------------

data_2020 = df[(df['Tarih'].dt.year == 2020)]

sum2020 = data_2020['Dağıtılan Enerji (MWh)'].sum()

avg2020 = sum2020/8760

#----------------------------------------------------------------------------

data_2021 = df[(df['Tarih'].dt.year == 2021)]

sum2021 = data_2021['Dağıtılan Enerji (MWh)'].sum()

avg2021 = sum2021/8760



data_2022 = df[(df['Tarih'].dt.year == 2022)]

sum2022 = data_2022['Dağıtılan Enerji (MWh)'].sum()

avg2022 = sum2022/5028


AVG_YEAR = (avg2018+avg2019+avg2020+avg2021+avg2022)/5

#print(AVG_YEAR)
print(AVG_YEAR)
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------



