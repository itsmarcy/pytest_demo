import logging
import pytest

from pytest_demo.demo import process_file, process_line, PunctuationFound


@pytest.fixture
def create_directory(tmp_path):
    p = tmp_path / "input_files"
    p.mkdir()
    return p


@pytest.fixture
def good_input_file(create_directory):
    p = create_directory / "input1.txt"
    p.write_text(
        """
        this file will pass
        """
    )
    return p


@pytest.fixture
def digit_input_file(create_directory):
    p = create_directory / "input1.txt"
    p.write_text(
        """
        this file will produce 1 error
        """
    )
    return p


@pytest.fixture
def punctuation_input_file(create_directory):
    p = create_directory / "input1.txt"
    p.write_text(
        """
        !! this should fail.
        """
    )
    return p


def test_process_file(good_input_file, tmpdir):
    result = process_file(good_input_file)
    file_name = str(good_input_file.stem) + "-out.txt"
    output_file = good_input_file.parent / file_name
    assert output_file.exists()
    assert result == 0


def test_process_file_filenotfound(caplog):
    process_file('fake/file.txt')
    for record in caplog.records:
        assert record.levelname == "ERROR"
    assert "File not found." in caplog.text


def test_process_file_digit_error(caplog, digit_input_file):
    process_file(digit_input_file)
    for record in caplog.records:
        assert record.levelname == "ERROR"
    assert "Digits found but continuing" in caplog.text


def test_process_file_punctuation(caplog, punctuation_input_file):
    process_file(punctuation_input_file)
    for record in caplog.records:
        assert record.levelname == "ERROR"
    assert "Punctuation found in the file" in caplog.text
    assert "No punctuation permitted in file." in caplog.text
    file_name = str(punctuation_input_file.stem) + "-out.txt"
    output_file = punctuation_input_file.parent / file_name
    assert not output_file.exists()


def test_process_line():
    with pytest.raises(PunctuationFound):
        process_line('line with punctuation!')
