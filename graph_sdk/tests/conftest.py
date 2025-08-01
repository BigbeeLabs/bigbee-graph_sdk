# graph_sdk/tests/conftest.py

import os
import sys
import pytest
from pathlib import Path
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from alembic import command
from alembic.config import Config

# ─── Path Setup ────────────────────────────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # accounts_sdk/
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "bigbee-app_collaborators"))

# ─── Load .env.test ────────────────────────────────────────────────────────────
env_path = Path(__file__).resolve().parents[1] / "env" / ".env.test"
if not env_path.exists():
    raise FileNotFoundError(f"Missing .env.test at {env_path}")
load_dotenv(dotenv_path=env_path)

# ─── Run Alembic Migrations ────────────────────────────────────────────────────
alembic_ini_path = Path(__file__).resolve().parents[2] / "alembic.ini"
alembic_cfg = Config(str(alembic_ini_path.resolve()))
command.upgrade(alembic_cfg, "head")

# ─── Session Setup ─────────────────────────────────────────────────────────────
from remote_models.db.session import engine
from remote_models.db.session_context import set_session, clear_session
from remote_models.host.session_bridge import register_session

@pytest.fixture(scope="function")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()

    set_session(session)
    register_session(lambda: session)

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()
        clear_session()
        register_session(lambda: None)
