# bigbee-graph_sdk/graph_sdk/db/session.py

import sys
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

print(f"[DEBUG] session.py executing from: {__file__}")
print(f"[DEBUG] sys.path: {sys.path}")

env_name = os.environ.get("ENV", "prod")
dotenv_path = Path(__file__).parent.parent / "env" / f".env.{env_name}"
print(f"[DEBUG] loading dotenv from: {dotenv_path}")

if dotenv_path.exists():
    load_dotenv(dotenv_path)
else:
    raise FileNotFoundError(f".env file not found at: {dotenv_path}")

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set in the environment")

engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(bind=engine)

def get_database_url():
    return DATABASE_URL