import csv


def save_outages(outages, output_path):
    """Save outage data to a CSV file."""
    try:
        with open(output_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Outage Start", "Outage End", "Duration (minutes)"])
            for start, end, duration in outages:
                duration_minutes = duration.total_seconds() / 60
                writer.writerow([start, end, duration_minutes])
        print(f"Outage data saved to {output_path}")
    except Exception as e:
        raise IOError(f"Failed to save outages: {e}")
