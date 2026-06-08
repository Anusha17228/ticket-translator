from deep_translator import GoogleTranslator
from langdetect import detect

# ── Test 1: Detect Hindi ──────────────────────────────────
def test_detect_hindi():
    text = "नमस्ते, मेरा इंटरनेट काम नहीं कर रहा है"
    lang = detect(text)
    assert lang == "hi", f"Expected 'hi', got '{lang}'"
    print("✅ Test 1 Passed: Hindi detection works")

# ── Test 2: Detect Tamil ──────────────────────────────────
def test_detect_tamil():
    text = "வணக்கம், என் கணக்கு திறக்கவில்லை"
    lang = detect(text)
    assert lang == "ta", f"Expected 'ta', got '{lang}'"
    print("✅ Test 2 Passed: Tamil detection works")

# ── Test 3: Detect French ─────────────────────────────────
def test_detect_french():
    text = "Bonjour, mon mot de passe ne fonctionne pas"
    lang = detect(text)
    assert lang == "fr", f"Expected 'fr', got '{lang}'"
    print("✅ Test 3 Passed: French detection works")

# ── Test 4: Detect Spanish ────────────────────────────────
def test_detect_spanish():
    text = "Hola, mi cuenta no funciona. Por favor ayudame"
    lang = detect(text)
    assert lang == "es", f"Expected 'es', got '{lang}'"
    print("✅ Test 4 Passed: Spanish detection works")

# ── Test 5: Detect German ─────────────────────────────────
def test_detect_german():
    text = "Hallo, mein Passwort funktioniert nicht"
    lang = detect(text)
    assert lang == "de", f"Expected 'de', got '{lang}'"
    print("✅ Test 5 Passed: German detection works")

# ── Test 6: Translate Hindi to English ───────────────────
def test_translate_hindi_to_english():
    text = "नमस्ते"
    result = GoogleTranslator(source='hi', target='en').translate(text)
    assert result is not None
    assert len(result) > 0
    print(f"✅ Test 6 Passed: Hindi→English = '{result}'")

# ── Test 7: Translate Tamil to English ───────────────────
def test_translate_tamil_to_english():
    text = "வணக்கம்"
    result = GoogleTranslator(source='ta', target='en').translate(text)
    assert result is not None
    assert len(result) > 0
    print(f"✅ Test 7 Passed: Tamil→English = '{result}'")

# ── Test 8: Translate English reply to Hindi ─────────────
def test_translate_reply_to_hindi():
    reply = "We will fix your issue within 24 hours."
    result = GoogleTranslator(source='en', target='hi').translate(reply)
    assert result is not None
    assert result != reply
    print(f"✅ Test 8 Passed: Reply→Hindi = '{result}'")

# ── Test 9: Translate English reply to Tamil ─────────────
def test_translate_reply_to_tamil():
    reply = "We will fix your issue within 24 hours."
    result = GoogleTranslator(source='en', target='ta').translate(reply)
    assert result is not None
    assert result != reply
    print(f"✅ Test 9 Passed: Reply→Tamil = '{result}'")

# ── Test 10: Translate English reply to French ───────────
def test_translate_reply_to_french():
    reply = "We will fix your issue within 24 hours."
    result = GoogleTranslator(source='en', target='fr').translate(reply)
    assert result is not None
    assert result != reply
    print(f"✅ Test 10 Passed: Reply→French = '{result}'")

# ── Test 11: Glossary replacement ────────────────────────
def test_glossary_replacement():
    glossary = {"पासवर्ड": "password", "इंटरनेट": "internet"}
    text = "मेरा पासवर्ड और इंटरनेट काम नहीं कर रहा"
    for term, replacement in glossary.items():
        text = text.replace(term, replacement)
    assert "password" in text
    assert "internet" in text
    print("✅ Test 11 Passed: Glossary replacement works")

# ── Test 12: English text not translated ─────────────────
def test_english_not_translated():
    text = "Hello, my internet is not working"
    lang = detect(text)
    if lang == "en":
        result = text
    else:
        result = GoogleTranslator(source=lang, target='en').translate(text)
    assert result == text
    print("✅ Test 12 Passed: English text unchanged")

# ── Run all tests ─────────────────────────────────────────
if __name__ == "__main__":
    print("\n" + "="*50)
    print(" RUNNING ALL TEST CASES")
    print("="*50 + "\n")

    test_detect_hindi()
    test_detect_tamil()
    test_detect_french()
    test_detect_spanish()
    test_detect_german()
    test_translate_hindi_to_english()
    test_translate_tamil_to_english()
    test_translate_reply_to_hindi()
    test_translate_reply_to_tamil()
    test_translate_reply_to_french()
    test_glossary_replacement()
    test_english_not_translated()

    print("\n" + "="*50)
    print(" ALL 12 TESTS PASSED! ✅")
    print("="*50)
