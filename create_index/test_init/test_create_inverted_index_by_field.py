import pytest
from create_index import created_index


@pytest.fixture
def user_list():
    user_list = [{
        "_id": 1,
        "name": "Francisca Rasmussen",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": True
    }, {
        "_id": 2,
        "name": "Cross Barlow",
        "created_at": "2016-06-23T10:31:39-10:00",
        "verified": True
    }]
    return user_list


@pytest.fixture
def ticket_list():
    ticket_list = [{
        "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
        "created_at": "2016-04-28T11:19:34-10:00",
        "type": "incident",
        "subject": "A Catastrophe in Korea (North)",
        "assignee_id": 2,
        "tags": [
            "Ohio"
        ]
    },
        {
            "_id": "1a227508-9f39-427c-8f57-1b72f3fab87c",
            "created_at": "2016-04-14T08:32:31-10:00",
            "type": "problem",
            "subject": "A Catastrophe in Micronesia",
            "assignee_id": 2,
            "tags": [
                "Ohio",
                "Oklahoma"
            ]
        }, {
            "_id": "4cce7415-ef12-42b6-b7b5-fb00e24f9cc1",
            "created_at": "2016-02-25T09:12:47-11:00",
            "type": "problem",
            "subject": "A Nuisance in Ghana",
            "assignee_id": 2,
            "tags": [
                "Ohio",
                "Oklahoma"
            ]
        }]
    return ticket_list


@pytest.fixture
def searchable_field_for_user():
    searchable_field_for_user = "verified"
    return searchable_field_for_user


@pytest.fixture
def searchable_field_for_ticket():
    searchable_field_for_ticket = "type"
    return searchable_field_for_ticket


@pytest.fixture
def searchable_field_for_ticket():
    searchable_field_for_ticket = "type"
    return searchable_field_for_ticket


def test_created_inverted_index_by_field_user(user_list, searchable_field_for_user):
    assert created_index.create_inverted_index_by_field(user_list, searchable_field_for_user) == {True: [1, 2]}


@pytest.mark.parametrize(
    "field, expected",
    [("type", {
        "incident": ["436bf9b0-1147-4c0a-8439-6f79833bff5b"],
        "problem": ["1a227508-9f39-427c-8f57-1b72f3fab87c", "4cce7415-ef12-42b6-b7b5-fb00e24f9cc1"]}),
     ("tags", {"Ohio": ["436bf9b0-1147-4c0a-8439-6f79833bff5b", "1a227508-9f39-427c-8f57-1b72f3fab87c",
                        "4cce7415-ef12-42b6-b7b5-fb00e24f9cc1"],
               "Oklahoma": ["1a227508-9f39-427c-8f57-1b72f3fab87c", "4cce7415-ef12-42b6-b7b5-fb00e24f9cc1"]})]
)
def test_created_inverted_index_by_field_ticket(ticket_list, field, expected):
    assert created_index.create_inverted_index_by_field(ticket_list, field) == expected
