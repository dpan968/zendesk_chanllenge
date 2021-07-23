# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
from collections import defaultdict
import pprint
import copy
import view.menu_enum as menu

user_path = 'data/users.json'
ticket_path = 'data/tickets.json'


# init()
def load_input_file(file_path):
    with open(file_path) as jsonFile:
        jsonList = json.load(jsonFile)
    jsonFile.close()
    return jsonList

# init()
def add_in_ticket_field_to_user_list(user_list, ticket_list):
    user_id_to_ticket_subject = defaultdict(list)

    for ticket in ticket_list:
        try:
            user_id_to_ticket_subject[ticket['assignee_id']].append(ticket['subject'])
        except KeyError:
            user_id_to_ticket_subject['missing_assignee_id'].append((ticket['subject']))
        except Exception as e:
            print(e)
            raise
        # What does raise do????? https://stackoverflow.com/questions/13957829/how-to-use-raise-keyword-in-python\
    user_list_with_ticket_subject = copy.deepcopy(user_list)
    for user in user_list_with_ticket_subject:
        user['tickets'] = user_id_to_ticket_subject[user['_id']]

    return user_list_with_ticket_subject

def add_assignee_name_to_ticket_list(user_list_dict, ticket_list):
    # add in the assignee_name field into the dictionary version of ticket_search_table
    ticket_list_with_assignee_name = copy.deepcopy(ticket_list)
    for ticket in ticket_list_with_assignee_name:
        if 'assignee_id' in ticket:
            if ticket['assignee_id'] in user_list_dict:
                ticket['assignee_name'] = user_list_dict[ticket['assignee_id']]['name']
            else:
                ticket['assignee_name'] = 'unknown'
    return ticket_list_with_assignee_name



def convert_list_to_dict(item_list, key):
    return {item[key]:item for item in item_list}



def init_game():
    pass


def search_by_id(item_list, item_id):
    if item_id in item_list:
        return item_list[item_id]
    else:
        print("No such id exists, please double check or try another id.")


def search_by_field(item_search_table, item_list_indexed, search_term, search_value):
    id_list = item_list_indexed[search_value]
    return [item_search_table[id] for id in id_list]



def create_index_by_field(item_list, field):

    search_table_by_field = defaultdict(list)

    if field == 'tags':
        for item in item_list:
            try:
                for tag in item['tags']:
                    search_table_by_field[tag].append(item['_id'])
            except KeyError:
                search_table_by_field['missing_field'].append((item['_id']))
            except Exception as e:
                print(e)
                raise
    else:
        for item in item_list:
            try:
                search_table_by_field[item[field]].append(item['_id'])
            except KeyError:
                search_table_by_field['missing_field'].append((item['_id']))
            except Exception as e:
                print(e)
                raise
    return search_table_by_field




def pretty_print_user(user_ids, user_search_table):
    for user_id in user_ids:
        pprint.pprint(user_search_table[user_id])

def pretty_print_ticket(ticket_ids, ticket_search_table):
    for ticket_id in ticket_ids:
        pprint.pprint(ticket_search_table[ticket_id])

def ask_user_input():
    print("Welcome to Zendesk Search.\n")
    user_input = input("Type 'quit' to exit at any time, Press 'Enter' to continue.\n")
    if user_input == 'quit':
        exit()
    else:
        print('Select search options: \n')
        print("* Press 1 to search Zendesk")
        print("* Press 2 to view a list of searchable fields")
        print("* Type 'quit' to exit")



def get_searchable_fields(item_list):

    max_key_count = max([len(item.keys()) for item in item_list])

    for item in item_list:
        if len(item.keys()) == max_key_count:
            searchable_fields =  list(item.keys())
            break
    return searchable_fields

def list_searchable_fields(searchable_fields, entity_name):
    print("-------------------------------")
    print(f"Search {entity_name} with")
    print(*searchable_fields, sep="\n")

def init():
    user_list = load_input_file(user_path)
    ticket_list = load_input_file(ticket_path)


    user_list_with_ticket_subject = add_in_ticket_field_to_user_list(user_list, ticket_list)
    user_search_table = convert_list_to_dict(user_list_with_ticket_subject, '_id')
    user_search_table_indexed_by_name = create_index_by_field(user_list_with_ticket_subject, 'name')
    user_search_table_indexed_by_created_at = create_index_by_field(user_list, 'created_at')
    user_search_table_indexed_by_verified = create_index_by_field(user_list, 'verified')

    ticket_list_with_assignee_name = add_assignee_name_to_ticket_list(user_search_table, ticket_list)
    ticket_search_table = convert_list_to_dict(ticket_list_with_assignee_name, '_id')
    ticket_search_table_indexed_by_created_at = create_index_by_field(ticket_list, 'created_at')
    ticket_search_table_indexed_by_type = create_index_by_field(ticket_list, 'type')
    ticket_search_table_indexed_by_subject = create_index_by_field(ticket_list, 'subject')
    ticket_search_table_indexed_by_assignee_id = create_index_by_field(ticket_list, 'assignee_id')
    ticket_search_table_indexed_by_tag = create_index_by_field(ticket_list, 'tags')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init()

    print(menu.WELCOME)
    print(menu.SELECT_OPTIONS)

    # USER_SEARCHABLE_FIELD = get_searchable_fields(user_list)
    # TICKET_SEARCHABLE_FIELD = get_searchable_fields(ticket_list)
    #
    # input_1 = input(WELCOME)
    # if input_1.lower() == 'quit':
    #     exit()
    # input_2 = input(SELECT_OPTIONS).lower()
    # while input_2 != 'quit':
    #
    #     if input_2 == '1':
    #
    #         search_entity = input("Select 1) Users or 2) Tickets\n")
    #         if search_entity == "1":
    #             entity = "user"
    #         elif search_entity == "2":
    #             entity = "ticket"
    #         search_term = input("Enter search term\n")
    #         # TODO: need to validate the search_term
    #         search_value = input('Enter search value\n')
    #         # TODO: need to validate the search_value
    #
    #         print(f'Searching {entity} for {search_term} with a value of {search_value}\n')
    #         # if entity == 'user' and search_term in USER_SEARCHABLE_FIELD:
    #         #
    #         #     if search_term == '_id':
    #         #         print(search_by_id(user_search_table, int(search_value)))
    #         #     else:
    #         #         pprint.pprint(search_by_field(user_search_table, user_search_table_indexed_by_name, search_term, search_value))
    #         # elif entity == 'ticket' and search_term in TICKET_SEARCHABLE_FIELD:
    #         #     pass
    #         # else:
    #         #     input('Wrong searchable field, please double check.\n')
    #
    #
    #
    #     elif input_2 == '2':
    #         list_searchable_fields(USER_SEARCHABLE_FIELD, 'User')
    #         list_searchable_fields(TICKET_SEARCHABLE_FIELD, 'Ticket')
    #         input_2 = input('\nPress 1 to search, type quit to exit the program\n')
    #     else:
    #         input_2 = input('Invalid value, please double check')
    #
    #
    #
    #















