import streamlit as st


st.set_page_config(
    page_title="Gurugram Real Estate Analytics App",
    page_icon="👋",
)

st.markdown("<h1 style='text-align: center;'> Welcome to Gurugram City<br> 🏡 Real Estate 🏡</h1>", unsafe_allow_html=True)

#st.title("🏡 Welcome to Gurugram City 🏡 <br> 🏡 Real Estate 🏡")

# Add some spacing
st.markdown('<br>'*2, unsafe_allow_html=True)

# Introduction
st.markdown('<h1 style="color: red;font-size: 38px;font-style: italic; font-family: Brush Script M7, cursive;">Introduction</h1>', unsafe_allow_html=True)
st.write('<h2 style="font-size:25px;font-style: italic">Welcome to the Real Estate Market Analyzer for Gurugram city. In this project, we leverage machine learning techniques to provide insights into the real estate market of Gurugram.</h2>', unsafe_allow_html=True)

# Project Overview
st.markdown('<h2 style="color: green; font-size: 32px;">Project Overview</h2>', unsafe_allow_html=True)
st.write('<h2 style="font-size:18px;">This project represents the culmination of my machine learning mentorship program, completed under the guidance of our mentor, Sir Nitish.</h2>', unsafe_allow_html=True)
st.write("- Objective: Gain practical experience in the end-to-end machine learning lifecycle in the real estate domain.")
st.write("- Modules: Price prediction, Analysis App,  and recommendation systems")

# Add some spacing
st.markdown('<br>'*2, unsafe_allow_html=True)

st.markdown('<h2 style="color: skyblue;font-style: italic; font-size: 30px;font-family: Brush Script M7, cursive;">Workflow : </h2>', unsafe_allow_html=True)

# Step 1: Data Acquisition (Web Scraping)
st.markdown('<h2 style="color: lightblue; font-size: 26px;">Step 1: Data Acquisition (Web Scraping)</h2>', unsafe_allow_html=True)
st.write('<h2 style="font-size:18px;">- We collected data for this project by scraping real estate listings from the 99acres website.</h2>', unsafe_allow_html=True)

# Step 2: Data Cleaning
st.markdown('<h2 style="color: lightblue; font-size: 26px;">Step 2: Data Cleaning</h2>', unsafe_allow_html=True)
st.write('<h2 style="font-size:18px;">-After acquiring the data, we performed extensive data cleaning to ensure high data quality.</h2>', unsafe_allow_html=True)

# Step 3: Feature Engineering
st.markdown('<h2 style="color: lightblue; font-size: 26px;">Step 3: Feature Engineering</h2>', unsafe_allow_html=True)
st.write('<h2 style="font-size:18px;">- We engineered new features to capture important aspects of the real estate market and improve model performance.</h2>', unsafe_allow_html=True)

# Step 4: Exploratory Data Analysis (EDA)
st.markdown('<h2 style="color: lightblue; font-size: 26px;">Step 4: Exploratory Data Analysis (EDA)</h2>', unsafe_allow_html=True)
st.write('<h2 style="font-size:18px;">- EDA helped us gain insights into the relationships between different features and the target variable, providing valuable insights for model building.</h2>', unsafe_allow_html=True)

# Step 5: Outlier Detection and Removal
st.markdown('<h2 style="color: lightblue; font-size: 26px;">Step 5: Outlier Detection and Removal</h2>', unsafe_allow_html=True)
st.write('<h2 style="font-size:18px;">- We identified and removed outliers to ensure the robustness of our machine learning models.</h2>', unsafe_allow_html=True)

# Step 6: Missing Value Imputation
st.markdown('<h2 style="color: lightblue; font-size: 26px;">Step 6: Missing Value Imputation</h2>', unsafe_allow_html=True)
st.write('<h2 style="font-size:18px;">- Missing values were filled using appropriate techniques to ensure completeness of the dataset.</h2>', unsafe_allow_html=True)

# Step 7: Feature Selection
st.markdown('<h2 style="color: lightblue; font-size: 26px;">Step 7: Feature Selection</h2>', unsafe_allow_html=True)
st.write('<h2 style="font-size:18px;">- We selected the most relevant features to reduce dimensionality and improve model performance.</h2>', unsafe_allow_html=True)

# Step 8: Machine Learning Model Development
st.markdown('<h2 style="color: lightblue; font-size: 26px;">Step 8: Machine Learning Model Development</h2>', unsafe_allow_html=True)
st.write('<h2 style="font-size:18px;">- We developed machine learning models to predict property prices based on various factors.</h2>', unsafe_allow_html=True)

# Step 9: Model Selection
st.markdown('<h2 style="color: lightblue; font-size: 26px;">Step 9: Model Selection</h2>', unsafe_allow_html=True)
st.write('<h2 style="font-size:18px;">- We evaluated multiple models and selected the best-performing one for deployment.</h2>', unsafe_allow_html=True)

# Step 10: Streamlit Web Application
st.markdown('<h2 style="color: lightblue; font-size: 26px;">Step 10: Streamlit Web Application</h2>', unsafe_allow_html=True)
st.write('<h2 style="font-size:18px;">- Finally, we built this web application using Streamlit to showcase our findings and provide interactive insights.</h2>', unsafe_allow_html=True)

# Add some spacing
st.markdown('<br>'*3, unsafe_allow_html=True)

# Gratitude Note
st.markdown('<h2 style="color: blue; font-size: 32px;font-style: italic;font-family: Brush Script M7, cursive;">Gratitude 😊</h2>', unsafe_allow_html=True)
st.write('<h2 style="font-size:20px;font-style: italic;">Thank you for taking the time to learn about my project. <br> and I would like to express my sincere gratitude to Nitish sir for his invaluable guidance.</h2>', unsafe_allow_html=True)

