import sender_stand_request

# Функция создания тела запроса
def get_kit_body(name):
    body = sender_stand_request.post_new_kit(name)
    return body

# Функция позитивной проверки

def positive_assert(self):
    kit_body = get_kit_body(self)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == self

# Функция негативной проверки

def negative_assert_code_400(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400

# Тест 1. Допустимое количество символов (1)
def test_create_kit_name_with_one_symbol():
    positive_assert("a")

# Тест 2. Допустимое количество символов (511)
def test_create_kit_name_with_many_symbol():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Количество символов меньше допустимого (0)
def test_create_kit_name_with_empty_body():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

# Тест 4. Количество символов больше допустимого (512)
def test_create_kit_name_with_very_many_symbol():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body)

# Тест 5. Разрешены английские буквы
def test_create_kit_name_with_english_letters():
    positive_assert("QWErty")

# Тест 6. Разрешены русские буквы
def test_create_kit_name_with_russian_letters():
    positive_assert("Мария")

# Тест 7. Разрешены спецсимволы
def test_create_kit_name_with_special_symbol():
    positive_assert("№%@",)

# Тест 8. Разрешены пробелы
def test_create_kit_name_with_space_in_body():
    positive_assert(" Человек и КО ")

# Тест 9. Разрешены цифры
def test_create_kit_name_with_numbers_in_body():
    positive_assert("123")

# Функция передачи пустого тела
def empty_body():
    return {}

# Тест 10. Параметр не передан в запросе
def test_create_kit_name_without_body():
    kit_body = empty_body()
    negative_assert_code_400(kit_body)

# Тест 11. Передан другой тип параметра (число)
def test_create_kit_name_with_another_param():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)



