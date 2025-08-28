# graph_sdk/domain/person/exports.py

# Purpose:
#   Declare exactly which symbols this package wants to re-export at the
#   SDK level. We use strings ("pkg.mod:Attr") so imports stay LAZY:
#   they won’t happen until the name is actually accessed by users.

EXPORTS = {
    # Domain class
    "Person": "graph_sdk.domain.person.person:Person",
    # DTOs (name them uniquely to avoid collisions in the flat namespace)
    "PersonFindDto": "graph_sdk.domain.person.person_dtos:PersonFindDto",
    "PeopleFindByDto": "graph_sdk.domain.person.person_dtos:PeopleFindByDto",
    "PersonCreateDto": "graph_sdk.domain.person.person_dtos:PersonCreateDto",
    "PersonUpdateDto": "graph_sdk.domain.person.person_dtos:PersonUpdateDto",
}