from hero import Hero
from item import Item
import view


def main_menu():
    hero = get_hero()
    user_choice = ''
    while user_choice != 0:
        view.print_main_menu()
        user_choice = view.get_input()

        # pick an item
        if user_choice == 1:
            name, description, weight = view.get_data_to_new_item()
            hero.pick_an_item(Item(name, description, weight))

        # drop item
        elif user_choice == 2:
            pass

        # show inventory
        elif user_choice == 3:
            print(hero.character)
            view.get_list(hero.get_items())

        # show the heaviest item
        elif user_choice == 4:
            hero.inventory.get_the_heaviest_item()

    view.print_exit_message()


def get_hero():
    first_name, last_name, race = view.get_data_to_hero()
    hero = Hero(first_name, last_name, race)

    return hero

