import streamlit as st

st.title("Surf Report App")

date = st.text_input("enter date: (Ex: 5/27/2026)")
time = st.selectbox(
    "Time of day",
    ["Morning", "Afternoon", "Evening"]
)
tide = st.selectbox(
    "Tide",
    ["High", "Low", "Outgoing", "Incoming"]
)
wave_height = st.number_input("Wave height (single rational number only):")
wind = st.number_input("Wind speed in kts (single rational number only):")
wind_direction = st.selectbox(
    "wind direction",
    ["offshore", "onshore", "cross shore"]
)


if wind < 10 and wind_direction == "offshore":

    if wave_height < 2:
        st.write("Best wind conditions but waves are tiny")
    
    if 2 <= wave_height < 4:
        st.write("Best wind conditions and the waves are medium sized")

    if wave_height >= 4:
        st.write("Best wind conditions and the waves are really big")

if wind < 10 and wind_direction == "onshore":

    if wave_height < 2:
        st.write("Wind may create small chop but waves are tiny")
    
    if 2 <= wave_height < 4:
        st.write("Wind may create small chop but the waves are rideable")

    if wave_height >= 4:
        st.write("Wind may create small chop but the waves are really big")

if wind < 10 and wind_direction == "cross shore":

    if wave_height < 2:
        st.write("Possible small north or south current but waves are tiny")
    
    if 2 <= wave_height < 4:
        st.write("Possible small north or south current and rideable waves are likely")

    if wave_height >= 4:
        st.write("Possible small north or south current and the waves are really big")

if 10 <= wind < 20 and wind_direction == "onshore":

    if wave_height < 2:
        st.write("Wind will make waves a little choppy but waves are tiny")
    
    if 2 <= wave_height < 4:
        st.write("Wind will make waves a little choppy but waves are rideable")

    if wave_height >= 4:
        st.write("Wind will make waves a little choppy but waves are really big")

if 10 <= wind < 20 and wind_direction == "cross shore":

    if wave_height < 2:
        st.write("Some current going north or south and the waves are tiny")
    
    if 2 <= wave_height < 4:
        st.write("Some current going north or south but waves could be surfable")

    if wave_height >= 4:
        st.write("Some current going north or south but the waves are really big")

if 10 <= wind < 20 and wind_direction == "offshore":

    if wave_height < 2:
        st.write("Wind is nice but the waves are tiny")
    
    if 2 <= wave_height < 4:
        st.write("Wind is nice and likely to catch some medium waves")

    if wave_height >= 4:
        st.write("Wind is nice and waves are really big")

if wind >= 20 and wind_direction == "onshore":

    if wave_height < 2:
        st.write("Strong wind and possible current, choppy and small waves")
    
    if 2 <= wave_height < 4:
        st.write("Strong wind and possible current, choppy but rideable waves possible")

    if wave_height >= 4:
        st.write("Strong wind and possible current, choppy but really big waves")

if wind >= 20 and wind_direction == "cross shore":

    if wave_height < 2:
        st.write("Strong current going north or south, and the waves are small")
    
    if 2 <= wave_height < 4:
        st.write("Strong current going north or south, but waves could be rideable")

    if wave_height >= 4:
        st.write("Strong current going north or south, but the waves are really big")

if wind >= 20 and wind_direction == "offshore":

    if wave_height < 2:
        st.write("Difficult to paddle when catching a wave, and the waves are small")
    
    if 2 <= wave_height < 4:
        st.write("Difficult to paddle when catching a wave, but rideable waves are likely")

    if wave_height >= 4:
        st.write("Difficult to paddle when catching a wave, but the waves are really big")
