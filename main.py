from database import init_db
from translator import process_all_tickets

print("====================================")
print(" Multilingual Ticket Translator")
print("====================================")

init_db()
process_all_tickets()
