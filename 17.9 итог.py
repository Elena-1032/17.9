def sort(chisla):
    for i in range(1, len(chisla)):  # сортировка вставками  решение 17.8.5
        x = chisla[i]
        idx = i
        while idx > 0 and chisla[idx - 1] > x:
            # count += 1
            chisla[idx] = chisla[idx - 1]
            idx -= 1
        chisla[idx] = x
    return chisla

def poisk(chisla, poisk_chislo, left, right): #двоичный поиск 17.7
    if left > right:  # если левая граница превысила правую,значит элемент отсутствует
        return False
    middle = (right + left) // 2  # находим середину
    if chisla[middle] == poisk_chislo:  # если элемент в середине, возвращаем этот индекс
        return middle
    elif poisk_chislo < chisla[middle]:  # если элемент меньше элемента в середине рекурсивно ищем в левой половине
        return poisk(chisla, poisk_chislo, left, middle - 1)
    else:  # иначе в правой
        return poisk(chisla, poisk_chislo, middle + 1, right)

chisla = input("Введите последовательность чисел через пробел: ").split()
chisla = list(map(int, chisla))
print(f"{chisla}, количество чисел {len(chisla)}")
new_chislo = int(input("Введите дополнительно число: "))
if new_chislo % 1 == 0:
    chisla.append(new_chislo)
print(f"Введены числа {chisla}, количество чисел {len(chisla)}")

chisla = list(set(chisla)) #Убираю дубли

chisla = sort(chisla) #сортировка через функцию
print(f'Сортировка вставками {chisla} ')

poisk_chislo = int(input("Введите число из ранее введенных чисел: "))
if poisk_chislo not in chisla:
     print(f'Число раннее не вводилось: {chisla}')
     poisk_chislo = int(input("Повторите введ числа из ранее введенных чисел: "))

ind_chislo = poisk(chisla, poisk_chislo, 0, len(chisla) - 1) #поиск числа через функцию, сохранение номера позиции
print(f"Вы ввели число {poisk_chislo}, позиция числа в списке: {ind_chislo}")

if ind_chislo == 0:
    print(f'предыдущее значение отсутствует, следующее значение {chisla[ind_chislo + 1]}')
elif ind_chislo == int(len(chisla)-1):
    print(f'предыдущее значение {chisla[ind_chislo-1]}, следующее значение отсутствует')
else:
    print(f'предыдущее значение {chisla[ind_chislo-1]}, следующее {chisla[ind_chislo + 1]}')
