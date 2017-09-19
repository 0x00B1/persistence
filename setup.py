import setuptools


setuptools.setup(
    name='cytominer_database',
    version='0.0.0',
    author=[
        'Allen Goodman',
        "Claire McQuin",
        "Shantanu Singh"
    ],
    author_email=[
        "allen.goodman@icloud.com",
        "mcquincl@gmail.com",
        "shsingh@broadinstitute.org"
    ],
    long_description="cytomining-database provides mechanisms to import CSV "
                     "files generated in a morphological profiling experiment "
                     "into a database backend. "
                     "Please refer to the online documentation at "
                     "http://cytominer-database.readthedocs.io",
    package_data={
        'cytominer_database': [
            'config/*.ini',
            'config/*.json',
            'config/*.sql'
        ],
    },
    packages=setuptools.find_packages(
        exclude=[
            'tests',
            'doc'
        ]
    ),
    include_package_data=True,
    install_requires=[
        'backports.tempfile>=1.0rc1',
        'click>=6.7',
        'configparser>=3.5.0',
        'csvkit>=1.0.1',
        'odo>=0.5.0',
        'pandas>=0.19.2',
        'pytest>=3.0.6'
    ],
    entry_points={
        'console_scripts': [
            'ingest=cytominer_database.ingest:__main__',
        ]
    },
    license='BSD',
    url='https://github.com/cytomining/cytominer-database'
)
