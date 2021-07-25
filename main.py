"""
Starting point of the search app.
The major user interaction logic is handled here, think here as the reception when you walk into a place.
"""
import view.menu_enum as menu
from init.init import init_app, list_searchable_fields
from pprint import pprint
from search.search import start_search

USER_DATA_PATH = 'data/users.json'
TICKET_DATA_PATH = 'data/tickets.json'

if __name__ == '__main__':

    mini_database = init_app(USER_DATA_PATH, TICKET_DATA_PATH)
    input_start = input(menu.WELCOME).lower()

    if input_start.lower() == 'quit':
        exit()
    input_action = input(menu.SELECT_OPTIONS).lower()

    while input_action != 'quit':
        if input_action == '1':
            input_action = start_search(mini_database, input_action)

        elif input_action == '2':
            list_searchable_fields(mini_database['User']['user_searchable_fields'], 'User')
            list_searchable_fields(mini_database['Ticket']['ticket_searchable_fields'], 'Ticket')
            input_action = input('\nPress 1 to search, type quit to exit the program\n').lower()
        elif input_action == 'quit':
            exit()
        else:
            input_action = input('Invalid value, please type 1, 2, or Quit\n').lower()
