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

def apply_to_leadership():
    """Send applications directly to leadership and HR contacts"""
    
    contacts = [
        # GBM - Gulf Business Machines
        {
            "company": "GBM (Gulf Business Machines)",
            "role": "HR / Recruitment Team",
            "email": "bahrain@gbmme.com",
            "contact_type": "HR"
        },
        {
            "company": "GBM (Gulf Business Machines)",
            "role": "Careers Team",
            "email": "careers@gbmme.com",
            "contact_type": "HR"
        },
        
        # Beyon / Batelco Group
        {
            "company": "Beyon Solutions",
            "role": "HR / Careers Team",
            "email": "jobs@beyonsolutions.com",
            "contact_type": "HR"
        },
        {
            "company": "Beyon Solutions",
            "role": "General Inquiry (Engineering Team)",
            "email": "info@beyonsolutions.com",
            "contact_type": "Management"
        },
        {
            "company": "Batelco (Beyon Group)",
            "role": "Business Accounts / Corporate Team",
            "email": "biz@btc.com.bh",
            "contact_type": "Corporate"
        },
        
        # HR Recruitment Agencies in Bahrain
        {
            "company": "Airswift Bahrain",
            "role": "Recruitment Team - Tech Sector",
            "email": "bahrain@airswift.com",
            "contact_type": "Recruiter"
        },
        
        # Direct Companies
        {
            "company": "Tech Mahindra Bahrain",
            "role": "HR Team",
            "email": "careers.bahrain@techmahindra.com",
            "contact_type": "HR"
        }
    ]
    
    print("=" * 70)
    print("  📧 Direct Leadership & HR Outreach Campaign")
    print("  Targeting: CTOs, VPs, Engineering Managers, HR Directors")
    print("=" * 70)
    print(f"\n📋 Sending to {len(contacts)} key contacts...\n")
    
    for i, contact in enumerate(contacts, 1):
        print(f"[{i}/{len(contacts)}] {contact['company']}")
        print(f"  Role: {contact['role']}")
        print(f"  Email: {contact['email']}")
        
        # Customize subject based on contact type
        if contact['contact_type'] == "HR":
            subject = f"Software Engineer with 4+ Years Experience - Available Immediately in Bahrain"
        elif contact['contact_type'] == "Management":
            subject = f"Experienced Software Engineer Seeking Opportunities at {contact['company'].split()[0]}"
        elif contact['contact_type'] == "Recruiter":
            subject = f"Candidate Seeking IT/Software Positions in Bahrain"
        else:
            subject = f"Application for Software Engineering Position - M. Sri Mathi"
        
        # Customize body based on contact type
        if contact['contact_type'] == "HR":
            body = f"""Dear HR Team at {contact['company']},

I hope this message finds you well. I am reaching out to express my strong interest in software engineering opportunities at {contact['company']}.

I am a Software Engineer with over 4 years of proven experience in Full Stack Development and QA Automation, currently based in Bahrain with a valid CPR and driving license.

**Technical Expertise:**
• Full Stack Development: React, Angular, Node.js, .NET, C#
• QA & Test Automation: Selenium, Python, Java, API Testing
• Databases: SQL Server, MySQL, MongoDB
• DevOps: CI/CD pipelines, Git, Jenkins
• Agile/Scrum methodologies and team collaboration

**Key Strengths:**
• 4+ years delivering high-quality software solutions
• Strong problem-solving and debugging capabilities
• Excellent communication and teamwork skills
• Quick learner, adaptable to new technologies
• Available to start immediately

I am particularly drawn to {contact['company']}'s reputation for innovation and excellence in the region. I would welcome the opportunity to contribute to your team's success.

Please find my resume attached. I would be grateful for the chance to discuss how my skills and experience align with your current or future openings.

Thank you for your time and consideration.

Best regards,
M. Sri Mathi
Software Engineer
+973 35102870
srimathip789@gmail.com
"""
        
        elif contact['contact_type'] == "Management":
            body = f"""Dear {contact['company']} Team,

I hope this message reaches the appropriate department. I am a Software Engineer with 4+ years of experience seeking opportunities to contribute to {contact['company']}'s technical initiatives.

**My Background:**
I specialize in Full Stack Development and QA Automation, with hands-on experience in:
• Building scalable web applications (React, Angular, Node.js, .NET)
• Implementing comprehensive test automation frameworks (Selenium, Python, Java)
• API development and integration
• Database design and optimization
• Agile software development practices

I am currently based in Bahrain with full legal authorization to work (valid CPR and driving license) and am available for immediate start.

I would appreciate if you could forward my resume to the appropriate hiring manager or technical lead, or advise me on the best way to explore career opportunities at {contact['company']}.

Please find my detailed resume attached.

Thank you for your consideration.

Best regards,
M. Sri Mathi
+973 35102870
srimathip789@gmail.com
"""
        
        else:  # Recruiter
            body = f"""Dear Recruitment Team,

I am reaching out to explore software engineering opportunities in Bahrain through {contact['company']}.

**Candidate Profile:**
• Position Sought: Software Engineer / Full Stack Developer / QA Automation Engineer
• Experience: 4+ years in software development and quality assurance
• Location: Based in Bahrain with valid CPR
• Availability: Immediate

**Technical Skills:**
• Languages: Python, Java, JavaScript, C#, SQL
• Frontend: React, Angular, HTML5, CSS3
• Backend: Node.js, .NET, REST APIs
• Testing: Selenium, API testing, test automation frameworks
• Tools: Git, Jenkins, Jira, Agile/Scrum

**Key Achievements:**
• Developed and deployed multiple full-stack applications
• Designed comprehensive test automation frameworks
• Improved software quality through robust QA processes
• Collaborated effectively in cross-functional teams

I am seeking roles with reputable companies in Bahrain's technology sector. Please find my detailed resume attached.

I would appreciate your assistance in connecting me with suitable opportunities.

Best regards,
M. Sri Mathi
Software Engineer
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
            print(f"  ✅ Sent successfully\n")
            
            # Log it
            with open(SENT_LOG, 'a') as f:
                f.write(f"{contact['email']}\n")
            
            time.sleep(6)  # Longer delay for professional outreach
            
        except Exception as e:
            print(f"  ❌ Failed: {e}\n")
    
    print("=" * 70)
    print("  ✅ Leadership & HR outreach campaign complete!")
    print("=" * 70)
    print(f"\n📊 Contacted {len(contacts)} key decision-makers and HR contacts")
    print("💡 These direct contacts often have faster response times!")

if __name__ == "__main__":
    apply_to_leadership()
