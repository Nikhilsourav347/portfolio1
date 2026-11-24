from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

OUT = 'dist/assets/Nikhil-Sourav-G-Resume.pdf'
wine = colors.HexColor('#4d1427'); sage = colors.HexColor('#667468'); ink = colors.HexColor('#20211d')
doc = SimpleDocTemplate(OUT, pagesize=A4, rightMargin=42, leftMargin=42, topMargin=34, bottomMargin=32)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Name', fontName='Helvetica-Bold', fontSize=22, leading=25, textColor=wine, spaceAfter=4))
styles.add(ParagraphStyle(name='Role', fontName='Helvetica', fontSize=9, leading=13, textColor=sage, spaceAfter=12))
styles.add(ParagraphStyle(name='Head', fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=wine, spaceBefore=11, spaceAfter=5, borderWidth=0, borderPadding=0))
styles.add(ParagraphStyle(name='Body', fontName='Helvetica', fontSize=8.6, leading=12.1, textColor=ink, spaceAfter=4))
styles.add(ParagraphStyle(name='Project', fontName='Helvetica-Bold', fontSize=9.5, leading=12, textColor=ink, spaceAfter=2))
story=[]
story += [Paragraph('NIKHIL SOURAV G', styles['Name']), Paragraph('Software Development & Cloud Engineering Intern Candidate', styles['Role'])]
contact = 'Coimbatore, Tamil Nadu, India  |  +91 9840380787  |  nikhilsourav2007@gmail.com<br/>linkedin.com/in/nikhil-sourav-g-521208330  |  github.com/Nikhilsourav347  |  leetcode.com/u/nikhil_sourav347/'
story += [Paragraph(contact, styles['Body'])]
story += [Paragraph('PROFILE', styles['Head']), Paragraph('Electrical and Electronics Engineering undergraduate and AWS Certified Cloud Practitioner with hands-on experience building full-stack and cross-platform applications using React, Node.js, Express, MongoDB and Flutter. Experienced in designing multi-agent AI backends, offline-first architectures and REST API integrations, with a strong foundation in data structures, algorithms and cloud computing. Seeking Software Development and Cloud Engineering internship roles.', styles['Body'])]
story += [Paragraph('TECHNICAL SKILLS', styles['Head'])]
skills = [
['Languages', 'C, Java, Python, JavaScript, Dart, SQL, HTML, CSS'],
['Frameworks & Libraries', 'React, Node.js, Express.js, Flutter, Riverpod, GoRouter'],
['Databases', 'MongoDB, Firebase, Sqflite, Hive'],
['Cloud & Tools', 'AWS Management Console, AWS CLI, Git, GitHub, REST APIs, Postman, VS Code, Android Studio'],
['Computer Science Fundamentals', 'Data Structures and Algorithms (DSA), Object-Oriented Programming (OOP), Database Management Systems (DBMS), Operating Systems (OS)'],
['Concepts', 'Multi-Agent Systems, LLM API Integration, Offline-First Architecture']]
t=Table([[Paragraph('<b>'+a+'</b>',styles['Body']),Paragraph(b,styles['Body'])] for a,b in skills],colWidths=[1.55*inch,5.75*inch])
t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BOTTOMPADDING',(0,0),(-1,-1),2),('TOPPADDING',(0,0),(-1,-1),2)])); story += [t]
story += [Paragraph('PROJECTS', styles['Head']), Paragraph('Agentic Analytics Platform (2026)',styles['Project']), Paragraph('<b>React, Node.js, Express.js, MongoDB, REST APIs</b>  |  github.com/Nikhilsourav347/Agentic-Analytics-Platforms<br/>Built a full-stack agentic analytics platform pairing a React dashboard frontend with a multi-agent Express.js backend that turns user queries into data-driven insights. Designed specialized AI agents for distinct analytics tasks, with data persisted in MongoDB and exposed through REST APIs. Delivered an interactive command-center UI for monitoring agent activity and viewing analytics results.',styles['Body']), Paragraph('MediTrack - Elder Care & Vitals Sync Platform (2025)',styles['Project']), Paragraph('<b>Flutter, Sqflite, GoRouter, fl_chart</b>  |  github.com/Nikhilsourav347/Medictrack.git<br/>Built an offline-first health assistant app for vitals logging, trend graphs and medication adherence. Developed Emergency SOS sharing by call, SMS and WhatsApp, PDF health reports, and a caregiver admin panel with background synchronization for reconnecting offline data.',styles['Body'])]
story += [Paragraph('EDUCATION',styles['Head']), Paragraph('<b>Karpagam Institute of Technology</b> | B.E. Electrical and Electronics Engineering | Aug 2024 - May 2028 | CGPA: 8.9 | Coimbatore, India',styles['Body']), Paragraph('<b>Adharsh Vidhayalaya Matric Hr. Sec. School</b> | HSC (Class XII), 2024 | 84.8% | Tamil Nadu, India',styles['Body'])]
story += [Paragraph('CERTIFICATIONS',styles['Head']), Paragraph('AWS Certified Cloud Practitioner (CLF-C02) - Amazon Web Services (AWS)<br/>Become a Full-Stack Web Developer - LinkedIn Learning<br/>GitHub Foundations - GitHub',styles['Body'])]
doc.build(story)
