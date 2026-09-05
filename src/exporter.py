import json
import pandas as pd


def export_to_csv(records, file_path):
    df = pd.DataFrame(records)
    df.to_csv(file_path, index=False, encoding="utf-8")


def export_to_json(records, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2, ensure_ascii=False)


def export_validation_report(report, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, ensure_ascii=False)
