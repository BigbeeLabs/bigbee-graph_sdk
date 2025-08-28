# graph_sdk/domain/role/entity.py

from remote_models.core.remote_model import RemoteModel

class Role(RemoteModel):
    provider_name = "bigbee-graph"
    resource_name = "roles"
