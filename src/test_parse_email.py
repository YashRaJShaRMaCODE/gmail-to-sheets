from gmail_service import get_gmail_service, get_unread_messages
from email_parser import parse_email

service = get_gmail_service()
messages = get_unread_messages(service, max_results=1)

if not messages:
    print("No unread emails to parse")
else:
    msg_id = messages[0]['id']
    email_data = parse_email(service, msg_id)

    print("FROM:", email_data['from'])
    print("SUBJECT:", email_data['subject'])
    print("DATE:", email_data['date'])
    print("CONTENT:", email_data['content'][:300])
