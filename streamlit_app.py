import pandas as pd
import streamlit as st
import numpy as np
import altair as alt

st.set_page_config(page_title="Mobile Picker", page_icon="📱", layout="wide", initial_sidebar_state="expanded")

# Load the DataFrame
df = pd.read_csv('cleaned_data.csv')


st.title("Mobile Picker")
st.write('**Get smartphone of your choice**')

st.divider()

mask = (df['Rating'] >= 4.4) & (df['Selling Price'] <= 30000)
most_popular_df = df[mask]
# Display the most popular phones in tabular format
st.write("Most popular phones")
st.write(most_popular_df[['Model', 'Brand', 'Selling Price', 'Rating']].head(3)) 

# Sidebar widgets
with st.sidebar:
    st.write("Input Options")
    # Unique brands with 'All' option
    brand = st.selectbox("Brand", options=['All'] + list(df['Brand'].unique()))
    st.divider()
    min_price, max_price = st.slider(
        "Price Range",
        min_value=float(df['Selling Price'].min()), 
        max_value=float(df['Selling Price'].max()), 
        value=(float(df['Selling Price'].min()), float(df['Selling Price'].max()))
    )
    st.divider()
    min_rating,max_rating=st.slider("Rating",
                                    df['Rating'].min(),
                                    df['Rating'].max(),
                                    value=(df['Rating'].min(),df['Rating'].max())
                                    )
    st.divider()
    st.write("Please refresh the page to **clear all filters**")
    
# text input model name
model_name=st.text_input("Enter Model you want")
st.write("You have selected the model:",model_name)

st.divider()


# Filter DataFrame based on sidebar inputs
filtered_df = df[
    (df['Selling Price'].between(min_price, max_price)) &
    (df['Brand'] == brand if brand != 'All' else True) &
    (df['Rating'].between(min_rating,max_rating)) |
    (df['Model'].str.lower() == model_name.lower())
]

# Display the filtered DataFrame
with st.expander("Load all records"):
    st.write(filtered_df)


st.markdown("[Developed by Siddhesh Vaity](https://www.linkedin.com/in/siddhesh-vaity-6aba6821a)", unsafe_allow_html=True)

