from statistics import median, mean

f = open('salary.txt', 'r', encoding='UTF8')
table = []
for line in f:
    city = ''
    salary = ''
    count = 0
    for i in range(len(line)):
        if count == 1:
            city += line[i]
        if count == 3:
            salary += line[i]
        if line[i] == '"':
            count += 1
    city = city.rstrip(city[-1])
    salary = salary.rstrip(salary[-1])
    table.append([city,salary])

table.pop(0)

for i in range(len(table)-3):
    if table[i][0] == 'Республика Марий Эл':
        table.pop(i)
    if table[i][0] == 'Республика Мордовия':
        table.pop(i)
    if table[i][0] == 'г. Севастополь':
        table.pop(i)

sal = []
for row in table:
    sal.append(int(row[1]))

sal = sorted(sal)

print(sal)

print()
print(mean(sal))
print()
print(median(sal))
print()
print(sal[0])
print(sal[21])
print(sal[29])
