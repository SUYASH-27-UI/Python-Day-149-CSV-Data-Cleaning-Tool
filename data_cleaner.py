import csv

def clean_data():
    cleaned_records = []
    seen_records = set()

    removed_duplicates = 0
    removed_incomplete = 0

    try:
        with open("students.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:

                # Remove extra spaces
                row = {
                    key.strip(): value.strip()
                    for key, value in row.items()
                    if key is not None
                }

                # Check missing values
                if not all(row.values()):
                    removed_incomplete += 1
                    continue

                # Check duplicate records
                record = tuple(row.values())

                if record in seen_records:
                    removed_duplicates += 1
                    continue

                seen_records.add(record)
                cleaned_records.append(row)

        with open("cleaned_students.csv", "w", newline="") as file:

            if cleaned_records:
                writer = csv.DictWriter(
                    file,
                    fieldnames=cleaned_records[0].keys()
                )

                writer.writeheader()
                writer.writerows(cleaned_records)

        print("\n===== DATA CLEANING REPORT =====")
        print("Original Records:", len(seen_records)
              + removed_duplicates + removed_incomplete)
        print("Clean Records:", len(cleaned_records))
        print("Duplicates Removed:", removed_duplicates)
        print("Incomplete Records Removed:", removed_incomplete)
        print("Output: cleaned_students.csv")

    except FileNotFoundError:
        print("students.csv file not found!")


clean_data()
