import xlrd


def excelreader(filename, sheetname):
    '''
    按行获取excel文件指定sheet所有数据，返回为二维列表形式
    :param filename:path and filename
    :param sheetname:
    :return: [[...],[...],...]
    '''
    data = xlrd.open_workbook('./data/%s' % filename)
    table = data.sheet_by_name('{}'.format(sheetname))
    li = []
    for i in range(1, table.nrows):
        li.append(table.row_values(i))
    print(li)
    return li


if __name__ == '__main__':
    a = excelreader(r'D:\casaba\自动化\new\data\sku (3).xlsx', 'product')
    print(a)
