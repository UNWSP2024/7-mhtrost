def main():
    number = int(input('Enter a number: '))
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if number > 10:
        print('Invalid input. Please enter a number 10 or less')
        return

    print('Number:', number)

    print('List of numbers:')
    print(f'{number_list}')

    print(f'List of numbers that are larger than {number}:')

    larger_numbers = display_larger_than_n_list(number, number_list)

    print(larger_numbers)

def display_larger_than_n_list(n, n_list):
    larger_list = []

    for value in n_list:
        if value > n:
            larger_list.append(value)
    return larger_list

if __name__ == '__main__':
    main()