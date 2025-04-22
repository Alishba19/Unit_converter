import streamlit as st
# Func
def distance_convertor(from_unit,to_unit,value):
    units = {
        "Meter": 1,
        "Kilometers": 1000,
        "Centimeter": 0.01,
        "Miles": 1609.34,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def temperature_convertor(from_unit,to_unit,value):
     if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
     elif from_unit == "Fahrenheit" and to_unit == "Celsius":
         result = (value - 32) * 5/9
     else:
         result = value
     return result
 
def weight_convertor(from_unit,to_unit,value):
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }
    result = value * units[from_unit] / units[to_unit]
    return result
 
 
def pressure_convertor(from_unit,to_unit,value):
    units = {
        "Pascals": 1,
        "Hectopascals": 100,
        "Kilopascals": 1000,
        "Bar": 100000,
    }
    result = value * units[from_unit] / units[to_unit]
    return result
 

# UI
st.title("Unit Converter")

category = st.selectbox("Select Category", ["Length", "Temperature", "Weight"])

if category == "Length":
   from_unit =  st.selectbox("From",["Meter", "Kilometers", "Centimetre", "Miles"])
   to_unit =  st.selectbox("To",["Meter", "Kilometers", "Centimetre", "Miles"])
   value =  st.number_input("Enter Value")
   if st.button("Convert"):
     result =  distance_convertor(from_unit,to_unit,value)
     st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
     
elif category == "Temperature":
   from_unit =  st.selectbox("From", ["Celsius", "Fahrenheit"])
   to_unit =  st.selectbox("To", ["Celsius", "Fahrenheit"])
   value =  st.number_input("Enter Value")
   if st.button("Convert"):
     result =  temperature_convertor(from_unit,to_unit,value)
     st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    
elif category == "Weight":
   from_unit =  st.selectbox("From",  ["Kilograms", "Grams", "Pounds", "Ounces"])
   to_unit =  st.selectbox("To",  ["Kilograms", "Grams", "Pounds", "Ounces"])
   value =  st.number_input("Enter Value")
   if st.button("Convert"):
     result =  weight_convertor(from_unit,to_unit,value)
     st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
     