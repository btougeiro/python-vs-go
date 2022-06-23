import time
import random

numbers_to_sort = 1000


def main():
    start = time.time()

    list_of_random_numbers = []
    for _ in range(numbers_to_sort):
        list_of_random_numbers.append(random.randint(0, 100))

    list_of_random_numbers.sort()

    end = time.time()
    duration = (end - start) * 1000

    print(f"{duration}ms")


if __name__ == '__main__':
    main()
