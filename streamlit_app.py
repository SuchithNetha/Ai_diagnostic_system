import streamlit as st
import pandas as pd
import numpy as np
from zenml.client import Client

# 1. Page Configuration
st.set_page_config(page_title="AI Medical Diagnostician", page_icon="🏥")

st.title("🏥 Medical Diagnosis Predictor")
st.markdown("---")

# 2. Model Loading Function
def load_model():
    try:
        client = Client()
        pipeline = client.get_pipeline("train_pipeline")
        last_run = pipeline.last_run
        model_artifact = last_run.steps["train_model"].output
        model = model_artifact.load() 
        return model
    except Exception as e:
        return None

model = load_model()

# Sidebar Status
if model:
    st.sidebar.success("✅ AI Brain Online")
else:
    st.sidebar.error("❌ AI Brain Offline. Run pipeline first.")

# 3. Define the UI Columns (This is what caused your error!)
st.subheader("Input Patient Symptoms")
col1, col2 = st.columns(2) # <--- These MUST be defined before the 'with' blocks

with col1:
    fever = st.checkbox("Fever")
    cough = st.checkbox("Cough")
    fatigue = st.checkbox("Fatigue")

with col2:
    nausea = st.checkbox("Nausea")
    headache = st.checkbox("Headache")
# 4. Disease Mapping (Update these names based on your dataset!)
# This turns "Class 0" into "Common Cold"
disease_map = {
    0: "Common Cold",
    1: "Influenza (Flu)",
    2: "COVID-19",
    3: "Bacterial Infection",
    4: "Allergies"
}

# 5. Prediction Logic
if st.button("Analyze Symptoms", type="primary"):
    if model:
        # Convert checkboxes to numeric input
        input_list = [1 if x else 0 for x in [fever, cough, fatigue,nausea, headache]]
        features = np.array([input_list])
        
        # Predict
        prediction_id = model.predict(features)[0]
        
        # Get name from map (default to the ID if not found)
        disease_name = disease_map.get(prediction_id, f"Category {prediction_id}")
        
        st.markdown("---")
        st.subheader("Diagnosis Result:")
        st.success(f"**Predicted Condition:** {disease_name}")
        st.info("Disclaimer: This tool is for educational purposes and provides preliminary AI estimates only.")
    else:
        st.error("The model is not available. Please ensure your ZenML pipeline has run successfully.")