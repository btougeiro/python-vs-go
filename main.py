import time
import random

numbers_to_sort = 100000

def bubble_sort(list_of_numbers_to_sort):
    swapped = True
    while swapped:
        swapped = False

        for i in range(1, numbers_to_sort):
            if list_of_numbers_to_sort[i - 1] > list_of_numbers_to_sort[i]:
                list_of_numbers_to_sort[i], list_of_numbers_to_sort[i - 1] = list_of_numbers_to_sort[i - 1], list_of_numbers_to_sort[i]
                swapped = True

def main():
    start = time.time()

    list_of_random_numbers = []

    for _ in range(numbers_to_sort):
        list_of_random_numbers.append(random.randint(0, 100))

    bubble_sort(list_of_random_numbers)

    end = time.time()
    duration = (end - start) * 1000

    print(f"{duration}ms")

if __name__ == '__main__':
    main()
