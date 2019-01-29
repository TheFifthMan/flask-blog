from .dev import DevConfig
from .testing import TestingConfig
from .prod import ProdConfig

config = {
    "dev":DevConfig,
    "test":TestingConfig,
    "prod":ProdConfig,
    "default":DevConfig
}
