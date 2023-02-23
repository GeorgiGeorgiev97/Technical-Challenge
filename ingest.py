import xml.etree.ElementTree as ET
import psycopg2


# Open the XML file
xml_file = 'enwiki-20230201-pages-articles-multistream1.xml-p1p41242'
with open(xml_file, 'rb') as f:
    xml_data = f.read()

# Parse the XML data
root = ET.fromstring(xml_data)



# Get the database connection parameters from the environment variables
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
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS
 wikipedia (
    id integer PRIMARY KEY,
    title text NOT NULL,
    content text NOT NULL
)
""")

# Iterate over the <page> elements and insert them into the database
for page in root.findall('{http://www.mediawiki.org/xml/export-0.10/}page'):
    page_id = page.find('{http://www.mediawiki.org/xml/export-0.10/}id').text
    title = page.find('{http://www.mediawiki.org/xml/export-0.10/}title').text
    text = page.find(
        '{http://www.mediawiki.org/xml/export-0.10/}revision/{http://www.mediawiki.org/xml/export-0.10/}text').text
    cur = conn.cursor()
    cur.execute("INSERT INTO wikipedia (id, title, content) VALUES (%s, %s, %s)", (page_id, title, text))
    conn.commit()
    cur.close()

# Close the database connection
conn.close()
