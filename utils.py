
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]
         
creds = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json", scope)
client = gspread.authorize(creds)

PLANILHA = os.environ.get("PLANILHA_NOME", "gastos mensais")
ABA = os.environ.get("ABA_NOME", "página 1")

sheet = client.open(PLANILHA).worksheet(ABA)

def append_to_sheet(categoria, valor, descricao, data):
    linha = [categoria, valor, descricao, data]
    sheet.append_row(linha)
