
import csv

filename = 'data/sitka_weather_07-2018_simple.csv'

with open(filename) as file:
    reader = csv.reader(file)
    # print(list(reader))
    header_row = next(reader)
    # print(header_row)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    # 从文件中获取最高温度
    highs = []
    for row in reader:
        print(row)