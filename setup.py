from setuptools import setup

long_description = None

with open("README.md", 'r') as fp:
    long_description = fp.read()

setup(
    name = 'pyEcoventV2',
    packages = ['ecovent','ecoventv2'],
    version='0.9.1',
    description='Python3 library for single-room energy recovery ventilators with api V2 from Vents / Blauberg / Flexit',
    long_description=long_description,
    python_requires='>=3.6.7',
    author='Matjaž Godec/Aleksander Lehmann',
    author_email='matjaz.godec@gmail.com,aleksander@flovik.no',
    url='https://github.com/gody01/pyEcoventV2',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)
