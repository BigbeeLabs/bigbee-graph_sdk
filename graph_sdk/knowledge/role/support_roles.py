# graph_sdk/knowledge/role/support_roles.py
from graph_sdk.knowledge.graph import Graph
from graph_sdk.domain.role.entity import Role

@Graph.register("support_roles")
def support_roles():
    return Role.support_roles()
