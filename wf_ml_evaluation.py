import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler
import numpy as np
from wf_ml_prediction import predict_input


def generate_and_predict(X_selected, scaler, nn_model, feature_name, base_value, delta_range, column_names, num_samples=4):
    feature_values = np.linspace(base_value + delta_range[0], base_value + delta_range[1], num=num_samples)
    predictions = []

    for value in feature_values:
        sample_input = X_selected.copy()
        sample_input[feature_name] = value
        sample_input_scaled = pd.DataFrame(scaler.transform(sample_input), columns=column_names)
        prediction = nn_model.predict(sample_input_scaled)
        predictions.append(prediction[0])

    return feature_values, predictions

def generate_and_predict_both(X_selected, scaler, nn_model, a_name, a_base, a_range, b_name, b_base, b_range,
                              column_names, num_samples=4):
    a_values = np.linspace(a_base + a_range[0], a_base + a_range[1], num=num_samples)
    b_values = np.linspace(b_base + b_range[0], b_base + b_range[1], num=num_samples)
    predictions = []

    for a, b in zip(a_values, b_values):
        sample_input = X_selected.copy()
        sample_input[a_name] = a
        sample_input[b_name] = b
        sample_input_scaled = pd.DataFrame(scaler.transform(sample_input), columns=column_names)
        prediction = nn_model.predict(sample_input_scaled)
        predictions.append(prediction[0])

    return a_values, b_values, predictions

def main():
    # ============================= #
    #     2.1 MACHINE LEARNING      #
    # ============================= #

    # Load and preprocess data, then save it to data_processing/
    data = pd.read_csv("data_processing\proc_irena_epi.csv")

    # Dropping categorical features and applying dimensionality reduction.
    X = data.drop(columns=["Region", "Country Code", "Country", "Public Flows (2021 USD M)", "EPI.new", "EPI.old", "CDA.new", "CDA.old"])
    y = data["EPI.new"]

    # Split the dataset into training and testing (80-20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the data (Z-score)
    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_train.columns)

    # Save the processed data for wf_ml_training.py to use
    X_train_scaled.to_csv("data_processing/X_train_scaled.csv", index=False)
    X_test_scaled.to_csv("data_processing/X_test_scaled.csv", index=False)
    y_train.to_csv("data_processing/y_train.csv", index=False)
    y_test.to_csv("data_processing/y_test.csv", index=False)

    # Run wf_ml_training.py to train and save the models
    os.system('python wf_ml_training.py')

    # =================================== #
    #     2.2 STATISTICAL EVALUATION      #
    # =================================== #

    # Load and predict with each model. Evaluate with chosen metrics.
    model_names = ["lr_model", "ridge_model", "lasso_model", "nn_model"]
    metrics = []

    for model_name in model_names:
        # Load the model from the models/ folder
        with open(f"models/{model_name}.pickle", "rb") as f:
            model = pickle.load(f)

        # Get predictions using the model
        y_pred = predict_input(model, X_test_scaled)

        # Compute evaluation metrics (MSE and MAE)
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)

        # Append the results to the metrics list
        metrics.append([model_name, mse, mae])

    # Save the evaluation results to evaluation/summary.txt
    df = pd.DataFrame(metrics, columns=["Model Name", "MSE", "MAE"])
    dataset_name = "proc_irena_epi"
    df["Dataset"] = dataset_name
    df["Method"] = ["Linear", "Ridge", "LASSO", "Neural"]
    df = df[["Dataset", "Method", "MAE", "MSE"]]
    with open("evaluation/summary.txt", "w") as f:
        f.write(df.to_string(index=False))  # index=False to remove the row index from the table
        print("\n" + df.to_string(index=False))

    # ============================ #
    #     2.3 EXPERIMENTATION      #
    # ============================ #

    # Select "Chile" and "United States" as Explainable Records
    countries = ["Chile", "United States of America (the)"]
    selected_indices = data[data["Country"].isin(countries)].index
    X_selected = pd.DataFrame(X.loc[selected_indices], columns=X_train.columns)
    y_selected = y.loc[selected_indices]

    # Load the Neural Network model (MLPRegressor)
    with open("models/nn_model.pickle", "rb") as f:
        nn_model = pickle.load(f)

    # Standardize the selected data (use the same scaler as before)
    X_selected_scaled = pd.DataFrame(scaler.transform(X_selected), columns=X_train.columns)

    # Make predictions using the neural network model
    y_pred_selected = nn_model.predict(X_selected_scaled)

    # Print the predictions to the console
    print(f"\nPredictions for Chile and United States using Neural Network model:")
    for country, actual, prediction in zip(countries, y_selected, y_pred_selected):
        error = prediction - actual
        print(f"{country} - Actual: {actual:.4f}, Predicted: {prediction:.4f}, Error: {error:.4f}")

    # Create 4 new inputs varying SDG 7b1 RE capacity per capita (Feature A) using Chile as the baseline
    chile_sdg7_value = X_selected.loc[X_selected.index[0], "SDG 7b1 RE capacity per capita (W/inhabitant)"]
    chile_flows_value = X_selected.loc[X_selected.index[0], "Public Flows per Capita (USD)"]
    print("\nPredictions for varying Feature A (SDG 7b1 RE capacity per capita) for Chile:")
    feature_a_values, predictions_feature_a = generate_and_predict(
        X_selected, scaler, nn_model, "SDG 7b1 RE capacity per capita (W/inhabitant)", chile_sdg7_value,
        (-100, 100), X_train.columns
    )
    for value_a, prediction in zip(feature_a_values, predictions_feature_a):
        print(f"Feature A: {value_a:.2f} W/inhabitant -> Predicted EPI.new: {prediction:.4f}")

    # Predict for varying Public Flows per Capita (Feature B) using Chile as the baseline
    print("\nPredictions for varying Feature B (Public Flows per Capita) for Chile:")
    feature_b_values, predictions_feature_b = generate_and_predict(
        X_selected, scaler, nn_model, "Public Flows per Capita (USD)", chile_flows_value,
        (-2, 2), X_train.columns
    )
    for value_b, prediction in zip(feature_b_values, predictions_feature_b):
        print(f"Feature B: {value_b:.2f} USD -> Predicted EPI.new: {prediction:.4f}")

    # Predict for increasing Feature A and Feature B together
    print("\nPredictions for increasing Feature A and Feature B together in the same direction:")
    a, b, predictions_both_increase = generate_and_predict_both(
        X_selected, scaler, nn_model, "SDG 7b1 RE capacity per capita (W/inhabitant)", chile_sdg7_value, (0, 200),
        "Public Flows per Capita (USD)", chile_flows_value, (0, 2), X_train.columns
    )
    for a, b, prediction in zip(a, b, predictions_both_increase):
        print(
            f"Feature A: {a:.2f} W/inhabitant, Feature B: {b:.2f} USD -> Predicted EPI.new: {prediction:.4f}")

    # Predict for varying Feature A and Feature B inversely
    print("\nPredictions for varying Feature A and Feature B inversely in opposite directions:")
    a, b, predictions_both_inverse = generate_and_predict_both(
        X_selected, scaler, nn_model, "SDG 7b1 RE capacity per capita (W/inhabitant)", chile_sdg7_value, (0, 200),
        "Public Flows per Capita (USD)", chile_flows_value, (0, -2), X_train.columns
    )
    for a, b, prediction in zip(a, b, predictions_both_inverse):
        print(
            f"Feature A: {a:.2f} W/inhabitant, Feature B: {b:.2f} USD -> Predicted EPI.new: {prediction:.4f}")


if __name__ == "__main__":
    main()