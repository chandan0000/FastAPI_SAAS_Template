from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# application import config.
from src.app.config import db_settings

# DB URL for connection
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_settings.username}:{db_settings.password}@{db_settings.hostname}:{db_settings.port}/{db_settings.name}"

# Creating DB engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creating and Managing session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print("Database is Ready!")

# Domain Modelling Dependency
Base = declarative_base()


TEST_SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL + "_test"
test_engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL)
TestSessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=test_engine)


def get_test_db():
    print("Test Database is Ready!")

    test_db = TestSessionLocal()
    try:
        yield test_db
    except:
        test_db.rollback()
    finally:
        test_db.close()
