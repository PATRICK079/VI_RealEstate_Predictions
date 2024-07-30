import streamlit as st
import joblib
import pandas as pd


# Load the trained model from file
@st.cache_resource(show_spinner="Loading model...")
def load_model():
    model = joblib.load("final_house_model.joblib")
    return  model
# Load the preprocessor (e.g., column transformer, scaler, etc.) from file
@st.cache_resource(show_spinner="Loading converter...")
def load_converter():
    converter = joblib.load("final_converter.joblib")
    return converter
# Load the list of column names used for feature engineering
@st.cache_resource(show_spinner="Loading column names...")
def load_col_names():
    col_names = joblib.load("poly_columns.joblib")
    return col_names
# Make predictions using the model and input data
@st.cache_data(show_spinner="Predicting...")
def make_prediction(_model, _converter, _col_names, house_type, bedrooms, bathrooms, toilets, parking_spaces):
    # Prepare categorical data
    cat_df = pd.DataFrame([house_type], columns=['HouseType'])
    cat_encoded = pd.get_dummies(cat_df, drop_first=True)

    # Prepare numerical data
    num_df = pd.DataFrame([[bedrooms, bathrooms, toilets, parking_spaces]], 
                          columns=['Bedrooms', 'Bathrooms', 'Toilets', 'Parking Spaces'])

    # Combine numerical and encoded categorical data
    combined_df = pd.concat([num_df, cat_encoded], axis=1)
    combined_df = combined_df.reindex(columns=col_names, fill_value=0)

    # Transform data and make prediction
    transformed_data = converter.transform(combined_df.values)
    prediction = model.predict(transformed_data)
    rounded_prediction = round(prediction[0])

    return f'The estimated rent price for the selected house type is around {rounded_prediction} Naira'

# Streamlit app
def main():
    st.title('House Rent Price Estimator')

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        bedrooms = st.number_input('Number of Bedrooms', min_value=0, max_value=100, value=1, step=1)
        bathrooms = st.slider('Number of Bathrooms', min_value=0, max_value=100, value=1, step=1)
        house_type = st.selectbox('House Type', ("DD - Detached Duplex", 'TD - Terraced Duplex', "SDD - Semi Detached Duplex", 'A - Apartment'))

    with col2:
        parking_spaces = st.number_input('Number of Parking Spaces', min_value=0.0, max_value=100.0, value=1.0, step=1.0)
        toilets = st.slider('Number of Toilets', min_value=0, max_value=100, value=1, step=1)

    if st.button('Apply', type='primary'):
        model = load_model()
        converter = load_converter()
        col_names = load_col_names()
        prediction = make_prediction(model, converter, col_names, house_type, bedrooms, bathrooms, toilets, parking_spaces)
        st.write(prediction)

if __name__ == '__main__':
    main()
