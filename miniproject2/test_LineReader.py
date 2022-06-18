from LineReader import *
from unittest.mock import MagicMock
from pytest import raises
import pytest

@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="first line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open

def test_returnsCorrectString(monkeypatch, mock_open):    
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    result = readFromFile("myFile.txt")
    mock_open.assert_called_once_with("myFile.txt", "r")
    assert result == "first line"

def test_throwsExceptionWithBadFile(monkeypatch, mock_open):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="first line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with raises(Exception):
        result = readFromFile("blah")