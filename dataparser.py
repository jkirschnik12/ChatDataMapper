import json
from get_all_tickers import get_tickers as gt
from get_all_tickers.get_tickers import Region
import constants


class DataParser:
    def __init__(self, filepath: str):
        self.message = self.get_messages(filepath)

    def mentions_by_ticker(self) -> dict:
        tickers_mentions = {}
        tickers = gt.get_tickers()
        return tickers_mentions


    @staticmethod
    def get_messages(filepath: str) -> json:
        with open(filepath) as json_file:
            data = json.load(json_file)
            return data["messages"]
