import pytest

from chunking import chunk_text


def test_chunk_text_normal():

    text = "ABCDEFGHIJ"

    result = chunk_text(text, 3)

    assert result == ["ABC", "DEF", "GHI", "J"]


def test_chunk_text_larger_chunk_size():

    text = "ABCDEFGHIJ"

    result = chunk_text(text, 20)

    assert result == ["ABCDEFGHIJ"]


def test_chunk_text_zero_size():

    text = "ABCDEFGHIJ"

    with pytest.raises(ValueError):
        chunk_text(text, 0)


def test_chunk_text_negative_size():

    with pytest.raises(ValueError):
        chunk_text("ABCDEFGHIJ", -1)

def test_chunk_text_empty_string():

    result = chunk_text("", 3)

    assert result == []

def test_chunk_text_size_one():

    result = chunk_text("ABC", 1)

    assert result == ["A", "B", "C"]

def test_chunk_text_exact_multiple():

    result = chunk_text("ABCDEF", 3)

    assert result == ["ABC", "DEF"]

@pytest.mark.parametrize(
    "text, chunk_size, expected",
    [
        ("ABC", 1, ["A", "B", "C"]),
        ("ABCDEF", 3, ["ABC", "DEF"]),
        ("ABCDE", 2, ["AB", "CD", "E"]),
        ("ABCDEFG", 4, ["ABCD", "EFG"]),
    ],
)
def test_chunk_text_parametrized(text, chunk_size, expected):
    result = chunk_text(text, chunk_size)

    assert result == expected