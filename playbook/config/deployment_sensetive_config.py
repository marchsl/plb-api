from playbook.config.general_config_constants import OtherConstants


class DevelopmentSensitiveConfigConstants(OtherConstants, ):
    DEBUG_MODE = True
    DEVELOPER_MODE = True
    IGNORE_PERMISSION = False
    IGNORE_JWT_TOKEN = False


class StagingSensitiveConfigConstants(OtherConstants, ):
    DEBUG_MODE = False
    DEVELOPER_MODE = False
    IGNORE_PERMISSION = False
    IGNORE_JWT_TOKEN = False


class LiveSensitiveConfigConstants(OtherConstants, ):
    DEBUG_MODE = False
    DEVELOPER_MODE = False
    IGNORE_PERMISSION = False
    IGNORE_JWT_TOKEN = False
