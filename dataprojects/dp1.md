# Data Project 1: Build a Data-driven API

In this Data Project you will build on your FastAPI code by providing data dynamically to your API.

- The database will be a MySQL RDS instance running in AWS.
- The API will be your FastAPI instance running in a container.
- The container will be running in Amazon EC2.
- Finally, a simple web page will display your API data visually.

## 1. Setup

This data project assumes you have successfully completed **Lab 6** and that pushes to your `fastapi-demo` repository build container images successfully. If you have not completed this step, you must before you can continue.

You may either develop/test your code locally or using Gitpod. There is no preference, though more advanced students who want the challenge may choose to develop locally.

### Set Environment Variables

1. Follow the instructions found at this page in Canvas and set your `DBHOST`, `DBUSER`, and `DBPASS` environment variables.
2. You will need to inject these same variables into your container when you run it in Amazon EC2 near the end of this project.

These `ENV` variables provide a server, username, and password for your code to communicate with the MySQL service.

### Python Installation

At the end of your `requirements.txt` file you should add an entry:
```
mysqlclient
```
And then in your environment (local computer or Gitpod) run this command:
```
python3 -m pip install mysqlclient
```

This installation allows you to import the `MySQLdb` package for database communications.

### Python Imports

Add the following entries to the top of your `app/main.py` file:

```
import json   # if not already present
import os
import MySQLdb
from fastapi.staticfiles import StaticFiles
```
These imports let you use environment variables within your code, communicate with the MySQL database service, and will enable FastAPI to display a simple HTML page (see below).

Next, below your instantiation of the `app = FastAPI()` object, enter these lines:

```
app.mount("/static", StaticFiles(directory="static"), name="static")

HOST = os.environ.get('DBHOST')
USER = os.environ.get('DBUSER')
PASS = os.environ.get('DBPASS')
```
These lines configure FastAPI to display static pages and populate three new variables with the `ENV` variables you set above.


### Static Files

Within the `app/` directory of your FastAPI, create a new subdirectory named `static`. Inside of it, copy these three files:

- [`index.html`](static/index.html) - A simple framework to display your API data for humans.
- [`script.js`](static/script.js) - The logic of the page that communicates with your API.
- [`styles.css`](static/styles.css) - A stylesheet for decorating the HTML file.

These files will dynamically communicate with your API to fetch data and display it in a human-readable page.

Take the time to read through the code and see what you can understand.

The static page configuration now means that your FastAPI deployment has an additional endpoint: `/static/index.html` appended to your API's URL will display this page.

## 2. Database Prep

1. Run a PhpMyAdmin container either locally or in Gitpod using these instructions. Connect to the RDS instance using these credentials. This will give you a GUI for interacting with your database.

2. Following the instructions from class, create a new database (if you haven't already) with your UVA user ID as the name (i.e. `nem2p` or `mst3k` etc.)

3. Click into your database on the left. Using the "Create new table" field on the page, create a table named `albums` with 5 columns.

4. Click on the "SQL" tab at the top of the screen. You will be given a large text box to run SQL queries against your database. 
Copy this script and paste **BUT EDIT** the name of the database before `albums` (where it says `mst3k` below replace it with your DB name) and then press GO.

    ```
    CREATE TABLE `mst3k`.`albums` (`id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(30) NULL , `artist` VARCHAR(30) NULL , `genre` VARCHAR(15) NULL , `year` INT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;
    ```

5. The command should execute quickly and you will see your `albums` table appear on the left. Click into that. Note that it is empty, i.e. it has no records.

6. Click on the INSERT tab at the top of the screen. Using the top form entry, add a favorite album of yours to the database. Leave the ID entry empty, but add an album NAME, ARTIST, GENRE, and YEAR. Then press GO to save it.

7. Next let's add more entries using direct SQL. Click into the SQL tab again. Copy the code below and modify it for another entry. The `id` should have the value of `NULL` (no quotes) and the `year` should have a 4-digit integer value (no quotes):

    ```
    INSERT INTO `albums`(
        `id`, 
        `name`, 
        `artist`, 
        `genre`, 
        `year`
    ) VALUES (
        NULL,
        '<ALBUM-NAME>',
        '<ALBUM-ARTIST>',
        '<ALBUM-GENRE>',
        '<ALBUM-YEAR>'
    )
    ```

    Here's an example entry:

    ```
    INSERT INTO `albums`(
        `id`, 
        `name`, 
        `artist`, 
        `genre`, 
        `year`
    ) VALUES (
        NULL,
        'Wincing the Night Away',
        'The Shins',
        'indie',
        2007
    )

8. Repeat this process until you have 10 entries in your database.

## 3. Connect FastAPI to the Database