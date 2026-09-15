import pandas as pd,streamlit as st
from sqlalchemy import create_engine,text
engine=create_engine("postgresql+psycopg://analytics:analytics@localhost:5434/analytics_db",pool_pre_ping=True)
st.set_page_config(page_title="Sales Analytics",layout="wide")
st.title("Sales Analytics Dashboard")
@st.cache_data(ttl=30)
def load():
    with engine.connect() as c:
        return pd.read_sql(text("SELECT order_date,customer_id,customer_name,product,category,region,quantity,unit_price,revenue FROM sales ORDER BY order_date"),c)
try: df=load()
except Exception as e:
    st.error("Start PostgreSQL and run the ETL pipeline first."); st.exception(e); st.stop()
a,b,c,d=st.columns(4)
a.metric("Orders",f"{len(df):,}"); b.metric("Customers",f"{df.customer_id.nunique():,}"); c.metric("Revenue",f"₹{df.revenue.sum():,.0f}"); d.metric("Avg Order",f"₹{df.revenue.mean():,.0f}")
st.subheader("Revenue by Region")
st.bar_chart(df.groupby("region")["revenue"].sum())
st.subheader("Revenue Trend")
st.line_chart(df.groupby("order_date")["revenue"].sum())
st.subheader("Top Products")
st.dataframe(df.groupby("product",as_index=False)["revenue"].sum().sort_values("revenue",ascending=False).head(10),use_container_width=True,hide_index=True)
