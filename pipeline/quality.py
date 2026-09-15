import pandas as pd
REQUIRED=["order_id","order_date","customer_id","customer_name","product","category","region","quantity","unit_price"]
def validate(df):
    missing=[c for c in REQUIRED if c not in df.columns]
    dup=int(df["order_id"].duplicated().sum()) if "order_id" in df else -1
    nulls=int(df.isna().sum().sum())
    return {"rows":len(df),"missing_columns":missing,"duplicate_orders":dup,"null_cells":nulls}
def clean(df):
    out=df.copy()
    out["order_date"]=pd.to_datetime(out["order_date"],errors="coerce").dt.date
    out["quantity"]=pd.to_numeric(out["quantity"],errors="coerce")
    out["unit_price"]=pd.to_numeric(out["unit_price"],errors="coerce")
    out=out.dropna(subset=REQUIRED)
    out=out[(out["quantity"]>0)&(out["unit_price"]>=0)]
    out["quantity"]=out["quantity"].astype(int)
    out["revenue"]=(out["quantity"]*out["unit_price"]).round(2)
    return out.drop_duplicates("order_id")
