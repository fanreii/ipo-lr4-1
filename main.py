a = int(input("Введите число: ")) # ввод числа с клавиатуры
spisok = [x for x in range(a) if x % 2 ==0] # цикл for с условием
print (spisok) # вывод списка