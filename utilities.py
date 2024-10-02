import requests


def get_rate():
    rate_data = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5').json()

    return {
        f"{rate_data[0]['ccy']}/{rate_data[0]['base_ccy']}": {
            "BUY": rate_data[0]['buy'], 'SELL': rate_data[0]['sale']
        },
        f"{rate_data[1]['ccy']}/{rate_data[1]['base_ccy']}": {
            "BUY": rate_data[1]['buy'], 'SELL': rate_data[1]['sale']
        }
    }


def form_massage(data: dict) -> str:
    msg = ""
    for key, value in data.items():
        msg += (
            f"{key}\n"
            f"BUY: {value["BUY"]}\n"
            f"SELL: {value["SELL"]}\n"
            f"\n"
        )
    return msg
