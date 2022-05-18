'''
This script is used to prepare data and plot a graph
using matplotlib and pandas to
generate data visualization about USD/BRL rate
 timeseries according to brazilian presidents

'''

import logging
import pandas as pd
import matplotlib.ticker as tick
import matplotlib.style as style
import matplotlib.pyplot as plt
import streamlit as st

logging.basicConfig(
    filename='./results.log',
    level=logging.INFO,
    filemode='w',
    format='%(message)s')

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
    except FileNotFoundError:
        logging.error('There is no such {}'.format(file_path))


def plot_graph(data_frame):
    '''
    Args:
            data_frame: (pd.DataFrame) pandas dataframe

    '''
    try:
        data_frame['data'] = pd.to_datetime(
            data_frame['data'], format='%d/%m/%Y')
        data_frame['valor'] = data_frame['valor'].astype(float)
        data_frame = data_frame['valor'].groupby(
            data_frame['data'].dt.to_period('M')).agg('mean').to_frame()
        data_frame = data_frame.rolling(3).mean()

        fhc = data_frame.loc['1995-01':'2003-01']
        lula = data_frame.loc['2003-01':'2011-01']
        dilma = data_frame.loc['2011-01':'2016-08']
        temer = data_frame.loc['2016-08':'2019-01']
        jair = data_frame.loc['2019-01':'2022-12']

        style.use('fivethirtyeight')

        fig, a_x = plt.subplots(figsize=(12, 4))

        y_fmt = tick.FormatStrFormatter('R$%1.1f')
        a_x.yaxis.set_major_formatter(y_fmt)
        a_x = plt.gca()
        a_x.set_ylim([0.1, 5.9])
        a_x.text(11500.0,
                 7.4,
                 "Valor Dólar-Real entre 1996 e 2022",
                 weight='bold',
                 size=16)
        a_x.text(12000.0,
                 7,
                 'Presidentes e crises ao longo do período',
                 size=12)
        # # Adding a signature
        a_x.text(8000.0,
                 -0.7,
                 'Victor Vieira and Emanuel Betcel' + ' ' * 120 +
                 'Source: Portal Brasileiro de Dados Abertos e Wikipedia',
                 color='#f0f0f0',
                 backgroundcolor='#4d4d4d',
                 size=10)

        width = 1.2

        a_x.plot(fhc.index.to_timestamp(), fhc['valor'],
                 color='#121480')
        a_x.plot(lula.index.to_timestamp(), lula['valor'],
                 color='#e81c09')
        a_x.plot(dilma.index.to_timestamp(), dilma['valor'],
                 color='#00B2EE')
        a_x.plot(temer.index.to_timestamp(), temer['valor'],
                 color='#044a06')
        a_x.plot(jair.index.to_timestamp(), jair['valor'],
                 color='#5B52FF')

        plt.axvline(pd.Timestamp('1999-01'), color='black', linestyle='dashdot',
                    linewidth=width, label="Efeito Samba")
        plt.axvline(pd.Timestamp('2008-09'), color='black', linestyle='solid',
                    linewidth=width, label="Crise Financeira Global")
        plt.axvline(pd.Timestamp('2014-01'), color='black', linestyle='dotted',
                    linewidth=width, label="Recessão Brasileira")
        plt.axvline(pd.Timestamp('2020-03'), color='black', linestyle='dashed',
                    linewidth=width, label="Pandemia COVID-19")

        plt.text(9500, 0.6, 'fhc', fontsize=16, weight='bold',
                 color='#121480')
        plt.text(12000.0, 2.0, 'lula', fontsize=16, weight='bold',
                 color='#e81c09')
        plt.text(15000.0, 0.9, 'dilma', fontsize=16, weight='bold',
                 color='#00B2EE')
        plt.text(17000.0, 2.3, 'temer', fontsize=16, weight='bold',
                 color='#044a06')
        plt.text(18000.0, 2.9, 'BOLSONARO', fontsize=16, weight='bold',
                 color='#5B52FF')

        a_x.legend(
            loc='upper center',
            bbox_to_anchor=(
                0.5,
                1.2),
            ncol=4,
            fontsize=12)
        a_x.grid(alpha=0.6)
        a_x.set_alpha(0.5)

        plt.savefig("dolarPresidentes.jpg", dpi=100, bbox_inches='tight')
        plt.show()

        st.pyplot(fig)

    except Exception as e:
        logging.error(type(e))


DF = read_data(PATH)
plot_graph(DF)
