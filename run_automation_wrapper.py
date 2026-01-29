import os
import subprocess
import sys

# Configuration
PROJECT_ROOT = r"c:\Users\Sri Mathi\OneDrive\Desktop\RESUME\job_automation"
ENV_VARS = {
    "EMAIL_ADDRESS": "srimathip789@gmail.com",
    "EMAIL_APP_PASSWORD": "wntwccrduqxggrfz",
    "PYTHONIOENCODING": "utf-8"
}

def run_script(script_path):
    print(f"\n--- Running: {script_path} ---")
    
    # Merge current environment with our variables
    env = os.environ.copy()
    env.update(ENV_VARS)
    
    # Use powershell to cd into the project root before running the script
    cmd = f'powershell -Command "cd \'{PROJECT_ROOT}\'; python {script_path}"'
    
    # Run the script
    result = subprocess.run(cmd, env=env, capture_output=True, text=True, shell=True, encoding='utf-8', errors='replace')
    
    print(result.stdout)
    if result.stderr:
        print("ERRORS:")
        print(result.stderr)
    return result.returncode

def main():
    # Full Automation Pipeline
    scripts = [
        r"01_email_automation\email_job_reader.py",
        r"03_job_portal_scanning\job_portal_scanner.py",
        r"03_job_portal_scanning\filter_bahrain_saudi.py",
        r"04_contact_extraction\contact_extractor.py",
        r"05_lead_management\merge_leads.py",
        r"01_email_automation\send_bulk_emails.py",
    ]
    
    for script in scripts:
        code = run_script(script)
        if code != 0:
            print(f"Stopping execution due to error in {script}")
            break

if __name__ == "__main__":
    main()
