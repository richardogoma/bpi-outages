import os
import tomllib
from src.extract import read_log
from src.transform import transform_log_data
from src.load import save_outages
from src.visualize import display_outages
from prefect import flow
from prefect.filesystems import LocalFileSystem


local_file_system_block = LocalFileSystem.load("config-file")
fs = local_file_system_block.basepath

# Load configurations
with open(f"{fs}\config.toml", "rb") as f:
    config = tomllib.load(f)
log_file = config["files"]["log_file"]
output_file = config["files"]["output_file"]


@flow(name="BPI ETL Pipeline")
def run_etl_pipeline(
    source: str = log_file, target: str = output_file, visualize: bool = False
):
    log_data = read_log(os.path.join(fs, source))

    outages = transform_log_data(log_data)

    save_outages(outages, os.path.join(fs, target))

    if visualize:
        display_outages(outages)


if __name__ == "__main__":
    run_etl_pipeline(source=log_file, target=output_file)
