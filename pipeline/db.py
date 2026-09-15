from sqlalchemy import create_engine,text
from pipeline.config import DATABASE_URL
engine=create_engine(DATABASE_URL,pool_pre_ping=True)
def init_db():
    with engine.begin() as c:
        c.execute(text('''CREATE TABLE IF NOT EXISTS sales (
        order_id VARCHAR(30) PRIMARY KEY, order_date DATE NOT NULL,
        customer_id VARCHAR(30) NOT NULL, customer_name VARCHAR(120) NOT NULL,
        product VARCHAR(120) NOT NULL, category VARCHAR(80) NOT NULL,
        region VARCHAR(50) NOT NULL, quantity INTEGER NOT NULL CHECK(quantity>0),
        unit_price NUMERIC(12,2) NOT NULL CHECK(unit_price>=0),
        revenue NUMERIC(14,2) NOT NULL CHECK(revenue>=0),
        loaded_at TIMESTAMPTZ NOT NULL DEFAULT NOW());
        CREATE INDEX IF NOT EXISTS idx_sales_date ON sales(order_date);
        CREATE INDEX IF NOT EXISTS idx_sales_region ON sales(region);
        CREATE INDEX IF NOT EXISTS idx_sales_category ON sales(category);'''))
