from pprint import pprint
from copy import deepcopy


def update(data, service, count):
    """
    Function for update configuration of service
    :param data: dict
    :param service: str
    :param count: int
    :return: dict
    """
    data_copy = deepcopy(data)

    for i in range(count):
        server_pairs = [(sum(data_copy[d].values()), d) for d in data_copy]
        min_server = min(server_pairs)[1]
        data_copy[min_server][service] = data_copy[min_server].get(service, 0) + 1
    return data_copy


def main():
    example_data = {
        'ginger': {
            'django': 2,
            'flask': 3,
        },
        'cucumber': {
            'flask': 1,
        },
    }

    print("Configuration before:")
    pprint(example_data)

    updated_data = update(example_data, 'pylons', 7)

    print("Configuration after:")
    pprint(updated_data)

if __name__ == '__main__':
    main()