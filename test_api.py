import google.generativeai as genai

# Setup client
client = genai.Client(api_key="AIzaSyDJJVFTUcE4EKWlYNtK3g-FcK6KgcB89hM")

try:
    # Testing with the latest available model (e.g., gemini-2.0-flash)
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents="Write a 3-word slogan for a tech company."
    )
    
    print(f"Model Output: {response.text}")
    print("✅ Connection Verified.")
except Exception as e:
    print(f"❌ Connection Failed: {e}")
