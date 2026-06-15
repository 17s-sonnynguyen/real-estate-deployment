# Real Estate Amenities Deployment Project

## Overview

This project demonstrates the complete workflow of deploying a machine learning model using a real estate amenities dataset. The primary focus is on deployment rather than advanced machine learning techniques.

A Logistic Regression model was trained to predict whether a property has a pool based on available features. The trained model was then saved and integrated into a FastAPI application capable of serving predictions through an HTTP API.

The project illustrates how a machine learning model can move beyond a Jupyter notebook and become a usable prediction service.

---

## Dataset

The dataset contains real estate amenity information for approximately 49,000 properties.

### Features

* `unified_id` – Unique property identifier
* `month` – Observation month
* `hot_tub` – Indicates whether the property has a hot tub (1 = Yes, 0 = No)
* `pool` – Indicates whether the property has a pool (1 = Yes, 0 = No)

### Target Variable

* `pool`

---

## Project Structure

```text
real-estate-deployment/
│
├── app.py
├── amenities.csv
├── pool_predictor.pkl
├── requirements.txt
└── RealEstateDeployment.ipynb
```

### File Descriptions

* `app.py` – FastAPI application
* `amenities.csv` – Original dataset
* `pool_predictor.pkl` – Saved machine learning model
* `requirements.txt` – Project dependencies
* `RealEstateDeployment.ipynb` – Jupyter notebook containing the project workflow

---

## Machine Learning Model

### Algorithm

Logistic Regression

### Features Used

* `hot_tub`
* `month_num`

### Model Performance

Accuracy: **92.13%**

The model was intentionally kept simple because the primary objective of this project was to learn deployment concepts rather than model optimization.

---

## API Development

The trained model was deployed locally using FastAPI.

### API Endpoints

#### Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Real Estate Pool Prediction API is running."
}
```

#### Prediction Endpoint

```http
POST /predict
```

Example Request:

```json
{
  "hot_tub": 1,
  "month_num": 12
}
```

Example Response:

```json
{
  "hot_tub": 1,
  "month_num": 12,
  "pool_prediction": 0
}
```

---

## Running the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start the API

```bash
uvicorn app:app --reload
```

### Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

The Swagger interface allows users to test the API directly from their browser.

---

## Deployment Workflow

The project follows a deployment-oriented workflow:

1. Load and prepare data
2. Train a machine learning model
3. Save the trained model
4. Build a FastAPI application
5. Connect the model to the API
6. Prepare deployment files
7. Configure cloud deployment settings
8. Test the deployed application

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* FastAPI
* Uvicorn
* GitHub

---

## Key Learning Outcomes

Through this project, the following deployment concepts were explored:

* Machine learning model persistence using Joblib
* Building REST APIs with FastAPI
* Serving predictions through HTTP requests
* Preparing deployment-ready project structures
* Version control using Git and GitHub
* Cloud deployment configuration

The project demonstrates how machine learning models can be transformed from notebook experiments into reusable services suitable for real-world applications.
