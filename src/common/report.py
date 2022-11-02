import os
import csv
import json

CSV_FILE_PATH = None
JSON_FILE_PATH = None


def config(json_file_path: str, csv_file_path: str) -> None:
    global CSV_FILE_PATH
    global JSON_FILE_PATH

    CSV_FILE_PATH = csv_file_path
    JSON_FILE_PATH = json_file_path


def to_csv(**kwargs) -> None:
    if CSV_FILE_PATH is None:
        return

    file_open_mode = 'a' if os.path.exists(CSV_FILE_PATH) else 'w'
    with open(CSV_FILE_PATH, file_open_mode, newline='') as f:
        writer = csv.DictWriter(f, fieldnames=kwargs.keys())

        if file_open_mode == 'w':
            writer.writeheader()

        writer.writerow(kwargs)


def to_json(**kwargs) -> None:
    if JSON_FILE_PATH is None:
        return

    file_open_mode = 'a' if os.path.exists(JSON_FILE_PATH) else 'w'
    obj_arr = []

    if file_open_mode == 'a':
        with open(JSON_FILE_PATH) as f:
            obj_arr = json.load(f)

    with open(JSON_FILE_PATH, 'w') as f:
        obj_arr.append(kwargs)
        json.dump(obj_arr, f, indent=2, separators=(',', ': '))
