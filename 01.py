import os, random, shutil, time
from google import genai

client = genai.Client()

def analyze(text):
    prompt = f'Only reply "happy", "sad", or "neutral" for this text: "{text}"'
    r = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    mood = r.text.strip().lower()
    return mood if mood in ["happy", "sad", "neutral"] else "neutral"

def copy_file(times):
    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    if not files: return
    f = random.choice(files)
    for i in range(times):
        new = f"{os.path.splitext(f)[0]}_{i}_{int(time.time())}{os.path.splitext(f)[1]}"
        shutil.copy(f, new)
        print("copied", new)

text = input("How are you feeling today? > ")
mood = analyze(text)
print("AI:", mood)
if mood == "happy": copy_file(2)
elif mood == "sad": copy_file(1)
else: print("neutral, nothing done")