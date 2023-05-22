# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:16:29 2023

@author: shubham
"""
import streamlit as st
import pickle
import random
from PIL import Image
import sklearn

# load the model
model = pickle.load(open('customer_model.pkl', 'rb'))

pickle_in = open("customer_model.pkl", "rb")
customer_model = pickle.load(pickle_in)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://p4.wallpaperbetter.com/wallpaper/25/1010/360/nature-black-widow-light-digital-wallpaper-preview.jpg");
             background-attachment: fixed;
	     background-position:75%;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

def welcome():
    return "Welcome All"

def predict_note_authentication(Education, Income, Kidhome, Teenhome, Recency, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth,
        AcceptedCmp3, AcceptedCmp4, AcceptedCmp5, AcceptedCmp1, AcceptedCmp2, Complain, Response, Age, Spent, Living_With,
        Children, Family_Size, Is_Parent, Total_Promos):

    prediction =customer_model.predict([[Education, Income, Kidhome, Teenhome, Recency, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth,
        AcceptedCmp3, AcceptedCmp4, AcceptedCmp5, AcceptedCmp1, AcceptedCmp2, Complain, Response, Age, Spent, Living_With,
        Children, Family_Size, Is_Parent, Total_Promos]])
    return prediction[0]

# noinspection PyUnreachableCode
def main():
    st.title("Customer Personality Analysis")
    st.write("Enter the customer details below:")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Customer Personality Analysis ML App </h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    Education = st.number_input("Education")
    Income = st.number_input("Income")
    Kidhome = st.number_input("Kidhome")
    Teenhome = st.number_input("Teenhome")
    Recency = st.number_input("Recency")
    MntWines = st.number_input("MntWines")
    MntFruits = st.number_input("MntFruits")
    MntMeatProducts = st.number_input("MntMeatProducts")
    MntFishProducts = st.number_input("MntFishProducts")
    MntSweetProducts = st.number_input("MntSweetProducts")
    MntGoldProds = st.number_input("MntGoldProds")
    NumDealsPurchases = st.number_input("NumDealsPurchases")
    NumWebPurchases = st.number_input("NumWebPurchases")
    NumCatalogPurchases = st.number_input("NumCatalogPurchases")
    NumStorePurchases = st.number_input("NumStorePurchases")
    NumWebVisitsMonth = st.number_input("NumWebVisitsMonth")
    AcceptedCmp3 = st.number_input("AcceptedCmp3")
    AcceptedCmp4 = st.number_input("AcceptedCmp4")
    AcceptedCmp5 = st.number_input("AcceptedCmp5")
    AcceptedCmp1 = st.number_input("AcceptedCmp1")
    AcceptedCmp2 = st.number_input("AcceptedCmp2")
    Complain = st.number_input("Complain")
    Response = st.number_input("Response")
    Age = st.number_input("Age")
    Spent = st.number_input("Spent")
    Living_With = st.number_input("Living_With")
    Children = st.number_input("Children")
    Family_Size = st.number_input("Family_Size")
    Is_Parent = st.number_input("Is_Parent")
    Total_Promos = st.number_input("Total_Promos")
     

    result = ""
    if st.button("Predict"):
        try:
            Education = object(Education)
            Income = float(Income)
            Kidhome = int(Kidhome)
            Teenhome =int (Teenhome)
            Recency =int (Recency)
            MntWines =int (MntWines)
            MntFruits =int (MntFruits)
            MntMeatProducts =int (MntMeatProducts)
            MntFishProducts =int (MntFishProducts)
            MntSweetProducts =int (MntSweetProducts)
            MntGoldProds = int(MntGoldProds)
            NumDealsPurchases =int (NumDealsPurchases)
            NumWebPurchases =int(NumWebPurchases)
            NumCatalogPurchases =int (NumCatalogPurchases)
            NumStorePurchases =int (NumStorePurchases)
            NumWebVisitsMonth =int (NumWebVisitsMonth)
            AcceptedCmp3 =int (AcceptedCmp3)
            AcceptedCmp4 =int (AcceptedCmp4)
            AcceptedCmp5 =int (AcceptedCmp5)
            AcceptedCmp1 = int(AcceptedCmp1)
            AcceptedCmp2 =int (AcceptedCmp2)
            Complain =int(Complain)
            Response =int (Response)
            Age =int(Age)
            Spent =int (Spent)
            Living_With =object  (Living_With)
            Children =int (Children)
            Family_Size =int (Family_Size)
            Is_Parent =int (Is_Parent)
            Total_Promos =int (Total_Promos)

    
    
            Result =  predict_note_authentication(Education, Income, Kidhome, Teenhome, Recency, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth,
            AcceptedCmp3, AcceptedCmp4, AcceptedCmp5, AcceptedCmp1, AcceptedCmp2, Complain, Response, Age, Spent, Living_With,
            Children, Family_Size, Is_Parent, Total_Promos)
        
            st.success('The output is {}'.format(result))
        except:
            st.error("An error occurred during prediction. Please check your inputs and try again.")

                                  
    if st.button("About"):
          st.text("Built with Streamlit")                                
                                  

if __name__ == '__main__':
    main()
