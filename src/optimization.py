import numpy as np
import pandas as pd

def optimize_prices(model, X_test, y_test):

    recommended_prices = []
    actual_profits = []
    optimized_profits = []

    for i in range(len(X_test)):

        row = X_test.iloc[i].copy()
        actual_price = row['Price']

        # Dynamic cost assumption
        cost_per_unit = actual_price - 0.30

        price_range = np.linspace(
            actual_price * 0.8,
            actual_price * 1.2,
            50
        )

        best_profit = -np.inf
        best_price = actual_price

        for p in price_range:

            row_modified = row.copy()
            row_modified['Price'] = p

            predicted_demand = model.predict(
                pd.DataFrame([row_modified])
            )[0]

            profit = (p - cost_per_unit) * predicted_demand

            if profit > best_profit:
                best_profit = profit
                best_price = p

        recommended_prices.append(best_price)

        actual_demand = y_test.iloc[i]
        actual_profit = (actual_price - cost_per_unit) * actual_demand

        actual_profits.append(actual_profit)
        optimized_profits.append(best_profit)

    return recommended_prices, actual_profits, optimized_profits