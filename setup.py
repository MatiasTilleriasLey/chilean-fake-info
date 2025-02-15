from setuptools import setup, find_packages

setup(
    name="chileanfakeinfo",
    version="0.1.1",
    packages=find_packages(exclude=["example"]),
    install_requires=[],
    author="Matias Tillerias",
    author_email="matias.tillerias@owasp.org",
    description="Generador de datos ficticios chilenos para pruebas y desarrollo.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MatiasTilleriasLey/chilean-fake-info",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

