# graph_sdk/domain/person/person.py

from remote_models.core.remote_model import RemoteModel
from graph_sdk.domain.email_address.email_address import EmailAddress
from acts_as_having import acts_as_having

@acts_as_having("email_addresses", remote=True, class_=EmailAddress)
class Person(RemoteModel):
    provider_name = "bigbee-graph"
    resource_name = "people"
