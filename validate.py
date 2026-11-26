import csv

seen_ids = set()

with open('patients.csv', 'r') as f:
    reader = csv.DictReader(f)
    print(f"Columns found: {reader.fieldnames}")
    
    for row_num, row in enumerate(reader, start=2):
        if not row['patient_id'].strip():
            continue  # Skip rows with empty patient_id
        patient_id = row['patient_id'].strip()
        age = row['age'].strip()
        
        # Check duplicate
        if patient_id in seen_ids:
            print(f"Row {row_num} FAILED - duplicates patient_id {patient_id}.")
            continue
        seen_ids.add(patient_id)
        
        # Check age
        if age == "":
            print(f"Row {row_num} FAILED - age is missing.")
            continue
            
        print(f"Row {row_num} OK - {patient_id} {row['name']}")