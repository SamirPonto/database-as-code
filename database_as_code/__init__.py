from sqlalchemy import inspect, text

from database_as_code.connection import connection
from database_as_code.obligations import (
    BaseObligations,
    Cost,
    Expense,
    create_obligations_schema,
    create_obligations_tables,
)

engine = connection()


inspector = inspect(engine)
print(inspector.get_table_names(schema="obligations"))
