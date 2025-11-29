"""
Streamlit Web App for House Price Prediction
This creates an interactive web interface for the ML model
"""
import streamlit as st
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import json

# Page config
st.set_page_config(
    page_title="🏠 House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# Title
st.title("🏠 House Price Predictor")
st.markdown("Predict house prices using Machine Learning")

# Sidebar for model info
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This app predicts house prices using a trained Linear Regression model.
    
    **Model:** Linear Regression  
    **Framework:** Scikit-learn  
    **MLOps:** ZenML + MLflow
    """)
    
    st.header("📊 Model Info")
    st.info("R² Score: ~0.58 (58% variance explained)")

# Main form
st.header("📝 Enter House Details")

# Create input form with key features
col1, col2 = st.columns(2)

with col1:
    lot_area = st.number_input("Lot Area (sq ft)", min_value=0, value=9600)
    gr_liv_area = st.number_input("Above Grade Living Area (sq ft)", min_value=0, value=1710)
    overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
    overall_cond = st.slider("Overall Condition (1-10)", 1, 10, 7)
    year_built = st.number_input("Year Built", min_value=1800, max_value=2024, value=1961)
    year_remod = st.number_input("Year Remodeled", min_value=1800, max_value=2024, value=1961)
    total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", min_value=0, value=850)
    first_flr_sf = st.number_input("1st Floor Area (sq ft)", min_value=0, value=856)

with col2:
    second_flr_sf = st.number_input("2nd Floor Area (sq ft)", min_value=0, value=854)
    full_bath = st.number_input("Full Bathrooms", min_value=0, value=1)
    half_bath = st.number_input("Half Bathrooms", min_value=0, value=0)
    bedrooms = st.number_input("Bedrooms Above Grade", min_value=0, value=3)
    tot_rms_abv_grd = st.number_input("Total Rooms Above Grade", min_value=0, value=7)
    fireplaces = st.number_input("Fireplaces", min_value=0, value=2)
    garage_cars = st.number_input("Garage Cars", min_value=0, value=2)
    garage_area = st.number_input("Garage Area (sq ft)", min_value=0, value=500)

# Additional features (with defaults)
st.subheader("Additional Features")
col3, col4 = st.columns(2)

with col3:
    lot_frontage = st.number_input("Lot Frontage (ft)", min_value=0, value=80)
    mas_vnr_area = st.number_input("Masonry Veneer Area (sq ft)", min_value=0, value=0)
    bsmtfin_sf_1 = st.number_input("Basement Finished Area 1 (sq ft)", min_value=0, value=700)
    bsmtfin_sf_2 = st.number_input("Basement Finished Area 2 (sq ft)", min_value=0, value=0)

with col4:
    bsmt_unf_sf = st.number_input("Basement Unfinished Area (sq ft)", min_value=0, value=150)
    wood_deck_sf = st.number_input("Wood Deck Area (sq ft)", min_value=0, value=210)
    open_porch_sf = st.number_input("Open Porch Area (sq ft)", min_value=0, value=0)
    mo_sold = st.number_input("Month Sold", min_value=1, max_value=12, value=5)
    yr_sold = st.number_input("Year Sold", min_value=2000, max_value=2024, value=2010)

# Predict button
if st.button("🔮 Predict Price", type="primary"):
    try:
        # Prepare input data
        input_data = {
            "Order": [1],
            "PID": [5286],
            "MS SubClass": [20],
            "Lot Frontage": [float(lot_frontage)],
            "Lot Area": [int(lot_area)],
            "Overall Qual": [int(overall_qual)],
            "Overall Cond": [int(overall_cond)],
            "Year Built": [int(year_built)],
            "Year Remod/Add": [int(year_remod)],
            "Mas Vnr Area": [float(mas_vnr_area)],
            "BsmtFin SF 1": [float(bsmtfin_sf_1)],
            "BsmtFin SF 2": [float(bsmtfin_sf_2)],
            "Bsmt Unf SF": [float(bsmt_unf_sf)],
            "Total Bsmt SF": [float(total_bsmt_sf)],
            "1st Flr SF": [int(first_flr_sf)],
            "2nd Flr SF": [int(second_flr_sf)],
            "Low Qual Fin SF": [0],
            "Gr Liv Area": [float(gr_liv_area)],
            "Bsmt Full Bath": [0],
            "Bsmt Half Bath": [0],
            "Full Bath": [int(full_bath)],
            "Half Bath": [int(half_bath)],
            "Bedroom AbvGr": [int(bedrooms)],
            "Kitchen AbvGr": [1],
            "TotRms AbvGrd": [int(tot_rms_abv_grd)],
            "Fireplaces": [int(fireplaces)],
            "Garage Yr Blt": [int(year_built)],
            "Garage Cars": [int(garage_cars)],
            "Garage Area": [float(garage_area)],
            "Wood Deck SF": [float(wood_deck_sf)],
            "Open Porch SF": [float(open_porch_sf)],
            "Enclosed Porch": [0],
            "3Ssn Porch": [0],
            "Screen Porch": [0],
            "Pool Area": [0],
            "Misc Val": [0],
            "Mo Sold": [int(mo_sold)],
            "Yr Sold": [int(yr_sold)],
        }
        
        # Convert to DataFrame
        df = pd.DataFrame(input_data)
        
        # Try to load model from MLflow
        try:
            # Try to load from latest run
            # You may need to update this path based on your MLflow setup
            model_uri = "runs:/37fd669970544f8ca4bbc9dc7f821cf6/model"  # Update with your run ID
            model = mlflow.sklearn.load_model(model_uri)
            
            # Make prediction
            prediction = model.predict(df)
            predicted_price = prediction[0]
            
            # Display result
            st.success(f"## 🎯 Predicted House Price: ${predicted_price:,.2f}")
            
            # Additional info
            st.info(f"""
            **Note:** This is a prediction based on the provided features.
            - Model accuracy: ~58% (R² Score)
            - Actual price may vary based on market conditions
            """)
            
        except Exception as e:
            st.error(f"Model loading error: {str(e)}")
            st.info("""
            **To fix this:**
            1. Ensure MLflow model is accessible
            2. Update model_uri in app.py with your run ID
            3. Or deploy model separately and call API endpoint
            """)
            
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
**Built with:**
- 🐍 Python
- 🤖 Scikit-learn
- 📊 MLflow
- 🔄 ZenML
- 🎨 Streamlit
""")

