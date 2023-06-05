import os
import json
import requests
from kooglepy.koogle import config

class Scraper:
    def __init__(self):
        self._max_get_response_try_num = config._max_get_response_try_num
        self._default_cookies = config._default_cookies
        self._default_headers = config._default_headers
        self._default_proxies = config._default_proxies
    def _json_value(self, data, *args, default=None):
        cur = data
        for a in args:
            try:
                if isinstance(a, int):
                    cur = cur[a]
                else:
                    cur = cur.get(a)
            except (IndexError, KeyError, TypeError, AttributeError):
                return default
        return cur

    def _get_response(self, **kwargs):

        _max_get_response_try_num = self._max_get_response_try_num
        response_try_num = 0
        while True:
            response_try_num += 1
            response = requests.get(**kwargs)

            if response.status_code == 200:
                if "429" in response.text:
                    print(429)
                    kwargs["proxies"] = {
                       "http": f"http://{self._default_proxies}",
                        "https": f"http://{self._default_proxies}"
                    }
                    continue
                return response.text

            if response_try_num >= _max_get_response_try_num:
                raise Exception(f"error: {response.status_code}//{response.text}")

    def _parse_data(self, data, parse_type):
        if parse_type == "get_data_by_keyword":
            data = data.replace("/*O_o*/\n", "")

            data = data.replace("google.search.cse.api19585(", "")
            data = data.replace(");", "")
            parsed_data = json.loads(data)

            results = self._json_value(parsed_data, "results")
            parsed_data_list = []
            for row in results:
                title = self._json_value(row, "titleNoFormatting")
                title = title.replace(" | GeekNews", "")
                url = self._json_value(row, "url")
                parsed_data = {
                    "title": title,
                    "url": url
                }
                parsed_data_list.append(parsed_data)
            return parsed_data_list
    def get_data_by_keyword(self, start, keyword):

        params = {
            "rsz": "filtered_cse",
            "num": "10",
            "start": start,
            "q": keyword,
            "hl": "ko",
            "source": "gcsc",
            "gss": ".io",
            "cselibv": "ffd60a64b75d4cdb",
            "cx": "010593175421032702917:f7zuzysul9w",
            "safe": "off",
            "cse_tok": "AFW0emzRQ1VBQo2jFS26lzqWaKb2:1685946224482",
            "exp": "csqr, cc, bf",
            "callback": "google.search.cse.api19585"
        }

        url = "https://cse.google.com/cse/element/v1"
        cookies = self._default_cookies
        headers = self._default_headers
        data = self._get_response(url=url, params=params, headers=headers, cookies=cookies)

        parsed_data_list = self._parse_data(data=data, parse_type="get_data_by_keyword")
        return parsed_data_list

scraper = Scraper()
start = 10
keyword = "k8s"
data = scraper.get_data_by_keyword(start=start, keyword=keyword)
print(data)
