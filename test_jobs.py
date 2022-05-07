from requests import get, post, delete

print('Получаем одну работу')
print(get('http://localhost:5000/api/v2/jobs/1').json())

print('Получаем несущестующую работу')
print(get('http://localhost:5000/api/v2/jobs/999').json())

print('Получаем все работы')
print(get('http://localhost:5000/api/v2/jobs').json())

print('Добавляем новую работу')
new_job = post('http://localhost:5000/api/v2/jobs', json={
    'job': 'new job',
    'work_size': 10,
    'team_leader': 1,
    'collaborators': '1, 2'
}).json()
job_id = str(new_job['job_id'])
print(new_job)

print('Проверяем добавленную работу')
print(get('http://localhost:5000/api/v2/jobs/' + job_id).json())

print('Удаляем добавленную работу')
print(delete('http://localhost:5000/api/v2/jobs/' + job_id).json())

print('Добавляем новую работу без обязательных полей')
print(post('http://localhost:5000/api/v2/jobs', json={
    'job': 'new job',
    'collaborators': '1, 2'
}).json())

print('Пробуем удалить работу без ID')
print(delete('http://localhost:5000/api/v2/jobs').json())

print('Пробуем удалить несущестующую работу')
print(delete('http://localhost:5000/api/v2/jobs/999').json())

# Получаем одну работу
# {'job': {'collaborators': '2, 3', 'end_date': None, 'id': 1, 'is_finished': False, 'job': 'new job', 'start_date': None, 'team_leader': 1, 'work_size': 5}}
# Получаем несущестующую работу
# {'message': 'Job 999 not found'}
# Получаем все работы
# {'jobs': [{'collaborators': '2, 3', 'end_date': None, 'id': 1, 'is_finished': False, 'job': 'new job', 'start_date': None, 'user': {'name': 'Ridley'}, 'work_size': 5}, {'co
# llaborators': '1, 3', 'end_date': None, 'id': 2, 'is_finished': False, 'job': 'new job 2', 'start_date': None, 'user': {'name': 'Mark'}, 'work_size': 10}]}
# Добавляем новую работу
# {'job_id': 3, 'success': 'OK'}
# Проверяем добавленную работу
# {'job': {'collaborators': '1, 2', 'end_date': None, 'id': 3, 'is_finished': False, 'job': 'new job', 'start_date': None, 'team_leader': 1, 'work_size': 10}}
# Удаляем добавленную работу
# {'success': 'OK'}
# Добавляем новую работу без обязательных полей
# {'message': {'team_leader': 'Missing required parameter in the JSON body or the post body or the query string'}}
# Пробуем удалить работу без ID
# {'message': 'The method is not allowed for the requested URL.'}
# Пробуем удалить несущестующую работу
# {'message': 'Job 999 not found'}
