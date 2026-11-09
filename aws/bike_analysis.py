import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Read the bike-share data
with open('bike_rentals.txt', 'r') as f:
    lines = f.readlines()

# Skip the header comment and read the data
data_str = ''.join(lines[1:])
df = pd.read_csv(StringIO(data_str), sep=r'\s+')

# Convert date column to datetime objects
df['date'] = pd.to_datetime(df['date'])
df['rainy'] = df['rain_mm'] > 0

# Print basic statistics
print("Bike-Share Rental Analysis:")
print("===========================")
print(f"Total days analysed: {len(df)}")
print(f"Total rentals: {df['rentals'].sum()}")
print(f"Average daily rentals: {df['rentals'].mean():.0f}")
print(f"Busiest day: {df.loc[df['rentals'].idxmax(), 'date'].date()} with {df['rentals'].max()} rentals")
print(f"Average rentals on dry days: {df.loc[~df['rainy'], 'rentals'].mean():.0f}")
print(f"Average rentals on rainy days: {df.loc[df['rainy'], 'rentals'].mean():.0f}")
print(f"Average trip length: {df['avg_trip_mins'].mean():.1f} minutes")

# Create a visualisation
sns.set_style("whitegrid")
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot daily rentals
ax1.plot(df['date'], df['rentals'], marker='o', color='seagreen', label='Rentals')
ax1.set_xlabel('Date')
ax1.set_ylabel('Rentals')
ax1.tick_params(axis='x', rotation=45)

# Add rainfall as bars on a secondary axis
ax2 = ax1.twinx()
ax2.bar(df['date'], df['rain_mm'], alpha=0.3, color='steelblue', width=0.5, label='Rain (mm)')
ax2.set_ylabel('Rain (mm)', color='steelblue')
ax2.tick_params(axis='y', labelcolor='steelblue')
ax2.set_ylim(0, df['rain_mm'].max() * 3)

# Formatting
fig.suptitle('30-Day Bike-Share Report', fontsize=18)
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the figure
plt.savefig('bike_analysis.png')
print("Analysis complete. Results saved to 'bike_analysis.png'")
