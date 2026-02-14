import streamlit as st
import pandas as pd
import requests
import random
import numpy as np
def maintenance(s,t1,b):
    for i in range(len(s)):
        lv=0
        if s[i]>1000:
            st.warning(f"Check pod {t1[i]}")
            st.warning("Turn off the engine")
            lv=1
            return
        if b[i]<10:
            st.warning(f"Low battery {t1[i]}")
            lv=1
    if not lv:
        st.success("All in right condition")
c1,c2 = st.columns(2)
with c1:
    st.title("**Team** ***Avishkar***")
with c2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIK4zn8Y_34QeUqWvDwEIa3KtGfFbd3Ysqiw&s",caption="Hyperloop Pod")
t=["Avishkar-1", "Avishkar-2", "Avishkar-3", "Avishkar-4"]
speed_values=[807, 604, 1040, 500]
battery_values=[75, 35, 60, 90]
st.divider()
st.header("Pod Tracker:slightly_smiling_face::")
pods= pd.DataFrame({
    "Pod Name":t,
    "Speed(km/h)":speed_values,
    "Battery(%)":battery_values,
    "Status": ["Operational", "Maintenance", "Operational", "Docked"]
},index=[1,2,3,4])
st.write(pods)
st.divider()
st.header("Route Monitoring:cowboy_hat_face::")
API_key="68b39eac2a09193fb6bde28efa8bce13"
url="https://api.openweathermap.org/data/2.5/weather?lat=12.78&lon=80.19&appid={}".format(API_key)#i have put the latitue and longitute of thaiyur
response = requests.get(url)
data1 = response.json()
weather1 =data1["weather"][0]["main"]
temperature = data1["main"]["temp"]
d={
    "rainy":700,
    "snowy":500,
    "cloudy":800,
    "thunder":0,
    "tornado":0,
    "mist":900,
    "sunny":950,
}
speed=d.get(weather1)
if speed==None:
    speed=1000
if speed!=1000:
    st.write(f"The speed is reduced to {speed} km/h")
else:
    st.write("The speed is 1000 km/h")
st.divider()
st.header("Energy Optimization Tip:zap: :")
response=requests.get('https://jsonplaceholder.typicode.com/posts')
data2=response.json()
selected= random.choice(data2)
st.subheader(selected['title'])
st.write(selected['body'])
st.divider()
st.header("Pod Health Insights:man_health_worker::")
p1= st.selectbox(
    label="Choose the first pod to compare",
    options=t ,
    index=0,
)
l=t.copy()
l.pop(t.index(p1))
p2= st.selectbox(
    label="Choose the second pod to compare",
    options=l,
    index=0,
)
var1=pods[pods["Pod Name"]==p1]
var2=pods[pods["Pod Name"]==p2]
df= pd.DataFrame(
    {
        "Battery(%)": [var1["Battery(%)"].values[0],var2["Battery(%)"].values[0]],
        "Speed":[var1["Speed(km/h)"].values[0],var2["Speed(km/h)"].values[0]],
    },
    index=[p1,p2],
)
st.table(df)
st.divider()
st.header("Did You Know?")
url2="https://api.api-ninjas.com/v1/factoftheday"
head = {"X-Api-Key": "s2coW0p5df8Wd18xr3RMsDNJNe6w4G0YCCQzpHQ2"}
response = requests.get(url2,headers=head)
data = response.json()
st.write(data[0]["fact"])
st.divider()
st.header("Live Pod Tracking")
arr=np.array([0,0.005,0.010,0.015,0.020,0.025 ])
df=pd.DataFrame({
    "lat":arr+12.790840369321526,
    "lon":arr+80.18934592829407,
})
st.map(df)
st.divider()
st.header("Maintenance predictor")
maintenance(speed_values,t,battery_values)