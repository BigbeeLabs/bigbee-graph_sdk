# graph_sdk/domain/role/exports.py

# Purpose:
#   Declare exactly which symbols this package wants to re-export at the
#   SDK level. We use strings ("pkg.mod:Attr") so imports stay LAZY:
#   they won’t happen until the name is actually accessed by users.

EXPORTS = {
    # Domain class (read-only)
    "Role": "graph_sdk.domain.role.entity:Role",

    # DTOs (prefixed to avoid flat-namespace collisions)
    "RoleFindDto": "graph_sdk.domain.role.dtos:RoleFindDto",
    "RolesFindByDto": "graph_sdk.domain.role.dtos:RolesFindByDto",
}
