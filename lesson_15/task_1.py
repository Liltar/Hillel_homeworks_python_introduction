# Во вложении файл csv с данными про аэропорты мира, написать программу которая сможет
#
# вернуть данные по таким параметрам:
#
# --iata_code - код аэропорта, должно вернуть 1 запись по коду аэропорта(всю строку) или вернуть ошибку AirportNotFoundError
# --country - страна, должно вернуть все записи по аэропортам или
# CountryNotFoundError
# --name - значение имени аэропорта, допустимо вхождение строки хотябы
# минимально, т.е. liman должен вернуть строки с такими названиями:
# Ilimanaq Heliport
# Sidi Slimane Airport
# Kilimanjaro International Airport
# West Kilimanjaro Airport
# Limanske Airfield
# Liman Airfield
# ...
# или AirportNotFoundError
#
#
# Только один параметр обязателен, если выбрано несколько - вернуть
# ошибку:
# MultipleOptionsError, если ни одного - NoOptionsFoundError
#
# ** доп. ошибки принимают два аргумента, текст ошибки и входные данные,
#
#    пример:
#
# AirportNotFoundError: ('Airport not found', 'OESD')
# CountryNotFoundError: ('Country not found', 'UGUGU')
#
#   IATA код может быть только 3х буквенным в верхнем регистре, сделать валидацию на него
#
#   или вернуть IATACodeError
import csv
import argparse
import re

class AirportNotFoundError(Exception):
    def __init__(self, message, error_str):
        self.message = 'Airport not found'
        self.error_str = error_str

    def __str__(self):
        return 'Error' + self.message + self.error_str


class CountryNotFoundError(Exception):
    def __init__(self, message, error_str):
        self.message = 'Country not found'
        self.error_str = error_str

    def __str__(self):
        return 'Error' + self.message + self.error_str


class MultipleOptionsError(Exception):
    pass


class NoOptionsFoundError(Exception):
    pass


class AirportFounder:

    def __init__(self, arguments):
        self.args = self.check_arguments(arguments)

    def check_argument(self, arguments):
        arg_dict = [('name', arguments.name),
                    ('country', arguments.country),
                    ('iata_code', arguments.iata_code)]
        result = []

        for args in arg_dict:
            if args[0] is not None:
                result.append(args)

        if len(result) == 1:
            return result
        elif len(result) > 1:
            raise MultipleOptionsError
        elif len(result) == 0:
            raise NoOptionsFoundError

    def find(self):
        with open('airport-codes_csv.csv', 'r', encoding='utf-8') as airport_codes:
            csv_reader = csv.DictReader(airport_codes)
            result = []
            row_header = next(csv_reader)
            target_column = -1
            for index, column_header in enumerate(row_header):
                if column_header == self.args[0][0]:
                    target_column = index
            pattern = r"[\w\s]*{self.args[0][1]}[\w\s]*"
            for row in csv_reader:
                if re.fullmatch(pattern, row[target_column], flags=re.IGNORECASE):
                    result.append(row)

        if len(result) == 0:
            raise Exception('Airport not found')

        for r in result:
            print(r)


parser = argparse.ArgumentParser(description='World Airports')
parser.add_argument('--iata_code')
parser.add_argument('--country')
parser.add_argument('--name')
arguments = parser.parse_args()