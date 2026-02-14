# Bhavesh_Balaji_GUI_application
## Overview
This project simulates multiple Hyperloop pods and provides insights into:
- Maintenance warning
- Live pod tracking on a map
- Route based speed adjustment using live weather data
- Speed and battery condition
- Fun facts about the Hyperloop
## Features
**Pod Status Table** displays pod name, speed, battery level, and operational status

**Maintenance Predictor**
Gives us alert if:
    - Speed exceeds safe limits
    - Battery level falls below threshold

**Route Monitoring (Weather-based Speed Control)**
  - Uses OpenWeatherMap API
  - Adjusts pod speed based on weather conditions

**Energy Optimization Tips**
  - Fetches random optimization-related content using a public API

**Pod Health Comparison**
  - Compare speed and battery levels between any two pods

**Did You Know? Section**
  - Displays a random fact of the day using API Ninjas

**Live Pod Tracking**
  - Visualizes pod movement using Streamlit’s map component
##How to Run the project:
pip install streamlit pandas numpy requests
streamlit run app.py

