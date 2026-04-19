from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor

def get_random_forest_model():
    return RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)

def get_xgboost_model():
    return XGBRegressor(n_estimators=100, max_depth=10, learning_rate=0.1, random_state=42)

def get_gbr_model():
    return GradientBoostingRegressor(n_estimators=100, max_depth=10, learning_rate=0.1, random_state=42)

def get_lgbm_model():
    return LGBMRegressor(n_estimators=100, max_depth=10, learning_rate=0.1, random_state=42)

def get_catboost_model():
    return CatBoostRegressor(n_estimators=100, max_depth=10, learning_rate=0.1, random_state=42, verbose=0)