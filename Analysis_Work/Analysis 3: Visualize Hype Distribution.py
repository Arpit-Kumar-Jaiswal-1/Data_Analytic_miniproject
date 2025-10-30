# Create the box plot using Altair
chart = alt.Chart(df).mark_boxplot().encode(
    # Set the x-axis to be the 'domains'
    x=alt.X('Common_Keywords', title='Product Domain (Keywords)'),
    
    # Set the y-axis to be the 'hype'
    y=alt.Y('Clicks', title='Hype (Clicks)'),
    
    # Add tooltips to see details on hover
    tooltip=['Common_Keywords', alt.Tooltip('Clicks', format=',.0f')]
).properties(
    title='Hype (Clicks) Distribution Across Product Domains'
).interactive() # Make the chart zoomable and pannable

# Save the chart as a JSON file
chart_json_path = 'hype_distribution_boxplot.json'
chart.save(chart_json_path)
print(f"Box plot saved as '{chart_json_path}'")
