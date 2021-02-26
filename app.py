import streamlit as st
import pandas as pd
import numpy as np
import datetime
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
### Date
'''
d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

'''
### Time
'''
t = st.time_input('Set an alarm for', datetime.time(8, 45))

st.write('Alarm is set for', t)


pickup_longitude = st.number_input('Insert pickup longitude')




pickup_latitude = st.number_input('Insert pickup latitude')




dropoff_longitude = st.number_input('Insert dropoff longitude')




dropoff_latitude = st.number_input('Insert dropoff latitude')



'''
### Passenger Count
'''
@st.cache
def get_select_box_data():
    print('get_select_box_data called')
    return pd.DataFrame({
          'first column': list(range(1, 11)),
          'second column': np.arange(10, 101, 10)
        })

df = get_select_box_data()

option = st.selectbox('Select a line to filter', df['first column'])

# filtered_df = df[df['first column'] == option]

# st.write(filtered_df)


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

# url = 'http://taxifare.lewagon.ai/predict_fare/'

url = 'http://taxifare.lewagon.ai/predict_fare/?key=2012-10-06%2012:10:20.0000001&pickup_datetime=2012-10-06%2012:10:20%20UTC&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2'

if url == 'http://taxifare.lewagon.ai/predict_fare/':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')
    
req = requests.get(url).json()

st.write(req)

'''
1.

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''