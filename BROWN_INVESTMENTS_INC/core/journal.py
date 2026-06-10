import sqlite3

class Journal:
    def log_trade(self, symbol, direction, result):
        conn = sqlite3.connect('data/journal.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS trades(symbol TEXT, direction TEXT, result TEXT)')
        c.execute('INSERT INTO trades VALUES (?,?,?)', (symbol,direction,result))
        conn.commit()
        conn.close()
