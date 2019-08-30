import os
from openpyxl import load_workbook


def get_file_structure(path):
    for root, dics, files in os.walk(path):
        for file in files:
            file_path =(os.path.join(root.replace("E:\\张文杰\\",""), file)).split('\\')
            yield file_path


if __name__ == '__main__':
    wb = load_workbook('structure.xlsx')
    ws = wb.active
    for i in get_file_structure('E:\张文杰\燎原学院'):
        ws.append(i)
    wb.save('structure.xlsx')


