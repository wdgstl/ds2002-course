# Hands-On SQL for Data Science

## Setup your repo
1. Go to your fork of the `ds2002-course` repository in GitHub.
2. Use the "Sync Fork" button at the top of the page to sync and update your branch with the upstream repo.
3. Now open your repository in Gitpod. Remember to simply append `gitpod.io/#` before the GitHub URL and it will open automatically.

## Set up Gitpod

1. Install the `mysql` client from the Gitpod terminal and for supporting the `MySQLdb` package:

    ```
    sudo apt install -y mysql-client
    pip install mysqlclient
    ```

2. Run the `mysql` command-line client:

    ```
    mysql -h $DBHOST -u$DBUSER -p$DBPASS
    ```

3. Select your database. Using the DB you have already created under your computing ID, select it with the `use` command:

    ```
    use mst3k;   # replace with your DB name
    ```

## Load Data from SQL Files

1. Open the `practice/11-datasci-sql` directory and open `data.sql`.
2. Let's browse the contents of the file.
3. How do we run a script using the command-line?

## Practice with SQL queries in the CLI

```
SELECT
UPDATE
DELETE
```

## Practice with SQL queries using Python

### imports

import json
import os
import MySQLdb

### Connection Strings

### Cursor

### Query

import json
import os
import MySQLdb

# db config stuff
DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DB = "nem2p"

db = MySQLdb.connect(host=DBHOST, user=DBUSER, passwd=DBPASS, db=DB)
cursor = db.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("SELECT * FROM albums ORDER BY name")
results = cursor.fetchall()
db.close()

print(results)
