from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SAMPLE_SPREADSHEET_ID = '1OQstaXj8e7wWv4-VM-uArPW0rE32kj_Eak056WnVDXg'
SAMPLE_RANGE_NAME = 'Лист1!A2:A30000'

def update_google_sheets():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    codes = []
    for row in values:
        codes.append(row[0].replace(".", "").strip("0"))
    items = UaTasks.select(UaTasks.code, UaTasks.avilable).where(UaTasks.code.in_(codes)).execute()
    items = {i.code: i.avilable for i in items}
    res = []
    for code in codes:
        if code in items:
            res.append(10 if items[code] else 0)
        else:
            res.append(0)

    service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Лист1!D2:D10000",
        valueInputOption='RAW', body={
            'values': [[r] for r in res],
        }).execute()