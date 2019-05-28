from os import path

from setuptools import find_packages, setup

DESCRIPTION = "Demo showing some pytest functionality."

HERE = path.abspath(path.dirname(__file__))
NAME = "pytest_demo"

TEST_REQUIREMENTS = [
    "pytest",
]

SETUP_REQUIREMENTS = [
    "pytest-runner",
]

try:
    with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
        LONG_DESCRIPTION = f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION


setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=["tests"]),
    tests_require=TEST_REQUIREMENTS,
    setup_requires=SETUP_REQUIREMENTS,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={
        "console_scripts": [
            "pytest_demo=pytest_demo.demo:main",
        ],
    },
)
