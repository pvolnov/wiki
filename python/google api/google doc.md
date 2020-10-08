Installing
---

https://developers.google.com/drive/api/v3/quickstart/python

`pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

1. Auth and save 

```python
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.file']


flow = InstalledAppFlow.from_client_secrets_file(
    'credentials.json', SCOPES)
creds = flow.run_local_server(port=0)
# Save the credentials for the next run
with open('token.pickle', 'wb') as token:
    pickle.dump(creds, token)

```

2. Create folder
```python
file_metadata = {
    'name': '06.08',
    'parents': ['1kMHxD1Ar-YJh5Q2Zj75dwuTdTRVCHw8I'],
    'mimeType': 'application/vnd.google-apps.folder'
}
# #
file = service.files().create(body=file_metadata,
                              fields='id').execute()
```

3. Upload file
```python
file_metadata = {
    'name': 'data.xlsx',
    'parents': ['1kMHxD1Ar-YJh5Q2Zj75dwuTdTRVCHw8I', '1UvqOcKSMKxOgB9y-gxPgjsM94tZUOPPg'],
}

media = MediaFileUpload('data.xlsx')
file = service.files().create(body=file_metadata,
                              media_body=media,
                              fields='id').execute()
```
