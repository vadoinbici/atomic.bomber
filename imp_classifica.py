classifica = {}
with open('classifica.txt', 'r', encoding='utf-8') as f:
    for riga in f:
        key, value = line.strip().split(': ', 1)
        classifica[int(key)] = value

classifica = sorted(classifica.items)
