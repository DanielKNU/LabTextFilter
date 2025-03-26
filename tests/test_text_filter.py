import pytest
import os
from src.text_filter import read_file, filter_and_write

@pytest.fixture
def temp_files(tmp_path):
    """Create temporary input and output files."""
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.txt"
    input_file.write_text("Hello world\nThis is a test\nGoodbye world\n", encoding='utf-8')
    return input_file, output_file

def test_read_file(temp_files):
    input_file, _ = temp_files
    lines = read_file(input_file)
    assert lines == ["Hello world\n", "This is a test\n", "Goodbye world\n"]

@pytest.mark.parametrize("keyword,expected_lines", [
    ("world", ["Hello world\n", "Goodbye world\n"]),
    ("test", ["This is a test\n"]),
    ("none", []),
])
def test_filter_and_write(temp_files, keyword, expected_lines):
    input_file, output_file = temp_files
    filter_and_write(input_file, output_file, keyword)
    with open(output_file, 'r', encoding='utf-8') as f:
        result = f.readlines()
    assert result == expected_lines

if __name__ == "__main__":
    input_path = "input.txt"
    output_path = "filtered.txt"
    keyword = "world"
    filter_and_write(input_path, output_path, keyword)