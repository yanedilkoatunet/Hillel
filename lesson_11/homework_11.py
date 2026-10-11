my_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def all_sum(string):
    total = 0
    try:
        for i in string.split(","):
            total += int(i)
        return total
    except ValueError:
        return "Не можу це зробити!"

for i in my_list:
    print(all_sum(i))