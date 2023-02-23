# Technical-Challenge

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


Run: uvicorn api:app --reload


You should now be able to create a GET Request at http://127.0.0.1:8000/search?search_query=KEYWORD using a tool like Postman.


To add a new article to the database, send a POST request to http://127.0.0.1:8000/wikipedia with a JSON body that looks like this:


{


    "id": ARTICLE_ID,
    
    
    "title": "ARTICLE_TITLE",
    
    
    "content": "ARTICLE_CONTENTS"
    
    
}


Note that you should replace ARTICLE_ID, ARTICLE_TITLE, and ARTICLE_CONTENTS with the actual values for the article you want to add. The id field should be a unique identifier for the article, as no built-in verification is implemented.


Note: There was an issue with connecting to the api inside the docker container and I believe it was due to some docker issues on my windows machine and was out of the scope of the task to spend so much time on this issue.


Answer to Additional Questions:


What is the bottleneck of the current design?


-The current design has bottlenecks in both ingestion and search operations. In terms of ingestion, parsing and extracting data from large XML files can be time inefficient. In terms of search, performing a full-text search on a large database can also be resource intensive.


How could the ingest performance be improved?


-If the volume of data is very large, platforms such as Apache Spark will significantly improve performance. 


How could the search performance be improved?


-Using engines such as Elasticsearch, which is designed for fast and efficient full-text searches.


-Indexing the content column in the database would imporove results.


-And caching could be used to cache frequently accessed results. A framework suitable for this is Redis.

