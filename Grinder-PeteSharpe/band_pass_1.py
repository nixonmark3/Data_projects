__author__ = 'Alper'

import pandas as pd

import scipy as sp
import scipy.signal as signal
import numpy as np


def main():
     df = pd.read_csv('/Users/noelbell/bds_datafiles/CuMtn_Vib_Data_Apr_2-6_2015/df_ch3_b.csv', parse_dates=True, index_col=0)
    #df = py_wrap.load_data_set()
     print('df......\n', df)
#     x_input = df['ch3'].values
     x_input = df.values

     filt_order = 6
     f_type = 'bandpass'
     analog_or_digital = False
     output_type = 'ba'
     wn_band = [.25, .75]

# get the b and a parameters of the filter:
     b, a = signal.butter(filt_order, wn_band, f_type, analog_or_digital, output_type )
     print('b.......', b)
     print('a.......', a)
     print('x input', x_input.T)

# filter the data
     x_filt = signal.lfilter(b,a, x_input.T)
     print('xfilt type.....', type(x_filt))
     print('x_filt....', x_filt)
     print('x_filt.bracket...', x_filt[1:,1:])
     df_new = pd.DataFrame(x_filt[1:,1:])
#     df_new.loc[:,'filt'] = x_filt.T
 #    print(' size of filt....', df.shape)

     for i in range(0,1):
        j = i * 50000
        j2 = j + 50000
        name='/Users/noelbell/bds_datafiles/CuMtn_Vib_Data_Apr_2-6_2015/fft_b_ch3_filt_{0}.csv'.format(i)
        short_df = df_new.iloc[:,j:j2]
        print(short_df)
        short_df.to_csv(name)


if __name__ == "__main__":
    main()
