import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df=pd.read_csv('C:/Users/DewaLab/dash_t/udemy/initial_filter.csv')
# df.set_index('Date_Time',inplace=True)
df=df.drop(['Unnamed: 0'], axis=1)
df=df.rename(columns={"Unnamed: 0.1": "Date_Time"})
df['Date_Time'] = pd.to_datetime(df['Date_Time'], errors='coerce',dayfirst=True)
# print(df.head(315))

# -------------------------Rain per Day-----------------------
# data=[go.Scatter(x=df['Date_Time'],y=df['Rain.2'],mode='markers')]

# can do x=df['Date_Time'].dt.month to get the values for specific months together

#------------------------- Taking average  value for each month (Air temp in this particular case) YESSSSSSSSSSSSSSSSSSSSSSS
# dfa=df.groupby(df['Date_Time'].dt.strftime('%B'))['Rain.2'].sum()
dfa=df.groupby(df['Date_Time'].dt.hour)['Air.Temp..2'].mean()

# Another way, but hasnt worked properly yet
# dg = df.groupby(pd.Grouper(key='Date_Time', freq='1M')).sum() # groupby each 1 month
# dg.index = dg.index.strftime('%B').sort_values()
dfa=dfa.to_frame().reset_index()

# dfa.columns=['Date_Time']
print((dfa))

data=[go.Scatter(x=dfa['Date_Time'],y=dfa['Air.Temp..2'],mode='markers+lines')]

# months = ['Jan', 'Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
# Jan,Feb,Mar,Apr,May,June,July,Aug,Sep,Oct,Nov,Dec=0
# JanC,FebC,MarC,AprC,MayC,JuneC,JulyC,Aug,Sep,Oct,Nov,Dec
# for i, r in df.iterrows():
#     if(df['Date_Time'].dt.month==0):

pyo.plot(data)
