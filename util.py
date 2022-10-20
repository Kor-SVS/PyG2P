from typing import Union


def is_empty_string(string: Union[str, None]):
    if string == None:
        return True

    string = string.strip()

    if len(string) == 0:
        return True

    return False
