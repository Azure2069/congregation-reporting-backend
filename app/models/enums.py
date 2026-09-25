from enum import Enum

class ServiceType(str, Enum):
    publisher="publisher"
    auxiliary_pioneer="auxiliary_pioneer"
    regular_pioneer="regular_pioneer"


class Role(str, Enum):
    publisher='publisher'
    group_overseer='group_overseer'
    secretary='secretary'
    elder='elder'
    admin='admin'
    service_overseer='service_overseer'

class Status(str, Enum):
    submitted="submitted"
    in_review="in_reviewed"
    approved='approved'
    returned='returned'

    