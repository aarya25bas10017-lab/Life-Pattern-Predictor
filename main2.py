import json
import os
from datetime import date

LOG_FILE = "activity_log.json"

def load_log():
    if not os.path.exists(LOG_FILE):
        return {}
    with open(LOG_FILE, "r") as f:
        return json.load(f)

def save_log(log):
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=4)

def log_daily_items():
    log = load_log()
    today = str(date.today())

    items = input("Enter items to carry (comma-separated): ").split(",")
    items = [i.strip() for i in items if i.strip()]

    forgotten = input("Enter forgotten items (comma-separated): ").split(",")
    forgotten = [i.strip() for i in forgotten if i.strip()]

    log[today] = {"items": items, "forgotten": forgotten}
    save_log(log)

    print("Saved successfully!")

def predict_items():
    log = load_log()
    if not log:
        print("No data available.")
        return

    total = {}
    forgotten = {}

    for entry in log.values():
        for item in entry["items"]:
            total[item] = total.get(item, 0) + 1
        for item in entry["forgotten"]:
            forgotten[item] = forgotten.get(item, 0) + 1

    print("\nLikely forgotten items:")
    for item in total:
        score = forgotten.get(item, 0) / total[item]
        print(f"{item} -> {score:.2f}")

def main():
    while True:
        print("\n1. Log items")
        print("2. Predict forgotten items")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            log_daily_items()
        elif choice == "2":
            predict_items()
        elif choice == "3":
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
