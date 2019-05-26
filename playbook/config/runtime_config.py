import os

from playbook.config.deployment_sensetive_config import LiveSensitiveConfigConstants, StagingSensitiveConfigConstants, \
    DevelopmentSensitiveConfigConstants


class DefaultRuntimeConfig:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # routing config constants
    APP_FQDN = 'localhost'
    HOST_IP = '127.0.0.1'
    PROTOCOL = 'http://'
    API_PREFIX = 'api/'
    API_VERSION = 'v1/'
    API_ROUTE = API_PREFIX + API_VERSION

    INTERNAL_PORT = '8000'
    INTERNAL_ADDRESS = PROTOCOL + '{}:{}/'.format(APP_FQDN, INTERNAL_PORT)
    INTERNAL_API_ADDRESS = INTERNAL_ADDRESS + API_ROUTE
    INTERNAL_IP_ADDRESS = PROTOCOL + '{}:{}/'.format(HOST_IP, INTERNAL_PORT)
    INTERNAL_IP_API_ADDRESS = INTERNAL_IP_ADDRESS + API_ROUTE

    EXTERNAL_ADDRESS = PROTOCOL + APP_FQDN + '/'
    EXTERNAL_API_ADDRESS = EXTERNAL_ADDRESS + API_ROUTE
    EXTERNAL_IP_ADDRESS = PROTOCOL + HOST_IP + '/'
    EXTERNAL_IP_API_ADDRESS = EXTERNAL_IP_ADDRESS + API_ROUTE

    # APP Secret key
    APP_SECRET_KEY = None

    # data base config constants
    DB_SCHEMA = None
    DB_TEST_SCHEMA = None
    DB_USERNAME = None
    DB_PASSWORD = None
    DB_URL = None
    DB_PORT = None


class LocalRuntimeConfig(DefaultRuntimeConfig, DevelopmentSensitiveConfigConstants):
    PROTOCOL = ''
    API_PREFIX = ''
    API_VERSION = ''
    API_ROUTE = API_PREFIX + API_VERSION

    APP_SECRET_KEY = ''

    DB_SCHEMA = ''
    DB_TEST_SCHEMA = ''
    DB_USERNAME = ''
    DB_PASSWORD = ''
    DB_URL = '127.0.0.1'
    DB_PORT = '3306'


class StagingRuntimeConfig(DefaultRuntimeConfig, StagingSensitiveConfigConstants):
    PROTOCOL = ''
    API_PREFIX = ''
    API_VERSION = ''
    API_ROUTE = API_PREFIX + API_VERSION

    APP_SECRET_KEY = ''

    DB_SCHEMA = ''
    DB_TEST_SCHEMA = ''
    DB_USERNAME = ''
    DB_PASSWORD = ''
    DB_URL = '127.0.0.1'
    DB_PORT = '3306'


class LiveRuntimeConfig(DefaultRuntimeConfig, LiveSensitiveConfigConstants):
    PROTOCOL = ''
    API_PREFIX = ''
    API_VERSION = ''
    API_ROUTE = API_PREFIX + API_VERSION

    APP_SECRET_KEY = ''

    DB_SCHEMA = ''
    DB_TEST_SCHEMA = ''
    DB_USERNAME = ''
    DB_PASSWORD = ''
    DB_URL = '127.0.0.1'
    DB_PORT = '3306'


class RuntimeConfig(LocalRuntimeConfig):
    pass
