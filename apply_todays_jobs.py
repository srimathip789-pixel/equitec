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
            "company": "Era Projects",
            "title": "QA/QC Engineer - Building Construction",
            "email": "hr@erabahrain.net"
        },
        {
            "company": "Era Projects",
            "title": "Project Engineer - High Rise Projects",
            "email": "hr@erabahrain.net"
        },
        {
            "company": "Zak Solutions",
            "title": "System Admin Engineer",
            "email": "zakrecruitment@zakq8.com"
        }
    ]
    
    print(f"🚀 Applying to {len(jobs)} positions from today's portal scan...\n")
    
    sent_to = set()
    
    for job in jobs:
        # Skip duplicate emails to same company
        if job['email'] in sent_to:
            print(f"⏭️  Skipping {job['company']} - {job['title']} (already sent to this email)")
            continue
            
        print(f"📨 Applying to {job['company']} for {job['title']}...")
        
        subject = f"Application for {job['title']} - M. Sri Mathi"
        
        body = f"""Dear Hiring Team at {job['company']},

I am writing to express my strong interest in the {job['title']} position currently available in Bahrain.

I am a Software Engineer with over 4 years of experience in Full Stack Development and Testing Automation (Selenium, Python, Java). My background includes extensive work in QA/QC processes, automation frameworks, and project coordination. I am currently based in Bahrain with a valid CPR and driving license.

Key highlights of my experience:
• 4+ years in Software Development & QA Automation
• Expertise in Selenium, Python, Java, C#, .NET
• Strong background in quality assurance and testing methodologies
• Experience with project documentation and stakeholder coordination

Please find my resume attached for your review. I would welcome the opportunity to discuss how my skills and experience align with your team's needs.

Best regards,
M. Sri Mathi
+973 35102870
srimathip789@gmail.com
"""
        try:
            send_email(
                to_address=job['email'],
                subject=subject,
                body=body,
                attachments=RESUME_FILES
            )
            print(f"  ✅ Sent successfully to {job['email']}")
            sent_to.add(job['email'])
            
            # Log it
            with open(SENT_LOG, 'a') as f:
                f.write(f"{job['email']}\n")
                
        except Exception as e:
            print(f"  ❌ Failed to send: {e}")
        
        time.sleep(5)
    
    print(f"\n✅ Application process complete! Sent to {len(sent_to)} companies.")

if __name__ == "__main__":
    apply_for_jobs()
