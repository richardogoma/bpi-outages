from prefect import flow
from prefect_github.repository import GitHubRepository


github_repository_block = GitHubRepository.load("bpi-outages-repo")

if __name__ == "__main__":
    flow.from_source(
        source=github_repository_block.repository_url,
        entrypoint="main.py:run_etl_pipeline",
    ).serve(
        name="bpi-etl-pipeline",
        tags=["bpi", "dev"],
        parameters={"visualize": False},
        pause_on_shutdown=False,
        interval=300,
        version="0.1.6",
        description="ETL pipeline for BPI data",
    )
