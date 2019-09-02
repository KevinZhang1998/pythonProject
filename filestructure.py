import os
from openpyxl import load_workbook


def get_file_structure(path):
    for root, dics, files in os.walk(path):
        for file in files:
            file_path =(os.path.join(root.replace("E:\\xxx\\",""), file)).split('\\')
            yield file_path


if __name__ == '__main__':
    wb = load_workbook('structure.xlsx')
    ws = wb.active
    for i in get_file_structure('E:\xxx\xxx'):
        ws.append(i)
    wb.save('structure.xlsx')


