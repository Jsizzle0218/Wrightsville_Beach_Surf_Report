import streamlit as st

st.title("Surf Report App")

date = st.text_input("enter date:")
time = st.text_input("enter time of day:")
tide = st.text_input("enter tide:")
wave_height = st.number_input("Wave height (single number only):")
wind = st.number_input("Wind speed in kts (single number only):")
wind_direction = st.selectbox(
    "wind direction",
    ["offshore", "onshore", "cross shore"]
)
if wind < 10 and wind_direction == "offshore":

    if wave_height < 2:
        st.write("Nice wind conditions with small waves")
    
    if 2 <= wave_height < 4:
        st.write("Nice wind conditions with rideable waves")

    if wave_height >= 4:
        st.write("Nice wind conditions with big waves")

if wind < 10 and wind_direction in ["onshore", "cross shore"]:

    if wave_height < 2:
        st.write("Okay wind conditions with small waves")
    
    if 2 <= wave_height < 4:
        st.write("Okay wind conditions with rideable waves")

    if wave_height >= 4:
        st.write("Okay wind conditions with big waves")

if 10 <= wind < 20 and wind_direction in ["onshore", "cross shore"]:

    if wave_height < 2:
        st.write("Poor wind conditions with small waves")
    
    if 2 <= wave_height < 4:
        st.write("Poor wind conditions with rideable waves possible")

    if wave_height >= 4:
        st.write("Poor winds conditions with big waves")

if 10 <= wind < 20 and wind_direction == "offshore":

    if wave_height < 2:
        st.write("Okay wind conditions with small waves")
    
    if 2 <= wave_height < 4:
        st.write("Okay wind conditions with rideable waves")

    if wave_height >= 4:
        st.write("Okay wind conditions with big waves")

if wind >= 20 and wind_direction in ["onshore", "cross shore"]:

    if wave_height < 2:
        st.write("Terrible wind conditions with small waves")
    
    if 2 <= wave_height < 4:
        st.write("Terrible wind conditions with rideable waves possible")

    if wave_height >= 4:
        st.write("Terrible wind conditions with big waves")

if wind >= 20 and wind_direction == "offshore":

    if wave_height < 2:
        st.write("Poor wind conditions with small waves")
    
    if 2 <= wave_height < 4:
        st.write("Poor wind conditions with rideable waves possible")

    if wave_height >= 4:
        st.write("Poor wind conditions with big waves")