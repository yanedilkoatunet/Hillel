"""Functions selected from previous homeworks."""
def sum_numbers(first_number, second_number):
    return first_number + second_number

def average_numbers(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")

    return sum(numbers) / len(numbers)

def reverse_string(text):
    return text[::-1]

def find_substring(text, substring):
    return text.find(substring)

def all_sum(string):
    try:
        total = 0

        for number in string.split(","):
            total += int(number)

        return total

    except ValueError:
        return "Не можу це зробити!"
