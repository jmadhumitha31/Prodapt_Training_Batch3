import csv

def export_vehicle_data(filename, vehicles):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Brand", "Model", "Year", "Owner"])

        for v in vehicles:
            owner = v.get_owner()
            if owner is None:
                owner = "N/A"
            else:
                owner = owner.replace("Owner:", "").strip()

            writer.writerow([v.brand, v.model, v.year, owner])

    return f"Vehicle data exported to {filename} successfully."