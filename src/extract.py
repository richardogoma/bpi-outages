def read_log(file_path):
    """Reads the log file and returns its contents as a string."""
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Log file not found at {file_path}")
