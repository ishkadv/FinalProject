Автотесты для создания корзины по чек листу:

1	Допустимое количество символов (1):
kit_body = {
"name": "a"
}	
Код ответа — 201
В ответе поле name совпадает с полем name в запросе

2	Допустимое количество символов (511):
kit_body = {
kit_body = {    "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
}	Код ответа — 201
В ответе поле name совпадает с полем name в запросе

3	Количество символов меньше допустимого (0):
kit_body = {
"name": ""
}	Код ответа — 400

4	Количество символов больше допустимого (512):
kit_body = {
kit_body = {  "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
}	Код ответа — 400

5	Разрешены английские буквы:
kit_body = {
"name": "QWErty"
}	Код ответа — 201
В ответе поле name совпадает с полем name в запросе

6	Разрешены русские буквы:
kit_body = {
"name": "Мария"
}	Код ответа — 201
В ответе поле name совпадает с полем name в запросе

7	Разрешены спецсимволы:
kit_body = {
"name": ""№%@","
}	Код ответа — 201
В ответе поле name совпадает с полем name в запросе

8	Разрешены пробелы:
kit_body = {
"name": " Человек и КО "
}	Код ответа — 201
В ответе поле name совпадает с полем name в запросе

9	Разрешены цифры:
kit_body = {
"name": "123"
}	Код ответа — 201
В ответе поле name совпадает с полем name в запросе

10	Параметр не передан в запросе:
kit_body = {
}	Код ответа — 400

11	Передан другой тип параметра (число):
kit_body = {
"name": 123
}	Код ответа — 400

Некоторые тесты вернутся с результатом FAILED. Это соответствует чек-листу.