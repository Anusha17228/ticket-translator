

Priya S <riyapriya2507@gmail.com>

15:46 (2 minutes ago)

to me



\# Multilingual Ticket Translator



\## What it does

Reads support tickets written in any language,

automatically detects the language, translates to

English for engineers, then translates the reply

back to the customer's original language.



\## Setup Instructions

1\. Install Python from python.org

2\. Open CMD and run:

&#x20;  pip install langdetect deep-translator pytest

3\. Add ticket .txt files to the /tickets folder

4\. Run: python main.py



\## Run Instructions

python main.py



\## Run Tests

python -m pytest test\_cases/ -v



\## Architecture Overview

\- translator.py - language detection and translation

\- database.py - saves all tickets to SQLite database

\- main.py - entry point, runs everything

\- glossary/ - technical terms kept unchanged

\- tickets/ - input ticket files (any language)

\- outputs/ - translated output files saved here



\## AI Capability Used

\- Agent Loop: automatically processes all tickets

\- External API: Google Translate via deep-translator



\## Assumptions and Limitations

\- Requires internet connection for translation

\- Works best with clearly written sentences

\- Supported languages: Hindi, Spanish, French, and more



