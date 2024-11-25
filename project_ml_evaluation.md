#### SER494: Project Evaluation
#### Title: Global Trends in Renewable Energy Adoption
#### Author: Gonzalo Allendes
#### Date: November 23rd, 2024

## Evaluation Metrics
### Metric 1
**Name:** Mean Squared Error (MSE)

**Choice Justification:** MSE is chosen for its ability to penalize large errors more heavily by squaring residuals,
making it effective for evaluating model sensitivity to extreme values. Given the dataset's significant outliers—such 
as countries with high renewable energy installed capacity per capita (e.g., Iceland or Norway)—MSE provides insight
into how well models handle these extremes.

### Metric 2
**Name:** Mean Average Error (MAE)

**Choice Justification:** MAE serves as a complementary metric to MSE, offering a simpler interpretation by averaging
the absolute residuals without squaring them. This allows for a direct comparison between the two metrics to highlight
differences in how they respond to outliers and have a broader understanding of model performance.

## Alternative Models
### Alternative 1: Linear Regression
**Construction:** A standard Linear Regression model was built using sklearn's ```LinearRegression```
implementation. It utilizes an ordinary least squares method to minimize the sum of the squared
residuals by calculating the weights vector ```w``` with the normal equation ```w = [(A^T * A)^-1 * A^T * b]```.

**Evaluation:** The Linear Regression model achieved an MSE of 131.1076 and an MAE of 9.3411.
The MSE will represent our baseline performance for comparison, while the MAE shows the average 
prediction error in absolute terms.

### Alternative 2: Ridge Linear Regression
**Construction:** A Ridge Regression model was built with sklearn's ```Ridge```  implementation. 
Ridge introduces a regularization term based on the L2 distance of each weight from the origin to
penalize large coefficients and reduce overfitting. Changing the loss function adds a term to
the normal equation ```w = [(A^T * A + λI)^-1 * A^T * b]```

**Evaluation:** Ridge Regression has an MSE of 131.2768 (slightly worse than Linear Regression, 
with an increase of 0.1692), and an MAE of 9.3428 with an increase of 0.0017. This small increase 
indicates that Ridge Regression does not provide an improvement in addressing overfitting. This is 
likely because the data does not exhibit a high degree of multicollinearity, so the advantage of 
Ridge's regularization is minimized.

### Alternative 3: LASSO (Least Absolute Shrinkage and Selection Operator) Linear Regression
**Construction:** A Lasso Regression model was built with sklearn's ```Lasso``` implementation.
Lasso adds an L1 regularization term, which can drive some coefficients to zero, effectively 
performing feature selection. Unlike Linear and Ridge, LASSO does not have a closed-form
solution. Instead, sklearn's ```LASSO``` uses coordinate descent to iteratively
optimize the model's weights.

**Evaluation:** The Lasso Regression model achieved an MSE of 140.9102, which is worse than both Linear and 
Ridge Regression by 9.8026 and 9.6334, respectively. The MAE of 9.7657 is also larger by
0.4246 and 0.4229 in comparison. The higher values for both MSE and MAE suggest that the model 
oversimplifies the problem by excessively reducing the impact of relevant features, which
leads to less accurate predictions. 

### Alternative 4: Neural Network (Multi-Layer Perceptron Regressor)
**Construction:** A Neural Network model was built using sklearn's MLPRegressor. This model
uses a multi-layer perceptron regressor to capture nonlinear relationships in the data. It is
worth mentioning that the algorithm uses Stochastic Gradient Descent, which will vary the
result of the error metrics from one iteration to the next.

**Evaluation:** The Neural Network (MLPRegressor) achieved a significantly better result 
than the linear models, with an MSE of 79.1784, which is substantially lower than the MSE 
for Linear Regression (131.1076, a difference of 51.9292), Ridge Regression (131.2768, a 
difference of 52.0984), and Lasso Regression (140.9102, a difference of 61.7318).
Additionally, the MAE of 7.6388 was also the lowest among all models, indicating more 
accurate predictions. It is worth noting that the percent difference in MSE is approximately
40% in comparison to a 20% reduction in MAE, which shows how the Neural Network is much 
better at handling outliers and capturing complex patterns in the data. 

## Best Model

**Model:** The best performing alternative was the Neural Network (Multi-Layer Perceptron 
Regressor).