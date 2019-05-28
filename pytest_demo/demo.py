""" Simple program that outputs the vowels of an input file"""
import logging
from argparse import ArgumentParser
from pathlib import Path
from string import punctuation

logger = logging.getLogger(__name__)


def main(args_list=None):
    """
    Takes an input file and creates a new out.txt file where it prints
    the vowels of the sentences if there is no punctuation present.
    """
    args = parse_command_line(args_list)
    process_file(args.input_file)


def parse_command_line(args_list=None):
    """
    """
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument(
        "input_file", help="Required input file to process"
    )
    args = parser.parse_args(args_list)
    return args


def process_file(path):
    exit_code = 0
    path = Path(path)
    lines = []
    try:
        with open(path) as inputfile:
            for line in inputfile:
                lines.append(process_line(line))
        with open(path.stem + "-out.txt", "w") as output:
            for line in lines:
                output.write(line + "\n")
    except FileNotFoundError:
        logger.exception("File not found.")
    except PunctuationFound:
        logger.exception("Punctuation found in the file")
    return exit_code


def process_line(line):
    for char in line:
        if char in punctuation:
            raise PunctuationFound("No punctuation permitted in file.")
    return ''.join([v for v in 'aeiou' if v in line])


class PunctuationFound(Exception):
    pass
