# NYC Taxi Trip Duration Prediction
Predict taxi trip duration using historical trip data from Kaggle.

### Description
Kaggle competition to build a model that predicts the total ride duration of taxi trips in New York City. The primary dataset is one released by the NYC Taxi and Limousine Commission, which includes pickup time, geo-coordinates, number of passengers, and several other variables.

### Dataset Description
The dataset is based on the 2016 NYC Yellow Cab trip record data made available in Big Query on Google Cloud Platform. The data was originally published by the NYC Taxi and Limousine Commission (TLC). The data was sampled and cleaned for the purposes of this playground competition. Based on individual trip attributes, participants should predict the duration of each trip in the test set. Download: https://www.kaggle.com/competitions/nyc-taxi-trip-duration/data

### File descriptions
- train.csv - the training set (contains 1458644 trip records)
- test.csv - the testing set (contains 625134 trip records)

### Data fields

- id - a unique identifier for each trip
- vendor_id - a code indicating the provider associated with the trip record
- pickup_datetime - date and time when the meter was engaged
- dropoff_datetime - date and time when the meter was disengaged
- passenger_count - the number of passengers in the vehicle (driver entered value)
- pickup_longitude - the longitude where the meter was engaged
- pickup_latitude - the latitude where the meter was engaged
- dropoff_longitude - the longitude where the meter was disengaged
- dropoff_latitude - the latitude where the meter was disengaged
- store_and_fwd_flag - This flag indicates whether the trip record was held in vehicle memory before sending to the vendor because the vehicle did not have a connection to the server - Y=store and forward; N=not a store and forward trip
- trip_duration - duration of the trip in seconds

### Feature Engineering

- Base features: vendor_id, pickup_hour, pickup_day, pickup_month, passenger_count, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude
- Engineered features: base features + manhattan_distance, haversine_distance, rush_hour

### Models

- Random Forest (baseline)
- XGBoost
- Gradient Boosting
- LGBM
- CatBoost

### Evaluation

The evaluation metric for this competition is Root Mean Squared Logarithmic Error.

The RMSLE is calculated as

<img width="391" height="129" alt="image" src="https://github.com/user-attachments/assets/d79919bd-363f-494b-bb83-71bb0262e7a0" />



Where:

\\(\epsilon\\) is the RMSLE value (score)<br/>
\\(n\\) is the total number of observations in the (public/private) data set,<br/>
\\(y_l\\) is your prediction of trip duration, and<br/>
\\(y\\) is the actual trip duration for \\(i\\).<br/>
\\(\log(x)\\) is the natural logarithm of \\(x\\)<br/>

### Validation
- Time-based split (simulates real-world prediction)

### Results
| Model | Features | Score |
| :--- | :----: | ---: |
| XGB_engineered | Base features + engineered | 0.045749 |
| GBR_engineered | Base features + engineered | 0.045789 |
| XGB_base | Base features | 0.048479 |
| Cat_engineered | Base features + engineered | 0.048498 |
| GBR_base | Base features | 0.048625 |
| LGBM_engineered	 | Base features + engineered | 0.048999|
| RF_engineered | Base features + engineered | 0.052283|
| Cat_base | Base features | 0.053268 |
| LGBM_base | Base features | 0.056816 |
| RF_base | Base features | 0.070132 |
