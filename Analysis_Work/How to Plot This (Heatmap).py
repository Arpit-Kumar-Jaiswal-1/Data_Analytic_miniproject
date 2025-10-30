# Set the figure size
plt.figure(figsize=(10, 6))

# Create the 2D histogram / heatmap
sns.histplot(data=df, 
             x='Clicks', 
             y='Customer_Satisfaction_Post_Refund', 
             bins=(50, 5),  # Bins for x-axis, Bins for y-axis
             cbar=True)     # Show the color bar

plt.title('Engagement (Clicks) vs. Sentiment (Satisfaction)')
plt.xlabel('Clicks')
plt.ylabel('Customer Satisfaction (Post Refund)')

# Save the figure to a file
plt.savefig('sentiment_clicks_heatmap.png')
print("Heatmap saved as 'sentiment_clicks_heatmap.png'")
