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

def apply_to_standard_chartered():
    """Send application to Standard Chartered HR"""
    
    contact = {
        "company": "Standard Chartered Bank (Bahrain)",
        "email": "AskHR@sc.com",
    }
    
    print(f"📨 Applying to {contact['company']}...")
    
    subject = f"Software Engineer / IT Professional Application - M. Sri Mathi (Bahrain Based)"
    
    body = f"""Dear Recruiting Team at Standard Chartered,

I am writing to express my strong interest in Software Engineering opportunities at Standard Chartered in Bahrain. I have followed the bank's digital transformation journey and its commitment to technology-driven banking solutions.

I am a Software Engineer with over 4 years of experience specializing in Full Stack Development and QA Automation. I am currently based in Bahrain with a valid CPR and driving license.

**My Profile Highlights:**
• 4+ years in software development (Python, Java, JavaScript, .NET, C#)
• Expertise in Full Stack frameworks (React, Angular, Node.js)
• Strong background in Test Automation (Selenium, API Testing)
• Experience in Agile environments and CI/CD development
• Knowledge of cloud technologies and modern software architecture

I am highly motivated to bring my technical skills and proactive approach to the Standard Chartered engineering team.

Please find my resume attached for your review. I look forward to the possibility of discussing how my background can contribute to the bank's technology initiatives.

Thank you for your consideration.

Best regards,
M. Sri Mathi
+973 35102870
srimathip789@gmail.com
"""
    
    try:
        send_email(
            to_address=contact['email'],
            subject=subject,
            body=body,
            attachments=RESUME_FILES
        )
        print(f"  ✅ Sent successfully to {contact['email']}")
        
        # Log it
        with open(SENT_LOG, 'a') as f:
            f.write(f"{contact['email']}\n")
            
    except Exception as e:
        print(f"  ❌ Failed to send: {e}")

if __name__ == "__main__":
    apply_to_standard_chartered()
