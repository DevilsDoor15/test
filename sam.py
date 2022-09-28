//program for nested list?
new_lst = []

for col in range(0, len(lst[0]), 3):
    inner = []
    for row in range(3):
        inner += lst[row][col:col+3]
    new_lst.append(inner)


new_lst = []

for col in range(0, len(lst[0]), 3):
    inner = []
    for row in lst:
        inner += row[col:col+3]
    new_lst.append(inner)


a = starting_list
for i in range(3):
    si = slice(i*3, i*3+3)
    for j in range(i):
        sj = slice(j*3, j*3+3)
        a[i][sj], a[j][si] = a[j][si], a[i][sj]


