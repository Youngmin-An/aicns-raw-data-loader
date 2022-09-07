import os
from setuptools import setup, find_packages

setup(name="aicns_raw_data_loader",
      version="0.0.2",
      description="Raw data loader library package in AICNS project",
      author="Youngmin An",
      author_email="youngmin.develop@gmail.com",
      license="Apache License 2.0",
      url="https://github.com/Youngmin-An/aicns-raw-data-loader",
      packages=find_packages(),
      install_requires=[
          'pendulum',
          'pyspark>=3.0.3',
          'aicns-feature-metadata'
      ]
)

