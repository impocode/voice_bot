from copy import deepcopy

from sqlalchemy import Column, ForeignKey, Table, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID

from models.base import base_fields, metadata
from models.utils import initialize_datetime_triggers

user_voice_model = Table(
    "user_voice_relations",
    metadata,
    *deepcopy(base_fields),
    # fmt: off
    Column("user_uuid", UUID, ForeignKey("public.users.uuid", onupdate="CASCADE", ondelete="CASCADE"), nullable=False, comment="User UUID"),
    Column("voice_uuid", UUID, ForeignKey("public.voices.uuid", onupdate="CASCADE", ondelete="CASCADE"), nullable=False, comment="Voice UUID"),
    UniqueConstraint("user_uuid", "voice_uuid", name="user_voice_constraint"),
    schema="public",
    comment="User voice relations"
)


create_datetime_trigger, drop_datetime_trigger = initialize_datetime_triggers(
    model=user_voice_model
)

__all__ = ["user_voice_model", "create_datetime_trigger", "drop_datetime_trigger"]
