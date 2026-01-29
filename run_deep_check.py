import csv
import os
from datetime import datetime

BASE_DIR = r"c:\Users\Sri Mathi\OneDrive\Desktop\RESUME\job_automation"
LOG_FILE = os.path.join(BASE_DIR, r"logs\sent_emails.log")
DATA_DIR = os.path.join(BASE_DIR, "data")
FILES_TO_CHECK = [
    os.path.join(DATA_DIR, "new_linkedin_leads.csv"),
    os.path.join(DATA_DIR, "recent_linkedin_companies.csv"), 
    os.path.join(DATA_DIR, "fintech_leads.csv"),
    os.path.join(DATA_DIR, "sector_leads.csv"),
    os.path.join(DATA_DIR, "manual_leads.csv")
]

def main():
    print("--- Deep Check for Unsent Leads ---")
    
    # Load Sent Emails
    sent_emails = set()
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            sent_emails = set(line.strip().lower() for line in f if line.strip())
    print(f"Loaded {len(sent_emails)} sent emails.")

    # Check Files
    new_leads = []
    for fpath in FILES_TO_CHECK:
        if not os.path.exists(fpath):
            print(f"File not found: {fpath}")
            continue
            
        print(f"\nScanning: {fpath}")
        try:
            with open(fpath, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                if not reader.fieldnames:
                    print("  (Empty file or no headers)")
                    continue
                count = 0
                for row in reader:
                    email = row.get('email', '').strip()
                    if email and '@' in email:
                        if email.lower() not in sent_emails:
                            if not any(l['email'] == email for l in new_leads):
                                row['source_file'] = fpath
                                new_leads.append(row)
                                count += 1
                                print(f"  + FOUND: {row.get('company', 'Unknown')} ({email})")
                if count == 0:
                    print("  (No new leads found)")
        except Exception as e:
            print(f"  Error: {e}")

    print(f"\nTotal UNIQUE New Leads Found: {len(new_leads)}")
    
    # Check Job Leads CSV
    JOB_LEADS_FILE = os.path.join(DATA_DIR, "job_leads.csv")
    if os.path.exists(JOB_LEADS_FILE):
        with open(JOB_LEADS_FILE, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            job_leads_count = sum(1 for _ in reader)
            print(f"Main job_leads.csv has {job_leads_count} entries.")
    
    # Check Scanner Log
    SCANNER_LOG = os.path.join(BASE_DIR, r"logs\scanner.log")
    if os.path.exists(SCANNER_LOG):
        print(f"\nLast 5 lines of scanner.log:")
        with open(SCANNER_LOG, 'r') as f:
            lines = f.readlines()
            for line in lines[-5:]:
                print(f"  {line.strip()}")

if __name__ == "__main__":
    main()
