# tests/domain/people/test_people_all.py

import uuid
from graph_sdk.domain.person.person import Person
from app_collaborators.domain.app_provider.app_provider import AppProvider
from app_collaborators.domain.app_provider.app_provider_dtos import AppProviderCreateDto
from app_collaborators.host.session_bridge import register_session

def test_person_fetch(db_session):
    register_session(lambda: db_session)
    create_app_provider()

    all = Person.all()

    before_count = len(all)

    created_person = Person.create({"given_name": "Merry","family_name": "Whether"})

    all = Person.all()

    assert isinstance(all, list)
    assert len(all) == (before_count + 1)

    found_person = Person.fetch(created_person.id)

    assert created_person.id == found_person.id

    created_person.delete()

    all = Person.all()

    assert (len(all)) == before_count

def create_app_provider():
    AppProvider.create(app_provider_create_dto())

def app_provider_create_dto():
    return AppProviderCreateDto(
        name="bigbee-graph",
        uri="http://localhost:8000",
        base_path="/v1",
        secret="secret",
        api_key="api_key"
    )