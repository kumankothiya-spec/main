# tests/conftest.py
import pytest

@pytest.fixture
def sample_data():
    return {"name": "Kuman", "role": "QA Lead"}

# tests/test_fixtures.py
def test_sample_data(sample_data):
    assert sample_data["name"] == "Kuman"
    assert "role" in sample_data

def test_pass():
    assert 10==10