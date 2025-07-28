from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='CQE',
    version='2.0.1',
    packages=['CQE', 'CQE.unit_classifier'],
    # both has to be empty
    package_data={'': ['unit.json', 'unit_models.zip'], },
    url='https://github.com/vivkaz/CQE',
    license='',
    long_description_content_type="text/markdown",
    long_description=long_description,
    author='satyaalmasian and vivian kazakova',
    author_email='satya.almasian@gmail.com',
    description='quantity extractor',
    install_requires=["emoji>=2.14.1",
                      "fuzzywuzzy>=0.18.0",
                      "inflect>=7.5.0",
                      "more-itertools>=10.7.0",
                      "numpy>=2.3.2",
                      "ordered-set>=4.1.0",
                      "protobuf>=6.31.1",
                      "python-levenshtein>=0.27.1",
                      "regex>=2024.11.6",
                      "requests>=2.32.4",
                      "spacy>=3.8.7",
                      "spacy-legacy>=3.0.12",
                      "spacy-transformers>=1.3.9",
                      "torch>=2.7.1",],
)
