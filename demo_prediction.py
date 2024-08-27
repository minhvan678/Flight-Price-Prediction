import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('model.joblib')

@st.cache()
def make_predictions(airline, flight, source_city, departure_time, stops, arrival_time, destination_city, ticket_class, duration, days_left):

    pred_input = []

    pred_input.append(airline)
    pred_input.append(flight)
    pred_input.append(source_city)
    pred_input.append(departure_time)
    pred_input.append(stops)
    pred_input.append(arrival_time)
    pred_input.append(destination_city)
    pred_input.append(ticket_class)
    pred_input.append(float(duration))
    pred_input.append(float(days_left))

    df = pd.DataFrame(np.array([pred_input]),
                   columns=['airline', 'flight', 'source_city', 'departure_time', 'stops',
                           'arrival_time', 'destination_city', 'class', 'duration', 'days_left'])

    prediction = model.predict(df)

    return prediction


def main():
    
    st.title('Flight Price Prediction')
    st.subheader('Fill the following details to get the idea about flight price')

    col1, col2 = st.columns([2, 1])
    days_left = col2.text_input('Days left')
    departure_time = col1.selectbox('Departure time', ['Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night'])

    col3, col4 = st.columns([2, 1])
    duration = col4.text_input('Duration')
    arrival_time = col3.selectbox('Arrival time', ['Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night'])

    col5, col6 = st.columns(2)
    source_city = col5.selectbox('Source city',['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'])
    destination_city = col6.selectbox('Destination city', ['Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai', 'Delhi'])

    stops = st.selectbox('Total Stops', ['zero', 'one', 'two_or_more'])

    airline = st.selectbox('Choose Airline', ['Vistara',  'Air_India', 'GO_FIRST' , 'AirAsia', 'SpiceJet'])

    ticket_class = st.selectbox('Class', ['Economy', 'Business'])

    flight = st.text_input('Flight')
    predict = st.button('Make Prediction',)

    
    if predict:
        with st.spinner('Wait for prediction....'):
            t = make_predictions(airline, flight, source_city, departure_time, stops, arrival_time, destination_city, ticket_class, duration, days_left)
        st.success(f'Price will be around {t}')

if __name__=='__main__': 
    main()