import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(data=None)
df_tmy = pd.DataFrame(data=None)

df = pd.read_csv('./RefBldgMediumOfficeNew2004_v1.3_7.1_4A_USA_MD_BALTIMORE.csv', delimiter=',', header=0)
# year = pd.to_datetime(df['Date/Time'])
# df['Date/Time'] = pd.to_datetime(df['Date/Time'])

df_tmy = pd.read_csv('./744860TYA.csv', delimiter=',', header=1)
df_tmy['Date (MM/DD/YYYY)'] = pd.to_datetime(df_tmy['Date (MM/DD/YYYY)'])
df_tmy.rename(columns=lambda x: x.replace('Date (MM/DD/YYYY)', 'date'), inplace=True)
year = pd.to_datetime(df_tmy.date)
df_tmy['year'] = year.dt.year
df_tmy_2004 = df_tmy[df_tmy.year == 2004]
df_tmy['month'] = year.dt.month
df_tmy_2004 = df_tmy[df_tmy.month == 3]


# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(df['Date/Time'], df['Electricity:Facility [kW](Hourly)'], label='Facility Energy Consumption')
ax.plot(df['Date/Time'], df['Heating:Electricity [kW](Hourly)'], label='Facility Heating Demand')
# ax.plot(df_tmy_2004[]
legend = ax.legend(loc='upper right')
ax.set_xlabel('Time')
ax.set_ylabel('Electrical Consumption [Bil. kWh]')
plt.show()
