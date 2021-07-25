"""
The init module has several major tasks:
    1. load files
    2. add in additional field(s) based on the desired output to users, such as add ticket subject field to user_list
    3. get searchable fields for each entity (user and ticket)
    4. most importantly, for each searchable field, create a set of corresponding inverted index table
    5. produce a collection (a dictionary) that contains key components to achieve high query performance

"""
import json
from collections import defaultdict
import copy


def load_input_file(file_path):
    with open(file_path) as jsonFile:
        jsonList = json.load(jsonFile)
    jsonFile.close()
    return jsonList


def add_ticket_subject_to_user_list(user_list, ticket_list):
    # add in the ticket_subject field into a deep copy of user_list
    user_id_to_ticket_subject = defaultdict(list)
    user_list_with_ticket_subject = copy.deepcopy(user_list)

    for ticket in ticket_list:
        user_id_to_ticket_subject[ticket.get('assignee_id', 'missing')].append(ticket['subject'])

    for user in user_list_with_ticket_subject:
        user['tickets'] = user_id_to_ticket_subject[user['_id']]

    return user_list_with_ticket_subject


def add_assignee_name_to_ticket_list(user_list_dict, ticket_list):
    # add in the assignee_name field into a deep copy of ticket_list
    ticket_list_with_assignee_name = copy.deepcopy(ticket_list)
    for ticket in ticket_list_with_assignee_name:
        if 'assignee_id' in ticket:
            if ticket['assignee_id'] in user_list_dict:
                ticket['assignee_name'] = user_list_dict[ticket['assignee_id']]['name']
            else:
                ticket['assignee_name'] = 'unknown'
    return ticket_list_with_assignee_name


def get_searchable_fields(item_list):
    # the function is required as some fields could be missing for a record in the search_entity,
    # eg. a ticket can have no assignee_id
    max_key_count = max([len(item.keys()) for item in item_list])
    for item in item_list:
        if len(item.keys()) == max_key_count:
            searchable_fields = list(item.keys())
            break
    return searchable_fields


def list_searchable_fields(searchable_fields, entity_name):
    print('-------------------------------')
    print(f'Search {entity_name} with')
    print(*searchable_fields, sep='\n')


def create_inverted_index_by_field(item_list, field):
    search_table_by_field = defaultdict(list)
    # ticket['tags'] return a list of tags
    if field == 'tags':
        for item in item_list:
            for tag in item.get('tags', []):
                search_table_by_field[tag].append(item['_id'])
    else:
        for item in item_list:
            # item.get() is used to avoid KeyError,
            # if item[field] does not exist, it returns the value 'missing'
            search_table_by_field[item.get(field, 'missing')].append(item['_id'])

    return search_table_by_field


def create_inverted_index_for_searchable_fields(item_list, searchable_fields):
    # create search table for each entity in a format of dictionary using search_field as the key
    index_table_for_searchable_fields = dict()

    for field in searchable_fields:
        index_table_for_searchable_fields[field] = create_inverted_index_by_field(item_list, field)
    return index_table_for_searchable_fields


def convert_list_to_dict(item_list, key):
    return {item[key]: item for item in item_list}


def init_app(user_data_path, ticket_data_path):
    mini_database = dict()

    user_list = load_input_file(user_data_path)
    ticket_list = load_input_file(ticket_data_path)

    user_searchable_fields = get_searchable_fields(user_list)
    ticket_searchable_fields = get_searchable_fields(ticket_list)

    user_list_with_ticket_subject = add_ticket_subject_to_user_list(user_list, ticket_list)
    user_dict_id_as_key = convert_list_to_dict(user_list_with_ticket_subject, '_id')

    ticket_list_with_assignee_name = add_assignee_name_to_ticket_list(user_dict_id_as_key, ticket_list)
    ticket_dict_id_as_key = convert_list_to_dict(ticket_list_with_assignee_name, '_id')

    indexed_user_table = create_inverted_index_for_searchable_fields(user_list, user_searchable_fields)
    indexed_ticket_table = create_inverted_index_for_searchable_fields(ticket_list, ticket_searchable_fields)
    # mini_database is a nested dictionary that provide all key information for searching purpose
    mini_database['User'] = {'user_list': user_list, 'user_searchable_fields': user_searchable_fields,
                             'user_list_with_ticket_subject': user_list_with_ticket_subject,
                             'user_dict_id_as_key': user_dict_id_as_key,
                             'indexed_user_table': indexed_user_table}

    mini_database['Ticket'] = {'ticket_list': ticket_list, 'ticket_searchable_fields': ticket_searchable_fields,
                               'ticket_list_with_assignee_name': ticket_list_with_assignee_name,
                               'ticket_dict_id_as_key': ticket_dict_id_as_key,
                               'indexed_ticket_table': indexed_ticket_table}

    return mini_database
