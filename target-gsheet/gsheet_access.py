import gspread
from oauth2client.service_account import ServiceAccountCredentials
from src.config import get_config_item
import time

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    './target-gsheet/client_secret.json', scope)
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
worksheet = client.open_by_key(get_config_item('spreadsheet_id'))

def write_to_spreadsheet(data, status=True):
    
    # get the active sheet
    sheet = worksheet.worksheet(get_config_item('active_sheet'))

    active_row = len(sheet.get_all_values())+1

    while status:
        try:
            if active_row == 1:
                for idx, (key, val) in enumerate(data.items()):
                    sheet.update_cell(1, idx+1, key)
                    sheet.update_cell(2, idx+1, val)
            else:
                for idx, (key, val) in enumerate(data.items()):
                    sheet.update_cell(active_row, idx+1, val)
            
            status = False    
        except Exception as err:
            print(err)
            time.sleep(10)
    
    return active_row