"""
This script is used to prepare data and plot a graph
using matplotlib and pandas to
generate data visualization about USD/BRL rate
 timeseries according to brazilian presidents
"""
from plistlib import InvalidFileException
import pandas as pd
import matplotlib.ticker as tick
import matplotlib.style as style
import matplotlib.pyplot as plt

PATH = "bcdata.csv"
try:
    DF = pd.read_csv(PATH, sep=";", decimal=',')
except InvalidFileException:
    print('There is no such {}'.format(PATH))

DF['data'] = pd.to_datetime(DF['data'], format='%d/%m/%Y')
DF['valor'] = DF['valor'].astype(float)
DF = DF['valor'].groupby(DF['data'].dt.to_period('M')).agg('mean').to_frame()
DF = DF.rolling(3).mean()

FHC = DF.loc['1995-01':'2003-01']
LULA = DF.loc['2003-01':'2011-01']
DILMA = DF.loc['2011-01':'2016-08']
TEMER = DF.loc['2016-08':'2019-01']
JAIR = DF.loc['2019-01':'2022-12']

style.use('fivethirtyeight')

FIG, AX = plt.subplots(figsize=(12, 4))

Y_FMT = tick.FormatStrFormatter('R$%1.1f')
AX.yaxis.set_major_formatter(Y_FMT)
AX = plt.gca()
AX.set_ylim([0.1, 5.9])
AX.text(731200.0,
        7.4,
        "Valor Dólar-Real entre 1996 e 2022",
        weight='bold',
        size=16)
AX.text(731800.0,
        7,
        'Presidentes e crises ao longo do período',
        size=12)
# Adding a signature
AX.text(726872.0,
        -0.7,
        'Victor Vieira and Emanuel Betcel' + ' ' * 120 +
        'Source: Portal Brasileiro de Dados Abertos e Wikipedia',
        color='#f0f0f0',
        backgroundcolor='#4d4d4d',
        size=10)

LINE_TYPE = "dashdot"
WIDTH = 1.6

AX.plot(FHC.index.to_timestamp(), FHC['valor'],
        color='#BF5FFF')
AX.plot(LULA.index.to_timestamp(), LULA['valor'],
        color='#ffa500')
AX.plot(DILMA.index.to_timestamp(), DILMA['valor'],
        color='#00B2EE')
AX.plot(TEMER.index.to_timestamp(), TEMER['valor'],
        color='#63FF45')
AX.plot(JAIR.index.to_timestamp(), JAIR['valor'],
        color='#5B52FF')

plt.axvline(pd.Timestamp('1999-01'), color='r', linestyle=LINE_TYPE,
            linewidth=WIDTH, label="Efeito Samba")
plt.axvline(pd.Timestamp('2008-09'), color='b', linestyle=LINE_TYPE,
            linewidth=WIDTH, label="Crise Financeira Global")
plt.axvline(pd.Timestamp('2014-01'), color='purple', linestyle=LINE_TYPE,
            linewidth=WIDTH, label="Recessão Brasileira")
plt.axvline(pd.Timestamp('2020-03'), color='black', linestyle=LINE_TYPE,
            linewidth=WIDTH, label="Pandemia COVID-19")


plt.text(730000.0, 0.6, 'FHC', fontsize=16, weight='bold',
         color='#BF5FFF')
plt.text(732500.0, 0.6, 'LULA', fontsize=16, weight='bold',
         color='#ffa500')
plt.text(734300.0, 0.6, 'DILMA', fontsize=16, weight='bold',
         color='#00B2EE')
plt.text(736250.0, 0.6, 'TEMER', fontsize=16, weight='bold',
         color='#63FF45')
plt.text(737650.0, 0.6, 'JAIR', fontsize=16, weight='bold',
         color='#5B52FF')


AX.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=4, fontsize=12)
AX.grid(alpha=0.6)
AX.set_alpha(0.5)

# plt.savefig("dolarPresidentes.jpg", dpi=100, bbox_inches='tight')
plt.show()
