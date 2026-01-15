from gmail_service import get_gmail_service, get_unread_messages

service = get_gmail_service()
messages = get_unread_messages(service, max_results=5)

print("Unread messages found:", len(messages))
for msg in messages:
    print("Message ID:", msg['id'])
