import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def compute_delay(row):
    g = row['Green_Time_s']
    arrival_rate = row['Arrival_Rate_vph'] / 3600  # veh/sec
    saturation_flow = 0.5  # example saturation flow rate
    x = arrival_rate / (saturation_flow * g / 60)
    delay = (x / (1 - x)) * 10 if x < 1 else 999  # avoid infinite delay
    return round(delay, 2)

df = pd.read_excel("intersection_data.xlsx")
df["Delay_s"] = df.apply(compute_delay, axis=1)
df.to_excel("intersection_delay_analysis.xlsx", index=False)

sns.scatterplot(data=df, x="Lane_Width_m", y="Delay_s", hue="Corner_Radius_m")
plt.title("Effect of Lane Width & Corner Radius on Delay")
plt.xlabel("Lane Width (m)")
plt.ylabel("Delay (s)")
plt.savefig("delay_plot.png")

print("📈 Delay analysis complete and saved to Excel and PNG.")
