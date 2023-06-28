import koogle_config
import psycopg2




class PostgreSql:
    def __init__(self):
        self.db = psycopg2.connect(host=koogle_config.postgresql_host,
                                   dbname=koogle_config.postgresql_dbname,
                                   user=koogle_config.postgresql_user,
                                   password=koogle_config.postgresql_password,
                                   port=koogle_config.postgresql_port)
        self.cursor = self.db.cursor()
    def __del__(self):
        self.cursor.close()
        self.db.close()

    def execute(self, *args, **kwargs):
        self.cursor.execute(*args, **kwargs)
    #     row = self.cursor.fetchall()
    #     return row

    # def commit(self):
    #     self.cursor.commit()
    #
    # def insert(self, table, column, values):
    #     sql = f'''INSERT INTO {table} {column} VALUES {values}'''
    #     try:
    #         self.cursor.execute(sql)
    #         self.db.commit()
    #     except Exception as e:
    #         print(f"insert error:{e}")

if __name__ == "__main__":
    # conn = psycopg2.connect(host='192.168.1.208', dbname="koogle", user="postgres", password="qwer1234!", port=5432)
    conn = psycopg2.connect(host=koogle_config.postgresql_host,
                                   dbname=koogle_config.postgresql_dbname,
                                   user=koogle_config.postgresql_user,
                                   password=koogle_config.postgresql_password,
                                   port=koogle_config.postgresql_port)
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
    keyword = "테스트"
    select = '''SELECT * FROM koogle_news where url=%s'''
    slect_args = ("https://news.hada.io/topic%3Fid%3D9040",)
    my_keyword = None
    insert = '''INSERT INTO koogle_news (keyword, publish_date, title, content, url) VALUES ('키워드2', '2023-06-26', '타이틀2', '콘텐트', 'https://www.naver.com')'''
    cursor.execute(select,slect_args)
    rows = cursor.fetchone()
    print(rows)
    # for row in rows:
    #     print(row)
    conn.close()

