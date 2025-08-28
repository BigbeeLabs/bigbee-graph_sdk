# tests/domain/role/test_role_remote_model.py

from graph_sdk.domain.role.entity import Role
from graph_sdk.domain.role.dtos import RolesFindByDto
from app_collaborators.domain.app_provider.app_provider import AppProvider
from app_collaborators.domain.app_provider.app_provider_dtos import AppProviderCreateDto


def test_role_remote_read_only(db_session):
    # Ensure provider is registered (simple helper, no session bridge)
    create_app_provider()

    # list
    roles = Role.all()
    assert isinstance(roles, list)
    assert any(r.system_name == "caregiver" for r in roles)

    # find_by via DTO
    found = Role.find_by(RolesFindByDto(system_name="caregiver"))
    assert found and found[0].display_name == "Caregiver"

    # fetch by id
    rid = found[0].id
    fetched = Role.fetch(rid)
    assert fetched.id == rid
    assert fetched.system_name == "caregiver"

    # combined filter should return exactly one
    both = Role.find_by(RolesFindByDto(system_name="support_provider", display_name="Support Provider"))
    assert both and len(both) == 1
    assert both[0].system_name == "support_provider"
    assert both[0].display_name == "Support Provider"


def create_app_provider():
    AppProvider.create(AppProviderCreateDto(
        name="bigbee-graph",
        uri="http://localhost:9000",
        base_path="/v1",
        secret="secret",
        api_key="api_key",
    ))
