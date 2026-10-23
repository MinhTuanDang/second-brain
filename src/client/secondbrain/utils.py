import logging
import uuid

LOG = logging.getLogger("secondbrain")


def string_to_uuid(s: str, salt="secondbrain_client") -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, s + salt))
