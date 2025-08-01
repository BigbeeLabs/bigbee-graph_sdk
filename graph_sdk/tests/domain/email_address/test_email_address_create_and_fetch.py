import uuid
from graph_sdk.domain.email_address.email_address import EmailAddress
from app_collaborators.domain.app_provider.app_provider import AppProvider
from app_collaborators.domain.app_provider.app_provider_dtos import AppProviderCreateDto
from app_collaborators.host.session_bridge import register_session

def test_email_address_create_and_fetch(db_session):
    register_session(lambda: db_session)
    create_app_provider()

    all = EmailAddress.all()
    before_count = len(all)

    created = EmailAddress.create({"address": f"test-{uuid.uuid4()}@example.com"})

    all = EmailAddress.all()
    print(f"all: {all}")
    assert isinstance(all, list)
    assert len(all) == before_count + 1

    fetched = EmailAddress.fetch(created.id)
    assert created.id == fetched.id

    created.delete()

    all = EmailAddress.all()
    assert len(all) == before_count

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
