import streamlit as st 
def converter(value,unit_form,unit_to):

    conversions = {
    "meters_kilometers": 0.001,
    "kilometers_meters": 1000,
    "grams_kilograms": 0.001,
    "kilograms_grams": 1000,
    }
    key = f"{unit_form}_{unit_to}"

    if key in conversions:
      conversion = conversions[key]
      return value * conversion
    else:
       'conversion not found'

st.title("Unit Converter")

value = st.number_input("Enter the Value: ", min_value=1.0,step=1.0)

unit_form = st.selectbox("Convert From:",["meters","kilometers","grams","kilograms"])

unit_to = st.selectbox("Convert to:",["meters","kilometers","grams","kilogram"])

if st.button("Convert"):
   result = converter(value, unit_form, unit_to)
   st.write(f"Convert value: {result}")
