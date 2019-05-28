""" Simple program that outputs the vowels of an input file.
This is the buggy version that does not complain about digits and crashes
when the input contains punctuation.

The idea is that you the programmer have MISSED these bugs in your program.
(That's what you get for being human.)"""

import logging
from argparse import ArgumentParser
from pathlib import Path
from string import punctuation

logger = logging.getLogger(__name__)


def main(args_list=None):
    """
    Takes an input file and creates a new out.txt file where it prints
    the vowels for each line. Digits output errors, and for demonstration
    purposes punctuation causes exceptions at a low level which should
    be turned into more error messages without crashing the program.
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
            with open(path.stem + "-out.txt", "w") as output:
                for line in inputfile:
                    output.write(process_line(line) + "\n")
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


if __name__ == '__main__':
    main()
