file_metadata = {
    'name': '06.08',
    'parents': ['1kMHxD1Ar-YJh5Q2Zj75dwuTdTRVCHw8I'],
    'mimeType': 'application/vnd.google-apps.folder'
}
# #
file = service.files().create(body=file_metadata,
                              fields='id').execute()