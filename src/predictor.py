import numpy as np

def predictor(model, train_data, test_data, features):
    
    X_test = test_data[features]

    model.fit(train_data[features], np.log1p(train_data["trip_duration"]))

    Y_pred_test = np.expm1(model.predict(X_test))

    test_data["trip_duration"] = Y_pred_test

    return Y_pred_test