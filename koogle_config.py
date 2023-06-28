from dotenv import load_dotenv
load_dotenv(verbose=True)

import os

_max_get_response_try_num = 3
_default_cookies = cookies = {
    '__Secure-3PSID': 'Wwip_Q4AReZ1ioIBANvcinAmBWpbzXIXA1ISZNWjpUZX_1Mgsk_w2-sRsiD0fTiLQvvRjg.',
    '__Secure-3PAPISID': 'mUdDtvElGk8BPT11/AUwwfi6_74YTF93RI',
    'NID': '511=XbD0zbSm-6SVF4XANvg8FGy2LN40nsl0BonuIJ0jSMh6IZpyI4lXRpocicmMoT25F4R6KL42VqPX0Nx_ymDS5poLhsvs2hTxdIriCc8w4fJJFhrfjN8rQONciVLxFbtYwFeJPx6h3TMfTdGOb3fTjH3W19sUn3xPENA3QJOTCnHMqKVVe8eoSilt9eWmQa7GPvHJCPics6JrCz2T7tsb6xyg_RUu3FlCVkKnLCmu0nUog_ibdVZdXmZ7jMUI2NRlr49u1Q',
    '1P_JAR': '2023-06-05-06',
    '__Secure-3PSIDCC': 'AP8dLtz6N4PGy1kvWrZ2StWw7yRZgJJ0dZ8Wn-Ep3PDN_1s_BtbC7c6ljmz_8PxodUZNago30Dk',
}

_default_headers = {
    'authority': 'cse.google.com',
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '__Secure-3PSID=Wwip_Q4AReZ1ioIBANvcinAmBWpbzXIXA1ISZNWjpUZX_1Mgsk_w2-sRsiD0fTiLQvvRjg.; __Secure-3PAPISID=mUdDtvElGk8BPT11/AUwwfi6_74YTF93RI; NID=511=XbD0zbSm-6SVF4XANvg8FGy2LN40nsl0BonuIJ0jSMh6IZpyI4lXRpocicmMoT25F4R6KL42VqPX0Nx_ymDS5poLhsvs2hTxdIriCc8w4fJJFhrfjN8rQONciVLxFbtYwFeJPx6h3TMfTdGOb3fTjH3W19sUn3xPENA3QJOTCnHMqKVVe8eoSilt9eWmQa7GPvHJCPics6JrCz2T7tsb6xyg_RUu3FlCVkKnLCmu0nUog_ibdVZdXmZ7jMUI2NRlr49u1Q; 1P_JAR=2023-06-05-06; __Secure-3PSIDCC=AP8dLtz6N4PGy1kvWrZ2StWw7yRZgJJ0dZ8Wn-Ep3PDN_1s_BtbC7c6ljmz_8PxodUZNago30Dk',
    'referer': 'https://news.hada.io/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'x-client-data': 'CKi1yQEIh7bJAQiktskBCKmdygEI2tPKAQi+issBCJShywEIhqDNAQiMp80BCNyqzQE=',
}

proxy_username = os.getenv('proxy_username')
proxy_password = os.getenv('proxy_password')
proxy_host = os.getenv('proxy_host')
proxy_port = os.getenv('proxy_port')

_default_proxies = f"{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"

postgresql_host = os.getenv('postgresql_host')
postgresql_dbname = os.getenv('postgresql_dbname')
postgresql_user = os.getenv('postgresql_user')
postgresql_password = os.getenv('postgresql_password')
postgresql_port = os.getenv('postgresql_port')


table = "koogle_news"