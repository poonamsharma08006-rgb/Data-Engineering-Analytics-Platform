import pandas as pd
from sqlalchemy import text
from pipeline.config import SOURCE_FILE
from pipeline.db import engine,init_db
from pipeline.quality import validate,clean
def run():
    raw=pd.read_csv(SOURCE_FILE)
    report=validate(raw)
    print("Quality report:",report)
    if report["missing_columns"]: raise ValueError(report["missing_columns"])
    df=clean(raw)
    if df.empty: raise ValueError("No valid rows after cleaning")
    init_db()
    with engine.begin() as c:
        c.execute(text("TRUNCATE TABLE sales"))
        df.to_sql("sales",c,if_exists="append",index=False,method="multi")
        m=c.execute(text("SELECT COUNT(*) orders,COUNT(DISTINCT customer_id) customers,ROUND(SUM(revenue),2) revenue,ROUND(AVG(revenue),2) avg_order_value FROM sales")).mappings().one()
    print("Loaded:",len(df),"rows")
    print("Analytics:",dict(m))
if __name__=="__main__": run()
