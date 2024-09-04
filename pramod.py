import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title('Interactive Data Visualization with Streamlit')


user_name = st.text_input('Enter your name:', 'Guest')


num_points = st.slider('Select the number of data points:', min_value=1, max_value=100, value=20)


np.random.seed(0)
data = pd.DataFrame({
    'X': np.arange(num_points),
    'Y': np.random.randn(num_points).cumsum()
})


st.write(f'Hello, {user_name}! Here is your data visualization:')


st.subheader('Generated Data')
st.write(data)


st.subheader('Data Plot')
fig, ax = plt.subplots()
ax.plot(data['X'], data['Y'], marker='o', linestyle='-', color='b')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Random Data Plot')


st.pyplot(fig)


stat = st.selectbox('Select a statistic to display:', ['Mean', 'Median', 'Standard Deviation'])


if stat == 'Mean':
    result = data['Y'].mean()
elif stat == 'Median':
    result = data['Y'].median()
elif stat == 'Standard Deviation':
    result = data['Y'].std()

st.subheader(f'{stat} of Y')
st.write(result)
