# graph_sdk/tests/domain/person/email_addresses/test_add_email_address.py

# graph_sdk/tests/domain/person/email_addresses/test_add_email_address.py

import uuid
from graph_sdk.domain.person.person import Person
from graph_sdk.domain.email_address.email_address import EmailAddress

from app_collaborators.domain.app_provider.app_provider import AppProvider
from app_collaborators.domain.app_provider.app_provider_dtos import AppProviderCreateDto

def test_add_email_address_to_person(db_session):
    create_app_provider()

    # Create a person
    person = Person.create({"given_name": "Alan", "family_name": "Turing"})

    # Create an email address
    email_address = EmailAddress.create({"address": f"alan-{uuid.uuid4()}@example.com"})
    print(f"email_address: {email_address}")

    # Link the email address to the person
    person.email_addresses << email_address

    # Refresh from remote and verify the link
    refreshed = Person.fetch(person.id)
    emails = list(refreshed.email_addresses)

    assert any(e.id == email_address.id for e in emails)

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