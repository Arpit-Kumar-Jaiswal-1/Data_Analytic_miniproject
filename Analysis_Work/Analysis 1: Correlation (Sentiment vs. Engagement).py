# Define the columns for sentiment and engagement
sentiment_col = 'Customer_Satisfaction_Post_Refund'
engagement_cols = ['Clicks', 'Conversions']

# Calculate correlations
corr_clicks = df[sentiment_col].corr(df[engagement_cols[0]])
corr_conversions = df[sentiment_col].corr(df[engagement_cols[1]])

print(f"Correlation between 'Satisfaction' and 'Clicks': {corr_clicks:.4f}")
print(f"Correlation between 'Satisfaction' and 'Conversions': {corr_conversions:.4f}")
