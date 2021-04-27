import pandas as pd
import numpy as np
# from IPython.display import display
# data = pd.read_csv('Production_Crops_E_All_Data_NOFLAG.csv',encoding='unicode_escape')
#
#
# year_list = data.columns.tolist()
# year_list = year_list[43:]
#
# all_data = []
# for location in data['Area'].unique():
#     print(location)
#     for item in data['Item'].unique():
#         for element in ['Area harvested']:
#             one_row = data[
#                 (data['Area'] == location) &
#                 (data['Item'] == item) &
#                 (data['Element'] == element)
#             ]
#             for year in year_list:
#                 one_data = []
#                 one_data.append(location)
#                 one_data.append(item)
#                 one_data.append(element)
#                 one_data.append(year)
#                 try:
# #                     value = one_row[year].values[0]
# #                     if np.isnan(value) == False:
#                     one_data.append(one_row[year].values[0])
#                 except:
#                      one_data.append(np.nan)
#                 all_data.append(one_data)
# all_data = pd.DataFrame(all_data)
# all_data.columns = ['Area','Item','Element','Year','Value']
#
# all_data1 = all_data
# all_data1.drop('Element',axis=1,inplace=True)
# all_data1.columns = ['Area','Item','Year','Area harvested(ha)']
# all_data1.set_index(['Area','Item','Year'])
# all_data1.to_csv('Area harvested.csv')


data1 = pd.read_csv('Yield.csv')
data1.set_index(['Area','Item','Year'],inplace=True)
data2 = pd.read_csv('Area harvested.csv')
data2.set_index(['Area','Item','Year'],inplace=True)
data = pd.concat([data1,data2],axis=1)
data.to_csv('result.csv')
