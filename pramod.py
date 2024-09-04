import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the title of the app
st.title('Interactive Data Visualization with Streamlit')

# Create a text input for the user
user_name = st.text_input('Enter your name:', 'Guest')

# Create a number input for the user
num_points = st.slider('Select the number of data points:', min_value=1, max_value=100, value=20)

# Generate random data
np.random.seed(0)
data = pd.DataFrame({
    'X': np.arange(num_points),
    'Y': np.random.randn(num_points).cumsum()
})

# Display a greeting message
st.write(f'Hello, {user_name}! Here is your data visualization:')

# Display the data as a table
st.subheader('Generated Data')
st.write(data)

# Plot the data
st.subheader('Data Plot')
fig, ax = plt.subplots()
ax.plot(data['X'], data['Y'], marker='o', linestyle='-', color='b')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Random Data Plot')

# Display the plot
st.pyplot(fig)

# Add a select box to choose a statistic
stat = st.selectbox('Select a statistic to display:', ['Mean', 'Median', 'Standard Deviation'])

# Calculate and display the selected statistic
if stat == 'Mean':
    result = data['Y'].mean()
elif stat == 'Median':
    result = data['Y'].median()
elif stat == 'Standard Deviation':
    result = data['Y'].std()

st.subheader(f'{stat} of Y')
st.write(result)
