import pytest
import os
from file_handler import CustomFile, ExtendedFile


@pytest.fixture
def txt_file(tmp_path):
    """
    Create a temporary sample text file with known content.
    """
    file = tmp_path / "first.txt"
    file.write_text("Hello\nWorld\n")
    return str(file)


@pytest.fixture
def txt_file2(tmp_path):
    """
    Create another temporary sample text file with known content.
    """
    file = tmp_path / "second.txt"
    file.write_text("Another\nFile\n")
    return str(file)


@pytest.fixture
def txt_file3(tmp_path):
    """
    Create third temporary sample text file with known content.
    """
    file = tmp_path / "third.txt"
    file.write_text("Third\nFile\n")
    return str(file)


def test_read_file(txt_file):
    """
    Test that CustomFile correctly reads lines from a text file.
    """
    cf = CustomFile(txt_file)
    lines = list(cf.read_file())
    assert lines == ["Hello", "World"]


def test_invalid_extension(tmp_path):
    """
    Test that a ValueError is raised when using a non .txt file.
    """
    file = tmp_path / "invalid.pdf"
    with pytest.raises(ValueError):
        CustomFile(str(file))


def test_nonexistent_file():
    """
    Test that a FileNotFoundError is raised when file does not exist.
    """
    with pytest.raises(FileNotFoundError):
        CustomFile("nonexistent.txt")


def test_add_operator(txt_file, txt_file2, tmp_path):
    """
    Test that two CustomFiles can be added together and written to a new file.
    """
    cf1 = CustomFile(txt_file)
    cf2 = CustomFile(txt_file2)
    temp_output = tmp_path / "temp_combined.txt"
    combined = cf1 + cf2
    os.replace("combined_files.txt", temp_output)
    combined = CustomFile(str(temp_output))
    assert os.path.exists(combined.filepath)
    content = list(combined.read_file())
    assert "Hello" in content[0]
    assert "File" in content[-1]


def test_str_decorator(capsys, txt_file):
    """
    Test that the __str__ method applies ANSI color formatting (magenta).
    """
    cf = CustomFile(txt_file)
    print(cf)
    output = capsys.readouterr().out
    assert "CustomFile" in output
    assert "\033[95m" in output


def test_concat_many_files(txt_file, txt_file2, txt_file3, tmp_path):
    """
    Test that multiple AdvancedFile instances can be concatenated correctly.
    """
    ef1 = ExtendedFile(txt_file)
    ef2 = ExtendedFile(txt_file2)
    ef3 = ExtendedFile(txt_file3)
    temp_output = tmp_path / "temp_combined_many.txt"
    combined = ExtendedFile.concat_many_files(
        ef1, ef2, ef3, output_path=str(temp_output)
    )
    assert os.path.exists(combined.filepath)
    content = list(combined.read_file())
    assert "Hello" in content[0]
    assert "File" in content[-1]


def test_concat_invalid_type(txt_file):
    """
    Test that concat_many_files raises TypeError when passed a non-CustomFile.
    """
    ef = ExtendedFile(txt_file)
    with pytest.raises(TypeError):
        ExtendedFile.concat_many_files(ef, "a string")
