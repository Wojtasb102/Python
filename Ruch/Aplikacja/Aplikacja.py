# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Connector import *
from Searcher import *

if __name__ == '__main__':
    connector = Connector("ruch tabele.xlsx", "Database.db")
    print(connector.get_header())
    print(connector.get_header_type())
    print(connector.get_header_sql_type())
    connector.delete_selected_tables(["przyjecia", "zwolnienia", "przeniesienia"])
    print(connector.sheet_list())
    connector.change_worksheet("przyjecia")
    print(connector.get_dimension())
    connector.change_worksheet("zwolnienia")
    print(connector.get_dimension())
    connector.change_worksheet("przeniesienia")
    print(connector.get_dimension())
    connector.insert_selected_excel_sheet_data_into_sql(["przyjecia", "zwolnienia", "przeniesienia"])
    searcher = Searcher("ruch tabele.xlsx", "Database.db")
    print(searcher.execute_query("SELECT COUNT (Lp) FROM przeniesienia ")[0][0])

    searcher.clear()
    searcher.calculate_changes("przyjecia", 1)
    searcher.calculate_changes("zwolnienia", -1)
    searcher.calculate_transfer("przeniesienia")

    searcher.save()
    print("DONE!")
    input("napis")
