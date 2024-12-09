def faint_number(k):
    num = ''
    if k < 3 or k > 20:
        return 'Введено некорректное число!'
    else:
        for i in range(1 , k +1 ):
            for j in range(i + 1, k+1):
                if k % (i + j) == 0:
                    num += str(i) + str(j)
        return num

a = faint_number(7)

print(a)






