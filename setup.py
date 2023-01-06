import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="chase",
    version="0.1.0",
    author="Mikolaj Stepniak",
    author_email="236659@edu.p.lodz.pl",
    description=("Simple simulation of a wolf chasing sheep"),
    license="MIT",
    license_files=('LICENSE'),
    keywords="example documentation tutorial",
    url="https://github.com/stepniaczky/chase",
    packages=['chase'],
    long_description=read('README.md'),
    classifiers=[
        'Development Status:: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
