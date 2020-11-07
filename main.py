import json
import constants
from dataparser import DataParser


def get_logs():
    dp = DataParser(constants.log_file_path)
    mentions_by_ticker = dp.mentions_by_ticker()
    # print(mentions_by_ticker)


if __name__ == '__main__':
    get_logs()
