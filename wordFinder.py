import openpyxl



def run_check():
    print("epic")


wrkbk = openpyxl.load_workbook("chinese vocab.xlsx")
known = input("Enter every character you know separated by a comma").split(",")
sh = wrkbk.active

searchable = []
results = []

for row in sh.iter_rows(min_row = 1, min_col = 1, max_row = 6000, max_col = 1):
    for cell in row:
        if(cell.value != None):
            searchable.append(cell.value)

for letter in known:
    for word in searchable:
        if(letter in word):
            results.append(word)

print(results)