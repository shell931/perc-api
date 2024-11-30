# loaders = [EnvLoader()]

from dotenv import load_dotenv
import os
from grift import BaseConfig, EnvLoader, ConfigProperty
from schematics.types import StringType

load_dotenv()
loaders = [EnvLoader()]

class AppConfig(BaseConfig):
    USER_API_URL = ConfigProperty(property_type=StringType(), exclude_from_varz=True)

settings = AppConfig(loaders)