import re
from datetime import datetime, timedelta


def extract_timestamps(log_data):
    """Extract timestamps from log data."""
    pattern = r"Inserted Bitcoin rates as at (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2})"
    matches = re.findall(pattern, log_data)
    return [datetime.fromisoformat(ts) for ts in matches]


def round_to_minute(dt):
    """Round a datetime object to the nearest minute."""
    return dt.replace(second=0, microsecond=0) + timedelta(
        minutes=1 if dt.second >= 30 else 0
    )


def calculate_outages(timestamps, threshold=timedelta(minutes=1)):
    """Identify gaps exceeding the threshold."""
    rounded_timestamps = [round_to_minute(ts) for ts in timestamps]
    outages = []
    for i in range(1, len(rounded_timestamps)):
        gap = rounded_timestamps[i] - rounded_timestamps[i - 1]
        if gap > threshold:
            outages.append((rounded_timestamps[i - 1], rounded_timestamps[i], gap))
    return outages
