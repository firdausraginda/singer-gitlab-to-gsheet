import gspread
from oauth2client.service_account import ServiceAccountCredentials
from src.config import get_config_item
import time
import os

# set the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# get creds from client_secret.json
path_to_client_secret = os.path.join(os.path.dirname(__file__), '../client_secret.json')
creds = ServiceAccountCredentials.from_json_keyfile_name(path_to_client_secret, scope)

# authorize gspread using client_secret.json
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
worksheet = client.open_by_key(get_config_item('spreadsheet_id'))

def write_to_spreadsheet(data, status=True):
    
    # get the active sheet
    sheet = worksheet.worksheet(get_config_item('active_sheet'))

    # set active row in spreadsheet
    active_row = len(sheet.get_all_values())+1

    # try to update spreadsheet, and wait 10s if fail before try again
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