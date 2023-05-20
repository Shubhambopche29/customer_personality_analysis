import streamlit as st
import pickle
import random

# load the model
model = pickle.load(open('customer_model.pkl', 'rb'))

def main():
    # Set a random background template
    bg_templates = ["primary", "secondary", "info", "success", "warning", "danger", "light", "dark"]
    bg_template = random.choice(bg_templates)
    st.markdown(f'<style>.reportview-container .main .block-container{{background-color: {bg_template};}}</style>', unsafe_allow_html=True)

    st.title("Customer Prediction")
    st.write("Enter the customer details below:")

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

    @st.cache()
    def predict():
        customer_data = [[Education, Income, Kidhome, Teenhome, Recency, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth,
        AcceptedCmp3, AcceptedCmp4, AcceptedCmp5, AcceptedCmp1, AcceptedCmp2, Complain, Response, Age, Spent, Living_With,
        Children, Family_Size, Is_Parent, Total_Promos]]
        result = model.predict(customer_data)[0]
        return result

    # Predict button
    if st.button("Predict"):
        try:
            result = predict()
            st.write("Prediction:", result)
        except Exception as e:
            st.error("An error occurred during prediction. Please check your inputs and try again.")

if __name__ == '__main__':
    main()
