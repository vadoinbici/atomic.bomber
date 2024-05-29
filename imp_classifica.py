def leggi_file(nome_file):
    classifica = {}
    with open(nome_file, 'r', encoding='utf-8') as f:
        for riga in f:
            key, value = riga.strip().split(': ', 1)
            classifica[int(key)] = value

        return classifica

def scrivi_record(record):
    with open('record.txt', 'r+', encoding='utf-8') as f:
        f.truncate(0)
    with open('record.txt', 'w', encoding='utf-8') as f:
        for key, value in record.items():
            f.write(f"{key}: {value}\n")

def confronto(class_temp, record):
    key, value = class_temp.items()
    key1, value1 = record.items()
    if key > key1:
        if value['case distrutte'] > value1['case distrutte']:
            if value['precisione'] > value1['precisione']:
                scrivi_record(class_temp)





class_temp = leggi_file('classifica.txt')
record = leggi_file('record.txt')
confronto(class_temp, record)
