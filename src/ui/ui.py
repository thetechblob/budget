# file to contain all ui relate requests
from src.services import file_handler



def get_nett_for_range():
    handler = file_handler.FileHandler()
    df = handler.read_transactions('transactions.csv')


