from setuptools import setup, find_packages

setup(
    name='thermaPy',
    version='0.0.1'
    packages=find_packages(),
    install_requires=[
       'opencv-python>=4.9.0.80'
       'matplotlib>=3.7.2'
    ]
)