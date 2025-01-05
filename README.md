# BPI Outages Analysis ETL Workflow

This project uses the UV Python package manager (written in Rust) to easily set up the project, manage packages, and handle the virtual environment.

The purpose of this project is to analyze log data from the [Bitcoin Price Index project](http://bit.ly/bitcoin-rates), while exploring UV, Prefect, and GitHub Copilot.

> **Prefect** is an open-source workflow orchestration tool primarily used for managing and monitoring data pipelines. It allows data engineers to design, schedule, and run complex data workflows in Python with features like automatic retries, caching, and real-time monitoring. Essentially, it turns regular Python functions into production-ready data pipelines with minimal extra code.

## Setup

Run the following command to set up the project:

```sh
uv run main.py
```