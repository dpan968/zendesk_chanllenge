import pprint
import distutils
import distutils.util

def search_by_id(item_list, item_id):
    if item_id in item_list:
        return item_list[item_id]
    else:
        print("No such id exists, please double check or try another id.")


def search_by_field(item_search_table, item_list_indexed, search_value):
    id_list = item_list_indexed[search_value]
    return [item_search_table[id] for id in id_list]


def start_search(mini_database, input_2):
    search_entity = input("Select 1) Users or 2) Tickets\n")
    search_term = input("Enter search term\n")
    search_value = input('Enter search value\n')
    print(f'Searching {search_entity} for {search_term} with a value of {search_value}\n')
    if search_entity == '1' and search_term in mini_database['User']['user_searchable_fields']:
        if search_term == '_id':
            pprint.pprint(search_by_id(mini_database['User']['user_dict_id_as_key'], int(search_value)))
        elif search_term == 'verified':
            search_value = bool(distutils.util.strtobool(search_value))
            pprint.pprint(search_by_field(mini_database['User']['user_dict_id_as_key'],
                                          mini_database['User']['indexed_user_table'][search_term],
                                          search_value))
        else:
            pprint.pprint(search_by_field(mini_database['User']['user_dict_id_as_key'],
                                          mini_database['User']['indexed_user_table'][search_term], search_value))

    elif search_entity == '2' and search_term in mini_database['Ticket']['ticket_searchable_fields']:
        pprint.pprint(search_by_field(mini_database['Ticket']['ticket_dict_id_as_key'],
                                      mini_database['Ticket']['indexed_ticket_table'][search_term], search_value))
    else:
        input_2 = input('Wrong input, please double check.\n')
    return input_2