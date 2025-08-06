import pandas as pd
import numpy as np

def generate_data(num_intersections=50):
    np.random.seed(42)
    data = {
        "Intersection_ID": range(1, num_intersections+1),
        "Lane_Width_m": np.random.uniform(2.5, 4.0, num_intersections),
        "Corner_Radius_m": np.random.uniform(5, 20, num_intersections),
        "Green_Time_s": np.random.randint(10, 60, num_intersections),
        "Arrival_Rate_vph": np.random.randint(300, 1500, num_intersections),
    }
    df = pd.DataFrame(data)
    df.to_excel("intersection_data.xlsx", index=False)
    print("🚦 Data generated and saved as intersection_data.xlsx")

if __name__ == "__main__":
    generate_data()
