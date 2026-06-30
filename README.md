# ML Energy Load Microservice

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">
  <img alt="pandas" src="https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white">
  <img alt="NumPy" src="https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white">
  <img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white">
  <img alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-11557C?logo=python&logoColor=white">
  <img alt="Random Forest" src="https://img.shields.io/badge/Random%20Forest-Regression-228B22?logoColor=white">
  <img alt="Flask" src="https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white">
  <img alt="REST API" src="https://img.shields.io/badge/REST%20API-Microservice-2C8EBB?logoColor=white">
  <img alt="Swagger" src="https://img.shields.io/badge/Swagger%20%2F%20OpenAPI-85EA2D?logo=swagger&logoColor=black">
  <img alt="YAML" src="https://img.shields.io/badge/YAML-CB171E?logo=yaml&logoColor=white">
  <img alt="Ubuntu" src="https://img.shields.io/badge/Ubuntu%2024.04-E95420?logo=ubuntu&logoColor=white">
  <img alt="Linux VM" src="https://img.shields.io/badge/Linux%20VM-Cloud%20Deployment-FCC624?logo=linux&logoColor=black">
  <img alt="Jetstream2" src="https://img.shields.io/badge/Jetstream2-Cloud%20Infrastructure-4B0082?logoColor=white">
  <img alt="Google Colab" src="https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white">
  <img alt="Jupyter Notebook" src="https://img.shields.io/badge/Jupyter%20Notebook-F37626?logo=jupyter&logoColor=white">
  <img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white">
  <img alt="Markdown" src="https://img.shields.io/badge/Markdown-000000?logo=markdown&logoColor=white">
</p>

A cloud-deployed machine learning microservice for predicting building heating and cooling loads using a Random Forest regression model. This project combines model development, REST API design, cloud deployment, and performance evaluation into an end-to-end intelligent systems application.

---

## Overview

This project predicts residential building energy loads from structural design features such as relative compactness, surface area, wall area, roof area, overall height, orientation, glazing area, and glazing area distribution.

The model was trained on the Energy Efficiency dataset and deployed as a cloud-based Flask microservice, allowing users to submit data and receive heating and cooling load predictions through documented API endpoints.

This project was developed as part of ENGR-E 222 and presented at the Indiana University Luddy School of Informatics, Computing, and Engineering Undergraduate Poster Symposium.

---

## Project Objective

The goal of this project was to build a complete machine learning service that could:

- Predict heating and cooling loads for residential buildings
- Train and optimize a Random Forest regression model
- Expose model functionality through REST API endpoints
- Deploy the service on cloud infrastructure
- Provide performance metrics and visual outputs
- Document the full system for reproducibility and presentation

---

## Poster

The project poster summarizes the model architecture, dataset, training process, performance metrics, service infrastructure, and future work.

[View Symposium Poster](Assets/energy-load-microservice-poster.pdf)

---

## Dataset

The project used the Energy Efficiency dataset, which contains simulated residential building data.

### Dataset Details

- 768 simulated residential buildings
- Buildings composed of 3.5 m × 3.5 m × 3.5 m cubes
- Constant building volume of 771.75 m³
- 8 input features
- 2 target outputs: heating load and cooling load

### Input Features

- Relative Compactness
- Surface Area
- Wall Area
- Roof Area
- Overall Height
- Orientation
- Glazing Area
- Glazing Area Distribution

### Target Outputs

- Heating Load
- Cooling Load

---

## Model Development

The machine learning model uses a Multi-Output Random Forest Regressor to predict both heating and cooling loads.

Random Forest was selected because the relationships between building geometry and energy load are nonlinear, and ensemble models can improve generalization while reducing overfitting.

### Model Configuration

- Model: Multi-Output Random Forest Regressor
- Number of Trees: 100
- Maximum Tree Depth: 3
- Minimum Samples to Split: 10
- Minimum Samples per Leaf: 20
- Random Seed: 42
- Parallel Jobs: -1

### Preprocessing

