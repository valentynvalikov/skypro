import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)

for i in range(int(len(lst_in))):
    lst_in[i].append(0)
    lst_in[i].insert(0, 0)
lst_in.insert(0, [0] * (len(lst_in) + 2))
lst_in.insert(-1, [0] * (len(lst_in) + 1))

res = 'wtf'
i = 1
j = 1
for i in range(1, 6):
    for j in range(1, 6):
        if ((lst_in[i][j] + lst_in[i][j - 1] + lst_in[i][j + 1] +
                lst_in[i-1][j-1] + lst_in[i-1][j] + lst_in[i-1][j+1]
                + lst_in[i+1][j-1] + lst_in[i+1][j] + lst_in[i+1][j+1]) > 1):
            print(i)
            print(j)
            res = 'НЕТ'
        else:
            res = 'ДА'
            break
print(res)