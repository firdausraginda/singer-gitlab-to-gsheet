import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    './target-gsheet/client_secret.json', scope)
spreadsheet_id = '1cB_puQw2rz5rQZcCmNfF-gPDkQ7Hwi3Yb2KSLwixeRA'
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
worksheet = client.open_by_key(spreadsheet_id)

def write_to_spreadsheet(data, status=True, active_sheet='Sheet1'):
    
    # get the active sheet
    sheet = worksheet.worksheet(active_sheet)

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