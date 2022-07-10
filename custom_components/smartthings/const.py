"""Constants used by the SmartThings component and platforms."""
from datetime import timedelta
import re

from homeassistant.const import Platform

DOMAIN = "smartthings"

APP_OAUTH_CLIENT_NAME = "Home Assistant"
APP_OAUTH_SCOPES = ["r:devices:*"]
APP_NAME_PREFIX = "homeassistant."

CONF_APP_ID = "app_id"
CONF_CLOUDHOOK_URL = "cloudhook_url"
CONF_INSTALLED_APP_ID = "installed_app_id"
CONF_INSTANCE_ID = "instance_id"
CONF_LOCATION_ID = "location_id"
CONF_REFRESH_TOKEN = "refresh_token"

DATA_MANAGER = "manager"
DATA_BROKERS = "brokers"
EVENT_BUTTON = "smartthings.button"

SIGNAL_SMARTTHINGS_UPDATE = "smartthings_update"
SIGNAL_SMARTAPP_PREFIX = "smartthings_smartap_"

SETTINGS_INSTANCE_ID = "hassInstanceId"

SUBSCRIPTION_WARNING_LIMIT = 40

STORAGE_KEY = DOMAIN
STORAGE_VERSION = 1

# Ordered 'specific to least-specific platform' in order for capabilities
# to be drawn-down and represented by the most appropriate platform.
PLATFORMS = [
    Platform.CLIMATE,
    Platform.FAN,
    Platform.LIGHT,
    Platform.LOCK,
    Platform.COVER,
    Platform.SWITCH,
    Platform.BINARY_SENSOR,
    Platform.SENSOR,
    Platform.SCENE,
]

IGNORED_CAPABILITIES = [
    "execute",
    "healthCheck",
    "ocf",
]

TOKEN_REFRESH_INTERVAL = timedelta(days=14)

VAL_UID = "^(?:([0-9a-fA-F]{32})|([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}))$"
VAL_UID_MATCHER = re.compile(VAL_UID)

SUPPORT_AC_OPTIONAL_MODE    = 0b01_0000_0000_0000
SUPPORT_AUTO_CLEANING_MODE  = 0b10_0000_0000_0000

ATTR_AC_OPTIONAL_MODE = "ac_optional_mode"
ATTR_AUTO_CLEANING_MODE = "auto_cleaning_mode"

SERVICE_SET_AC_OPTIONAL_MODE = "set_ac_optional_mode"
SERVICE_SET_AUTO_CLEANING_MODE = "set_auto_cleaning_mode"

AC_OPTIONAL_MODES = ["off","sleep","windFree","windFreeSleep","quiet","speed","smart"]
AUTO_CLEANING_MODES = ["on", "speedClean", "quietClean", "off"]

ATTRIBUTE_FAN_OSCILLATION_MODE = "fanOscillationMode"
ATTRIBUTE_AC_OPTIONAL_MODE = "acOptionalMode"
ATTRIBUTE_SUPPORTED_AC_OPTIONAL_MODE = "supportedAcOptionalMode"
ATTRIBUTE_AUTO_CLEANING_MODE = "autoCleaningMode"

CAPABILITY_FAN_OSCILLATION_MODE = "fanOscillationMode"
CAPABILITY_AC_OPTIONAL_MODE = "custom.airConditionerOptionalMode"
CAPABILITY_AUTO_CLEANING_MODE = "custom.autoCleaningMode"

COMMAND_FAN_OSCILLATION_MODE = "setFanOscillationMode"
COMMAND_AC_OPTIONAL_MODE = "setAcOptionalMode"
COMMAND_AUTO_CLEANING_MODE = "setAutoCleaningMode"
