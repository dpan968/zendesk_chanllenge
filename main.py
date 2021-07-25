# TODO: try to replace for loops with alternatives.

import json
from collections import defaultdict
import pprint
import copy
import view.menu_enum as menu
import distutils
import distutils.util
from init.init import init_app, list_searchable_fields
from search.search import start_search

USER_DATA_PATH = 'data/users.json'
TICKET_DATA_PATH = 'data/tickets.json'


# def load_input_file(file_path):
#     with open(file_path) as jsonFile:
#         jsonList = json.load(jsonFile)
#     jsonFile.close()
#     return jsonList
#
#
# def add_ticket_subject_to_user_list(user_list, ticket_list):
#
#     user_id_to_ticket_subject = defaultdict(list)
#     for ticket in ticket_list:
#         user_id_to_ticket_subject[ticket.get('assignee_id', 'missing')].append(ticket['subject'])
#
#     user_list_with_ticket_subject = copy.deepcopy(user_list)
#     for user in user_list_with_ticket_subject:
#         user['tickets'] = user_id_to_ticket_subject[user['_id']]
#
#     return user_list_with_ticket_subject
#
#
# def add_assignee_name_to_ticket_list(user_list_dict, ticket_list):
#     # TODO: refine the for-loop logic, the current mixture of logics is ugly!
#     # add in the assignee_name field into the dictionary version of ticket_search_table
#     ticket_list_with_assignee_name = copy.deepcopy(ticket_list)
#     for ticket in ticket_list_with_assignee_name:
#         if 'assignee_id' in ticket:
#             if ticket['assignee_id'] in user_list_dict:
#                 ticket['assignee_name'] = user_list_dict[ticket['assignee_id']]['name']
#             else:
#                 ticket['assignee_name'] = 'unknown'
#     return ticket_list_with_assignee_name
#
#
#
# def convert_list_to_dict(item_list, key):
#     return {item[key]:item for item in item_list}








# def create_inverted_index_by_field(item_list, field):
#
#     search_table_by_field = defaultdict(list)
#
#     if field == 'tags':
#         for item in item_list:
#             for tag in item.get('tags', []):
#                 search_table_by_field[tag].append(item['_id'])
#     else:
#         for item in item_list:
#             search_table_by_field[item.get(field, 'missing')].append(item['_id'])
#
#     return search_table_by_field
#
#
# def create_inverted_index_for_searchable_fields(item_list, searchable_fields):
#     index_table_for_searchable_fields = dict()
#
#     for field in searchable_fields:
#         index_table_for_searchable_fields[field] = create_inverted_index_by_field(item_list, field)
#     return index_table_for_searchable_fields


# def get_searchable_fields(item_list):
#
#     max_key_count = max([len(item.keys()) for item in item_list])
#     for item in item_list:
#         if len(item.keys()) == max_key_count:
#             searchable_fields = list(item.keys())
#             break
#     return searchable_fields
#
# def list_searchable_fields(searchable_fields, entity_name):
#     print("-------------------------------")
#     print(f"Search {entity_name} with")
#     print(*searchable_fields, sep="\n")





