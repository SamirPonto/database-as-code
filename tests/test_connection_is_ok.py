import pytest
from sqlalchemy import inspect, select

from database_as_code import (
    connection,
    create_obligations_schema,
    create_obligations_tables,
)


@pytest.fixture
def engine():
    return connection()


@pytest.fixture
def inspector(engine):
    return inspect(engine)


def test_connection_is_not_none(engine):
    assert engine is not None


def test_select_return_tuple_1_(engine):
    query_test = select(1)
    with engine.connect() as conn:
        result = conn.execute(query_test)
        assert result.fetchone() == (1,)


def test_obligations_schema_is_created(engine, inspector):
    create_obligations_schema(engine)
    assert "obligations" in inspector.get_schema_names()


def test_cost_table_is_create_on_obligations_schema(engine, inspector):
    create_obligations_tables(engine)
    assert "cost" in inspector.get_table_names(schema="obligations")


def test_expense_table_is_create_on_obligations_schema(inspector):
    assert "expense" in inspector.get_table_names(schema="obligations")
