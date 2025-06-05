import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("C:/path/to/your/creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("CafeVersionAnanda2Copy").sheet1

data = sheet.get_all_records()
print(data)

sheet.update_cell(2, 2, "Шулэн")