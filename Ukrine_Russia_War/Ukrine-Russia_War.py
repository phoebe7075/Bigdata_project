import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
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
last_date = loss_eq_Calc['date'][last_index].date().strftime("%d %B %Y")
military_total_losses_cost = loss_eq_Calc.iloc[-1:,2:].sort_values(by=[last_index],axis=1,ascending=False).T # .T로 인덱스와 열을 바꿔줌
military_total_losses_cost.rename(columns={last_index:'losses_cost'}, inplace = True)


# 그래프 x,y축 지정을 위한 전처리

military_total_losses_cost.reset_index(inplace=True)
military_total_losses_cost.rename(columns={'index':'equipment_name'},inplace=True)
print(military_total_losses_cost)


# 각 카테고리 별 군대 구분
air_units = ['helicopter', 'aircraft']
naval_units = ['naval ship']
ground_units = ['APC', 'military auto', 'tank', 'field artillery', 'MRL','anti-aircraft warfare', 'mobile SRBM system']

def murge_category(unit):
    if unit in ground_units:
        return "Ground Units"
    elif unit in naval_units:
        return "Naval Units"
    else:
        return "Air Units"
    
military_total_losses_cost['unit_type'] = military_total_losses_cost['equipment_name'].apply(lambda x : murge_category(x))


print(military_total_losses_cost)
# Bar 그래프
#plt.figure(figsize=(14,12))
fig = px.bar(military_total_losses_cost, x ='equipment_name', y='losses_cost',text_auto=True,
             title=f'Russian Equipment Losses cost in Ukraine War \n({last_date})')
fig.update_traces(textfont_size=18, textangle=0, cliponaxis=False)
fig.update_layout(
    xaxis_title="Equipment Name",
    yaxis_title="Cost of Equipment Losses",
    font_size = 18
)
fig.update_yaxes(tickformat='$,',ticksuffix='M')
fig.show()


# Stacked Bar 그래프

#plt.figure(figsize=(14,10))
fig = px.bar(
    military_total_losses_cost, x='unit_type', y='losses_cost',color='equipment_name',text_auto=True,
    title=f'Russian Equipment Losses cost in Ukraine War \n({last_date})'
)

fig.update_layout(
    xaxis_title="Unit Type",
    yaxis_title="Cost of Equipment Losses",
    font_size = 18
)
fig.update_yaxes(tickformat='$,',ticksuffix='M')
fig.show()


# Pie 그래프

#plt.figure(figsize=(10,10))

fig = px.pie(military_total_losses_cost, values='losses_cost', names=military_total_losses_cost['unit_type'], 
             title=f'Percentages of Russian Equipment Losses cost in Ukraine War \n({last_date})')
fig.update_layout(
    font_size = 22
)
fig.show()


# Pie 그래프 추가

# fig = px.pie(military_total_losses_cost, values='losses_cost', names=military_total_losses_cost['equipment_name'], 
#              title=f'Percentages of Russian Equipment Losses cost in Ukraine War \n({last_date})')
# fig.update_layout(
#     font_size = 22
# )
# fig.show()



# 선분 그래프 (일자별 손실량 각 군장비별)
rank_list = military_total_losses_cost['equipment_name'].values.tolist()

plt.figure(figsize=(14,8))
sns.set_style("darkgrid")
for equip in rank_list:
    sns.lineplot(x='date', y=equip, data=loss_eq_Calc, marker='o')
    
plt.xlabel('Date',fontsize=18)
plt.ylabel('Cost of Equipment Losses', fontsize=18)
plt.title('Russian Equipment Losses Cost in Ukraine War 2022')
plt.legend(labels=rank_list)

plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('$%iM')) # matplotlib에서 y축 단위설정 함수
plt.show()

# 선분 그래프 (일자별 손실량 각 군 편제 별)

# 각 일자별 손실량 합산
total_loss_cost_per_day = loss_eq_Calc.iloc[:,:1].copy()
total_loss_cost_per_day['ground_units'] = loss_eq_Calc[ground_units].sum(axis=1)
total_loss_cost_per_day['naval_units'] = loss_eq_Calc[naval_units].sum(axis=1)
total_loss_cost_per_day['air_units'] = loss_eq_Calc[air_units].sum(axis=1)

print(total_loss_cost_per_day.tail())

# 그래프 그리기
units = ['ground_units', 'naval_units', 'air_units']
plt.figure(figsize=(14,8))
sns.set_style("darkgrid")
for unit in units:
    sns.lineplot(x='date', y=unit, data=total_loss_cost_per_day, marker='o')



plt.xlabel('Date',fontsize=18)
plt.ylabel('Cost of Equipment Losses Per Unit',fontsize=18)
plt.title('Russian Military Units Equipment Losses Cost in Ukraine War 2022')
plt.legend(labels=units)
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('$%iM')) 

plt.show()


# 손실량 일자별로 정렬한 Bar 그래프

cost_per_day = loss_eq_Calc.iloc[:,:1].copy()
cost_per_day['losses'] = loss_eq_Calc.iloc[:,2:].sum(axis=1)
cost_per_day['losses_day'] = cost_per_day['losses']

for i in range(1,last_index+1):
    cost_per_day['losses_day'][i] = cost_per_day['losses'][i] - cost_per_day['losses'][i-1]
    
cost_per_day.drop('losses',axis=1,inplace=True)
print(cost_per_day.head())

fig = px.bar(cost_per_day, x ='date', y='losses_day',text_auto=True,
             title=f'Russian Equipment Losses cost per Day in Ukraine War \n({last_date})')
fig.update_traces(textfont_size=100, textangle=0, cliponaxis=False, textposition='outside')
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Cost of Equipment Losses",
    font_size = 18
)
fig.update_yaxes(tickformat='$,.0f',ticksuffix='M')
fig.show()