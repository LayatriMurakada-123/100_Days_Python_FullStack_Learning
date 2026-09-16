import segno

# Developer Profile Details
profile = """
================================
        DEVELOPER PROFILE
================================

Name: Layatri Murakada

Role: Python Full Stack Developer

Skills:
Python
SQL
HTML
CSS
JavaScript
React

Email:
layatrimurakada@gmail.com

LinkedIn:
https://www.linkedin.com/in/layatri-murakada-86403a296/

GitHub:
https://github.com/LayatriMurakada-123

YouTube:
https://www.youtube.com/@LayatriMurakada-h1o

Instagram:
https://www.instagram.com/layatri_murakada/

================================
        THANK YOU!
================================
"""

# Create QR Code
qr = segno.make(profile)

# Save QR Code
qr.save("developer_profile.png", scale=10)

print("Developer Profile QR Code Created Successfully!")
