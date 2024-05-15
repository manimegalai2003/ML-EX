import streamlit as st
import pandas as pd

# Load data from CSV
@st.cache
def load_data():
    data = pd.read_csv('tennisdata.csv')
    return data

data = load_data()

st.title("Tennis Data Analysis")

# Display the first 5 rows of the data
st.write("The first 5 values of data are:")
st.write(data.head())

# Obtain Train data and Train output
X = data.iloc[:,:-1]
st.write("\nThe First 5 values of train data are:")
st.write(X.head())

y = data.iloc[:,-1]
st.write("\nThe first 5 values of Train output are:")
st.write(y.head())

# Convert categorical features to numerical values
outlook_mapping = {'Sunny': 0, 'Overcast': 1, 'Rainy': 2}
X['Outlook'] = X['Outlook'].map(outlook_mapping)

temperature_mapping = {'Hot': 0, 'Mild': 1, 'Cool': 2}
X['Temperature'] = X['Temperature'].map(temperature_mapping)

humidity_mapping = {'High': 0, 'Normal': 1}
X['Humidity'] = X['Humidity'].map(humidity_mapping)

windy_mapping = {'False': 0, 'True': 1}
X['Windy'] = X['Windy'].map(windy_mapping)

st.write("\nNow the Train data is:")
st.write(X.head())

play_tennis_mapping = {'No': 0, 'Yes': 1}
y = y.map(play_tennis_mapping)
st.write("\nNow the Train output is:")
st.write(y)

# Split the data into training and testing sets
train_size = int(0.8 * len(data))
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

st.write("\nTrain data shape:", X_train.shape)
st.write("Test data shape:", X_test.shape)

st.write("\nTrain output shape:", y_train.shape)
st.write("Test output shape:", y_test.shape)
