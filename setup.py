from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

DESCRIPTION = read('README.md')


setup(
    name='bincut',
    version='0.0.1',
    description='Binary Cutter',
    long_description=DESCRIPTION,
    author='Aki Sheltie',
    author_email='verifsec@gmail.com',
    url='https://www.github.com/sheltie03/bincut/',
    packages=find_packages(),
    install_requires=[],
    keywords='binary',
    entry_points={
        'console_scripts': [
            'bincut=cutter.bincut:main',
        ]
    },
    package_data={}
)
