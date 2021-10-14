import pytest
import data_store


def test_load_data_returns_empty_list_when_out_of_memory(mocker):
    # Arrange
    mocker.patch("json.load", side_effect=MemoryError("out of memory"))

    # Act
    data = data_store.load_data()

    # Assert
    assert data == []


def test_load_data_returns_exception_when_file_is_missing(mocker):
    # Arrange
    mocker.patch("json.load", side_effect=FileNotFoundError("file not found"))

    # Act
    with pytest.raises(FileNotFoundError) as exc_info:
        data = data_store.load_data()

    # Assert
    assert str(exc_info.value) == "file not found"
