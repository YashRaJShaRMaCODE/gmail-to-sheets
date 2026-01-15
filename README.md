# 📧 Gmail to Google Sheets Automation

**Author:** Yash Raj Sharma  


## 📖 Project Overview

This project is a Python-based automation system that integrates the **Gmail API** and **Google Sheets API** using **OAuth 2.0 authentication**.  
It reads real unread emails from a Gmail inbox, extracts structured information, and appends the data into a Google Sheet in an append-only and duplicate-safe manner.

The system is designed to be **idempotent**, meaning running the script multiple times will not create duplicate rows in the spreadsheet.


## 🎯 Objective

For each qualifying unread email in the Gmail inbox, the script appends a new row to Google Sheets with the following fields:

| Column | Description |
|------|-------------|
| From | Sender email address |
| Subject | Email subject |
| Date | Date & time received |
| Content | Email body (plain text) |


## 🏗️ High-Level Architecture

Gmail Inbox
|
| (Gmail API + OAuth 2.0)
v
Python Automation Script
|
|-- Email parsing
|-- Duplicate detection (state.json)
|
v
Google Sheets

## 🛠️ Tech Stack

- **Language:** Python 3  
- **APIs:** Gmail API, Google Sheets API  
- **Authentication:** OAuth 2.0 (Installed App)  
- **Libraries:**
  - google-api-python-client
  - google-auth
  - google-auth-oauthlib
  - google-auth-httplib2
  - beautifulsoup4
  - python-dateutil

## 📂 Project Structure
gmail-to-sheets/
├── src/
│ ├── gmail_service.py
│ ├── sheets_service.py
│ ├── email_parser.py
│ ├── state_manager.py
│ └── main.py
│
├── credentials/
│ └── credentials.json (NOT committed)
│
├── proof/
│ ├── inbox.png
│ ├── sheet.png
│ └── oauth.png
│
├── config.py
├── requirements.txt
├── .gitignore
└── README.md

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <YOUR_REPOSITORY_LINK>
cd gmail-to-sheets

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Google Cloud Configuration

Create a Google Cloud project

Enable Gmail API and Google Sheets API

Configure OAuth Consent Screen (External)

Add your Gmail address as a test user

Create OAuth Client (Desktop App)

Download credentials.json and place it inside:

credentials/credentials.json

4️⃣ Configure Google Sheet

Edit config.py:

SPREADSHEET_ID = "YOUR_GOOGLE_SHEET_ID"
SHEET_NAME = "Sheet1"

5️⃣ Run the Script
python src/main.py

🔐 OAuth Flow Explanation

The project uses the OAuth 2.0 Installed App flow.

On the first run:

A browser window opens

The user grants Gmail and Sheets permissions

A token.json file is created locally

On subsequent runs:

The stored token is reused and refreshed automatically

This approach ensures secure authentication without storing user credentials.

🧠 Duplicate Prevention Logic

Each Gmail email has a unique Message ID.
The script maintains a list of processed Message IDs to prevent duplicate entries.

How it works:

Fetch unread emails

Check Message ID against stored state

If already processed → skip

Else → process and store Message ID

This guarantees append-only, duplicate-free execution.

💾 State Persistence Method

Processed email IDs are stored in a local JSON file:

{
  "processed_ids": [
    "message_id_1",
    "message_id_2"
  ]
}

Why this approach?

Lightweight and fast

No external database required

Survives script re-runs

Simple and reliable for automation use-cases

🚧 Challenges Faced & Solutions
Issue: OAuth Insufficient Scope Errors

Encountered 403 Insufficient Authentication Scopes

Occurred due to reusing tokens created with limited permissions

Solution:

Unified Gmail and Sheets scopes

Deleted existing token.json to force re-authentication

⚠️ Limitations

Email attachments are not processed

Only unread Inbox emails are handled

Local state file is not suitable for distributed systems

Very large inboxes may require pagination enhancements

📸 Proof of Execution

Screenshots demonstrating successful execution are included in the /proof folder:

Gmail inbox with unread emails

Google Sheet populated with rows

OAuth consent screen

🎥 Demo Video: (Add link here)

🔄 Post-Submission Modification Readiness

The modular design allows quick changes such as:

Filtering emails from the last 24 hours

Adding new columns (e.g., labels)

Excluding automated emails (no-reply)

✅ Conclusion

This project demonstrates:

Secure OAuth-based API integration

Clean and modular Python design

Reliable duplicate prevention

Production-style automation logic

Real-world Gmail to Sheets data pipeline