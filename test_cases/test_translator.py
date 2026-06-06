from translator import detect_language, load_glossary

def test_english_detected():
    # Longer sentence = more accurate detection
    result = detect_language("My login is not working and I need help with my account password")
    assert result == "en"

def test_glossary_loads():
    g = load_glossary()
    assert "error" in g

def test_hindi_not_english():
    lang = detect_language("मेरा लॉगिन काम नहीं कर रहा है और मुझे मदद चाहिए")
    assert lang != "en"
