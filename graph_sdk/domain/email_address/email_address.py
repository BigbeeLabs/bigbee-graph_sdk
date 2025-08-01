# graph_sdk/domain/email_address/email_address.py

from remote_models.core.remote_model import RemoteModel

class EmailAddress(RemoteModel):
    provider_name = "bigbee-graph"
    resource_name = "email_addresses"
