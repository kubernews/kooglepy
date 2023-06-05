
class Scraper:
    def __init__(self):
        pass

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
    def _get_response(self):
        pass
    def _get_text(self):
        pass
    def get_raw_data_by_keyword(self, keyword):
        url = f"https://news.hada.io/search?q={keyword}"
        return None

scraper = Scraper()
s = scraper.get_raw_data_by_keyword()
