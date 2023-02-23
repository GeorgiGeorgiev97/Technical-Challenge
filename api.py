
import psycopg2


# Define the database connection parameters


host = "localhost"
port = "5432"
database = "postgres"
user = "postgres"
password = "veritas"
# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

# Define the FastAPI app
app = FastAPI()


# Define the database table schema
class Wikipedia(BaseModel):
    id: int
    title: str
    content: str


# Define the endpoint for inserting a Wikipedia page into the database
@app.post("/wikipedia")
def create_wikipedia_page(wikipedia: Wikipedia):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO wikipedia (id, title, content) VALUES (%s, %s, %s)",
        (wikipedia.id, wikipedia.title, wikipedia.content),
    )
    conn.commit()
    cur.close()
    return {"message": "Wikipedia page added to the database."}


# For testing the connection to the db
@app.get("/")
def read_root():
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM wikipedia")
    count = cur.fetchone()[0]
    cur.close()
    return {"message": f"Connected to database with {count} rows."}


# Define the endpoint for searching the database
@app.post("/search")
def search_wikipedia_pages(search_query: str):
    cur = conn.cursor()
    cur.execute(
        "SELECT id, title FROM wikipedia WHERE content LIKE %s",
        ('%' + search_query + '%',)
    )

    rows = cur.fetchall()
    results = []
    print(results)
    for row in rows:
        results.append({"id": row[0], "title": row[1]})
    cur.close()
    return results
