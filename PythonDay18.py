import smtplib
import ssl
from email.message import EmailMessage
sender_email = "layatrimurakada@gmail.com"
password = "zhle bbcn afqb rxpd"

receiver_email = "kirlampalliharika@gmail.com"
message = EmailMessage()
message["from"] = sender_email
message["To"] = receiver_email
message["subject"] = "welcome Mail. meeting invitation from Codegnan"
message.set_content(f"""

Hi Harika Priyadharshini,


We are excited to invite you to a meeting with Codegnan.
Please join the meeting on July 11, 2026 at 10:00 PM (Asia/Kolkata\nYour meeting link is: https://meet.cliqqai.com/422406
Please follow the instructions below to join the meeting:\nMake sure there is no background noise
Click on the meeting link provided above.\nEnsure you have a stable internet connection.
Enable noise cancellation on your devic\nWe look forward to speaking with you.


Thank you,
Codegnan
""")

context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls(context = context)
    smtp.ehlo()
    smtp.login(sender_email , password)
    smtp.send_message(message)
