import streamlit as st
import pickle
import pandas as pd
from PIL import Image
from dependency import internet_map
from dependency import onlinesec
from dependency import onlinebac,deviceprot,streamtv,streammov,techsupp,contrac,pay_method

dv, model = pickle.load(open('model_telco.pkl','rb'))



image =Image.open('churn1.png')
image2 =Image.open('churn2.png')

st.image(image,use_container_width=False)

add_select_box = st.sidebar.selectbox('How would you like to predict ?',('Online','Batch'))

st.sidebar.info('This app is created to predict the Churn')
st.sidebar.image(image2)

st.title('Telecom Churn Prediction')

if add_select_box == 'Online':
    gender = st.selectbox('Gender :',['Male','Female'])
    gender_val = 1 if gender =='Male' else 0
    senior_citizen = st.selectbox('Customer is a Senior Citizen :',[0,1])
    partner = st.selectbox('Customer has a Partner :',['Yes','No'])
    partner_val = 1 if partner =='Yes' else "No"
    dependent = st.selectbox('Dependent :',['Yes','No'])
    dep_val = 1 if dependent =='Yes' else 'No'
    tenure = st.number_input('No of years customer been with this telco provider :',min_value=0,max_value=240,value=0)
    phn_service = st.selectbox('Customer has phoneservice :', ['Yes', 'No'])
    phn = 1 if phn_service =='Yes' else 'No'
    multi_lines = st.selectbox('Customer has a multiple Lines :',['Yes', 'No'])
    multi = 1 if multi_lines =='Yes' else 'No'
    internetservice = st.selectbox(' Customer has internetservice:', ['No','DSL','Fiber Optic'])
    internet = internet_map[internetservice]
    onlinesecurity = st.selectbox(' Customer has onlinesecurity:', ['Yes', 'No', 'No Internet Service'])
    online_sec = onlinesec[onlinesecurity]
    onlinebackup = st.selectbox(' Customer has onlinebackup:', ['Yes', 'No', 'No Internet Service'])
    online_bac = onlinebac[onlinebackup]
    deviceprotection = st.selectbox(' Customer has deviceprotection:', ['Yes', 'No', 'No Internet Service'])
    device_prot = deviceprot[deviceprotection]
    techsupport = st.selectbox(' Customer has techsupport:', ['Yes', 'No', 'No Internet Service'])
    tech_supp = techsupp[techsupport]
    streamingtv = st.selectbox(' Customer has streamingtv:', ['Yes', 'No', 'No Internet Service'])
    stream_tv = streamtv[streamingtv]
    streamingmovies = st.selectbox(' Customer has streamingmovies:', ['Yes', 'No', 'No Internet Service'])
    stream_mov = streammov[streamingmovies]
    contract = st.selectbox(' Customer has a contract:', ['Month-to-month', 'one_year', 'two_year'])
    contracting = contrac[contract]
    paperlessbilling = st.selectbox(' Customer has a paperlessbilling:', ['Yes', 'No'])
    paper_bill = 1 if paperlessbilling == 'Yes' else 0
    paymentmethod = st.selectbox('Payment Option:',['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    payment = pay_method[ paymentmethod]
    monthlycharges = st.number_input('Monthly charges :', min_value=0, max_value=240, value=0)
    totalcharges = tenure * monthlycharges
    output = ""
    output_prob = ""
    input_dict = {
        "gender": gender_val,
        "seniorcitizen": senior_citizen,
        "partner": partner_val,
        "dependents": dep_val,
        "tenure": tenure,
        "phoneservice": phn,
        "multiplelines": multi,
        "internetservice": internet,
        "onlinesecurity": online_sec,
        "onlinebackup": online_bac,
        "deviceprotection": device_prot,
        "techsupport": tech_supp,
        "streamingtv": stream_tv,
        "streamingmovies": stream_mov,
        "contract": contracting,
        "paperlessbilling": paper_bill,
        "paymentmethod": payment,
        "monthlycharges": monthlycharges,
        "totalcharges": totalcharges
    }

    if st.button('Predict'):
        X = dv.transform([input_dict])
        y_pred = model.predict_proba(X)[0, 1]
        churn = y_pred >= 0.5
        output_prob = float(y_pred)
        output = bool(churn)
    st.success(' Churn  : {0} ,  Risk Score  : {1}'.format(output, output_prob))

if add_select_box == 'Batch':
    file_upload = st.file_uploader('Upload the CSV file for Prediction',type=['csv'])
    if file_upload is not None:
        data = pd.read_csv(file_upload)
        X = dv.transform([data])
        y_pred = model.predict_proba(X)[0,1]
        churn = y_pred >=0.5
        churn = bool(churn)
        st.write(churn)