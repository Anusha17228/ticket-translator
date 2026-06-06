import os
import json
from langdetect import detect
from deep_translator import GoogleTranslator

def load_glossary():
    path = "glossary/glossary.json"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def apply_glossary(text, glossary):
    for term in glossary:
        text = text.replace(term, term)
    return text

def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"

def translate_to_english(text, lang):
    try:
        if lang == "en":
            return text
        return GoogleTranslator(source=lang, target="en").translate(text)
    except Exception as e:
        print(f" Error: {e}")
        return text

def translate_reply(reply_en, lang):
    try:
        if lang == "en":
            return reply_en
        return GoogleTranslator(source="en", target=lang).translate(reply_en)
    except Exception as e:
        print(f" Error: {e}")
        return reply_en

def save_output(ticket_name, original, lang, translated, reply_en, reply_translated):
    os.makedirs("outputs", exist_ok=True)
    out_path = f"outputs/{ticket_name}_output.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"=== ORIGINAL TICKET (Language: {lang}) ===\n")
        f.write(original + "\n\n")
        f.write(f"=== TRANSLATED TO ENGLISH ===\n")
        f.write(translated + "\n\n")
        f.write(f"=== ENGINEER REPLY (English) ===\n")
        f.write(reply_en + "\n\n")
        f.write(f"=== REPLY TRANSLATED BACK ({lang}) ===\n")
        f.write(reply_translated + "\n")
    print(f" Saved: {out_path}")

def process_all_tickets():
    glossary = load_glossary()
    ticket_files = [f for f in os.listdir("tickets") if f.endswith(".txt")]
    print(f"\nProcessing {len(ticket_files)} ticket(s)...\n")
    for filename in ticket_files:
        print(f"Processing: {filename}")
        with open(f"tickets/{filename}", "r", encoding="utf-8") as f:
            original_text = f.read().strip()
        processed_text = apply_glossary(original_text, glossary)
        lang = detect_language(processed_text)
        english_text = translate_to_english(processed_text, lang)
        print(f" Language detected: {lang}")
        print(f" English: {english_text[:60]}")
        reply_en = "Thank you for contacting support. We will resolve your issue within 24 hours."
        reply_translated = translate_reply(reply_en, lang)
        save_output(filename.replace(".txt",""), original_text, lang, english_text, reply_en, reply_translated)
        print(f" Done!\n")
    print("All tickets processed!")

if __name__ == "__main__":
    process_all_tickets()
