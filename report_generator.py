import pandas as pd

df = pd.read_excel("intersection_delay_analysis.xlsx")

avg_delay = df["Delay_s"].mean()
worst_case = df[df["Delay_s"] == df["Delay_s"].max()]

with open("report.txt", "w", encoding="utf-8") as f:  # ✅ specify UTF-8 encoding
    f.write("🚗 Urban Intersection Delay Report 🚗\n")
    f.write(f"Average Delay: {avg_delay:.2f} seconds\n")
    f.write("Worst Intersection:\n")
    f.write(worst_case.to_string(index=False))
    f.write("\n\nRefer to delay_plot.png for visual analysis.")
print("📝 Report generated as report.txt")
