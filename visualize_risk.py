import pandas as pd
import matplotlib.pyplot as plt
import os


def visualize_risk():

    file_path = "data/risk_history.csv"

    if not os.path.exists(file_path):
        print("Risk history file not found!")
        return

    df = pd.read_csv(file_path)

    if df.empty:
        print("No risk records available!")
        return

    df["Date"] = pd.to_datetime(df["Date"])

    risk_values = {
        "LOW": 1,
        "MEDIUM": 2,
        "HIGH": 3
    }

    df["Risk_Number"] = df["Risk_Level"].map(risk_values)

    df = df.dropna(subset=["Risk_Number"])

    if df.empty:
        print("No valid risk records available!")
        return

    print("\n===== RISK HISTORY =====")
    print(df[["Date", "Risk_Level"]])

    os.makedirs("graphs", exist_ok=True)

    plt.figure(figsize=(10, 5))

    plt.plot(
        df["Date"],
        df["Risk_Number"],
        marker="o"
    )

    plt.title("Weather Risk History")
    plt.xlabel("Date")
    plt.ylabel("Risk Level")

    plt.yticks(
        [1, 2, 3],
        ["LOW", "MEDIUM", "HIGH"]
    )

    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("graphs/risk_history.png")

    print("\nRisk graph saved in graphs/risk_history.png")

    plt.show()


if __name__ == "__main__":
    visualize_risk()