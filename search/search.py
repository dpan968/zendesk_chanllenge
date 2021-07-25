from pprint import pprint
import distutils
import distutils.util
import view.menu_enum as menu


def search_by_field(item_search_table, item_list_indexed, search_value):
    id_list = item_list_indexed[search_value]
    return [item_search_table[_id] for _id in id_list]


def start_search(mini_database, input_action):
    search_entity_mapping = {'1': 'Users', '2': 'Tickets'}
    search_entity = input(menu.CHOOSE_SEARCH_ENTITY).lower()
    search_term = input(menu.CHOOSE_SEARCH_TERM).lower()
    search_value = input(menu.TYPE_SEARCH_VALUE)
    print(f'Searching {search_entity_mapping[search_entity]} for {search_term} with a value of {search_value}\n')

    if search_entity == '1' and search_term in mini_database['User']['user_searchable_fields']:
        if search_term == '_id':
            try:
                search_value = int(search_value)
            except ValueError:
                print('Please enter an integer\n')
        elif search_term == 'verified' and search_value != 'missing':
            search_value = bool(distutils.util.strtobool(search_value))

        matched_records = search_by_field(mini_database['User']['user_dict_id_as_key'],
                                          mini_database['User']['indexed_user_table'][search_term], search_value)
        count_of_matched_records = len(matched_records)
        pprint(matched_records)
        print(f'Total returned records: {count_of_matched_records}\n')

    elif search_entity == '2' and search_term in mini_database['Ticket']['ticket_searchable_fields']:
        if search_term == 'assignee_id':
            try:
                search_value = int(search_value)
            except ValueError:
                print('Please enter an integer\n')
        matched_records = search_by_field(mini_database['Ticket']['ticket_dict_id_as_key'],
                                          mini_database['Ticket']['indexed_ticket_table'][search_term], search_value)
        count_of_matched_records = len(matched_records)
        pprint(matched_records)
        print(f'Total returned records: {count_of_matched_records}\n')
    elif search_term == 'quit' or search_value == 'quit':
        exit()
    else:
        input_action = input('Wrong input, please double check.\n')
    return input_action
