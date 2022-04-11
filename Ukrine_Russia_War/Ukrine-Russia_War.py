import seaborn as sns
import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
loss_eq=pd.read_csv(r'Ukrine_Russia_War\archive\russia_losses_equipment.csv')

print(loss_eq.tail())

eq_cost = [21.43, 12.8, 0.5, 0.039, 2, 2.3, 0.06, 600, 115, 20]
loss_eq.drop(['fuel tank', 'drone', 'special equipment'], axis=1, inplace=True) #계산불가능 값 제외
loss_eq['date'] = pd.to_datetime(loss_eq['date']) ## Object를 datetime으로 형변환

loss_eq_Calc = loss_eq.copy()
i = 0
for x in loss_eq.columns.to_list()[2:]: # 계산
    loss_eq_Calc[x] = loss_eq[x] * eq_cost[i]
    i += 1
loss_eq_Calc.fillna(0,inplace=True) # 결측치 제거
print(loss_eq_Calc.tail())

last_index = len(loss_eq_Calc.index)-1
military_total_losses_cost = loss_eq_Calc.iloc[-1:,2:].sort_values(by=[last_index],axis=1,ascending=False).T # .T로 인덱스와 열을 바꿔줌
military_total_losses_cost.rename(columns={last_index:'losses_cost'}, inplace = True)
print(military_total_losses_cost)
air_units = ['helicopter', 'aircraft']
naval_units = ['naval ship']
ground_units = ['APC', 'military auto', 'tank', 'field artillery', 'MRL','anti-aircraft warfare', 'mobile SRBM system']
military_total_losses_cost.reset_index(inplace=True)
military_total_losses_cost.rename(columns={'index':'equipment_name'},inplace=True)
print(military_total_losses_cost)