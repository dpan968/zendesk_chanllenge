import pytest
from create_index import created_index


@pytest.fixture
def ticket_list():
    ticket_list = [{
        "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
        "created_at": "2016-04-28T11:19:34-10:00",
        "type": "incident",
        "subject": "A Catastrophe in Korea (North)",
        "assignee_id": 1,
        "tags": [
            "Ohio",
            "Pennsylvania",
            "American Samoa",
            "Northern Mariana Islands"
        ]
    }]
    return ticket_list


@pytest.fixture
def user_list_dict():
    user_list_dict = {1: {
        "_id": 1,
        "name": "Francisca Rasmussen",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": True
    }}
    return user_list_dict


@pytest.fixture
def user_list_dict_missing_user():
    user_list_dict_missing_user = {2: {
        "_id": 2,
        "name": "Francisca Rasmussen",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": True
    }}
    return user_list_dict_missing_user


def test_user_name_found(user_list_dict, ticket_list):
    assert created_index.add_assignee_name_to_ticket_list(user_list_dict, ticket_list) == [{
        "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
        "created_at": "2016-04-28T11:19:34-10:00",
        "type": "incident",
        "subject": "A Catastrophe in Korea (North)",
        "assignee_id": 1,
        "tags": [
            "Ohio",
            "Pennsylvania",
            "American Samoa",
            "Northern Mariana Islands"
        ],
        "assignee_name": "Francisca Rasmussen"
    }]


def test_user_name_not_found(user_list_dict_missing_user, ticket_list):
    assert created_index.add_assignee_name_to_ticket_list(user_list_dict_missing_user, ticket_list) == [{
        "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
        "created_at": "2016-04-28T11:19:34-10:00",
        "type": "incident",
        "subject": "A Catastrophe in Korea (North)",
        "assignee_id": 1,
        "tags": [
            "Ohio",
            "Pennsylvania",
            "American Samoa",
            "Northern Mariana Islands"
        ],
        "assignee_name": "unknown"
    }]
