import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="lt614nstudent",
    version="0.0.1",
    description="Utility library to convert from metric to imperial measures",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://learningtree.com",
    author="Student",
    author_email="student@learningtree.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    packages=find_packages(exclude=("tests",)),
)
