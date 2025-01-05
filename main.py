import tomllib
from src.extract import read_log
from src.transform import transform_log_data
from src.load import save_outages
from src.visualize import display_outages
from prefect import flow


# Load configurations
with open("config.toml", "rb") as f:
    config = tomllib.load(f)
log_file = config["files"]["log_file"]
output_file = config["files"]["output_file"]


@flow(name="ETL Pipeline")
def main():
    log_data = read_log(log_file)

    outages = transform_log_data(log_data)

    save_outages(outages, output_file)

    show_visual = (
        input("Do you want to display the outages visualization? (y/n): ")
        .strip()
        .lower()
    )
    if show_visual == "y":
        display_outages(outages)


if __name__ == "__main__":
    main()
