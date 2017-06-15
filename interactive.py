from main import update
from termcolor import colored

def check_not_null(value):
    if not value:
        raise ValueError('this field is required')

config = {
        'ginger': {
            'django': 2,
            'flask': 3,
        },
        'cucumber': {
            'flask': 1,
        },
    }

print('Базовая конфигурация', config)
while True:
    command = input(
        """
        Введите одну из следующих команд:
        u- обновить конфигурацию
        exit- выйти
        """
    )

    if command == 'u':
        try:
            service_name = check_not_null(input('Введите название сервиса: '))
        except ValueError:
            print(colored('\nОшибка: это поле обязательно к заполнению\n', 'red'))
            continue

        try:
            count = int(input('Введите количество процесов: '))
        except ValueError:
            print(colored('\nОшибка: это поле должно быть числом\n', 'red'))
            continue

        config = update(config, service_name, int(count))
        print('Новая конфигурация:\n', config)
    elif command == 'exit':
        break
    else:
        print(colored('\nОшибка: данной команды не существует!!!\n', 'red'))