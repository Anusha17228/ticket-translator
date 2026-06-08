# Multilingual Ticket Translator
AI Prototype Challenge Project

## What It Does
Reads support tickets written in any regional or international language,
automatically detects the language, translates to English for engineers,
and translates the engineer reply back to the customer's original language.

## Supported Languages (30+)
Indian: Hindi, Tamil, Telugu, Malayalam, Kannada, Marathi, 
Gujarati, Punjabi, Bengali, Urdu, Odia

International: French, German, Spanish, Italian, Portuguese, 
Russian, Chinese, Japanese, Korean, Arabic, Turkish, 
Vietnamese, Thai, Indonesian, Dutch, Polish, Swedish

## Setup Instructions
1. Install Python 3.12 or above
2. Open Command Prompt
3. Run: pip install deep-translator langdetect
4. Put ticket .txt files inside the tickets/ folder
5. Run: python translator.py
6. Check outputs/ folder for results

## Run Instructions
python translator.py

## Architecture Overview
tickets/ folder → translator.py → detects language
→ translates to English → engineer reply
→ translates reply back to original language
→ saves both versions in outputs/ folder

## Assumptions and Limitations
- Requires internet connection for Google Translate API
- Language detection may fail on very short texts (less than 10 words)
- Glossary.json must be manually updated for new technical terms
- Translation accuracy depends on Google Translate

## AI Usage
Built using Claude AI as coding assistant.
Demonstrates External API Integration (Google Translate)
and Agent Loop processing multiple tickets automatically.
