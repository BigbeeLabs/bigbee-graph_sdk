# graph_sdk/domain/role/entity.py

from remote_models.core.remote_model import RemoteModel

class Role(RemoteModel):
    provider_name = "bigbee-graph"
    resource_name = "roles"

    @classmethod
    def support_roles(cls):
        cls.tagged_with(name="support", on="care_circle")