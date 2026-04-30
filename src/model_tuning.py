import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import root_mean_squared_log_error

def objective(trial, factory, features, train_data):

    # Use full training data for hyperparameter tuning
    X = train_data[features]
    y = np.log1p(train_data['trip_duration'])

    # Define the hyperparameters to tune
    param = {
        'n_estimators': trial.suggest_int('n_estimators', 100, 1000),
        'max_depth': trial.suggest_int('max_depth', 3, 20),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3, log=True),
        'subsample': trial.suggest_float('subsample', 0.5, 1.0),
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.5, 1.0),
        'min_child_weight': trial.suggest_int('min_child_weight', 1, 10),
        'gamma': trial.suggest_float('gamma', 0, 5),
        'reg_alpha': trial.suggest_float('reg_alpha', 0, 5),
        'reg_lambda': trial.suggest_float('reg_lambda', 0, 5)
    }

    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    rmse_scores = []

    # Train the model with the current hyperparameters and evaluate using cross-validation
    for train_idx, y_idx in kf.split(X):
        X_train, X_val = X.iloc[train_idx], X.iloc[y_idx]
        y_train, y_val = y.iloc[train_idx], y.iloc[y_idx]

        model = factory(**param)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_val)
        rmse = root_mean_squared_log_error(y_val, y_pred)
        rmse_scores.append(rmse)

    
    # Evaluate the model on the validation set
    y_pred = model.predict(X)
    rmse = root_mean_squared_log_error(y, y_pred)
    
    # Return the average RMSE across all folds
    return np.mean(rmse_scores)