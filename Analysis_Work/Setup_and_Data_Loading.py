import pandas as pd
import scipy.stats as stats
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

# Load the dataset
file_path = 'marketing_and_product_performance.csv'
df = pd.read_csv(file_path)

# Inspect the data to make sure it's loaded correctly
print(df.head())
df.info()
