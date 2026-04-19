from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_log_error

def train_model(model, features, train_data):

    X = train_data[features]
    y = train_data["trip_duration"]

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_val)
    score = root_mean_squared_log_error(y_val, y_pred)

    return score