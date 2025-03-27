from setuptools import setup, find_packages

setup(
    name="bigdata-infrastructure",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "openpyxl",
        "pyspark",
        "requests",
        "mkdocs",
        "mkdocs-material",
        "mkdocs-mermaid2-plugin"
    ],
    author="Juan Esteban Atehortua Sanchez",
    author_email="juan.atehortua@est.iudigital.edu.co",
    description="Proyecto de big data para procesamiento de datos",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JuanesMedCol/bigdata-infrastructure",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
