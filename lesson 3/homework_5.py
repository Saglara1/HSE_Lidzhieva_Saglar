import re
import csv
import json

def make_traders_table(txt_intput_file_path, json_input_file_path, csv_output_file_path):
    """
    Функция, которая принимает в себя путь к файлу с ИНН и путь к файлу с информацией об организациях.
    Возвращает словарь, в котором ключи - это ИНН, а значения - словари с ключами 'ogrn' и 'address'.

    :param txt_intput_file_path: путь к файлу с ИНН
    :param json_input_file_path: путь к файлу с информацией об организациях
    :param csv_output_file_path: путь к файлу, в который будет записана таблица
    :return: None
    """
    with open(txt_intput_file_path, "r", encoding='utf-8') as f:
        inn = [line.strip() for line in f]

    traders_data = {}
    with open(json_input_file_path, "r", encoding='utf-8') as f:
        data = json.load(f)
        for trader in data:
            if trader["inn"] in inn:
                traders_data[trader["inn"]] = {"ogrn": trader["ogrn"], "address": trader["address"]}

    with open(csv_output_file_path, "w", newline="", encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=";")
        for item in inn:
            if item in traders_data:
                writer.writerow([item, traders_data[item]["ogrn"], traders_data[item]["address"]])

def extract_emails(text):
    """
    Функция, которая принимает в себя текст и возвращает список email-адресов, найденных в тексте.
    :param text:
    :return:
    """
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

def extract_emails_from_json(json_input_file, json_output_file):
    """
    Функция, которая принимает в себя путь к файлу с информацией о сообщениях и путь к файлу, в который будет записан словарь.
    :param json_input_file:
    :param json_output_file:
    :return:
    """
    with open(json_input_file, 'r', encoding='utf-8') as f:
        messages = json.load(f)
    emails_dict = {}
    for message in messages:
        inn = message['publisher_inn']
        emails = extract_emails(message['msg_text'])
        if emails:
            if inn not in emails_dict:
                emails_dict[inn] = set()
            emails_dict[inn].update(emails)

    with open(json_output_file, 'w') as f:
        json.dump({k: list(v) for k, v in emails_dict.items()}, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    traders_txt = 'traders.txt'
    traders_json = 'traders.json'
    traders_csv = 'traders.csv'
    messages_json = '1000_efrsb_messages.json'
    emails_json = 'emails.json'
    make_traders_table(traders_txt, traders_json, traders_csv)
    extract_emails_from_json(messages_json, emails_json)
