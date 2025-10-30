# Get the unique categories
categories = df['Subscription_Tier'].unique()
    
# Create a list of ROI data for each category
groups = []
for tier in categories:
    groups.append(df[df['Subscription_Tier'] == tier]['ROI'])
        
# Perform the one-way ANOVA
f_statistic, p_value = stats.f_oneway(*groups)

print(f"\n--- ANOVA (ROI by Subscription_Tier) ---")
print(f"F-Statistic: {f_statistic:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print("Result: There IS a statistically significant difference in ROI.")
else:
    print("Result: There is NO statistically significant difference in ROI.")
