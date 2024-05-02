from setuptools import find_packages, setup

with open("./README.md","r") as f:
    long_description = f.read()

setup(
    name="chileanfakeinfo",
    version="0.0.1",
    description="Fake info from chile for testing",
    package_dir={"":"chileanfakeinfo"},
    packages=find_packages(where="chileanfakeinfo"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Matías Bastian Ezequiel Tillerias Ley", 
) 