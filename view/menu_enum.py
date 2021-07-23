from enum import Enum
class Top_Level_Menu(Enum):
    WELCOME = "Welcome to Zendesk Search \n Type 'quit' to exit at any time, Press 'Enter' to continue"
    SELECT_OPTIONS = "Select search option: \n * Press 1 to search Zendesk \n Press 2 to view a list of searchable fields\n " \
                     "* Type 'quit' to exit"