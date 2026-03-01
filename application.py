import streamlit as st
import pandas as pd
import requests
import random
import numpy as np
import datetime as dt
z=0
users = {
    "viewer": {"password": "123"},
    "controller": {"password": "456"},
    "operator": {"password": "789"},
}
if st.checkbox("Log in"):
    user1 = st.selectbox(
        label="Role:",
        options=users.keys(),
        index=None,
    )
    if user1:
        pas = st.text_input("Password:")
        if pas:
            if users[user1]["password"] == pas:
                z = 1
                st.success("WELCOME")
                st.divider()
            else:
                st.error("Wrong password")
                z = 0

def maintenance(s,t1,b):
    lv=0
    for i in range(len(s)):
        if s[i]>1000:
            st.warning(f"Check pod {t1[i]}")
            st.error("Turn off the engine")
            lv=1
        if b[i]<10:
            st.warning(f"Low battery {t1[i]}")
            lv=1
    if not lv:
        st.success("All in right condition")
if z==1:
    c1, c2 = st.columns(2)
    with c1:
        st.title("**Team** ***Avishkar***")
    with c2:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIK4zn8Y_34QeUqWvDwEIa3KtGfFbd3Ysqiw&s",
                 caption="Hyperloop Pod")
    t = ["Avishkar-1", "Avishkar-2", "Avishkar-3", "Avishkar-4"]
    speed_values = [807, 604, 1040, 500]
    battery_values = [75, 35, 60, 90]
    st.divider()
    st.header("Pod Tracker:slightly_smiling_face::")
    pods = pd.DataFrame({
        "Pod Name": t,
        "Speed(km/h)": speed_values,
        "Battery(%)": battery_values,
        "Status": ["Operational", "Maintenance", "Operational", "Docked"]
    }, index=[1, 2, 3, 4])
    st.write(pods)
    st.divider()
    st.header("Route Monitoring:cowboy_hat_face::")
    API_key = "68b39eac2a09193fb6bde28efa8bce13"
    url = "https://api.openweathermap.org/data/2.5/weather?lat=12.78&lon=80.19&appid={}".format(
        API_key)  # i have put the latitue and longitute of thaiyur
    response = requests.get(url)
    data1 = response.json()
    weather1 = data1["weather"][0]["main"]
    temperature = data1["main"]["temp"]
    d = {
        "rainy": 700,
        "snowy": 500,
        "cloudy": 800,
        "thunder": 0,
        "tornado": 0,
        "mist": 900,
        "sunny": 950,
    }
    speed = d.get(weather1)
    if speed == None:
        speed = 1000
    if speed != 1000:
        st.write(f"The speed is reduced to {speed} km/h")
    else:
        st.write("The speed is 1000 km/h")
    st.divider()
    if user1 in ["controller", "operator"]:
        st.header("Energy Optimization Tip:zap: :")
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        data2 = response.json()
        selected = random.choice(data2)
        st.subheader(selected['title'])
        st.write(selected['body'])
        st.divider()
    st.header("Pod Health Insights:man_health_worker::")
    p1 = st.selectbox(
        label="Choose the first pod to compare",
        options=t,
        index=0,
    )
    l = t.copy()
    l.pop(t.index(p1))
    p2 = st.selectbox(
        label="Choose the second pod to compare",
        options=l,
        index=0,
    )
    var1 = pods[pods["Pod Name"] == p1]
    var2 = pods[pods["Pod Name"] == p2]
    df = pd.DataFrame(
        {
            "Battery(%)": [var1["Battery(%)"].values[0], var2["Battery(%)"].values[0]],
            "Speed": [var1["Speed(km/h)"].values[0], var2["Speed(km/h)"].values[0]],
        },
        index=[p1, p2],
    )
    st.table(df)
    st.divider()
    st.header("Did You Know?")
    url2 = "https://api.api-ninjas.com/v1/factoftheday"
    head = {"X-Api-Key": "s2coW0p5df8Wd18xr3RMsDNJNe6w4G0YCCQzpHQ2"}
    response = requests.get(url2, headers=head)
    data = response.json()
    st.write(data[0]["fact"])
    st.divider()
    st.header("Live Pod Tracking")
    arr = np.array([0, 0.005, 0.010, 0.015, 0.020, 0.025])
    df = pd.DataFrame({
        "lat": arr + 12.790840369321526,
        "lon": arr + 80.18934592829407,
    })
    st.map(df)
    st.divider()
    if user1 in ["controller", "operator"]:
        st.header("Maintenance predictor")
        maintenance(speed_values, t, battery_values)
    if "logbuffer" not in st.session_state:
        st.session_state.logbuffer = []
    p1=st.selectbox(
        label="Choose the pod to log:",
        options=t,
        index=None,
    )
    w = st.checkbox("LOGGING")
    if w:
        log_entry = {
            "Timestamp": dt.datetime.now(),
            "Pod Name": p1,
            "Speed": random.randint(600, 900),
            "Battery": random.randint(30, 100),
        }
        st.session_state.logbuffer.append(log_entry)
        if len(st.session_state.logbuffer) == 3:
            df = pd.DataFrame(st.session_state.logbuffer)
            df.to_csv("podlog4.csv", mode="a", header=False, index=False)
            st.session_state.logbuffer.clear()
            st.success("3 logs saved and buffer cleared")
        st.rerun()
    else:
        st.write("Logging is currently disabled")
else:
    st.stop()