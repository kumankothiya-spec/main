import logging

import pytest


def reverse_string(s: str) -> str:
    return s[::-1]

@pytest.mark.smoke
def test_reverse_string():
    logging.info("test_reverse_string -> hello")
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"