# tests/test_strings.py

def reverse_string(s: str) -> str:
    return s[::-1]

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"