import pytest
import os
from main import CustomFile, AdvancedFile


@pytest.fixture
def txt_file(tmp_path):
    file = tmp_path/'sample.txt'
    file.write_text("Hello\nWorld\n")
    return str(file)


@pytest.fixture
def another_txt_file(tmp_path):
    file = tmp_path/'another.txt'
    file.write_text("Another\nFile\n")
    return str(file)


def test_read_file(txt_file):
    cf = CustomFile(txt_file)
    lines = list(cf.read_file())
    assert lines == ["Hello", "World"]


def test_invalid_extension(tmp_path):
    file = tmp_path/'invalid.pdf'
    file.write_text("Should Fail")
    with pytest.raises(ValueError):
        CustomFile(str(file))


def test_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        CustomFile('nonexistent.txt')


def test_add_operator(txt_file, another_txt_file, tmp_path):
    cf1 = CustomFile(txt_file)
    cf2 = CustomFile(another_txt_file)

    # Create a temporary file path inside tmp_path
    output_path = tmp_path / "combined.txt"

    # Use __add__ manually and pass the temp path
    combined = cf1.__add__(cf2, str(output_path))

    assert os.path.exists(combined.filepath)

    content = list(combined.read_file())
    assert "Hello" in content[0]
    assert "File" in content[-1]


def test_str_decorator(capsys, txt_file):
    cf = CustomFile(txt_file)
    print(cf)
    output = capsys.readouterr().out
    assert "CustomFile" in output
    assert '\033[95m' in output


def test_concat_many_files(txt_file, another_txt_file):
    cf1 = AdvancedFile(txt_file)
    cf2 = AdvancedFile(another_txt_file)
    combined = cf1 + cf2
    assert os.path.exists(combined.filepath)
    content = list(combined.read_file())
    assert "Hello" in content[0]
    assert "File" in content[-1]


def test_concat_invalid_type(txt_file):
    cf = CustomFile(txt_file)
    with pytest.raises(TypeError):
        AdvancedFile.concat_many_files(cf, "a string")
