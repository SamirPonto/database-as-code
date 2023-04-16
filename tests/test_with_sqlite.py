import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from database_as_code import (
    BaseObligations,
    Cost,
    Expense,
    connection,
    create_obligations_schema,
    create_obligations_tables,
)


# Define test fixtures
@pytest.fixture(scope="session")
def engine():
    # Set up an in-memory SQLite database for testing
    engine = connection()
    create_obligations_schema(engine)
    create_obligations_tables(engine)
    yield engine
    engine.dispose()


@pytest.fixture(scope="function")
def session(engine):
    # Set up a database session for each test
    session = Session(bind=engine)
    yield session
    session.rollback()


# Define tests
def test_create_obligations_schema(engine):
    with engine.connect() as conn:
        result = conn.execute(
            text(
                """SELECT schema_name
                FROM information_schema.schemata
                WHERE schema_name = 'obligations';"""
            )
        )
        assert result.fetchone()[0] == "obligations"


def test_create_obligations_tables(session):
    # Add a record to the Cost table
    cost = Cost(month="2022-01", name="Rent", value=1000.00)
    session.add(cost)
    session.commit()

    # Verify that the record was added to the database
    result = session.execute(
        text("SELECT * FROM obligations.cost WHERE month = '2022-01';")
    )
    assert result.fetchone() is not None

    # Add a record to the Expense table
    expense = Expense(month="2022-01", name="Office Supplies", value=50.00)
    session.add(expense)
    session.commit()

    # Verify that the record was added to the database
    result = session.execute(
        text("SELECT * FROM obligations.expense WHERE month = '2022-01';")
    )
    assert result.fetchone() is not None
