import base64
from bs4 import BeautifulSoup
from email.utils import parsedate_to_datetime


def _get_header(headers, name):
    for header in headers:
        if header['name'].lower() == name.lower():
            return header['value']
    return ""


def _decode_body(data):
    decoded_bytes = base64.urlsafe_b64decode(data)
    return decoded_bytes.decode("utf-8", errors="ignore")


def _extract_body(payload):
    """
    Recursively extract email body
    """
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                return _decode_body(part['body']['data'])
            elif part['mimeType'] == 'text/html':
                html = _decode_body(part['body']['data'])
                soup = BeautifulSoup(html, 'html.parser')
                return soup.get_text()
            else:
                result = _extract_body(part)
                if result:
                    return result
    else:
        if payload['body'].get('data'):
            return _decode_body(payload['body']['data'])

    return ""


def parse_email(service, message_id):
    """
    Fetch and parse a Gmail message by ID
    """
    msg = service.users().messages().get(
        userId='me',
        id=message_id,
        format='full'
    ).execute()

    headers = msg['payload']['headers']

    sender = _get_header(headers, 'From')
    subject = _get_header(headers, 'Subject')
    date_raw = _get_header(headers, 'Date')

    try:
        date = parsedate_to_datetime(date_raw)
        date = date.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        date = date_raw

    body = _extract_body(msg['payload'])

    return {
        "from": sender,
        "subject": subject,
        "date": date,
        "content": body.strip()
    }
