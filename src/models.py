from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
import tempfile

tmp_dir = tempfile.mkdtemp()

def get_random_forest_model(**kwargs):
    
    defaults = {
        'n_estimators': 100,
        'max_depth': 10,
        'random_state': 42
    }

    defaults.update(kwargs)

    return RandomForestRegressor(**defaults)

def get_xgboost_model(**kwargs):
    
    defaults = {
        'n_estimators': 100,
        'max_depth': 10,
        'learning_rate': 0.1,
        'random_state': 42
    }

    defaults.update(kwargs)

    return XGBRegressor(**defaults)

def get_gbr_model(**kwargs):
    
    defaults = {
        'n_estimators': 100,
        'max_depth': 10,
        'learning_rate': 0.1,
        'random_state': 42
    }

    defaults.update(kwargs)
    return GradientBoostingRegressor(**defaults)

def get_lgbm_model(**kwargs):
    defaults = {
        'n_estimators': 100,
        'max_depth': 10,
        'learning_rate': 0.1,
        'random_state': 42
    }
    defaults.update(kwargs)
    return LGBMRegressor(**defaults)

def get_catboost_model(**kwargs):
    defaults = {
        'train_dir': tmp_dir,
        'n_estimators': 100,
        'max_depth': 10,
        'learning_rate': 0.1,
        'random_state': 42,
        'verbose': 0
    }
    defaults.update(kwargs)
    return CatBoostRegressor(**defaults)