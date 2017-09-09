def print_main_menu():
    options = ['Pick an item', 'drop item', 'Show inventory', 'Show the heaviest item']
    get_list(options)
    print_exit_option()


def get_list(options):
    print('')
    number = 1
    for option in options:
        print('{}. {}'.format(number, option))
        number += 1
    print('')


def print_exit_option():
    print('0. Exit\n')


def get_input():
    number = input('\nWrite number: ')
    if number.isdigit():
        return int(number)

    return None


def print_exit_message():
    print('\nGood bye:) ')


def get_data_to_hero():
    print('Create your Hero')
    first_name = input('First name: ')
    last_name = input('Last name: ')
    race = input('race: ')

    return first_name, last_name, race


def get_data_to_new_item():
    name = input('Name: ')
    description = input('Description: ')
    weight = int(input('Weight: '))

    return name, description, weight
