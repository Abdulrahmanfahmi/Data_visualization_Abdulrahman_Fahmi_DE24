from pathlib import Path

DATA_DIRECTORY = Path(__file__).parents[1]/"Data"


if __name__ == "__main__":
    print(DATA_DIRECTORY)