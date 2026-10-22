import openpyxl


def read_excel():

    workbook = openpyxl.load_workbook(
        "testdata/login data.xlsx"
    )

    sheet = workbook.active

    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):

        username = row[0]
        password = row[1]

        data.append((username, password))

    return data

