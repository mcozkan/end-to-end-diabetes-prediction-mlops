import os
from dotenv import load_dotenv
from sqlmodel import create_engine, Session, SQLModel


# get connection string from .env
load_dotenv()

POSTGRES_CONNECTION_STRING = os.getenv("POSTGRES_CONNECTION_STRING")
if POSTGRES_CONNECTION_STRING is None:
    raise ValueError("POSTGRES_CONNECTION_STRING is not set in the .env variables.")


# Define an engine in order to start connection
engine = create_engine(POSTGRES_CONNECTION_STRING, echo = True)

# define a function to create the database and tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# start connection engine :
def get_db():
    db = Session(engine) # Session creates a new session for interacting with the database
    try:
        # yield ensures database connections are always properly closed, preventing memory leaks and connection pool exhaustion.
        yield db
        # Route uses the session...
        # Route finishes...
    finally:
        db.close() # Close the session to release resources and return the connection to the pool