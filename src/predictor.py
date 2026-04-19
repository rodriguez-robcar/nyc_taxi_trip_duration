def predictor(model, train_data, test_data, features):
    
    X_test = test_data[features]

    model.fit(train_data[features], train_data["trip_duration"])

    Y_pred_test = model.predict(X_test)

    test_data["trip_duration"] = Y_pred_test

    return Y_pred_test