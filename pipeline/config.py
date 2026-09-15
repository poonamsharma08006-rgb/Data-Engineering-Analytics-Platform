import os
DATABASE_URL=os.getenv("DATABASE_URL","postgresql+psycopg://analytics:analytics@localhost:5434/analytics_db")
SOURCE_FILE=os.getenv("SOURCE_FILE","data/sales.csv")
