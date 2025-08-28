# graph_sdk/domain/event/event.py

from remote_models.core.remote_model import RemoteModel

class Event(RemoteModel):
    provider_name = "bigbee-graph"
    resource_name = "events"
