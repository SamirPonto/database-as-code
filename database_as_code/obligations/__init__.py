from sqlalchemy import Column, Engine, Float, Integer, String, text
from sqlalchemy.orm import declarative_base

BaseObligations = declarative_base()


class BaseObligation(BaseObligations):
    __table_args__ = {"schema": "obligations"}
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    month = Column(String)
    name = Column(String)
    value = Column(Float)


class Cost(BaseObligation):
    __tablename__ = "cost"


class Expense(BaseObligation):
    __tablename__ = "expense"


def create_obligations_schema(engine: Engine) -> None:
    with engine.connect() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS obligations;"))
        conn.commit()
        conn.close()


def create_obligations_tables(engine: Engine) -> None:
    BaseObligations.metadata.create_all(bind=engine)