- `StandardScaler` was used to normalize features
- Dataset split: 75% training / 25% testing
- `GridSearchCV` was used for initial hyperparameter selection
- Manual tuning was applied to improve generalization

---

## Results

The final model showed strong predictive performance for estimating building energy loads.

| Metric | Result |
|---|---:|
| Accuracy Score | 93.33% |
| R² Score | 0.9333 |
| Mean Absolute Error | 1.8772 |
| Mean Squared Error | 6.5556 |

### Feature Importance Insights

The most influential features were:

- Relative Compactness
- Overall Height

The least influential features were:

- Orientation
- Glazing Area Distribution

The correlation and feature importance analysis showed that building geometry had a strong effect on heating and cooling load prediction.

---

## Microservice Architecture

The trained model was deployed as a Flask-based REST API, allowing users to interact with the model through multiple service endpoints.

```text
Input Dataset
    ↓
Preprocessing
    ↓
Random Forest Model
    ↓
Flask REST API
    ↓
Prediction / Metrics / Visualization
    ↓
User Response
```

---

## API Endpoints

The service includes endpoints for model information, prediction, performance reporting, visualization, and web display.

| Endpoint | Purpose |
|---|---|
| `/model_info` | Returns model details and metadata |
| `/prediction` | Accepts uploaded data and returns heating/cooling load predictions |
| `/performance` | Returns model evaluation metrics |
| `/figure` | Generates a histogram or visual output |
| `/html` | Displays results in a browser-friendly format |

---

## Cloud Deployment

The service was deployed and tested on Jetstream2 cloud virtual machines.

### Deployment Stack

- Ubuntu 24.04.2
- Python 3.11.12
- Flask
- Pandas
- NumPy
- scikit-learn
- Matplotlib
- Swagger / OpenAPI
- GitHub
- Jetstream2 Cloud Infrastructure

---

## Repository Structure

```text
ml-energy-load-microservice/
├── Assets/
│   └── energy-load-microservice-poster.pdf
│
├── Model Development/
│   └── model training and development files
│
├── Week 1/
├── Week 2/
├── Week 4/
├── Week 5/
├── Week 6/
├── Week 7/
├── Week 8/
├── Week 9/
│
├── .gitignore
├── .gitattributes
└── README.md
```

---

## Tech Stack

### Languages & Libraries

- Python
- Pandas
- NumPy
- scikit-learn
- Matplotlib

### Machine Learning

- Random Forest Regression
- Multi-Output Regression
- StandardScaler
- GridSearchCV

### API & Deployment

- Flask
- REST API
- Swagger / OpenAPI
- YAML
- Jetstream2
- Linux Virtual Machines

### Tools

- GitHub
- Google Colab
- Jupyter Notebook
- Cloud VM Environment

---

## What I Learned

This project strengthened my understanding of how machine learning models move from experimentation to deployment.

Key learning outcomes included:

- Building and tuning a multi-output regression model
- Designing REST API endpoints around a trained model
- Deploying a model as a cloud-accessible microservice
- Evaluating model accuracy, error, and feature importance
- Documenting a technical system for both academic and engineering audiences
- Connecting machine learning performance to real-world energy efficiency applications

---

## Limitations

- The dataset is based on simulated building energy data
- Model performance may differ on real-world building data
- Additional features such as climate, materials, ventilation, and lighting loads could improve realism
- Deployment was designed for academic demonstration rather than production-scale use

---

## Future Improvements

- Train and evaluate the model on real-world building energy datasets
- Add additional input variables such as climate, material type, and ventilation load
- Compare Random Forest against Gradient Boosting, XGBoost, and neural network models
- Improve the API with authentication, validation, and better error handling
- Add Docker support for easier deployment
- Build a simple front-end interface for non-technical users

---

## Why This Project Matters

Energy-efficient building design is an important engineering challenge, and predictive modeling can help estimate performance earlier in the design process.

This project demonstrates how machine learning, cloud deployment, and API development can be combined into a complete intelligent system that turns a trained model into a usable engineering tool.
