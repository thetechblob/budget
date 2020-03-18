# budget
Budgeting tool

## Steps

1. Seed the correct database
2. Load new unclassified transactions
3. Classify new transactions
4. Review classification `csv` file
5. Confirm `csv` classification
6. Retrieve nett balance in date range

## Configuring and running `app.py`

1. In `app.py` set `db_name` to desired database.
2. In `app.py` set `seed_file` to file use for seeding the database.
3. In `app.py` set `new_transactions` to `csv` file where new transactions will be stored.
4. In `app.py` set `classification_csv_file` to file name and location for classified `csv` file to be manually reviewed.
5. In `app.py` select ML model of choice (eg, `SVMClassifier`)
6. Run `python app.py` on command line.  This will seed the db afresh, train the model, updload the new data and generate prediction.
7. Evaluate the and confirm the classification in the `classification_csv_file`, save, and run appropriate commands in `app.py` to update classified transactions.  
8. Get nett balance on transactions between date ranges by running appropriate function in `app.py`.

To seed the data base `seed_file` must by `csv` with the following headings

|Date|Description|Account|Amount|Notes|
|----|-----------|-------|------|------|



