import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

data=pd.read_csv('Project_data.csv')
x= data.iloc[:,1:- 1]

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
le_Start=LabelEncoder()
le_Reason=LabelEncoder()

x['Start']=le_Start.fit_transform(x['Start'])
x['Reason']=le_Reason.fit_transform(x['Reason'])
y=le.fit_transform(data['Place'])

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x,y, test_size=0.25, random_state=7, stratify=data["Place"])

from sklearn.ensemble import RandomForestClassifier
rfc= RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=7)
rfc.fit(x_train, y_train)

from sklearn.metrics import accuracy_score
y_predic= rfc.predict(x_test)

Start_Dict= {'Delhi':0 ,'Mumbai':1}
Nature_Dict= {'Adventure':0, 'Beach':1,'Historic':2 ,'Mountains':3, 'Nature':4, 'Party':5 }

st.title('Make your trips...')
st.header(""" Welcome to make your trips! 
        Create your own trip, based on your budget, preferences & COVID conditions.""")
st.write("")
st.markdown(""" _ Please make sure when you are giving inputs, consider it for two persons._""")
        
with st.form(key="JMD"):
    Start_Journey = st.selectbox("*Select the location for depart*", ("Delhi", "Mumbai"))
    Flight_budget= st.number_input("*What is your flight budget? (kindly select from Rs. 5000 and onwards)*", min_value=5000, max_value=35000, step= 500)
    Hotel_stars= st.selectbox("*Choose the rating for your hotel you wish to stay*", (1,2,3,4,5))
    Hotel_Budget= st.number_input("*What is your accomodation budget*", min_value=5000, max_value=45000, step=1000)
    Expectations = st.selectbox("*What are looking in the the travelling*?", ('Nature', 'Mountains', 'Beach', 'Party', 'Historic', 'Adventure'))
    Covid_risk = st.selectbox("*What COVID risk you might take*? ('1' being the lowest & '5' being the highest)", (1,2,3,4,5))
    Submit= st.form_submit_button(label="Confirm & Submit")
    Suitable_Journey= rfc.predict([[Start_Dict[Start_Journey], Flight_budget, Hotel_stars, Hotel_Budget, Nature_Dict[Expectations], Covid_risk]])
    place= le.inverse_transform(Suitable_Journey)[0]

st.write("")    
if place=="Maharashtra":
    st.write("You should visit Lonavala, Kokan or Mahabaleshwar in Maharashtra. You can experience peace and can work simultaneously. You will find great internet connectivity in these places, so internet wouldn't be a barrier.")
elif place=="Kerla":
    st.write("You should visit Kochi, Munnar or Alappuzha in Kerala. You can enjoy nature, back waters and and some historic places. You will find great internet connectivity in these places, so internet wouldn't be a barrier.")
elif place== "Karnataka":
    st.write("You should visit Coorg, Hampi or Madikeri in Karnataka to enjoy the beautiful greenery, nature and cup of coffee. These are one of the best places to work and while relaxing. You will find great internet connectivity in these places, so internet wouldn't be a barrier.")
elif place=="Goa":
    st.write("You should visit Goa, it has an incredible vibe, you can enjoy beach, parties and water sports. Most of the people are spending weeks in Goa while working. You can experience peace and can work simultaneously. You will find great internet connectivity in these places, so internet wouldn't be a barrier.")
elif place=="Himachal":
    st.write("You should visit Kulu, Manali, Kasol or Dharamshala in Himachal Pradesh, you can work while enjoying the beautiful view of the Himalyan mountains, you can trek and can play adventurous sports in weekends. You will find great internet connectivity in these places, so internet wouldn't be a barrier.")
elif place== "North-East":
    st.write( "You should decide from one of the North-Eastern states, you can visit Gangtok, Shillong or Guwahati as these places are better with internet conncections than other destinations in that region. You can enjoy immense peace & pure nature while working, also you can try their traditional food.")
elif place=="Uttarakhand":
    st.write("You should visit Dehradun, Rishikesh, Mussoorie or Nainital in Uttarakhand, you can work along side of the beautiful mountains and ponds, the grenery of these places could catch your eye. You can visit valley of flowers, different of origins of the rivers, and  can enjoy adventurous sports. You will find great internet connectivity in these places, so internet wouldn't be a barrier.")
st.write('')
st.markdown("_This application is using data & machine learning algorithm, it has achived 97.6% of accuracy! However, you might observe wrong result which belong to 2.4% of inaccuracy._")
