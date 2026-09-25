import pytest
from unittest.mock import patch

from document_service import get_document_title


@pytest.fixture
def fake_document():

    return {
        "id": "DOC-123",
        "title": "Mocked Document",
        "status": "active"
    }

@pytest.fixture
def another_document():
    return {
        "id": "DOC-456",
        "title": "Another Document"
    }

def test_get_document_title(fake_document):

    with patch(
        "document_service.fetch_document",
        return_value=fake_document
    ) as mock_fetch:

        result = get_document_title("DOC-123")

    assert result == "Mocked Document"

    mock_fetch.assert_called_once_with("DOC-123")

def test_get_document_title_document_not_found(mocker):
    mock_fetch = mocker.patch("document_service.fetch_document")

    mock_fetch.side_effect = ValueError("Document not found")

    with pytest.raises(ValueError, match="Document not found"):
        get_document_title("DOC-123")

def test_get_another_document_title(another_document):
    with patch(
        "document_service.fetch_document",
        return_value=another_document
    ):
        result = get_document_title("DOC-456")

    assert result == "Another Document"