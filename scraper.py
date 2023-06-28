import re
import json
from datetime import datetime
import requests
import koogle_config
from loguru import logger
class Scraper:
    def __init__(self):
        self._max_get_response_try_num = koogle_config._max_get_response_try_num
        self._default_cookies = koogle_config._default_cookies
        self._default_headers = koogle_config._default_headers
        self._default_proxies = koogle_config._default_proxies
        self.logger:logger = logger
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
            try:
                kwargs["proxies"] = {
                    "http": f"http://{self._default_proxies}",
                    "https": f"http://{self._default_proxies}"
                }
                response = requests.get(**kwargs)
            except Exception as e:
                self.logger.info(f"request error, response_try_num:{response_try_num}")
                if response_try_num < _max_get_response_try_num:
                    continue
                else:
                    raise ConnectionError(f"error: {e}")


            if "Unauthorized access to internal API" in response.text:
                raise ConnectionRefusedError("Unauthorized access to internal API")

            if response.status_code == 200:
                return response.text

            if response_try_num >= _max_get_response_try_num:
                raise ConnectionError(f"error: {response.status_code}//{response.text}")

    def _parse_data(self, data, parse_type):
        pass
        #pase your data
        # if parse_type == "your parse type":
        #
        #     parsed_data = json.loads(data)
        #
        #     results = self._json_value(parsed_data, "results")
        #
        #     for row in results:
        #         value = self._json_value(row, "key")
        #
        #         parsed_data = {
        #             "key": value,
        #         }
        #         yield parsed_data
    def _generate(self, results):
        pass
    def get_data_by_keyword(self, start, keyword):

        params = {
            "rsz": "filtered_cse",
            "num": "10",
            "start": start,
            "q": keyword,
            "hl": "ko",
            "source": "gcsc",
            "gss": ".io",
            "cselibv": "827890a761694e44",
            "cx": "010593175421032702917:f7zuzysul9w",
            "safe": "off",
            "cse_tok": "AFW0emxsFhJRYHXpY4-3ZUEgTpcU:1687932436810",
            "exp": "csqr, cc, bf",
            "callback": "google.search.cse.api19585"
        }

        url = "https://cse.google.com/cse/element/v1"
        cookies = self._default_cookies
        headers = self._default_headers
        proxies = {
            "http": f"http://{self._default_proxies}",
            "https": f"https://{self._default_proxies}"
        }
        data = self._get_response(url=url, params=params, headers=headers, cookies=cookies, proxies=proxies)
        results = self._parse_data(data=data, parse_type="get_data_by_keyword")
        yield from self._generate(results)

class NewsHadaScraper(Scraper):
    def init(self):
        self.last_index = 0
        self.keyword = None
        super().__init__()

    def _parse_data(self, data, parse_type):
        if parse_type == "get_data_by_keyword":
            data = data.replace("/*O_o*/\n", "")

            data = data.replace("google.search.cse.api19585(", "")
            data = data.replace(");", "")
            parsed_data = json.loads(data)
            last_index = self._json_value(parsed_data, "cursor", "resultCount")

            last_index = last_index.replace(",", "")
            self.last_index = int(last_index)
            results = self._json_value(parsed_data, "results")
            return results
    def _generate(self, results):
        for row in results:
            publish_date = None
            content = self._json_value(row, "contentNoFormatting")
            match_date_string = re.search(r'\d{4}. \d{1,2}. \d{1,2}.', content)
            if match_date_string:
                match_date = datetime.strptime(match_date_string.group(), "%Y. %m. %d.").date()
                publish_date = match_date

            title = self._json_value(row, "titleNoFormatting")
            title = title.replace(" | GeekNews", "")
            url = self._json_value(row, "url")

            parsed_data = {
                "keyword": self.keyword,
                "title": title,
                "content": content,
                "publish_date": publish_date,
                "url": url
            }
            yield parsed_data
    def get_data_by_keyword(self, start, keyword):
        self.keyword = keyword
        params = {
            "rsz": "filtered_cse",
            "num": "10",
            "start": start,
            "q": keyword,
            "hl": "ko",
            "source": "gcsc",
            "gss": ".io",
            "cselibv": "827890a761694e44",
            "cx": "010593175421032702917:f7zuzysul9w",
            "safe": "off",
            "cse_tok": "AFW0emxsFhJRYHXpY4-3ZUEgTpcU:1687932436810",
            "exp": "csqr, cc, bf",
            "callback": "google.search.cse.api19585"
        }

        url = "https://cse.google.com/cse/element/v1"
        cookies = self._default_cookies
        headers = self._default_headers

        data = self._get_response(url=url, params=params, headers=headers, cookies=cookies, timeout=10)

        results = self._parse_data(data=data, parse_type="get_data_by_keyword")
        yield from self._generate(results)

if __name__ == "__main__":
    scraper = Scraper()
    start = 10
    keyword = "k8s"
    data = scraper.get_data_by_keyword(start=start, keyword=keyword)
    print(data)
