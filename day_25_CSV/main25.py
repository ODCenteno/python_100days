import csv
import pandas

# with open('./weather_data.csv', mode='r', encoding='utf-8') as data_file:
#     data = csv.reader(data_file)
#     data_rows = []
#     for row in data:
#         data_rows.append(row)
#     data_rows.pop(0)
#     temperures = []
#     for temp in data_rows:
#         temperures.append(int(temp[1]))
#     print(temperures)

# data = pandas.read_csv('./weather_data.csv')
# print(data)
# print(data['temp'])
#
# list_temp = data['temp'].to_list()
# sum_temp = sum([x for x in list_temp])
# print(sum_temp)
# avg_temp = sum_temp/len(list_temp)
# print(avg_temp)
#
# print(f'Highest temperature: {data["temp"].max()}')
#
# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == 'Monday']
# print(monday.condition)
#
#
# data = data.assign(temp_f=lambda x: x['temp']*9/5+32)
# print(data)
# data.to_csv('new_temp.csv')

# ###### SQUIRRELS

SD = pandas.read_csv('./Squirrels/Squirrel_Data.csv')
print(SD['Primary Fur Color'])
n_gray = 0
n_cinna = 0
n_black = 0
for color in SD['Primary Fur Color']:
    if color == 'Cinnamon':
        n_cinna += 1
    elif color == 'Gray':
        n_gray += 1
    elif color == 'Black':
        n_black += 1
print(n_black, n_cinna, n_gray)

data_dict = {
    'Fur Color': ['Black', 'Red', 'Gray'],
    'Count': [n_black, n_cinna, n_gray]
}
df = pandas.DataFrame(data_dict)
df.to_csv('./Squirrels/squirrel_count.csv')

# print(titles)