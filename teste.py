import requests
from prettyconf import config

SECRET_KEY = config('NOTION_API_SECRET_KEY')
API_URL = config('NOTION_API_URL')
TESTS_DATABASE_ID = config('TESTS_DATABASE_ID')

headers = {
    'Authorization': f'Bearer {SECRET_KEY}',
    'Notion-Version': '2021-08-16',
}

database_id = TESTS_DATABASE_ID
url = f'{API_URL}/databases/{database_id}'
response = requests.get(url, headers=headers)

print(url)
print(response.status_code)
print(response.text)
