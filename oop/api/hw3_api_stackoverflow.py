import time
import requests

class Stackoverflow_API:
    
    def __init__(self) -> None:
        self.stackoverflow_host = 'https://api.stackexchange.com'

    def _get_headers(self):
        """Метод возвращает заголовки."""

        return {'Content-Type': 'application/json'}
    
    def get_questions(self, fromdate, todate, tags):
        """Метод возвращает все вопросы с указанным тегом и за указанный период."""

        url = f'{self.stackoverflow_host}/2.3/questions'

        params = {'fromdate': fromdate, 'todate': todate, 'order': 'desc', 'sort': 'activity', 'tagged': tags, 'site': 'stackoverflow'}
        headers = self._get_headers()

        response = requests.get(url=url, params=params, headers=headers)

        response.raise_for_status()

        return response.json()


current_datetime = round(time.time())
one_day_seconds = 86400
period = one_day_seconds * 2
fromdate = current_datetime - period


stackoverflow = Stackoverflow_API()

print(stackoverflow.get_questions(fromdate=fromdate, todate=current_datetime, tags='Python'))