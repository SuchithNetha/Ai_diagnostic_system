# 🏠 House Price Predictor - ML Pipeline Project

A production-grade Machine Learning pipeline for predicting housing prices using the Ames Housing dataset. Built with **ZenML**, **MLflow**, and **Scikit-learn**, implementing design patterns for maintainability and extensibility.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![ZenML](https://img.shields.io/badge/ZenML-0.64.0-orange.svg)
![MLflow](https://img.shields.io/badge/MLflow-2.15.1-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Design Patterns](#-design-patterns)
- [Results](#-results)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- ✅ **Complete ML Pipeline**: End-to-end pipeline from data ingestion to model deployment
- ✅ **Design Patterns**: Factory, Strategy, and Template patterns for extensibility
- ✅ **Experiment Tracking**: MLflow integration for tracking experiments and models
- ✅ **Model Deployment**: REST API service for predictions
- ✅ **Modular Architecture**: Easy to extend and modify
- ✅ **Production-Ready**: Follows MLOps best practices

## 🏗️ Architecture

The project implements a modular architecture using design patterns:

### Design Patterns Used

1. **Factory Pattern** - Data ingestion based on file type
2. **Strategy Pattern** - Flexible strategies for data processing
3. **Template Pattern** - Consistent pipeline step structure

### Pipeline Flow

```
Data Ingestion → Missing Values → Feature Engineering → Outlier Detection 
    → Data Splitting → Model Training → Model Evaluation → Deployment
```

## 📁 Project Structure

```
prices-predictor-system/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── config.yaml              # ZenML configuration
│
├── run_pipeline.py          # Training pipeline entry point
├── run_deployment.py        # Deployment pipeline entry point
├── sample_predict.py        # Example prediction script
│
├── pipelines/               # Pipeline definitions
│   ├── training_pipeline.py
│   └── deployment_pipeline.py
│
├── steps/                   # ZenML pipeline steps
│   ├── data_ingestion_step.py
│   ├── handle_missing_values_step.py
│   ├── feature_engineering_step.py
│   ├── outlier_detection_step.py
│   ├── data_splitter_step.py
│   ├── model_building_step.py
│   ├── model_evaluator_step.py
│   └── ...
│
├── src/                     # Core business logic
│   ├── ingest_data.py       # Factory pattern
│   ├── handle_missing_values.py
│   ├── feature_engineering.py
│   ├── outlier_detection.py
│   ├── data_splitter.py
│   ├── model_building.py
│   └── model_evaluator.py
│
├── data/                    # Raw data
│   └── archive.zip          # Ames Housing dataset
│
├── analysis/                # Exploratory Data Analysis
│   └── EDA.ipynb
│
└── explanations/            # Design pattern examples
    ├── factory_design_patter.py
    ├── strategy_design_pattern.py
    └── template_design_pattern.py
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/prices-predictor-system.git
   cd prices-predictor-system
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize ZenML** (if not already done)
   ```bash
   zenml init
   ```

5. **Set up ZenML stack with MLflow**
   ```bash
   # Create MLflow tracker
   zenml experiment-tracker register mlflow_tracker --flavor=mlflow
   
   # Create MLflow model deployer
   zenml model-deployer register mlflow --flavor=mlflow
   
   # Create and activate stack
   zenml stack register local-mlflow-stack \
       -a default \
       -o default \
       -e mlflow_tracker \
       -d mlflow
   
   zenml stack set local-mlflow-stack
   ```

## 💻 Usage

### 1. Training the Model

Run the training pipeline:

```bash
python run_pipeline.py
```

This will:
- Ingest and process the data
- Train the model
- Evaluate performance
- Save the model to MLflow

### 2. View MLflow UI

After training, view experiment results:

```bash
mlflow ui --backend-store-uri ./mlruns
```

Open `http://localhost:5000` in your browser.

### 3. Deployment (Linux/macOS)

Deploy the model as a REST API:

```bash
python run_deployment.py
```

**Note**: Automatic deployment has limitations on Windows. See [Troubleshooting](#-troubleshooting).

### 4. Make Predictions

#### Using the sample script:
```bash
python sample_predict.py
```

#### Using HTTP request:
```bash
curl -X POST http://127.0.0.1:8000/invocations \
  -H "Content-Type: application/json" \
  -d @sample_data.json
```

## 🎨 Design Patterns

### Factory Pattern
Creates appropriate data ingestor based on file type (ZIP, CSV, JSON, etc.)

### Strategy Pattern
Allows switching between different strategies for:
- Missing value handling (drop, fill with mean/median/mode)
- Feature engineering (log transform, scaling, encoding)
- Outlier detection (Z-score, IQR)
- Model evaluation

### Template Pattern
Ensures consistent structure across all pipeline steps

## 📊 Results

The model achieves:
- **R² Score**: ~0.58 (58% variance explained)
- **MSE**: Tracked in MLflow
- **Model**: Linear Regression with preprocessing pipeline

View detailed metrics in the MLflow UI.

## 📚 Documentation

- [PROJECT_ANALYSIS.md](PROJECT_ANALYSIS.md) - Complete project analysis
- [INTERVIEW_QA.md](INTERVIEW_QA.md) - Interview questions and answers
- [explanations/](explanations/) - Design pattern examples

## 🔧 Troubleshooting

### Windows Deployment Issue

If you encounter daemon-related errors on Windows:

1. **Manual Model Serving**:
   ```bash
   # Get the latest run ID from MLflow
   mlflow models serve -m runs:/<run_id>/model -p 8000 --host 127.0.0.1
   ```

2. **Alternative**: Use WSL (Windows Subsystem for Linux) for full daemon support

### Common Issues

- **ZenML stack not found**: Run `zenml stack set local-mlflow-stack`
- **Port 8000 already in use**: Change port in deployment config
- **Missing data**: Ensure `data/archive.zip` exists

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Ames Housing Dataset
- ZenML team for the amazing MLOps framework
- MLflow for experiment tracking
- Scikit-learn for ML algorithms

## 📧 Contact

Your Name - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/yourusername/prices-predictor-system](https://github.com/yourusername/prices-predictor-system)

---

⭐ If you found this project helpful, please give it a star!

