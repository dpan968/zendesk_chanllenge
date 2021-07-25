import pytest
from create_index import created_index


@pytest.fixture
def user_list():
    user_list = [{
        "_id": 1,
        "name": "Francisca Rasmussen",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": True
    }]
    return user_list


@pytest.fixture
def ticket_list_assigned_to_user_1():
    ticket_list_assigned_to_user_1 = [{
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
    },
        {
            "_id": "1a227508-9f39-427c-8f57-1b72f3fab87c",
            "created_at": "2016-04-14T08:32:31-10:00",
            "type": "incident",
            "subject": "A Catastrophe in Micronesia",
            "assignee_id": 1,
            "tags": [
                "Puerto Rico",
                "Idaho",
                "Oklahoma",
                "Louisiana"
            ]
        }]
    return ticket_list_assigned_to_user_1


@pytest.fixture
def ticket_list_not_assigned_to_user_1():
    ticket_list_not_assigned_to_user_1 = [{
        "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
        "created_at": "2016-04-28T11:19:34-10:00",
        "type": "incident",
        "subject": "A Catastrophe in Korea (North)",
        "assignee_id": 2,
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
            "assignee_id": 2,
            "tags": [
                "Puerto Rico",
                "Idaho",
                "Oklahoma",
                "Louisiana"
            ]
        }]
    return ticket_list_not_assigned_to_user_1


def test_user_has_tickets(user_list, ticket_list_assigned_to_user_1):
    assert created_index.add_ticket_subject_to_user_list(user_list, ticket_list_assigned_to_user_1) == [{
        "_id": 1,
        "name": "Francisca Rasmussen",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": True,
        "tickets": ["A Catastrophe in Korea (North)", "A Catastrophe in Micronesia"]
    }]


def test_user_has_no_tickets(user_list, ticket_list_not_assigned_to_user_1):
    assert created_index.add_ticket_subject_to_user_list(user_list, ticket_list_not_assigned_to_user_1) == [{
        "_id": 1,
        "name": "Francisca Rasmussen",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": True,
        "tickets": []
    }]
