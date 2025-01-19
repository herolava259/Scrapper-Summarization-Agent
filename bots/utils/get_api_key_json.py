import json


def get_api_key(source: str) -> str:
    key= ''
    with open('./bots/configs/API_KEYS.json') as f: #
        data = json.load(f)

        key = [d for d in data if d['source'] == source ][0]
    return key['api_key']