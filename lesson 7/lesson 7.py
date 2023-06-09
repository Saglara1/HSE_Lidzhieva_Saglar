from datetime import date
import json
import requests
from bs4 import BeautifulSoup

url_params = "?" \
             "UniDbQuery.Posted=True&" \
             "UniDbQuery.From=17.09.2013&" \
             "UniDbQuery.To=15.05.2023"

currency_ids = {
    "EUR": "R01239",
    "USD": "R01235",
    "CNY": "R01375"

}

class ParserCBRF:
  def __init__(self, currency_ids, url_params):
      self.url_params = url_params
      self.currency_ids = currency_ids

  def start(self, currency_name, save_path='data.json'):
      html = self._get_page(self.currency_ids[currency_name])
      soup = BeautifulSoup(html, "html.parser")
      raw_data = [i.text for i in soup.find("table", {"class": "data"}).find_all("td")]

      items = [item for item in raw_data[1:] if item != '1']
      dates = [item for idx, item in enumerate(items) if idx % 2 == 0]
      values = [item for idx, item in enumerate(items) if idx % 2 != 0]
      data = dict(zip(dates, values))
      with open(save_path, 'w') as f:
        json.dump(data, f, indent=4)
      return data

  def _today_human_date(self):
      today = date.today().strftime("%d.%m.%Y")
      return today


  def _get_page(self, currency_idx):
      url = f"https://www.cbr.ru/currency_base/dynamics/?" \
            f"UniDbQuery.Posted=True&" \
            f"UniDbQuery.so=1&" \
            f"UniDbQuery.VAL_NM_RQ={currency_idx}&" \
            f"UniDbQuery.From=17.09.2013&" \
            f"UniDbQuery.To={self._today_human_date()}"
      print(url)
      r = requests.get(url)

      return r.text
parser = ParserCBRF(currency_ids, url_params)
data = parser.start(currency_name='CNY')