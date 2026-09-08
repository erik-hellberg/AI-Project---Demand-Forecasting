Several forecasting methods were evaluated, including Naive Forecasting, Moving Average, Exponential Moving Average and Random Forest models. The best-performing model was Random Forest v3, which achieved a Test MAE of 17.77 and outperformed the Naive Forecast by approximately 31.9%.

The model achieved an RMSE of 21.97 and a MAPE of 8.95%, indicating that the forecasts were on average relatively close to the actual demand. Feature importance analysis showed that Promotion, Week and Rolling Mean features were among the most influential variables.

However, the model showed a positive bias of 5.41, meaning that it tended to underestimate demand. The average actual demand was 193.95 units, compared with an average forecast of 188.54 units. Future improvements could include additional historical data, seasonal variables and further hyperparameter tuning.

> **Built an end-to-end demand forecasting model in Python, comparing traditional forecasting methods with Random Forest regression. Achieved 31.9% lower MAE than the naive baseline, with a final MAPE of 8.95%.**