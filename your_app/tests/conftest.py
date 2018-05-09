import pytest

from your_app.app import create_app


@pytest.yield_fixture(scope='session')
def app():
    """
    Setup our flask test app, this only gets executed once per test
    because of the session scope.


    :return: Flask app
    """
    params = {
        'DEBUG': False,
        'TESTING': True,
        'SERVER_NAME': 'test.com:5000'
    }

    _app = create_app(settings_override=params)

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    """
    you can define pytest fixtures with the function scope
    if you want them to be initialized for every test function

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()


@pytest.fixture(scope='module')
def cur():
    """
    you can define pytest fixtures with the module scope
    if you want them to be initialized for every test module

    :return: pass
    """
    pass


@pytest.fixture
def signed_up_user():
    """
        pytest fixture can be a good way to share data across
        your test suites using dependency injection

        see link here: https://docs.pytest.org/en/latest/fixture.html#fixture

        but you can decide to use pytest-datadir or pytest-datafiles

    :return: a dictionary as signed user
    """
    return dict(name='aaron', email='abiliyok@gmail.com')
