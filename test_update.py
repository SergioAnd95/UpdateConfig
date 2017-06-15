import itertools
import pytest
import main


def test_update_equal_loaded_services():

    config = {
        'ginger': {
            'flask': 3,
        },
        'cucumber': {
            'flask': 3,
        },
    }

    config = main.update(config, 'django', 3)
    assert config == {
        'ginger': {
            'flask': 3,
            'django': 1,
        },
        'cucumber': {
            'flask': 3,
            'django': 2,
        },
    }


def test_update_same_service():
    config = {
        'ginger': {
            'django': 2,
            'flask': 3,
        },
        'cucumber': {
            'flask': 1,
        },
    }

    config = main.update(config, 'django', 3)
    assert config == {
        'ginger': {
            'django': 2,
            'flask': 3,
        },
        'cucumber': {
            'flask': 1,
            'django': 3,
        },
    }



def test_update():
    config = {
        'ginger': {
            'django': 2,
            'flask': 3,
        },
        'cucumber': {
            'flask': 1,
        },
    }

    config = main.update(config, 'pylons', 7)
    assert config == {
        'ginger': {
            'django': 2,
            'flask': 3,
            'pylons': 1,
        },
        'cucumber': {
            'flask': 1,
            'pylons': 6,
        },
    }


def test_initial():
    config = {
        'ginger': {},
        'cucumber': {},
    }

    config = main.update(config, 'flask', 3)
    config = main.update(config, 'django', 3)

    assert sum(config['ginger'].values()) == sum(config['cucumber'].values())
    assert sum(sum(x.values()) for x in config.values()) == 3+3


@pytest.mark.xfail(reason="Advanced test. Optional to implement")
def test_predictable_config():
    permutations = []
    services = [
        ('flask', 7),
        ('django', 13),
        ('pylons', 17)
    ]

    for permutation in itertools.permutations(services):
        config = {
            'ginger': {},
            'cucumber': {},
        }
        for svc, num in permutation:
            main.update(config, svc, num)
        assert sum(sum(x.values()) for x in config.values()) == 7+13+17
        permutations.append(config)

    assert all(p == permutations[0] for p in permutations[1:])