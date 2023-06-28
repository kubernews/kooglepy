import psycopg2


class PostgreSql:
    def __init__(self):
        self.db = psycopg2.connect(host='192.168.1.208', dbname="postgres", user="postgres", password="qwer1234!", port=5432)
        self.cursor = self.db.cursor()
    def __del__(self):
        self.cursor.close()
        self.db.close()

    def execute(self, query, *args):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()

    def insert(self, table, column, values):
        sql = f'''INSERT INTO {table} {column} VALUES {values}'''
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(f"insert error:{e}")

if __name__ == "__main__":
    conn = psycopg2.connect(host='192.168.1.208', dbname="koogle", user="postgres", password="qwer1234!", port=5432)
    conn.autocommit = True
    cursor = conn.cursor()

    """CREATE TABLE vendors (vendor_id SERIAL PRIMARY KEY,vendor_name VARCHAR(255) NOT NULL)"""
    #create_sql = """CREATE database koogle"""
    create_table = """
        CREATE TABLE koogle_news 
            (
                kid SERIAL PRIMARY KEY,
                keyword VARCHAR(255),
                publish_date DATE,
                title TEXT,
                content TEXT,
                url TEXT
            )
        """

    select = """SELECT * FROM koogle_news;"""
    insert = '''INSERT INTO koogle_news (keyword, publish_date, title, content, url) VALUES ('테스트', '2023-06-26', '타이틀', '콘텐트', 'https://www.naver.com')'''
    cursor.execute(select)
    rows = cursor.fetchall()
    print(rows)
    conn.close()