# def init_app(USER_DATA_PATH, TICKET_DATA_PATH):
#
#     mini_database = dict()
#
#     user_list = load_input_file(USER_DATA_PATH)
#     ticket_list = load_input_file(TICKET_DATA_PATH)
#
#     user_searchable_fields = get_searchable_fields(user_list)
#     ticket_searchable_fields = get_searchable_fields(ticket_list)
#
#     user_list_with_ticket_subject = add_ticket_subject_to_user_list(user_list, ticket_list)
#     user_dict_id_as_key = convert_list_to_dict(user_list_with_ticket_subject, '_id')
#
#     ticket_list_with_assignee_name = add_assignee_name_to_ticket_list(user_dict_id_as_key, ticket_list)
#     ticket_dict_id_as_key = convert_list_to_dict(ticket_list_with_assignee_name, '_id')
#
#     # create search table for each entity in a format of dictionary using search_field as the key
#     indexed_user_table = create_inverted_index_for_searchable_fields(user_list, user_searchable_fields)
#     indexed_ticket_table = create_inverted_index_for_searchable_fields(ticket_list, ticket_searchable_fields)
#
#
#
#     mini_database['User'] = {'user_list':user_list, 'user_searchable_fields': user_searchable_fields,
#                            'user_list_with_ticket_subject': user_list_with_ticket_subject,
#                            'user_dict_id_as_key': user_dict_id_as_key,
#                            'indexed_user_table':indexed_user_table}
#
#     mini_database['Ticket'] = {'ticket_list':ticket_list, 'ticket_searchable_fields': ticket_searchable_fields,
#                              'ticket_list_with_assignee_name': ticket_list_with_assignee_name,
#                              'ticket_dict_id_as_key': ticket_dict_id_as_key,
#                              'indexed_ticket_table': indexed_ticket_table}
#
#     return mini_database
# def search_by_id(item_list, item_id):
#     if item_id in item_list:
#         return item_list[item_id]
#     else:
#         print("No such id exists, please double check or try another id.")
#
#
# def search_by_field(item_search_table, item_list_indexed, search_value):
#     id_list = item_list_indexed[search_value]
#     return [item_search_table[id] for id in id_list]
#
#
# def start_search(mini_database, input_2):
#     search_entity = input("Select 1) Users or 2) Tickets\n")
#     search_term = input("Enter search term\n")
#     search_value = input('Enter search value\n')
#     print(f'Searching {search_entity} for {search_term} with a value of {search_value}\n')
#     if search_entity == '1' and search_term in mini_database['User']['user_searchable_fields']:
#         if search_term == '_id':
#             pprint.pprint(search_by_id(mini_database['User']['user_dict_id_as_key'], int(search_value)))
#         elif search_term == 'verified':
#             search_value = bool(distutils.util.strtobool(search_value))
#             pprint.pprint(search_by_field(mini_database['User']['user_dict_id_as_key'],
#                                           mini_database['User']['indexed_user_table'][search_term],
#                                           search_value))
#         else:
#             pprint.pprint(search_by_field(mini_database['User']['user_dict_id_as_key'],
#                                           mini_database['User']['indexed_user_table'][search_term], search_value))
#
#     elif search_entity == '2' and search_term in mini_database['Ticket']['ticket_searchable_fields']:
#         pprint.pprint(search_by_field(mini_database['Ticket']['ticket_dict_id_as_key'],
#                                       mini_database['Ticket']['indexed_ticket_table'][search_term], search_value))
#     else:
#         input_2 = input('Wrong input, please double check.\n')
#     return input_2


if __name__ == '__main__':

    mini_database = init_app(USER_DATA_PATH, TICKET_DATA_PATH)

    input_1 = input(menu.WELCOME).lower()
    if input_1.lower() == 'quit':
        exit()
    input_2 = input(menu.SELECT_OPTIONS).lower()
    while input_2 != 'quit':

        if input_2 == '1':
            input_2 = start_search(mini_database, input_2)
            # search_entity = input("Select 1) Users or 2) Tickets\n")
            # search_term = input("Enter search term\n")
            # search_value = input('Enter search value\n')
            # print(f'Searching {search_entity} for {search_term} with a value of {search_value}\n')
            # if search_entity == '1' and search_term in mini_database['User']['user_searchable_fields']:
            #     if search_term == '_id':
            #         pprint.pprint(search_by_id(mini_database['User']['user_dict_id_as_key'], int(search_value)))
            #     elif search_term == 'verified':
            #         search_value = bool(distutils.util.strtobool(search_value))
            #         pprint.pprint(search_by_field(mini_database['User']['user_dict_id_as_key'],
            #                                       mini_database['User']['indexed_user_table'][search_term],
            #                                       search_value))
            #     else:
            #         pprint.pprint(search_by_field(mini_database['User']['user_dict_id_as_key'], mini_database['User']['indexed_user_table'][search_term], search_value))
            #
            # elif search_entity == '2' and search_term in mini_database['Ticket']['ticket_searchable_fields']:
            #     pprint.pprint(search_by_field(mini_database['Ticket']['ticket_dict_id_as_key'], mini_database['Ticket']['indexed_ticket_table'][search_term], search_value))
            # else:
            #     input('Wrong input, please double check.\n')

        elif input_2 == '2':
            list_searchable_fields(mini_database['User']['user_searchable_fields'], 'User')
            list_searchable_fields(mini_database['Ticket']['ticket_searchable_fields'], 'Ticket')
            input_2 = input('\nPress 1 to search, type quit to exit the program\n')
        else:
            input_2 = input('Invalid value, please double check\n')

















