from setuptools import setup

setup(
    name='homu',
    version='0.2.0',
    author='Barosl Lee',
    url='https://github.com/barosl/homu',
    description='A bot that integrates with GitHub and your favorite continuous integration service',

    packages=['homu'],
    install_requires=[
        'github3.py==1.0.0a2',
        'toml==0.9.1',
        'Jinja2==2.8',
        'requests==2.9.1',
        'bottle==0.12.9',
        'waitress==0.8.10',
    ],
    package_data={
        'homu': [
            'html/*.html',
        ],
    },
    entry_points={
        'console_scripts': [
            'homu=homu.main:main',
        ],
    },
    zip_safe=False,
)
