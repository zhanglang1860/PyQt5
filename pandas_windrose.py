

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "D:\study_code\windrose")))
print(sys.path)
from windrose import plot_windrose,WindroseAxes
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np


def main():
    # df = pd.read_csv("samples/sample_wind_poitiers.csv", parse_dates=["Timestamp"])
    # # df['Timestamp'] = pd.to_timestamp()
    # df = df.set_index("Timestamp")

    N = 500
    ws = np.random.random(N) * 6
    wd = np.random.random(N) * 360
    df = pd.DataFrame({'speed': ws, 'direction': wd})

    print(df)
    print(df.dtypes)

    bins = np.arange(0.01, 8, 1)
    # bins = np.arange(0, 8, 1)[1:]
    plot_windrose(df, kind="contour", bins=bins, cmap=cm.hot, lw=3, rmax=20000)
    plt.show()

    bins = np.arange(0, 30 + 1, 1)
    bins = bins[1:]

    ax, params = plot_windrose(df, kind="pdf", bins=bins)
    print("Weibull params:")
    print(params)
    # plt.savefig("screenshots/pdf.png")
    plt.show()


def main1():
    df= pd.read_csv("./2634.csv")
    print([column for column in df])
    # print(df)


    skip_rows=df[df['SDR']=='Date & Time Stamp'].index.values
    df_data = pd.read_csv("./2634.csv",header=skip_rows[0]+1)
    # date_index = pd.to_datetime(df_data['Date & Time Stamp'])
    df_data.set_index(pd.to_datetime(df_data['Date & Time Stamp']), inplace=True)



    print(df_data['CH1Avg'].loc['2017-4-10':'2017-4-11'])

    ws = df_data['CH1Avg'].loc['2017-5-1':]
    wd = df_data['CH10Avg'].loc['2017-5-1':]
    df = pd.DataFrame({'speed': ws, 'direction': wd})



    print(df)
    print(df.dtypes)

    bins = np.arange(0.01, 8, 1)
    # bins = np.arange(0, 8, 1)[1:]
    # plot_windrose(df, kind="contour", bins=bins, cmap=cm.hot, lw=3, rmax=20000)

    ax = WindroseAxes.from_ax()
    ax.bar(wd, ws, normed=True, opening=0.8, edgecolor='white')
    ax.set_legend()

    plt.show()

    # # print([column for column in df])
    # print("Weibull params:")
    # df_data_period=df_data.to_period('M')
    # df_data.index= df_data_period.index.asfreq('M')
    # print(df_data['CH1Avg'].groupby('Date & Time Stamp').mean())
if __name__ == "__main__":
    main1()
