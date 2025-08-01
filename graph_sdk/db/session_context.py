# bigbee-package_name/package_name/db/session_context.py

import contextvars
from sqlalchemy.orm import Session

_active_session: contextvars.ContextVar[Session | None] = contextvars.ContextVar("active_session", default=None)

def set_session(session: Session):
    _active_session.set(session)

def get_session() -> Session | None:
    return _active_session.get()

def clear_session():
    _active_session.set(None)