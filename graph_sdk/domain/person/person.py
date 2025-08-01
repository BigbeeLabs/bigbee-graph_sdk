# graph_sdk/domain/person/person.py

from remote_models.core.remote_model import RemoteModel

class Person(RemoteModel):
    provider_name = "bigbee-graph"
    resource_name = "people"
