# Fit the Ordinary Least Squares (OLS) regression model
model = smf.ols('Revenue_Generated ~ Budget', data=df).fit()

# Print the full summary
print("\n--- Linear Regression Summary (Revenue_Generated ~ Budget) ---")
print(model.summary())
