import os
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso, Ridge
from sklearn.neural_network import MLPRegressor

# Step 1: Load the preprocessed data from data_processing/
X_train_scaled = pd.read_csv("data_processing/X_train_scaled.csv")
X_test_scaled = pd.read_csv("data_processing/X_test_scaled.csv")
y_train = pd.read_csv("data_processing/y_train.csv").values.ravel()
y_test = pd.read_csv("data_processing/y_test.csv").values.ravel()

# Step 2: Train models
models = {
    "lr_model": LinearRegression(),
    "ridge_model": Ridge(),
    "lasso_model": Lasso(),
    "nn_model": MLPRegressor(max_iter=10000, learning_rate_init=0.01)
}

# Step 3: Train and save each model
for model_name, model in models.items():
    model.fit(X_train_scaled, y_train)
    with open(f"models/{model_name}.pickle", "wb") as f:
        pickle.dump(model, f)

    # Print confirmation
    print(f"{model_name} has been saved.")