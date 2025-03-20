import streamlit as st

# Conversion Functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1.0, 'Kilometers': 0.001, 'Centimeters': 100,
        'Millimeters': 1000, 'Inches': 39.3701, 'Feet': 3.28084,
        'Yards': 1.09361, 'Miles': 0.000621371
    }
    return value * length_units[to_unit] / length_units[from_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Grams': 1.0, 'Kilograms': 0.001, 'Milligrams': 1000,
        'Pounds': 0.00220462, 'Ounces': 0.035274
    }
    return value * weight_units[to_unit] / weight_units[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32
    return value

# Page Title with Styling
st.markdown("""
    <h1 style='text-align: center; color: #FF5733; font-size: 40px;'>
        🔄 Unit Converter 🔄
    </h1>
    <h3 style='text-align: center; color: #3498DB; font-size: 25px;'>
        Convert Length 📏 | Weight ⚖ | Temperature 🌡
    </h3>
    <hr style='border: 2px solid #FF5733;'>
""", unsafe_allow_html=True)

# Sidebar for Selection
st.sidebar.markdown("<h2 style='color:#E74C3C;'>⚙ Choose Conversion Type:</h2>", unsafe_allow_html=True)
option = st.sidebar.radio("", ("📏 Length", "⚖ Weight", "🌡 Temperature"))

# Custom Styling
st.markdown("""
    <style>
    .stTextInput, .stNumberInput, .stSelectbox, .stButton>button {
        font-size: 18px;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #28A745;
        color: white;
        padding: 12px;
        border-radius: 12px;
        transition: 0.3s;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #218838;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# Conversion Section
if option == "📏 Length":
    st.markdown("<h3 style='color: #9B59B6;'>📏 Length Converter</h3>", unsafe_allow_html=True)
    value = st.number_input("Enter value:", min_value=0.0, step=0.01)
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit", ['Meters', 'Kilometers', 'Centimeters', 'Millimeters', 'Inches', 'Feet', 'Yards', 'Miles'])
    with col2:
        to_unit = st.selectbox("To Unit", ['Meters', 'Kilometers', 'Centimeters', 'Millimeters', 'Inches', 'Feet', 'Yards', 'Miles'])
    
    if st.button("Convert 🔄"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"✅ Converted Value: {result} {to_unit}")

elif option == "⚖ Weight":
    st.markdown("<h3 style='color: #E67E22;'>⚖ Weight Converter</h3>", unsafe_allow_html=True)
    value = st.number_input("Enter value:", min_value=0.0, step=0.01)
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit", ['Grams', 'Kilograms', 'Milligrams', 'Pounds', 'Ounces'])
    with col2:
        to_unit = st.selectbox("To Unit", ['Grams', 'Kilograms', 'Milligrams', 'Pounds', 'Ounces'])

    if st.button("Convert 🔄"):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"✅ Converted Value: {result} {to_unit}")

elif option == "🌡 Temperature":
    st.markdown("<h3 style='color: #1ABC9C;'>🌡 Temperature Converter</h3>", unsafe_allow_html=True)
    value = st.number_input("Enter value:", step=0.1)
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit", ['Celsius', 'Fahrenheit', 'Kelvin'])
    with col2:
        to_unit = st.selectbox("To Unit", ['Celsius', 'Fahrenheit', 'Kelvin'])

    if st.button("Convert 🔄"):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"✅ Converted Value: {result} {to_unit}")