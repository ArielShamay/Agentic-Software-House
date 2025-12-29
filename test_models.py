import os
import google.generativeai as genai
from dotenv import load_dotenv

# טעינת המפתח
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ שגיאה: לא נמצא מפתח API בקובץ .env")
else:
    # חיבור לגוגל
    genai.configure(api_key=api_key)

    print("🔍 בודק איזה מודלים זמינים עבורך...")
    try:
        found = False
        for m in genai.list_models():
            # אנחנו מחפשים רק מודלים שיודעים לייצר טקסט (generateContent)
            if 'generateContent' in m.supported_generation_methods:
                print(f"- {m.name}")
                found = True
        
        if not found:
            print("❌ לא נמצאו מודלים זמינים. בדוק את המפתח שלך.")
            
    except Exception as e:
        print(f"❌ שגיאה בחיבור: {e}")