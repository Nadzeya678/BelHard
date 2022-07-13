#Номера уведомлений
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# vehicle_num = input('Введите номер машины:')
# url = list('https://ozerco.by/js/prif.html', 'http://rudolf.by/transport-info/', 'http://bmat.by/cgi-bin/checknew.cgi')
# for elem in url:
#     r = requests.get(url)
# if vehicle_num in url:
#  с озерца выгрузить: 1.Номер уведомления	2.Регистрационный номер уведомления	3.Разрешение на временное хранение	4. Номер предшествующего свидетельства
# или хотя бы одно какое-то...
# я вообще подумала, что отлично можно и одним сайтом обойтись)))
#
# import pandas as pd
# vehicle_num = input('Введите номер машины:')
# url1 = pd.read_html('https://ozerco.by/js/prif.html', header=0, parse_data=['Транспортное средство, прицеп'])
# url2 = pd.read_html('http://rudolf.by/transport-info/', header=0, parse_data=['№ Автотранспорта'])
# url3 = pd.read_html('http://bmat.by/cgi-bin/checknew.cgi', header=0, parse_data=['Гос. номер'])
# ls1 = [url1, url2, url3]
# for elem in ls1:
#     r = requests.get(url,'Транспортное средство, прицеп')
# if vehicle_num in r:
#         with open('test.html', 'w') as output_file:
#        ????     output_file.write(r.text.encode('????'))

import requests
response = requests.get('https://ya.ru')  # get-запрос
print(response.text)  # вывод содержимого страницы
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('http://httpbin.org/get', params=payload)  # запрос с параметрами
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url, headers=headers)  # запрос с определенными html заголовками