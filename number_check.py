import requests
import re

def check(number: str):
  url = f"https://zniis.ru/bdpn/check/?num={number}"

  try:
    data = requests.get(url).text
    operator = re.search(r"Оператор: (.*?)<br>", data).group(1)
    region = re.search(r"Регион: (.*?)<br />", data).group(1)
    return [operator, region]
  except Exception as ex:
    return False