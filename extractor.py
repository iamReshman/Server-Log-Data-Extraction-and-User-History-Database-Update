from datetime import datetime

def extract_email_date_pairs(log_file_path):
    email_date_list = []

    with open(log_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("From "):
                parts = line.split()
                if len(parts) >= 7:
                    email = parts[1]
                    # Construct the date string
                    date_str = " ".join(parts[2:])  # e.g., "Sat Jan 5 09:14:16 2008"
                    try:
                        # Pad single-digit day with zero to fix parsing issues
                        date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
                        formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")
                        email_date_list.append({
                            "email": email,
                            "date": formatted_date
                        })
                    except ValueError:
                        # Try parsing again with two-digit day format
                        try:
                            date_str_fixed = " ".join([
                                parts[2],
                                parts[3],
                                parts[4].zfill(2),  # pad single digit day
                                parts[5],
                                parts[6]
                            ])
                            date_obj = datetime.strptime(date_str_fixed, "%a %b %d %H:%M:%S %Y")
                            formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")
                            email_date_list.append({
                                "email": email,
                                "date": formatted_date
                            })
                        except Exception as e:
                            print("Date parse failed for line:", line)
                            print("Error:", e)

    print(f"✅ Extracted {len(email_date_list)} email-date records.")
    return email_date_list

