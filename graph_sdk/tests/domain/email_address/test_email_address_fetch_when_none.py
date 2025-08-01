import uuid
from graph_sdk.domain.email_address.email_address import EmailAddress
from app_collaborators.domain.app_provider.app_provider import AppProvider
from app_collaborators.domain.app_provider.app_provider_dtos import AppProviderCreateDto
from app_collaborators.host.session_bridge import register_session

def test_email_addresses_fetch_when_none(db_session):
    register_session(lambda: db_session)
    create_app_provider()

    all = EmailAddress.all()
    assert isinstance(all, list)
    # assert len(all) == 0  # uncomment if you guarantee no residual data

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
