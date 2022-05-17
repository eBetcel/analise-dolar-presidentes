'''
This script is used to prepare data and plot a graph
using matplotlib and pandas to
generate data visualization about USD/BRL rate
 timeseries according to brazilian presidents

'''

from plistlib import InvalidFileException
import pandas as pd
import matplotlib.ticker as tick
import matplotlib.style as style
import matplotlib.pyplot as plt
import streamlit as st

PATH = "bcdata.csv"


def read_data(file_path):
    '''
    Args:
            path: (string) relative path to .csv file

    Returns:
            data_frame: (pd.DataFrame) pandas dataframe loaded
    '''
    try:
        data_frame = pd.read_csv(file_path, sep=";", decimal=',')
        return data_frame
    except InvalidFileException:
        ('There is no such {}'.format(file_path))


DF = read_data(PATH)

try:
    DF['data'] = pd.to_datetime(DF['data'], format='%d/%m/%Y')
    DF['valor'] = DF['valor'].astype(float)
    DF = DF['valor'].groupby(
        DF['data'].dt.to_period('M')).agg('mean').to_frame()
    DF = DF.rolling(3).mean()

except ValueError:
    print('Failed to convert date')

try:
    FHC = DF.loc['1995-01':'2003-01']
    LULA = DF.loc['2003-01':'2011-01']
    DILMA = DF.loc['2011-01':'2016-08']
    TEMER = DF.loc['2016-08':'2019-01']
    JAIR = DF.loc['2019-01':'2022-12']

except ValueError:
    print('Error slicing date list')

style.use('fivethirtyeight')

FIG, AX = plt.subplots(figsize=(12, 4))

Y_FMT = tick.FormatStrFormatter('R$%1.1f')
AX.yaxis.set_major_formatter(Y_FMT)
AX = plt.gca()
AX.set_ylim([0.1, 5.9])
AX.text(11500.0,
        7.4,
        "Valor Dólar-Real entre 1996 e 2022",
        weight='bold',
        size=16)
AX.text(12000.0,
        7,
        'Presidentes e crises ao longo do período',
        size=12)
# # Adding a signature
AX.text(8000.0,
        -0.7,
        'Victor Vieira and Emanuel Betcel' + ' ' * 120 +
        'Source: Portal Brasileiro de Dados Abertos e Wikipedia',
        color='#f0f0f0',
        backgroundcolor='#4d4d4d',
        size=10)

WIDTH = 1.2

AX.plot(FHC.index.to_timestamp(), FHC['valor'],
        color='#121480')
AX.plot(LULA.index.to_timestamp(), LULA['valor'],
        color='#e81c09')
AX.plot(DILMA.index.to_timestamp(), DILMA['valor'],
        color='#00B2EE')
AX.plot(TEMER.index.to_timestamp(), TEMER['valor'],
        color='#044a06')
AX.plot(JAIR.index.to_timestamp(), JAIR['valor'],
        color='#5B52FF')

plt.axvline(pd.Timestamp('1999-01'), color='black', linestyle='dashdot',
            linewidth=WIDTH, label="Efeito Samba")
plt.axvline(pd.Timestamp('2008-09'), color='black', linestyle='solid',
            linewidth=WIDTH, label="Crise Financeira Global")
plt.axvline(pd.Timestamp('2014-01'), color='black', linestyle='dotted',
            linewidth=WIDTH, label="Recessão Brasileira")
plt.axvline(pd.Timestamp('2020-03'), color='black', linestyle='dashed',
            linewidth=WIDTH, label="Pandemia COVID-19")

plt.text(9500, 0.6, 'FHC', fontsize=16, weight='bold',
         color='#121480')
plt.text(12000.0, 2.0, 'LULA', fontsize=16, weight='bold',
         color='#e81c09')
plt.text(15000.0, 0.9, 'DILMA', fontsize=16, weight='bold',
         color='#00B2EE')
plt.text(17000.0, 2.3, 'TEMER', fontsize=16, weight='bold',
         color='#044a06')
plt.text(18000.0, 2.9, 'BOLSONARO', fontsize=16, weight='bold',
         color='#5B52FF')


AX.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=4, fontsize=12)
AX.grid(alpha=0.6)
AX.set_alpha(0.5)

# plt.savefig("dolarPresidentes.jpg", dpi=100, bbox_inches='tight')
plt.show()

st.pyplot(FIG)
