from requests import get, post, delete

print('Получаем одного ползователя')
print(get('http://localhost:5000/api/v2/users/1').json())

print('Пробуем получить несущестующего пользователя')
print(get('http://localhost:5000/api/v2/users/999').json())

print('Получаем всех опльзователей')
print(get('http://localhost:5000/api/v2/users').json())

print('Создание пользователя')
new_user = post('http://localhost:5000/api/v2/users', json={
    'name': 'testUser',
    'email': 'test_user@mars.org',
    'about': 'about test user',
    'password': 'testpass'
}).json()
user_id = str(new_user['user_id'])
print(new_user)

print('Проверяем наличие добавленного пользователя')
print(get('http://localhost:5000/api/v2/users/' + user_id).json())

print('Пробуем создать пользователя без обязательных атрибутов')
print(post('http://localhost:5000/api/v2/users', json={
    'name': 'user wo attributes',
}).json())

print('Удаляем ранее созданного пользователя')
print(delete('http://localhost:5000/api/v2/users/' + user_id).json())

print('Пробуем удалить несущестующего пользователя')
print(delete('http://localhost:5000/api/v2/users/999').json())

print('Пробуем удалить пользователя без ID')
print(delete('http://localhost:5000/api/v2/users').json())

# Получаем одного ползователя
# {'user': {'about': None, 'created_date': '2022-05-07 20:16:26', 'email': 'cap@mars.org', 'id': 1, 'name': 'Ridley'}}
# Пробуем получить несущестующего пользователя
# {'message': 'User 999 not found'}
# Получаем всех опльзователей
# {'users': [{'about': None, 'created_date': '2022-05-07 20:16:26', 'email': 'cap@mars.org', 'id': 1, 'name': 'Ridley'}, {'about': None, 'created_date': '2022-05-07 20:16:26'
# , 'email': 'mark_wanty@mars.org', 'id': 2, 'name': 'Mark'}]}
# Создание пользователя
# {'success': 'OK', 'user_id': 3}
# Проверяем наличие добавленного пользователя
# {'user': {'about': 'about test user', 'created_date': '2022-05-07 20:16:39', 'email': 'test_user@mars.org', 'id': 3, 'name': 'testUser'}}
# Пробуем создать пользователя без обязательных атрибутов
# {'message': {'about': 'Missing required parameter in the JSON body or the post body or the query string'}}
# Удаляем ранее созданного пользователя
# {'success': 'OK'}
# Пробуем удалить несущестующего пользователя
# {'message': 'User 999 not found'}
# Пробуем удалить пользователя без ID
# {'message': 'The method is not allowed for the requested URL.'}


