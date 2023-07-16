import logging

LOG = logging.getLogger(__name__)


def check_value(parameter_name, value, validValues=None):
    if validValues is not None:
        if value not in validValues:
            raise ValueError("%s '%s' is not supported. Use: '%s'" % (parameter_name, value, "', '".join(validValues)))
    else:
        if not isinstance(value, (int, float, str)):
            raise ValueError(f"{parameter_name}: value type ({type(value)}) not supported for xml element.")
