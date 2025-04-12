import streamlit as st
import pandas as pd
import pydeck as pdk
import altair as alt

st.title("US Health Indicators Viewer 🩺🇺🇸")

# Load the dataset
df = pd.read_csv("County_Data_with_Lat_Long.csv")

# Ensure data types are correct for numerical columns
df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')
df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')

# Dictionary for selecting health indicator names
friendly_names = {
    "Obesity (%)": "OBESITY_CrudePrev",
    "Depression (%)": "DEPRESSION_CrudePrev",
    "Diabetes (%)": "DIABETES_CrudePrev",
    "Smoking (%)": "CSMOKING_CrudePrev",
    "High Blood Pressure (%)": "BPHIGH_CrudePrev",
    "COPD (%)": "COPD_CrudePrev",
    "Poor Physical Health (%)": "PHLTH_CrudePrev",
    "Poor Mental Health (%)": "MHLTH_CrudePrev",
}

# Dropdown to select a health indicator
selected_friendly = st.selectbox("Choose a health indicator", list(friendly_names.keys()))
selected_column = friendly_names[selected_friendly]

# Aggregate data by state
state_data = df.groupby('StateDesc').agg({
    selected_column: 'mean',
    'Latitude': 'mean',
    'Longitude': 'mean'
}).reset_index()

# Show data preview
st.write(f"Preview of {selected_friendly} (aggregated by State):")
st.dataframe(state_data[['StateDesc', selected_column, 'Latitude', 'Longitude']])

# Download button for state-level data
csv = state_data.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download State-Level Data as CSV",
    data=csv,
    file_name=f'state_level_{selected_column}.csv',
    mime='text/csv'
)

# Map visualization by county (raw data)
st.subheader(f"Health Indicator Map by County - {selected_friendly}")
deck = pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=37.0902, longitude=-95.7129, zoom=4, pitch=50
    ),
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=df,
            get_position=["Longitude", "Latitude"],
            get_elevation=selected_column,
            elevation_scale=50,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
            radius=30000,
            get_fill_color="[255, 0, 0, 160]",
        ),
    ],
)
st.pydeck_chart(deck)
# Bar chart showing selected indicator values by "Country" (StateDesc used as placeholder for countries)
st.subheader(f"Average {selected_friendly} by Country (State placeholder)")

country_bar_chart = alt.Chart(state_data).mark_bar().encode(
    x=alt.X('StateDesc:N', sort='-y', title='Country'),
    y=alt.Y(f'{selected_column}:Q', title=f"{selected_friendly} (%)"),
    tooltip=['StateDesc', selected_column]
).properties(
    width=800,
    height=500
).interactive()

st.altair_chart(country_bar_chart)

# Optional: Raw data display
if st.checkbox("Show raw data (by State)"):
    st.dataframe(state_data[['StateDesc', selected_column, 'Latitude', 'Longitude']])
