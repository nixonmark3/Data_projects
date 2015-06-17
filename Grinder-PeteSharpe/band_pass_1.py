__author__ = 'Alper'

import pandas as pd

import scipy as sp
import numpy as np


def summary_fft(df, tag, window_num, start_index, end_index, window_size, no_of_freq, df_fft):
    print('start and end.......', df.iloc[start_index,:], df.iloc[end_index,:])
    data = df[tag].ix[start_index:end_index]
    # sp.fft returns fft with frequencies and magnitudes
    df_fft2 = df_fft
    fft_data = sp.fft(data)

    print('shape = ', np.shape(fft_data))
    #print(fft_data)
    result = []
    abs_fft_data = np.abs(fft_data)
    #df_fft_data = pd.DataFrame(abs_fft_data[1:])
    #while len(result) < no_of_freq:


        # freq returned from sp.fft is cycles/window but we want uniform cycles per day.  1440 could be parameterized
        # different from 1440
        #freq = freq * 3840 / window_size
    result.append((fft_data))
        #print(freq, max_value)
    # adding frequencies and magnitudes to dataframe
    #print('result.....\n', result)
    for i, x in enumerate(result):
        df_fft2['freq{0}'.format(i + 1)].ix[window_num] = result[i][0]
        df_fft2['max_val{0}'.format(i + 1)].ix[window_num] = result[i][1]
    #print('df_fft2.......\n', df_fft2)
    return df_fft2, fft_data


def rolling_fft(df, tag, no_of_freq, window_size):
    # add columns for freq and magnitude results
    df_fft = pd.DataFrame()
    df_fft_all = pd.DataFrame()
    for i, x in enumerate(range(no_of_freq)):
        df_fft['freq{0}'.format(i + 1)] = [np.NaN] * 1152
        df_fft['max_val{0}'.format(i + 1)] = [np.NaN] * 1152

    #for i in range((len(df.index) - window_size)//3840):
    #for i in range(1152):
    for i in range(0,20):
        j = i * 1024
        #print(i, j, range((len(df.index) - window_size)//3840))
        df_fft2, fft_data = summary_fft(df, tag,i, j, j + window_size, window_size, no_of_freq,df_fft)
        df_fft_all.loc[:,'freq{0}'.format(i)] = fft_data
        
    return df_fft2, df_fft_all


def main():
     df = pd.read_csv('/Users/noelbell/bds_datafiles/CuMtn_Vib_Data_Apr_2-6_2015/df_all_Node33286b.csv', parse_dates=True, index_col=0)
    #df = py_wrap.load_data_set()

     no_of_freq = 110

     window_size = 2048
     # tag hardwired....any and all tags in dataset
     print('calling rolling.... \n ...... \n .......  \n...... \n .......')
     df_fft2, df_fft_data = rolling_fft(df, 'ch3', no_of_freq, window_size)

     print(df_fft_data)


     name='/Users/noelbell/bds_datafiles/CuMtn_Vib_Data_Apr_2-6_2015/fft_b_nomax.csv'
     df_fft_data.to_csv(name)


if __name__ == "__main__":
    main()
