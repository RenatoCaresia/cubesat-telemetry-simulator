import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/telemetry_log.csv")

print(df.head())
print()
print("Average temperature:", df["temperature_c"].mean())
print("Minimum battery:", df["battery_percent"].min())
print("Maximum altitude:", df["altitude_km"].max())

plt.plot(df["sequence"], df["battery_percent"])
plt.title("CubeSat Battery Over Time")
plt.xlabel("Packet Sequence")
plt.ylabel("Battery (%)")
plt.show()