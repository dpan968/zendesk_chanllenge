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
        "created_at": "2016-06-23T10:31:39-10:00"
        #     missing verified
    }]
    return user_list


@pytest.fixture
def ticket_list():
    ticket_list = [{
        "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
        "created_at": "2016-04-28T11:19:34-10:00",
        # missing type
        "subject": "A Catastrophe in Korea (North)",
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
            "tags": [
                "Puerto Rico",
                "Idaho",
                "Oklahoma",
                "Louisiana"
            ]
        }]
    return ticket_list


def test_get_searchable_fields_for_user(user_list):
    assert created_index.get_searchable_fields(user_list) == ["_id", "name", "created_at", "verified"]


def test_get_searchable_fields_for_ticket(ticket_list):
    assert created_index.get_searchable_fields(ticket_list) == ["_id", "created_at", "type", "subject", "tags"]
