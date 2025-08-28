# graph_sdk/domain/event/event.py

from remote_models.core.remote_model import RemoteModel

class EventOccurrence(RemoteModel):
    provider_name = "bigbee-graph"
    resource_name = "event_occurrences"
