import csv
import urllib.parse
import webbrowser
import time
import os
import subprocess

# Configuration
RESUME_FILES = [
    r"c:\Users\Sri Mathi\OneDrive\Desktop\RESUME\job_automation\resumes\2026 resume\Sri_Mathi_Software_Engineer_2026.docx",
    r"c:\Users\Sri Mathi\OneDrive\Desktop\RESUME\job_automation\resumes\2026 resume\SriMathi_CV_4+exp.pdf"
]

def copy_to_clipboard(file_paths):
    """Copies the given files to the system clipboard using PowerShell."""
    valid_paths = [p for p in file_paths if os.path.exists(p)]
    if not valid_paths:
        print("⚠ No valid resume files found to copy.")
        return

    ps_paths = ",".join([f"'{p}'" for p in valid_paths])
    command = f"Set-Clipboard -Path {ps_paths}"

    try:
        subprocess.run(["powershell", "-Command", command], check=True)
        print(f"✓ Copied {len(valid_paths)} resume file(s) to CLIPBOARD.")
        print("  📎 Press Ctrl+V in WhatsApp to attach them.")
    except subprocess.CalledProcessError as e:
        print(f"⚠ Failed to copy to clipboard: {e}")

def send_whatsapp(phone, message):
    """Opens WhatsApp with pre-filled message"""
    clean_phone = phone.replace(" ", "").replace("-", "")
    encoded_message = urllib.parse.quote(message)
    
    app_url = f"whatsapp://send?phone={clean_phone}&text={encoded_message}"
    
    print(f"  📱 Opening WhatsApp for {clean_phone}...")
    try:
        os.startfile(app_url)
    except:
        web_url = f"https://wa.me/{clean_phone}?text={encoded_message}"
        webbrowser.open_new_tab(web_url)
    
    time.sleep(2)

def main():
    print("=" * 60)
    print("  📲 WhatsApp Follow-up for Today's Applications")
    print("=" * 60)
    
    companies = [
        {
            "name": "Era Projects",
            "phone": "+973 65000000",
            "positions": ["QA/QC Engineer - Building Construction", "Project Engineer - High Rise"]
        },
        {
            "name": "Zak Solutions",
            "phone": "+973 17404961",
            "positions": ["System Admin Engineer"]
        }
    ]
    
    print(f"\n📋 Will send WhatsApp follow-ups to {len(companies)} companies\n")
    
    for i, company in enumerate(companies, 1):
        print(f"\n[{i}/{len(companies)}] {company['name']}")
        print(f"  Positions: {', '.join(company['positions'])}")
        
        # Create message
        positions_text = " and ".join(company['positions'])
        message = f"""Hi, I recently applied via email for the {positions_text} position(s) at {company['name']}.

I am a Software Engineer with over 4 years of experience in Full Stack Development and Testing Automation (Selenium, Python, Java). I am currently based in Bahrain with valid CPR.

I have attached my resume for your review. I would appreciate the opportunity to discuss how my skills align with your team's needs.

Best regards,
M. Sri Mathi
+973 35102870
srimathip789@gmail.com"""
        
        # Copy resumes to clipboard
        copy_to_clipboard(RESUME_FILES)
        
        # Open WhatsApp
        send_whatsapp(company['phone'], message)
        
        print(f"  ✅ WhatsApp opened for {company['name']}")
        print(f"  📎 Resume files are in your clipboard - press Ctrl+V to attach")
        
        if i < len(companies):
            input("\n  ⏸️  Press Enter after sending to continue to next company...")
    
    print("\n" + "=" * 60)
    print("  ✅ WhatsApp follow-up process complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
