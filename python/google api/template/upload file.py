file_metadata = {
    'name': 'data.xlsx',
    'parents': ['1kMHxD1Ar-YJh5Q2Zj75dwuTdTRVCHw8I', '1UvqOcKSMKxOgB9y-gxPgjsM94tZUOPPg'],
}

media = MediaFileUpload('data.xlsx')
file = service.files().create(body=file_metadata,
                              media_body=media,
                              fields='id').execute()