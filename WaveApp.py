import streamlit as st
import sqlite3

conn = sqlite3.connect("surf_sessions.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    time TEXT,
    tide TEXT,
    wave_height REAL,
    wind REAL,
    wind_direction TEXT,
    result TEXT
)
''')

conn.commit()

st.title("Surf Report App")

date = st.text_input("enter date:")
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

if st.button("Submit"):

    result = ""

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
    
    st.write(result)

    cursor.execute('''
    INSERT INTO sessions (
        date,
        time,
        tide,
        wave_height,
        wind,
        wind_direction,
        result
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        date,
        time,
        tide,
        wave_height,
        wind,
        wind_direction,
        result
    ))

    conn.commit()
