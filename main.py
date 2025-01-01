from src.extract import read_log
from src.transform import extract_timestamps, calculate_outages
from src.load import save_outages
from src.visualize import display_outages


def main():
    # File paths
    log_file = "data/output.log"
    output_file = "data/outages.csv"

    # ETL process
    print("Starting ETL process...")
    log_data = read_log(log_file)
    print("Log file read successfully.")

    timestamps = extract_timestamps(log_data)
    print(f"Extracted {len(timestamps)} timestamps.")

    outages = calculate_outages(timestamps)
    print(f"Identified {len(outages)} outages.")

    save_outages(outages, output_file)
    print("ETL process completed successfully.")

    # Streamlit visualization
    display_outages(outages)


if __name__ == "__main__":
    main()
