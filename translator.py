import os
import json
from langdetect import detect
from deep_translator import GoogleTranslator

LANGUAGE_NAMES = {
    "hi": "Hindi",
    "ta": "Tamil",
    "te": "Telugu",
    "ml": "Malayalam",
    "kn": "Kannada",
    "mr": "Marathi",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "bn": "Bengali",
    "ur": "Urdu",
    "or": "Odia",
    "as": "Assamese",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "it": "Italian",
    "pt": "Portuguese",
    "ru": "Russian",
    "zh-cn": "Chinese",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
    "tr": "Turkish",
    "vi": "Vietnamese",
    "th": "Thai",
    "id": "Indonesian",
    "nl": "Dutch",
    "pl": "Polish",
    "sv": "Swedish",
    "en": "English"
}

def load_glossary(path="glossary.json"):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def detect_language(text):
    try:
        lang = detect(text)
        lang_name = LANGUAGE_NAMES.get(lang, lang)
        print(f" Detected language: {lang_name} ({lang})")
        return lang
    except:
        print(" Could not detect language, defaulting to English")
        return "en"

def apply_glossary(text, glossary):
    for term, replacement in glossary.items():
        text = text.replace(term, replacement)
    return text

def translate_to_english(text, source_lang):
    try:
        if source_lang == "en":
            return text
        # Handle Chinese variant
        if source_lang == "zh-cn" or source_lang == "zh":
            source_lang = "zh-CN"
        translator = GoogleTranslator(source=source_lang, target='en')
        result = translator.translate(text)
        return result if result else text
    except Exception as e:
        print(f" Translation error: {e}")
        return text

def translate_reply(reply_text, target_lang):
    try:
        if target_lang == "en":
            return reply_text
        if target_lang == "zh-cn" or target_lang == "zh":
            target_lang = "zh-CN"
        translator = GoogleTranslator(source='en', target=target_lang)
        result = translator.translate(reply_text)
        return result if result else reply_text
    except Exception as e:
        print(f" Reply translation error: {e}")
        return reply_text

def save_output(ticket_name, original, lang, translated, reply_en, reply_translated):
    os.makedirs("outputs", exist_ok=True)
    lang_name = LANGUAGE_NAMES.get(lang, lang)
    out_path = f"outputs/{ticket_name}_output.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"=== ORIGINAL TICKET ===\n")
        f.write(f"Language Detected: {lang_name} ({lang})\n")
        f.write("-" * 40 + "\n")
        f.write(original + "\n\n")
        f.write(f"=== TRANSLATED TO ENGLISH ===\n")
        f.write("-" * 40 + "\n")
        f.write(translated + "\n\n")
        f.write(f"=== ENGINEER REPLY (English) ===\n")
        f.write("-" * 40 + "\n")
        f.write(reply_en + "\n\n")
        f.write(f"=== REPLY IN ORIGINAL LANGUAGE ({lang_name}) ===\n")
        f.write("-" * 40 + "\n")
        f.write(reply_translated + "\n")
    print(f" Saved: {out_path}")

def process_all_tickets():
    glossary = load_glossary()

    if not os.path.exists("tickets"):
        print("ERROR: tickets folder not found!")
        return

    ticket_files = [f for f in os.listdir("tickets") if f.endswith(".txt")]

    if not ticket_files:
        print("No ticket files found in tickets folder!")
        return

    print(f"\n{'='*50}")
    print(f" MULTILINGUAL TICKET TRANSLATOR")
    print(f" Processing {len(ticket_files)} ticket(s)")
    print(f"{'='*50}\n")

    success = 0
    failed = 0

    for filename in ticket_files:
        print(f"Ticket: {filename}")
        print("-" * 30)
        try:
            with open(f"tickets/{filename}", "r", encoding="utf-8") as f:
                original_text = f.read().strip()

            processed_text = apply_glossary(original_text, glossary)
            lang = detect_language(processed_text)
            lang_name = LANGUAGE_NAMES.get(lang, lang)
            english_text = translate_to_english(processed_text, lang)
            print(f" English: {english_text[:80]}...")

            reply_en = "Thank you for contacting support. We have received your ticket and our team will resolve the issue within 24 hours. Please feel free to contact us again if needed."

            reply_translated = translate_reply(reply_en, lang)
            print(f" Reply ({lang_name}): {reply_translated[:60]}...")

            save_output(
                filename.replace(".txt", ""),
                original_text,
                lang,
                english_text,
                reply_en,
                reply_translated
            )
            success += 1
            print(f" Status: Done!\n")

        except Exception as e:
            print(f" Error processing {filename}: {e}\n")
            failed += 1

    print(f"{'='*50}")
    print(f" DONE! Success: {success} | Failed: {failed}")
    print(f" Check the outputs/ folder for results")
    print(f"{'='*50}")

if __name__ == "__main__":
    process_all_tickets()
