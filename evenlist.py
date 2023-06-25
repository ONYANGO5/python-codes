def filter_even_numbers(numbers):
  """
  Takes a list of integers as input and returns a new list with only the even numbers.

  Args:
    numbers: The list of integers.

  Returns:
    A new list with only the even numbers.
  """

  even_numbers = []
  for number in numbers:
    if number % 2 == 0:
      even_numbers.append(number)

  return even_numbers


def main():
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  even_numbers = filter_even_numbers(numbers)
  print(even_numbers)


if __name__ == "__main__":
  main()
