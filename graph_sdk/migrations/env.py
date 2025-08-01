import os
from logging.config import fileConfig
from pathlib import Path
from alembic import context
from sqlalchemy import engine_from_config, pool
from dotenv import load_dotenv

# Load the correct .env file based on ENV (defaults to 'dev')
env = os.getenv("ENV", "dev")
dotenv_path = Path(__file__).resolve().parents[1] / "env" / f".env.{env}"
if not dotenv_path.exists():
    raise FileNotFoundError(f".env file not found: {dotenv_path}")
load_dotenv(dotenv_path)
database_url = os.environ["DATABASE_URL"]

# Alembic config
config = context.config
fileConfig(config.config_file_name)

# Import all *Record models to register tables
from app_collaborators.domain.app_provider.app_provider_record import AppProviderRecord
from app_collaborators.domain.app_client.app_client_record import AppClientRecord
from app_collaborators.db.base import Base

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        {"sqlalchemy.url": database_url},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()