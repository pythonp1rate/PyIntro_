import streamlit as st
import pandas as pd
import numpy as np

# Simple Streamlit App - Basic Version
# This creates a basic web app with interactive elements

def create_basic_app():

    # In set_page_conig, we can set
    # Some basic configurations of the page
    # In general we always do this in every app
    st.set_page_config(
    page_title="My First App",
    page_icon="🎈", 
    layout="wide",
    initial_sidebar_state="collapsed")

    # Set page title
    st.title("🎓 My First Streamlit App (Updated)")
    
    # Add a header
    st.header("Welcome to Streamlit!")
    
    # Add some text
    st.write("This is a simple example of what you can do with Streamlit.")
    
    # Create a sidebar
    st.sidebar.title("Controls")
    
    # Add a slider
    age = st.sidebar.slider("Select your age:", 0, 100, 25)
    st.write(f"You are {age} years old!")
    
    # Add a text input
    name = st.text_input("What's your name?", "Student")
    st.write(f"Hello, {name}! 👋")
    
    # Add a selectbox
    favorite_color = st.selectbox(
        "What's your favorite color?",
        ["Red", "Blue", "Green", "Yellow", "Purple"]
    )
    st.write(f"Your favorite color is {favorite_color}! 🎨")

    demographic_data = pd.DataFrame({
        "Name": name,
        "Age": age,
        "Favorite Color": favorite_color
    }, index=[0])
    st.download_button(
        label="Download your data as CSV",
        data=demographic_data.to_csv(index=False),
        file_name='demographic_data.csv',
        mime='text/csv'
    )  
    
    # Add a checkbox
    if st.checkbox("Show me a surprise!"):
        st.balloons()  # This creates a fun balloon animation!
    
    # Add a button
    if st.button("Click me!"):
        st.success("Button clicked! 🎉")
    
    # Create some sample data
    st.subheader("Sample Data")
    data = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100)
    })
    
    # Display the data as a table
    st.dataframe(data.head(10))
    
    # Add some statistics
    st.subheader("Statistics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Mean X", f"{data['x'].mean():.2f}")
    
    with col2:
        st.metric("Mean Y", f"{data['y'].mean():.2f}")
    
    with col3:
        st.metric("Data Points", len(data))
    
    # Add a download button
    csv = data.to_csv(index=False)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='sample_data.csv',
        mime='text/csv'
    )

# Run the app
# This runs if the program is run directly
# It doesn't run if the program is imported 
if __name__ == "__main__":
    create_basic_app()
