import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sheets_service import get_sheets_service, append_row
from config import SPREADSHEET_ID, SHEET_NAME

service = get_sheets_service()

append_row(
    service,
    SPREADSHEET_ID,
    SHEET_NAME,
    ["test@gmail.com", "Hello", "2026-01-15", "This is a test row"]
)

print("Row added successfully")
