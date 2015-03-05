__author__ = 'noelbell'

# flint hills jetA tower flood data
# excel files converted to csv files with 1st column time stamp, tagnames in first row
# each file has 1 month of data...90Meg

import csv
import pandas as pd
import numpy as np
import xlrd as excelread
import collections as collect

#ordereddict will keep order of columns (in collections module)

# reader = csv.DictReader(open('/volumes//Macintosh HD/Users/noelbell/Documents/big_data/Flooding Data/4months.csv'))
#
# result = {}
# i=0
# for row in reader:
#
#     key = row.pop('TimeStamp')
#     # i =1+i
#     # print(i)
#     # if key in result:
#     #     # implement your duplicate row handling here
#     #     pass
#
#     result[key] = row
#     #print(row)
#_desc
#
#
# df = pd.DataFrame.from_dict(result, orient='index')
# df2 = df.sort_index(axis=1)
# #print(df)
# print(df2)

# df1 = pd.read_csv('/volumes//Macintosh HD/Users/noelbell/Documents/big_data/Flooding Data/June2009csv.csv',parse_dates=True,index_col=0)
# print("June")
# df1_desc = df1.describe()
# df2 = pd.read_csv('/volumes//Macintosh HD/Users/noelbell/Documents/big_data/Flooding Data/July2009csv.csv',parse_dates=True,index_col=0)
# print("July")
# df2_desc = df2.describe()
# df3 = pd.read_csv('/volumes//Macintosh HD/Users/noelbell/Documents/big_data/Flooding Data/August2009csv.csv',parse_dates=True,index_col=0)
# print("August")
# df3_desc = df3.describe()
# df4 = pd.read_csv('/volumes//Macintosh HD/Users/noelbell/Documents/big_data/Flooding Data/September2009csv.csv',parse_dates=True,index_col=0)
# print("Sept")
# df4_desc = df4.describe()
# df = pd.concat([df1,df2,df3,df4])
# df_all_desc = df.describe()
# df1_desc.to_csv('/volumes//Macintosh HD/Users/noelbell/Documents/big_data/Flooding Data/June_desc.csv')
# df2_desc.to_csv('/volumes//Macintosh HD/Users/noelbell/Documents/big_data/Flooding Data/July_desc.csv')
# df3_desc.to_csv('/volumes//Macintosh HD/Users/noelbell/Documents/big_data/Flooding Data/August_desc.csv')
# df4_desc.to_csv('/volumes//Macintosh HD/Users/noelbell/Documents/big_data/Flooding Data/Sept_desc.csv')
# df_all_desc.to_csv('/volumes//Macintosh HD/Users/noelbell/Documents/big_data/Flooding Data/4months_desc.csv')
#df.to_csv('/volumes//Macintosh HD/Users/noelbell/Documents/big_data/Flooding Data/June-Sept2009_df.csv')

dfnew = pd.read_csv('/volumes//Macintosh HD/Users/noelbell/Documents/big_data/Flooding Data/June-Sept2009_df_events.csv', parse_dates=True, index_col=0)
print(dfnew)