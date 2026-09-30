import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("data/telemetry_log.csv")

latest_mission = df["mission_id"].iloc[-1]

mission_df = df[df["mission_id"] == latest_mission]

window_size = 5

temperature_values = mission_df["temperature_c"].to_numpy()

moving_average = np.convolve(
    temperature_values,
    np.ones(window_size) / window_size,
    mode="valid"
)

print(moving_average)

plt.plot(
    mission_df.index,
    mission_df["temperature_c"],
    label="Raw temperature"
)

plt.plot(
    mission_df.index[window_size - 1:],
    moving_average,
    label="Moving average"
)

plt.legend()
plt.show()


print(mission_df.head())
print()

print(
    "Average temperature:",
    mission_df["temperature_c"].mean()
)

print(
    "Minimum battery:",
    mission_df["battery_percent"].min()
)

print(
    "Maximum altitude:",
    mission_df["altitude_km"].max()
)

plt.plot(
    mission_df["sequence"],
    mission_df["battery_percent"]
)
plt.title("CubeSat Battery Over Time")
plt.xlabel("Packet Sequence")
plt.ylabel("Battery (%)")
plt.show()


plt.plot(
    mission_df["sequence"],
    mission_df["temperature_c"]
)
plt.title("CubeSat Temperature Over Time")
plt.xlabel("Packet Sequence")
plt.ylabel("Temperature (°C)")
plt.show()


plt.plot(
    mission_df["sequence"],
    mission_df["signal_dbm"]
)
plt.title("CubeSat Signal Strength Over Time")
plt.xlabel("Packet Sequence")
plt.ylabel("Signal (dBm)")
plt.show()
print("Analyzing mission:", latest_mission)