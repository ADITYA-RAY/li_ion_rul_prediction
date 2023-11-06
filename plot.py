import pandas as pd
import matplotlib.pyplot as plt

csv_filename = "arduino_data.csv"
df = pd.read_csv(csv_filename, parse_dates=["Timestamp"])

# Select the last 500 data points
df_last_500 = df.iloc[-1500:]

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 8))
ax1.plot(df_last_500["Timestamp"], df_last_500["Voltage (V)"], label="Voltage (V)", color="blue")
ax1.set_ylabel("Voltage (V)")
ax1.set_title("Voltage Over Time (Last 500 Data Points)")
ax1.grid(True)

# Plot Current data
ax2.plot(df_last_500["Timestamp"], abs(df_last_500["Current (A)"]), label="Current (A)", color="green")
ax2.set_xlabel("Timestamp")
ax2.set_ylabel("Current (A)")
ax2.set_title("Current Over Time (Last 3000 Data Points)")
ax2.grid(True)

# Display a legend for both subplots
ax1.legend()
ax2.legend()

# Rotate x-axis labels for both subplots
plt.xticks(rotation=45)

# Adjust subplot spacing
plt.tight_layout()

# Save the plots as separate image files (e.g., PNG)
plt.savefig("voltage_plot_last_500.png")
plt.savefig("current_plot_last_500.png")

# If you want to display the plots interactively, use the following line:
# plt.show()
