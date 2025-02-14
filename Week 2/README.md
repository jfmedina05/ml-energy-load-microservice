# Project Weeks 2 & 3, Energy Effieciency Dataset, Random Forest Regression
## Developer(s): Jaiden Medina

## Dataset Description
The goal of this project was to take the dataset created by **Angeliki Xifara** and processed by **Athanasios Tsanas** who is a Civil/Structural Engineer and the other is affiliated with the Oxford Centre for Industrial and Applied Mathematics at the University of Oxford in the United Kingdom, respectively. This research was documented in **“Accurate quantitative estimation of energy performance of residential buildings using statistical machine learning tools,” Energy and Buildings, vol. 49** and the research aligned with a  **"body of research on the topic of energy performance of buildings, EPB, due to growing concerns about energy waste and its perennial adverse impact on the environment"**.

The dataset was generated using simulations of "12 different building shapes simulated in Ecotect". These simulations were based on elementary cubes (3.5m × 3.5m × 3.5m) that were combined to form "12 building forms where each building form is composed of 18 elements (elementary cubes)." Despite variations in surface areas and dimensions, all buildings maintained an identical volume of 771.75 m³. Additionally, "the materials used for each of the 18 elements are the same for all building forms," with selections made from "the newest and most common materials in the building construction industry"

A total of 768 building configurations were created for the simulation. "The dataset comprises 768 samples and 8 features, aiming to predict two real-valued responses" [1, Kaggle - Data Set Information]. These eight features, labeled X1 through X8, include Relative Compactness, Surface Area, Wall Area, Roof Area, Overall Height, Orientation, Glazing Area, and Glazing Area Distribution. They were used to predict Heating Load (y1) and Cooling Load (y2).

## Problem Statement
This dataset predicts the heating and cooling loads of buildings based on 8 structural features, including surface area, height, and glazing distribution. Simulated from 12 building shapes, it helps understand how building design impacts energy efficiency, contributing to efforts to reduce energy waste.

## Model
I chose this model because after exploring and cleaning the dataset, I identified the need for scaling due to the significant differences in feature ranges, which could negatively impact model performance. Standard Scaling was selected to normalize the data, ensuring that it works well with models like Random Forest. Since dimensionality reduction wasn't necessary (the data was balanced and sufficiently dimensional), I focused on finding the best model for predicting continuous variables like Heating Load and Cooling Load. Random Forest Regression was the most suitable option, as it handles non-linear relationships and prevents overfitting, offering reliable predictions for energy efficiency based on building features.

### HyperParameters
The final hyperparameters I selected were max_depth=1, max_leaf_nodes=None, min_samples_leaf=20, min_samples_split=10, n_estimators=100, random_state=42, and n_jobs=-1. These adjustments successfully reduced overfitting while maintaining a strong predictive capability, ultimately achieving the desired accuracy.

## Final Results
Using the aforementioned hyperparameters and model, I was able to achieve an accuracy of ~80%. This was pursued because my initial accuracy was 99.7% which showed significant signs of overfitting. It can be assumed that the model effectively found the right set of parameters to maximize heating and cooling loads (y1-y2) without overfitting or underfitting the data based on the characteristics (x1-x8). 
