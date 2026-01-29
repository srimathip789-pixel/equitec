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

def send_whatsapp(phone, message, company_name):
    """Opens WhatsApp with pre-filled message"""
    clean_phone = phone.replace(" ", "").replace("-", "")
    encoded_message = urllib.parse.quote(message)
    
    app_url = f"whatsapp://send?phone={clean_phone}&text={encoded_message}"
    
    print(f"  📱 Opening WhatsApp for {company_name}...")
    try:
        os.startfile(app_url)
    except:
        web_url = f"https://wa.me/{clean_phone}?text={encoded_message}"
        webbrowser.open_new_tab(web_url)
    
    time.sleep(2)

def main():
    print("=" * 70)
    print("  📲 WhatsApp Follow-up to Leadership & Corporate Contacts")
    print("=" * 70)
    
    companies = [
        {
            "name": "GBM (Gulf Business Machines)",
            "phone": "+973 17584333",
            "type": "Corporate Office",
            "context": "leading IT solutions provider"
        },
        {
            "name": "Batelco/Beyon Business",
            "phone": "+973 32111888",
            "type": "Business WhatsApp Line",
            "context": "major telecom and technology group"
        },
        {
            "name": "Batelco Business Helpline",
            "phone": "+973 17881888",
            "type": "Corporate Support",
            "context": "business customer support"
        }
    ]
    
    print(f"\n📋 Will send WhatsApp to {len(companies)} corporate contacts\n")
    print("⚠️  NOTE: These are business numbers, not HR direct lines.")
    print("   Your message will request forwarding to HR/Recruitment.\n")
    
    for i, company in enumerate(companies, 1):
        print(f"\n{'='*70}")
        print(f"[{i}/{len(companies)}] {company['name']}")
        print(f"  Type: {company['type']}")
        print(f"  Phone: {company['phone']}")
        print(f"{'='*70}\n")
        
        # Professional message for corporate switchboard
        message = f"""Good afternoon,

I hope this message finds you well. I recently sent my application via email to your HR department and wanted to follow up through this channel as well.

I am a Software Engineer with 4+ years of experience in Full Stack Development and QA Automation, currently based in Bahrain with valid CPR.

I am very interested in career opportunities at {company['name']}, {company['context']}.

Could you kindly forward my contact details to your HR or Recruitment team?

**My Information:**
• Name: M. Sri Mathi
• Position Sought: Software Engineer / QA Automation Engineer
• Experience: 4+ years
• Location: Bahrain (CPR holder)
• Email: srimathip789@gmail.com
• Mobile: +973 35102870

I will attach my resume in the next message.

Thank you for your assistance.

Best regards,
Sri Mathi"""
        
        # Copy resumes to clipboard
        copy_to_clipboard(RESUME_FILES)
        
        # Open WhatsApp
        send_whatsapp(company['phone'], message, company['name'])
        
        print(f"\n  ✅ WhatsApp opened for {company['name']}")
        print(f"  📎 Resume files are in your clipboard - press Ctrl+V to attach")
        print(f"\n  💡 TIP: This is a business number, so:")
        print(f"     1. Send the message")
        print(f"     2. Press Ctrl+V to attach resumes")
        print(f"     3. Send the attachments")
        print(f"     4. They will forward to HR if relevant")
        
        if i < len(companies):
            input(f"\n  ⏸️  Press Enter after sending to continue to next company...")
            print("\n")
    
    print("\n" + "=" * 70)
    print("  ✅ WhatsApp corporate follow-up complete!")
    print("=" * 70)
    print("\n💡 Key Points:")
    print("  • These were sent to business/corporate lines")
    print("  • They are more likely to respond during business hours")
    print("  • Your email applications are still the primary contact method")
    print("  • WhatsApp serves as an additional touchpoint\n")

if __name__ == "__main__":
    main()
