import pytest
from search import search


@pytest.fixture
def user_search_table():
    user_search_table = {1: {
        "_id": 1,
        "name": "Francisca Rasmussen",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": True
    },
        2: {
            "_id": 2,
            "name": "Cross Barlow",
            "created_at": "2016-06-23T10:31:39-10:00",
            "verified": True
        },
        3: {
            "_id": 3,
            "name": "Ingrid Wagner",
            "created_at": "2016-07-28T05:29:25-10:00",
            "verified": False
        }}
    return user_search_table


@pytest.fixture
def user_list_indexed():
    user_list_indexed = {True: [1, 2], False: [3]}
    return user_list_indexed


@pytest.fixture
def search_field_user_verified():
    search_field_user_verified = True
    return search_field_user_verified


def test_search_user_by_verified(user_search_table, user_list_indexed, search_field_user_verified):
    assert search.search_by_field(user_search_table, user_list_indexed, search_field_user_verified) == [{
        "_id": 1,
        "name": "Francisca Rasmussen",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": True
    },
        {
            "_id": 2,
            "name": "Cross Barlow",
            "created_at": "2016-06-23T10:31:39-10:00",
            "verified": True
        }]


@pytest.fixture
def ticket_search_table():
    ticket_search_table = {"436bf9b0-1147-4c0a-8439-6f79833bff5b":
        {
            "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
            "created_at": "2016-04-28T11:19:34-10:00",
            "type": "incident",
            "subject": "A Catastrophe in Korea (North)",
            "assignee_id": 24,
            "tags": [
                "Ohio",
                "Pennsylvania",
                "American Samoa",
                "Northern Mariana Islands"
            ]
        },
        "1a227508-9f39-427c-8f57-1b72f3fab87c":
            {
                "_id": "1a227508-9f39-427c-8f57-1b72f3fab87c",
                "created_at": "2016-04-14T08:32:31-10:00",
                "type": "incident",
                "subject": "A Catastrophe in Micronesia",
                "assignee_id": 38,
                "tags": [
                    "Puerto Rico",
                    "Idaho",
                    "Oklahoma",
                    "Louisiana"
                ]
            }}
    return ticket_search_table


@pytest.fixture
def ticket_list_indexed():
    ticket_list_indexed = {"incident": ["436bf9b0-1147-4c0a-8439-6f79833bff5b", "1a227508-9f39-427c-8f57-1b72f3fab87c"]}
    return ticket_list_indexed


@pytest.fixture
def search_field_ticket_type():
    search_field_ticket_type = "incident"
    return search_field_ticket_type


def test_search_ticket_by_type(ticket_search_table, ticket_list_indexed, search_field_ticket_type):
    assert search.search_by_field(ticket_search_table, ticket_list_indexed, search_field_ticket_type) == [
        {
            "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
            "created_at": "2016-04-28T11:19:34-10:00",
            "type": "incident",
            "subject": "A Catastrophe in Korea (North)",
            "assignee_id": 24,
            "tags": [
                "Ohio",
                "Pennsylvania",
                "American Samoa",
                "Northern Mariana Islands"
            ]
        },
        {
            "_id": "1a227508-9f39-427c-8f57-1b72f3fab87c",
            "created_at": "2016-04-14T08:32:31-10:00",
            "type": "incident",
            "subject": "A Catastrophe in Micronesia",
            "assignee_id": 38,
            "tags": [
                "Puerto Rico",
                "Idaho",
                "Oklahoma",
                "Louisiana"
            ]
        }]
