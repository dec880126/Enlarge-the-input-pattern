row_num = int(input('Please tell me the number of row:'))
row = []

for i in range(row_num) :
    row.append(input())

print('--------Output--------')


for j in range(row_num) :
    a = list(row[j])
    for g in range(len(a)) :
        change = a[g]
        if change == '*' :
            a[g] = 'o'
    for k in range(2) :
        for f in range(len(a) - 1) :
            print(a[f]*4, end = '')
        print(a[len(a) - 1]*4)
