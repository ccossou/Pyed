import logging

LOG = logging.getLogger(__name__)


def check_value(parameter_name, value, valid_values=None):
    if valid_values is not None:
        if value not in valid_values:
            raise ValueError(f"{parameter_name} '{value}' is not supported. Use: {valid_values}")
    else:
        if not isinstance(value, (int, float, str)):
            raise ValueError(f"{parameter_name}: value type ({type(value)}) not supported for xml element.")
