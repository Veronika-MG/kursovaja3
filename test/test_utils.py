from utils import filter_sort, format_date, mask_card, load_data, formatted_data


def test_filter_sort():
    data = [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
      },
      {
        "id": 41428829,
        "state": "NOT EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
          "amount": "8221.37",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
      }]

    result = filter_sort(data)
    assert  len(result) == 1

def test_formate_date():
    str_date = "2019-07-03T18:35:29.512364"
    result = format_date(str_date)
    assert result == "03.07.2019"

def test_mask_card():
    card = "MasterCard 7158300734726758"
    result = mask_card(card)
    assert result == "MasterCard 7158 30** **** 6758"


def test_load_data():
    result = load_data()
    assert type(result) == list

def test_formatted_data():
    item = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }
    result = formatted_data(item)
    assert result == "03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD\n"

