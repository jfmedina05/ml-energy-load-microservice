# Project Overview
## Jaiden Medina
Using the energy efficiency dataset, this work describes the development of a predictive machine learning model to estimate heating and cooling loads in buildings. A Random Forest regression model was used, optimized, and exported for deployment as a cloud-based microservice.

# Project Repository Checklist
- [x] .gitignore
- [x] updated README.md

## Model Development
- [x] E222_Lab2and3_S25_INITIALS (1).ipynb
- [x] E222_Lab2and3_S25_INITIALS.ipynb - Colab.pdf
- [x] rfr.pkl
- [x] README.md
 
## Week 1
- [x] ML Refresh Activity (ipynb)
- [x] Week 1 pre-lab document

## Week 2
- [x] E222_Lab2and3_S25_INITIALS (1).ipynb
- [x] E222_Lab2and3_S25_INITIALS.ipynb - Colab.pdf
- [x] rfr.pkl
- [x] Project Description (DOCX)
- [x] Week 2 pre-lab document
- [x] README.md (project data and model documentation)

## Week 4
- [x] Model load test file (ipynb)
- [x] Model load test file (pdf)
- [x] Lab 4 description file (pdf)
- [x] Project Description (DOCX)
- [x] myFirstApp directory containing 
    * server.py
    * master.yml
    * requirements.txt
    * src directory (containing hello.py)
- [x] Week 4 pre-lab document
- [x] README.md (lab details provided)

## Week 5
- [x] Week 5 Lab: Customizing APIs
    * Created relevant endpoints using Swagger Editor
    * Developed functions to complement endpoints
    * Tested service endpoints using Jetstream2 virtual machines
- [x] Part I: Github and Jetstream2
    * Updated individual Git repository with Week 5 contents
    * Activated virtual environment and navigated repository
    * Reviewed `src` folder contents, `requirements.txt`, and virtual environments
- [x] Part II: Endpoint Exploration
    * Used Swagger Editor to create OpenAPI Specification (YAML file)
    * Identified and explored endpoints: path parameters, query parameters, POST vs. GET requests
    * Deployed and tested service on Jetstream2 VM
    * Verified endpoints `/hello`, `/sum`, `/file`, `/list`, and `/readfile`
- [x] Part III: Custom Endpoints
    * Implemented `/model_info` endpoint in `master.yml`
    * Completed `model.py` with model specifics
    * Created `/prediction` endpoint for file uploads and predictions
    * Integrated `rfr.pkl` model into `model.py`
    * Developed `/performance` endpoint to provide accuracy/performance metrics
    * Updated `requirements.txt` as needed
- [x] Final Steps
    * Committed and pushed Week 5 lab work to GitHub
    * Deactivated virtual environment and shelved VM instance

## Week 6
- [x] Week 6 Lab: More on Customizing APIs
    * Further developed and refined API endpoints using Swagger Editor
    * Created functions to complement new endpoints
    * Tested service endpoints using Jetstream2 virtual machines
- [x] Updating and Testing on Jetstream2
    * Logged into ACCESS account and launched Jetstream2 instance
    * Updated individual Git repository with Week 6 contents
    * Activated virtual environment (`source .venv/bin/activate`)
    * Reviewed provided data folder and testing script for debugging
- [x] Custom Endpoints Implementation
    * Checked comments in `model.py` and updates in `master.yml`
    * Implemented `/model_info` endpoint for model details
    * Completed `model.py` with model specifics and tested endpoint
    * Developed `/prediction` endpoint to handle file uploads and return predictions
    * Integrated `rfr.pkl` model and verified `file_predict` function
    * Created `/performance` endpoint to provide model performance metrics
    * Updated `requirements.txt` for any additional dependencies
- [x] Final Steps
    * Committed and pushed Week 6 lab work to GitHub
    * Deactivated virtual environment and shelved VM instance

## Week 7
- [x] Week 06/07 Lab: More on Customizing APIs
    * Continued refining API endpoints using Swagger Editor
    * Developed additional functions and tested services on Jetstream2
- [x] Updating and Testing on Jetstream2
    * Pulled latest updates from GitHub repositories
    * Activated virtual environment (`source .venv/bin/activate`)
    * Utilized the provided data folder for testing before connecting endpoints
- [x] New Custom Endpoints Implementation
    * `/model_info` endpoint finalized and tested
    * `/prediction` endpoint updated to handle file uploads and generate predictions
    * `/performance` endpoint added to return accuracy or other metrics
    * `/figure` endpoint created to generate histograms from test data
    * `/html` endpoint implemented to display histograms in a separate tab
- [x] myMLAppV1 Folder Structure
    * Organized all relevant files for the ML app, including:
        - `src` folder with all scripts
        - `requirements.txt` for dependencies
        - `master.yml` for API configuration
- [x] Final Steps
    * Committed and pushed Week 7 lab work to GitHub
    * Deactivated virtual environment and shelved VM instance
