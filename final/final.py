"""
https://www.cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.so=1&UniDbQuery.VAL_NM_RQ=R01239&UniDbQuery.From=17.09.2013&UniDbQuery.To=17.06.2023
"""

import os
from collections import OrderedDict
from datetime import datetime, date
import json
import requests
from bs4 import BeautifulSoup

currency_ids = {
    "EUR": "R01239",
    "USD": "R01235",
    "CNY": "R01375"

}


class ParserCBRF:
    def __init__(self, currency_ids):
        self.currency_ids = currency_ids
        self.save_path = "parsed_data/"

    def _to_json(self, data, save_file_name):
        # если директория "parsed data" отсуствует, то создадим её
        if not os.path.exists(self.save_path):
            os.mkdir(self.save_path)

        # сохраняем файл как json
        with open(self.save_path + save_file_name, 'w') as f:
            json.dump(data, f, indent=4)

    def start(self, currency_name, save_file_name='data.json'):
        html = self._get_page(self.currency_ids[currency_name])
        soup = BeautifulSoup(html, "html.parser")
        raw_data = [i.text for i in soup.find("table", {"class": "data"}).find_all("td")][1:]

        dates, values = [], []

        for i in range(len(raw_data)):
            if raw_data[i].count('.'):
                dates.append(raw_data[i])
                values.append(float(raw_data[i + 2].replace(',', '.')))

            if raw_data[i] == '10':
                break

        data = OrderedDict(zip(dates, values))
        self._to_json(data, save_file_name)
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


class ChangeRateCB:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, 'r') as f:
            self.data = sorted([[datetime.strptime(date_str, "%d.%m.%Y"), float(value_str)]
                                for date_str, value_str in json.load(f).items()],
                               key=lambda x: x[0])

    # Возвращает курс обмена на определённую дату
    def changerate_by_date(self, date):
        date = datetime.strptime(date, "%d.%m.%Y")
        for item in self.data:
            if item[0] == date:
                return item[1]
        raise (Exception("Курс обмена за указанную дату не обнаружено"))

    # Возвращает курс обмена на последнюю доступную дату
    def cnangerate_last(self):
        return self.data[-1]

    # Возвращает отсортированный список кортеж пар (дата, курс обмена) за определённый период
    def cnangerate_range_dates(self, from_date, to_date):
        from_date = datetime.strptime(from_date, "%d.%m.%Y")
        to_date = datetime.strptime(to_date, "%d.%m.%Y")
        result = []
        for item in self.data:
            if from_date <= item[0] <= to_date:
                result.append(item)
        return result


parser = ParserCBRF(currency_ids)
data = parser.start(currency_name='EUR')
сhange_rate_object = ChangeRateCB("parsed_data/data.json")