#Task 1
string = input("Введіть строку: ")
unique_symbols = ""
for i in string:
    if i not in unique_symbols:
        unique_symbols += i
if len(unique_symbols) >= 10:
    print(True)
else:
    print(False)

#Task 2
while True:
    word = input("Type a word with h: ")
    if word.__contains__("h") or word.__contains__("H"):
        break

#Task 3
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 =[]
for i in lst1:
    if isinstance(i, str):
        lst2.append(i)
print(lst2)

#Task 4
lst_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for i in lst_num:
    if i % 2 ==0:
        total += i
print(total)