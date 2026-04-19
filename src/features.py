import pandas as pd
import numpy as np

def preprocess_trip_data(df):
    # Remove trips with zero passengers
    df = df[df["passenger_count"] > 0]

    # Remove outliers based on trip duration (keep trips between 1 minute and 2 hours)
    df = df[(df["trip_duration"] > 60) &
            (df["trip_duration"] < 3600 * 2)]
    
    return df

def convert_to_datetime(df):
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    return df

def extract_datetime_features(df):
    df["pickup_hour"] = df["pickup_datetime"].dt.hour
    df["pickup_day"] = df["pickup_datetime"].dt.dayofweek
    df["pickup_month"] = df["pickup_datetime"].dt.month
    return df

def create_rush_hour_feature(df):
    df['rush_hour'] = (df['pickup_hour'].isin([8,9,10,16,17,18,19]).astype(int) & 
                       df['pickup_day'].isin([0,1,2,3,4]).astype(int))
    return df

def calculate_manhattan_distance(lat1, lon1, lat2, lon2):
    return np.abs(lat2 - lat1) + np.abs(lon2 - lon1)

def calculate_haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometers

    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)

    a = np.sin(delta_phi / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(delta_lambda / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return R * c