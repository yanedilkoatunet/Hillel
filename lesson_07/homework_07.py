# task 1
def multiplication_table(number):
    multiplier = 1
    while number * multiplier <= 25:
        result = number * multiplier
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

multiplication_table(3)

# task 2
def sum_numbers(number1, number2):
    return number1 + number2

print(sum_numbers(5, 10))

# task 3
def average_numbers(numbers):
    return sum(numbers) / len(numbers)

print(average_numbers([2, 4, 6, 8]))

# task 4
def reverse_string(text):
    return text[::-1]

print(reverse_string("Hello"))

# task 5
def longest_word(words):
    return max(words, key=len)

print(longest_word(["cat", "elephant", "dog", "monkey"]))


# task 6
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

# task 7
def get_even_numbers(numbers):
    """Повертає список парних чисел."""
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers

print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]))

# task 8
def sum_even_numbers(numbers):
    """Повертає суму парних чисел."""
    result = 0

    for number in numbers:
        if number % 2 == 0:
            result += number

    return result

print(sum_even_numbers([1, 2, 3, 4, 5, 6]))

# task 9
def remove_duplicates(numbers):
    """Повертає список без повторюваних значень."""
    unique_numbers = list(set(numbers))

    return unique_numbers

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

# task 10
def count_letter(text, letter):
    """Повертає кількість входжень заданої літери в текст."""
    count = 0

    for symbol in text:
        if symbol == letter:
            count += 1

    return count

print(count_letter("Hello everyone", "e"))