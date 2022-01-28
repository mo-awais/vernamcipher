from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="vernamcipher",
    version="0.1.2",
    author="Mohammed Awais",
    author_email="me@mohammedawais.me",
    description="A Python implementation of truly-random Vernam Cipher encryption.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/mo-awais/vernamcipher",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
)