"""
CSDF Practical No. 2: CAPTCHA Generation and Verification
Reference: CSDF2 .pdf & Assignment Group A-2 Manual
"""

import os
import random
import string
from captcha.image import ImageCaptcha
from PIL import Image

# 1. Generate random CAPTCHA text (6 characters of uppercase letters & digits)
characters = string.ascii_uppercase + string.digits
captcha_text = ''.join(random.choices(characters, k=6))

# 2. Create CAPTCHA image using ImageCaptcha
captcha = ImageCaptcha(width=250, height=80)
image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'captcha.png')
captcha.write(captcha_text, image_path)

print("=" * 50)
print("===== CAPTCHA GENERATION AND VERIFICATION =====")
print("=" * 50)
print(f"CAPTCHA image generated: captcha.png")
print("Opening the CAPTCHA image on your screen...")

# 3. Open the generated image in system default viewer
try:
    img = Image.open(image_path)
    img.show()
except Exception as e:
    print(f"(Could not display image automatically: {e})")

# 4. Verify user input
user_input = input("\nEnter the CAPTCHA shown in the image: ").strip()

if user_input.upper() == captcha_text:
    print("\n[SUCCESS] CAPTCHA verified successfully!")
    print(">>> Access Granted. <<<")
else:
    print("\n[FAILED] Incorrect CAPTCHA!")
    print(f"(Correct was: {captcha_text})")
    print(">>> Access Denied. <<<")

print("=" * 50)
