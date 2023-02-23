# Technical-Challenge
Wikipedia search engine
This project provides a search engine for Wikipedia articles. It allows users to search for articles and also to add new articles to the database.

Requirements
To run this project, you will need to download a Wikipedia dump file in XML format. You can find the latest dumps at https://dumps.wikimedia.org/.

Building the project
To build the project, follow these steps:

Clone the repository
Use: docker compose build web
Before you can use the search engine, you need to ingest the Wikipedia dump into the database. To do this, follow these steps:
Download the Wikipedia dump file and place it in the project directory.
Run the ingest script: python ingest.py
This will create a new table named wikipedia in the database and fill it with the contents of the Wikipedia dump.

Running the project
To run the project, follow these steps:

Start the database: docker-compose up db
Start the web server: docker-compose up web
Start the API server: uvicorn api:app --reload
You should now be able to create a POST Request at http://127.0.0.1:8000/search?search_query=KEYWORD using a tool like Postman.

To add a new article to the database, send a POST request to http://127.0.0.1:8000/wikipedia with a JSON body that looks like this:

{
    "id": ARTICLE_ID,
    "title": "ARTICLE_TITLE",
    "content": "ARTICLE_CONTENTS"
}
Note that you should replace ARTICLE_ID, ARTICLE_TITLE, and ARTICLE_CONTENTS with the actual values for the article you want to add. The id field should be a unique identifier for the article, as no built-in verification is implemented.
