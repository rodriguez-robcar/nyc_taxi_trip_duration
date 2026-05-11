# NYC Taxi Trip Duration Prediction

### 📌 Project Overview
This project focuses on predicting the total ride duration of taxi trips in New York City. Using a dataset of approximately 1.45 million records, the goal is to build a regression model that can accurately estimate how long a trip will take based on pickup locations and timestamps.

### 🛠️ Tech Stack
- <b>Language</b>: Python

- <b>Libraries</b>: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

- <b>Models</b>: Random Forest, Gradient Boosting, XGBoost, LightGBM, CatBoost

### 📊 Dataset Description
The dataset is based on the 2016 NYC Yellow Cab trip record data made available in Big Query on Google Cloud Platform. The data was originally published by the NYC Taxi and Limousine Commission (TLC). The data was sampled and cleaned for the purposes of this playground competition. Based on individual trip attributes, participants should predict the duration of each trip in the test set. 



#### Data Setup

1. Initialize Directory: Create the data/raw folder structure to store the source files.

2. Data Placement: Download the NYC Taxi dataset from https://www.kaggle.com/competitions/nyc-taxi-trip-duration/data and move the raw CSVs into the /data/raw/ path to ensure the internal data loaders can find them.

#### File descriptions
- train.csv - the training set (contains 1458644 trip records)
- test.csv - the testing set (contains 625134 trip records)

#### Data fields

- <mark>id</mark> - a unique identifier for each trip
- <mark>vendor_id</mark> - a code indicating the provider associated with the trip record
- <mark>pickup_datetime</mark> - date and time when the meter was engaged
- <mark>dropoff_datetime</mark> - date and time when the meter was disengaged
- <mark>passenger_count</mark> - the number of passengers in the vehicle (driver entered value)
- <mark>pickup_longitude</mark> - the longitude where the meter was engaged
- <mark>pickup_latitude</mark> - the latitude where the meter was engaged
- <mark>dropoff_longitude</mark> - the longitude where the meter was disengaged
- <mark>dropoff_latitude</mark> - the latitude where the meter was disengaged
- <mark>store_and_fwd_flag</mark> - This flag indicates whether the trip record was held in vehicle memory before sending to the vendor because the vehicle did not have a connection to the server - Y=store and forward; N=not a store and forward trip
- <mark>trip_duration </mark> - duration of the trip in seconds <b>(Target Variable)</b>

### 🚀 Workflow

#### 1. Data Cleaning & Analysis

- Handled outliers to remove trips with unrealistic durations.

- Performed distribution analysis to identify skewed features.

#### 2. Feature Engineering

Created new features to capture temporal and spatial patterns:

- <b>Temporal</b>: Extracted hour, day_of_week, and month.

- <b>Binary Flags</b>: Created rush_hour to account for NYC traffic patterns.

- <b>Geospatial</b>: Calculated Haversine distance and Manhattan distance between pickup and dropoff points.

#### 3. Data Preprocessing

- <b>Ordinal Encoding (Best for Tree Models)</b>: Keep temporal features as numerical (1-12 or 0-23) because tree models can split based on ordering

#### 4. Modeling & Evaluation

Compared multiple models to find the best balance between speed and accuracy:

- <b>Random Forest</b>: Used as a robust baseline.

- <b>Gradient Boosting (XGBoost/LGBM/CatBoost)</b>: Optimized hyperparameters to minimize Root Mean Squared Logarithmic Error (RMSLE).

The evaluation metric for this competition is Root Mean Squared Logarithmic Error.

The RMSLE is calculated as

<img width="391" height="129" alt="image" src="https://github.com/user-attachments/assets/d79919bd-363f-494b-bb83-71bb0262e7a0" />



Where:

- $\epsilon$ is the RMSLE value (score)<br/>
- $n$ is the total number of observations<br/>
- $\hat{y}_i$ is the predicted trip duration<br/>
- $y_i$ is the actual trip duration for $i$.<br/>
- $\log(x)$ is the natural logarithm of $(x)$<br/>


### 📈 Results

- <b>Best Model</b>: XGBoost

- <b>Key Metric</b>: RMSLE: 0.45749

| Model | Features | Score |
| :--- | :----: | ---: |
| XGB_engineered | Base features + engineered | 0.45749 |
| GBR_engineered | Base features + engineered | 0.45789 |
| XGB_base | Base features | 0.48479 |
| Cat_engineered | Base features + engineered | 0.48498 |
| GBR_base | Base features | 0.48625 |
| LGBM_engineered	 | Base features + engineered | 0.48999|
| RF_engineered | Base features + engineered | 0.52283|
| Cat_base | Base features | 0.53268 |
| LGBM_base | Base features | 0.56816 |
| RF_base | Base features | 0.70132 |
