# tests/domain/people/test_person_delete.py

from graph_sdk.domain.person.person import Person
from app_collaborators.domain.app_provider.app_provider import AppProvider
from app_collaborators.domain.app_provider.app_provider_dtos import AppProviderCreateDto
from app_collaborators.host.session_bridge import register_session

def test_person_delete(db_session):
    register_session(lambda: db_session)
    create_app_provider()

    # Ensure there's at least one person to delete
    if not Person.all():
        Person.create({"given_name": "ToDelete", "family_name": "Person"})

    people = Person.all()
    assert people, "Expected at least one person to delete"

    person_to_delete = people[0]
    deleted = Person.destroy(person_to_delete["id"])
    assert deleted is True or deleted is None  # allow for void/no-content delete

    remaining = Person.all()
    assert person_to_delete["id"] not in [p["id"] for p in remaining]

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
