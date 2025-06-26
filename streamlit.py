import streamlit as st
import pandas as pd

st.title('Telecom Churn Prediction ---Dashboard ')

st.markdown('##### Build by Balachandar Madasamy')


upload_file = st.file_uploader('Choose a CSV file ', type = 'csv')

if upload_file is not None:
    st.write("File Uploaded Successfully ...!!!")

    df = pd.read_csv(upload_file)
    st.subheader('Data Preview')
    st.write(df.head(10))

    st.subheader("Data Description")
    st.write(df.describe())

    st.success("Successfully Described the Data")




