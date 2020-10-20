import csv
import operator
import time

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '=' : operator.eq,
    '<=' : operator.le,
    '>=' : operator.ge,
    '>' : operator.gt,
    '<' : operator.lt,
}

def GetFilters():
    filters = input('Digite os filtros separador por '';'' : ')
    result = []
    for filter in filters.split(sep = ";"):
        result.append(filter.split(sep = ' '))
    
    return result

def GetHeaderId(row):
    index = 0
    result = dict()
    for att in row:
        result[att] = index
        index += 1

    return result

def EvaluateRow(row, filters, headersDict):
    for filter in filters:
        i = headersDict[filter[0]]
        if(ops[filter[1]](row[i], filter[2]) == False):
            return False
    return True

pathFile = input('Digite o caminho do csv: ')
filters = GetFilters()

start = time.time()
rows = []
with open(pathFile, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';',)
    
    headersDict = dict()
    for row in spamreader:
        if(spamreader.line_num == 1):
            headersDict = GetHeaderId(row)
            rows.append(row)
        else:
            if(EvaluateRow(row, filters, headersDict)):
                rows.append(row)
end = time.time()

print(f'Tempo de processamento: {end-start}')

pathOutFile = input('Digite o caminho de saída do novo csv: ')
with open(pathOutFile, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(rows)