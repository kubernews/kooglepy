import scraper
import db_postgresql
import requests
import time
from loguru import logger
from whatap import method_profiling



@method_profiling
def test_app():
    logger.error("hahahahahahahaha")
    response = requests.get(url="https://www.naver.com")
    print(response.status_code)
    time.sleep(3)
    return "test"
# @method_profiling
@method_profiling
def crawl_newshada(keyword, start=0, end=10):
    current_page = 0
    cnt = 0
    dup_cnt = 0
    CRAWL = True
    logger.info(f"키워드 :{keyword} - 크롤링 시작 - 총 {end - start}개 수집 요청함")
    db_conn = db_postgresql.PostgreSql()
    scraper_hada = scraper.NewsHadaScraper()

    while True:
        ##1. 크롤링 시작 인덱스와 키워드를 설정하면 제너레이터 객체가 생성된다
        keyword_scraper = scraper_hada.get_data_by_keyword(start=start, keyword=keyword)
        ##2. 생성된 제너레이터 객체는 해당 페이지의 데이터 리스트를 가지고 있다. 반복문을 통해 한개씩 가져온다.
        for index, data in enumerate(keyword_scraper):

            ##2.1 크롤링할 수를 넘어서면 반복문을 중지하고, CRAWL 조건을 False로 만들어준다.
            last_index = scraper_hada.last_index
            if start >= min(end, last_index - 10):
                CRAWL = False
                break
            else:
                ##2.2 갯수 1개 증가, 중복이 되건 안되건 1을 추가한다.
                start += 1
                cnt += 1

            ## 2.3 중복확인(url 기준), 중복으로 판명될 경우에는 디비에 insert 하지 않는다.
            select_query = f'''SELECT * FROM koogle_news where url=%s'''
            select_args = (data.get('url'),)
            db_conn.cursor.execute(select_query, select_args)
            if db_conn.cursor.fetchone():
                dup_cnt += 1
                continue

            ## 2.4 중복된 url 이 아닌 경우 디비에 넣어준다.
            insert_values = (data.get('keyword'), data.get('publish_date'), data.get('title'), data.get('content'), data.get('url'))
            insert_query = '''INSERT INTO koogle_news (keyword, publish_date, title, content, url) VALUES (%s, %s, %s, %s, %s)'''
            db_conn.cursor.execute(insert_query, insert_values)
            db_conn.db.commit()


        ## 반복문이 끝나면 다음페이지로 넘어간다.
        if CRAWL == True:
            # 다음 페이지로 이동
            logger.info(f"크롤링 진행 중 - 현재 페이지 인덱스:{current_page} - 총 크롤링된 뉴스:{cnt} - 새로 수집된 뉴스:{cnt-dup_cnt} - 디비에 이미 존재하는 뉴스:{dup_cnt}")
            current_page += 1
        else:
            logger.info(f"크롤링 완료 - 현재 페이지 인덱스:{current_page} - 총 크롤링된 뉴스:{cnt} - 새로 수집된 뉴스:{cnt-dup_cnt} - 디비에 이미 존재하는 뉴스:{dup_cnt}")
            break

    db_conn.db.close()
    db_conn.cursor.close()

