def preprocess_trip_data(df):
    # Remove trips with zero passengers
    df = df[df["passenger_count"] > 0]

    # Remove outliers based on trip duration (keep trips between 1 minute and 2 hours)
    df = df[(df["trip_duration"] > 60) &
            (df["trip_duration"] < 3600 * 2)]
    
    return df