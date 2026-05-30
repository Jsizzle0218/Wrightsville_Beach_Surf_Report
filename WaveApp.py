import streamlit as st

st.title("Surf Report App")

date = st.text_input("enter date: (Ex: 5/27/2026)")
time = st.selectbox("Time of day", ["Morning", "Afternoon", "Evening"])
tide = st.selectbox("Tide", ["High", "Low", "Outgoing", "Incoming"])
wave_height = st.number_input("Wave height (single rational number only):")
wind = st.number_input("Wind speed in kts (single rational number only):")
wind_direction = st.selectbox("wind direction", ["offshore", "onshore", "cross shore"])

def wave_rate(wave_height):
    
    if wave_height < 2:
        return "Small waves"
    elif wave_height < 4:
        return "Rideable waves"
    else: 
        return "Big waves"

def wind_rate(wind, wind_direction):

    if wind < 10 and wind_direction == "offshore":
        return "with excellent offshore wind"
    elif wind < 10 and wind_direction == "onshore":
        return "with nice onshore wind"
    elif wind < 10 and wind_direction == "cross shore":
        return "with nice cross shore wind"
    elif 10 <= wind < 20 and wind_direction == "onshore":
        return "with slight choppy onshore wind"
    elif 10 <= wind < 20 and wind_direction == "cross shore":
        return "with slight drifty cross shore wind"
    elif 10 <= wind < 20 and wind_direction == "offshore":
        return "with nice offshore wind"
    elif wind >= 20 and wind_direction == "onshore":
        return "with very choppy onshore wind"
    elif wind >= 20 and wind_direction == "cross shore":
        return "with very drifty cross shore wind"
    elif wind >= 20 and wind_direction == "offshore":
        return "with strong offshore wind"

if st.button("Submit"):
    st.write(wave_rate(wave_height) + " " + wind_rate(wind, wind_direction))
