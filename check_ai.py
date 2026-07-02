import google.generativeai as genai

# PASTE YOUR KEY HERE
API_KEY = "paste your api key here."

genai.configure(api_key=API_KEY)

print("--- 📡 CONTACTING GOOGLE AI ---")
try:
    # Ask Google: "What models can I use?"
    models = genai.list_models()
    
    found_any = False
    for m in models:
        # We only care about models that can generate content (write text)
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ AVAILABLE: {m.name}")
            found_any = True
            
    if not found_any:
        print("❌ Connect successful, but no text models found. Check your Project settings.")
        
except Exception as e:
    print(f"❌ CONNECTION ERROR: {e}")
