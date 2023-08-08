import collections.abc
import logging

LOG = logging.getLogger(__name__)


def assert_list_dict_equal(input_list, ref_list):
    """
    Assert if All the dicts in both lists are equal (comparing indexes to indexes)

    :param list input_list: input list of dictionnaries
    :param list ref_list: reference list of dictionnaries

    """

    assert len(input_list) == len(ref_list), "List have different sizes"

    for (d1, d2) in zip(input_list, ref_list):
        assert_dict_equal(d1, d2)


def assert_dict_equal(input_dict, dict_ref):
    """
    Assert if Dicts are equal. If not, display the differences

    :param dict input_dict: Input dictionary
    :param dict dict_ref: Reference dictionary

    """

    (is_equal, msg) = compare_dict(input_dict, dict_ref)

    assert is_equal, msg


def assert_dict_subset(input_dict, dict_ref):
    """
    Assert if dict_ref is subset of input_ref. If not, display the differences

    :param dict input_dict: Input dictionary
    :param dict dict_ref: Reference dictionary assumed to be a subset of input dict

    """

    (is_equal, msg) = is_subset(input_dict, dict_ref)

    assert is_equal, msg


def compare_dict(input_dict, dict_ref, msg=None, prefix=None):
    """
    Compare 2 dicts. Will return an error message explaining the differences

    :param dict input_dict: Input dictionary
    :param dict dict_ref: Reference dictionary

    Warning: All other parameters are internal (for recursivity) and must NOT be used

    :return: if dict are equal and error message associated with it
    :rtype: (bool, msg)
    """

    is_equal = True

    if not msg:
        msg = ""

    keys1 = set(input_dict.keys())
    keys2 = set(dict_ref.keys())

    d1_prefix = "input_dict"
    d2_prefix = "dict_ref"
    if prefix:
        d1_prefix += prefix
        d2_prefix += prefix

    common_keys = keys1.intersection(keys2)

    # Keys present in keys1 not present in keys2
    new_keys1 = keys1.difference(keys2)
    if len(new_keys1) != 0:
        is_equal = False
        msg += "Keys exclusive to {}:\n".format(d1_prefix)
        for key in new_keys1:
            msg += "\t{}[{}] = {}\n".format(d1_prefix, key, input_dict[key])

    # Keys present in keys2 not present in keys1
    new_keys2 = keys2.difference(keys1)
    if len(new_keys2) != 0:
        is_equal = False
        msg += "Keys exclusive to {}:\n".format(d2_prefix)
        for key in new_keys2:
            msg += "\t{}[{}] = {}\n".format(d2_prefix, key, dict_ref[key])

    # Common keys
    for key in common_keys:
        value1 = input_dict[key]
        value2 = dict_ref[key]
        if isinstance(value1, dict):
            new_prefix = prefix if prefix else ""
            new_prefix += "[{}]".format(key)
            (value_equal, tmp_msg) = compare_dict(value1, value2, prefix=new_prefix)
            if not value_equal:
                is_equal = False
            msg += tmp_msg
        elif value1 != value2:
            is_equal = False
            msg += "Difference for:\n"
            msg += "\t{}[{}] = {}\n".format(d1_prefix, key, value1)
            msg += "\t{}[{}] = {}\n".format(d2_prefix, key, value2)

    return is_equal, msg

def is_subset(input_dict, dict_ref, msg=None, prefix=None):
    is_subset = True

    if not msg:
        msg = ""

    keys1 = set(input_dict.keys())
    keys2 = set(dict_ref.keys())

    d1_prefix = "input_dict"
    d2_prefix = "dict_ref"
    if prefix:
        d1_prefix += prefix
        d2_prefix += prefix

    common_keys = keys1.intersection(keys2)

    # Keys present in keys2 not present in keys1
    new_keys2 = keys2.difference(keys1)
    if len(new_keys2) != 0:
        is_subset = False
        msg += "Keys exclusive to {}:\n".format(d2_prefix)
        for key in new_keys2:
            msg += "\t{}[{}] = {}\n".format(d2_prefix, key, dict_ref[key])

    # Common keys
    for key in common_keys:
        value1 = input_dict[key]
        value2 = dict_ref[key]
        if isinstance(value1, dict):
            new_prefix = prefix if prefix else ""
            new_prefix += "[{}]".format(key)
            (value_equal, tmp_msg) = compare_dict(value1, value2, prefix=new_prefix)
            if not value_equal:
                is_subset = False
            msg += tmp_msg
        elif value1 != value2:
            is_subset = False
            msg += "Difference for:\n"
            msg += "\t{}[{}] = {}\n".format(d1_prefix, key, value1)
            msg += "\t{}[{}] = {}\n".format(d2_prefix, key, value2)

    return is_subset, msg

def update_dict(d, u):
    """
    Recursively merge or update dict-like objects.
    i.e, change a value to a key that already exists or
    add a (key, value) that did not previously existed

    source: https://stackoverflow.com/questions/3232943/update-value-of-a-nested-dictionary-of-varying-depth

    :param dict d: Original dictionnary
    :param dict u: dictionnary of updates to apply to 'd'
    :return dict d: Return updated version of 'd'
    """

    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = update_dict(d.get(k, {}), v)
        else:
            d[k] = v
    return d


def init_log(level="INFO", extra_config=None):
    """

    :param str level: log level for standard output (ERROR, WARNING, INFO, DEBUG)
    :param dict extra_config: [optional] Set of extra properties to be added to the dict_config for logging
    :return:
    :rtype:
    """

    import logging.config

    log_config = {
        "version": 1,
        "formatters":
            {
                "form01":
                    {
                        "format": "%(asctime)s %(levelname)-8s %(message)s",
                        "datefmt": "%H:%M:%S"
                    },
            },
        "handlers":
            {
                "console":
                    {
                        "class": "logging.StreamHandler",
                        "formatter": "form01",
                        "level": level,
                        "stream": "ext://sys.stdout",
                    },
            },
        "loggers":
            {
                "":
                    {
                        "level": "NOTSET",
                        "handlers": ["console"],
                    },
            },
        "disable_existing_loggers": False,
    }

    if extra_config is not None:
        log_config = update_dict(log_config, extra_config)

    logging.config.dictConfig(log_config)
