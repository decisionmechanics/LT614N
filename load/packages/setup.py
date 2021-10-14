import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    # PyPI name
    name="awfulawfulpackage",
    version="0.0.1",
    description="An awful, awful package",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/decisionmechanics/awfulawfulpackage",
    author="Andrew Tait",
    author_email="Andrew.Tait@decisionmechanics.com",
    license="MIT",
    # Add metadata
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
    ],
    # Keeping the list up-to-date is a burden in large packages
    packages=find_packages(exclude=["tests*"]),
    # Include JSON files in package
    include_package_data=True,
    package_data={"": ["data/*.json"]},
    # Third-party dependencies
    install_requires=["numpy >= 1.21.2", 'importlib; python_version == "3.0"'],
    # Create a script so we can call "awfulawfulpackage" directly
    entry_points={
        "console_scripts": [
            "awfulawfulpackage=awfulawfulpackage.__main__:main",
        ]
    },
)
