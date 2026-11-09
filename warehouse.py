import csv
import sqlite3
from pathlib import Path
ROOT = Path(__file__).resolve().parent
DB = ROOT / 'output' / 'warehouse.db'

def initialize(db_path=DB):
    db_path=Path(db_path); db_path.parent.mkdir(parents=True,exist_ok=True)
    with sqlite3.connect(db_path) as c:
        c.execute('CREATE TABLE IF NOT EXISTS orders (order_id TEXT PRIMARY KEY, day TEXT, store TEXT, amount REAL)')
        c.execute('CREATE TABLE IF NOT EXISTS daily_sales (day TEXT, store TEXT, revenue REAL, PRIMARY KEY(day,store))')

def load(db_path=DB, csv_path=ROOT/'samples'/'orders.csv'):
    with sqlite3.connect(db_path) as c, Path(csv_path).open(newline='') as f:
        for row in csv.DictReader(f):
            c.execute('INSERT OR REPLACE INTO orders VALUES (?,?,?,?)',
                      (row['order_id'],row['day'],row['store'],float(row['amount'])))

def aggregate(db_path=DB):
    with sqlite3.connect(db_path) as c:
        c.execute('DELETE FROM daily_sales')
        c.execute('INSERT INTO daily_sales SELECT day,store,ROUND(SUM(amount),2) FROM orders GROUP BY day,store')
        return c.execute('SELECT day,store,revenue FROM daily_sales ORDER BY day,store').fetchall()

def run(db_path=DB):
    initialize(db_path);load(db_path);return aggregate(db_path)

if __name__=='__main__':
    print(run())
