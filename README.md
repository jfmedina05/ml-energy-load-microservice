# ML Energy Load Microservice

A cloud-deployed machine learning microservice that predicts building heating and cooling loads using a Random Forest regression model. This project combines model development, REST API design, and cloud deployment to deliver real-time predictions through a documented service interface.

## Tech Stack
Python, scikit-learn, Flask, OpenAPI/Swagger, YAML, Jetstream2, GitHub

## Features
- Predicts building energy loads from uploaded input data
- Exposes REST endpoints for model info, predictions, performance metrics, and visualizations
- Deployable on cloud virtual machines for real-time use

## Results
- Trained and exported a Random Forest model for heating/cooling load prediction
- Built a working API with endpoints including `/model_info`, `/prediction`, `/performance`, `/figure`, and `/html`
- Hosted and tested the service on Jetstream2 cloud VMs
