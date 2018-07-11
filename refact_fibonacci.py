def get_fibonacci(first_number, second_number, quantity):
    print("0")
    for i in range(quantity-1):
        fibonacci_number = first_number + second_number
        first_number = second_number
        second_number = fibonacci_number
        print(fibonacci_number)


def main():
    number = 30
    print("The first %d numbers of the Fibonacci sequences are these: " % number)
    fibonacci_number = get_fibonacci(1, 0, number)
    print("Finished!")


if __name__ == '__main__':
    main()
