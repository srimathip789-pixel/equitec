import os
import sys
import time
import smtplib
import ssl
from email.message import EmailMessage

# Configuration
SENDER_EMAIL = "srimathip789@gmail.com"
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD", "wntwccrduqxggrfz")

RESUME_FILES = [
    r"c:\Users\Sri Mathi\OneDrive\Desktop\RESUME\job_automation\resumes\2026 resume\Sri_Mathi_Software_Engineer_2026.docx",
    r"c:\Users\Sri Mathi\OneDrive\Desktop\RESUME\job_automation\resumes\2026 resume\SriMathi_CV_4+exp.pdf"
]

SENT_LOG = r"c:\Users\Sri Mathi\OneDrive\Desktop\RESUME\job_automation\logs\sent_emails.log"

def send_email(to_address, subject, body, attachments):
    """Send email with attachments"""
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_address
    msg["Subject"] = subject
    msg.set_content(body)
    
    # Attach files
    for resume_path in attachments:
        if os.path.exists(resume_path):
            with open(resume_path, "rb") as f:
                file_data = f.read()
                file_name = os.path.basename(resume_path)
                msg.add_attachment(
                    file_data,
                    maintype="application",
                    subtype="octet-stream",
                    filename=file_name,
                )
    
    # Send
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, EMAIL_APP_PASSWORD)
        server.send_message(msg)

def apply_for_jobs():
    jobs = [
        {
            "company": "Unipal",
            "title": "Full Stack Software Engineer",
            "email": "support@unipal.me"
        },
        {
            "company": "Binance",
            "title": "QA Engineer (Java coding)",
            "email": "careers@binance.com"
        },
        {
            "company": "SEL Middle East",
            "title": "Project Engineer II - Automation",
            "email": "careers@selinc.com"
        },
        {
            "company": "01 Systems",
            "title": "Senior Quality Assurance Automation Engineer",
            "email": "asharif@01systems.com"
        }
    ]
    
    print(f"🚀 Starting individual applications for {len(jobs)} jobs from the image...")
    
    for job in jobs:
        print(f"\n📨 Applying to {job['company']} for {job['title']}...")
        
        subject = f"Application for {job['title']} role - M. Sri Mathi"
        
        body = f"""Dear Hiring Team at {job['company']},

I'm writing to express my strong interest in the {job['title']} position I saw posted for Manama.

I am a Software Engineer with over 4 years of experience in Full Stack Development and Testing Automation (Selenium, Python, Java). I am currently based in Bahrain and am impressed by {job['company']}'s impact in the region.

Please find my resume attached for your review. I look forward to the possibility of discussing how my skills could benefit your team.

Best regards,
M. Sri Mathi
+973 35102870
"""
        try:
            send_email(
                to_address=job['email'],
                subject=subject,
                body=body,
                attachments=RESUME_FILES
            )
            print(f"  ✅ Sent successfully to {job['email']}")
            
            # Log it
            with open(SENT_LOG, 'a') as f:
                f.write(f"{job['email']}\n")
                
        except Exception as e:
            print(f"  ❌ Failed to send: {e}")
        
        time.sleep(5) # Small delay

if __name__ == "__main__":
    apply_for_jobs()
