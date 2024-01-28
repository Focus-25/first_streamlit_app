import streamlit as st
import pandas as pd
import requests

# Title and headers
st.title('My parents new healthy Diner')
st.header('Breakfast Favorites')

# Breakfast menu
st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')
st.text('Avocado Toast')

# Build your own fruit smoothie
st.header('Build Your Own Fruit Smoothie')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)

# Fruityvice fruit advice
st.header("Fruityvice Fruit Advice!")

# Get fruit data from Fruityvice API
fruit_choice = st.text_input('What fruit would you like information about?', 'kiwi')
fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit_choice}")

if fruityvice_response.status_code == 200:
    # Normalize the JSON response data for display
    # This converts the JSON data into a flat pandas DataFrame
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    
    # Display the normalized data in a Streamlit dataframe
    # This creates a table in the app showing the fruit information
    st.dataframe(fruityvice_normalized)
else:
    st.error("Failed to fetch data for the fruit: " + fruit_choice)
