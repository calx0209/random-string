from setuptools import setup, find_packages

setup(
    name="rndstr",
    version='1.1',
    description='a random string generate',
    author='calx0209',
    url='https://github.com/calx0209/random-string',
    pachage=find_packages(),
    entry_points={
        "console_scripts":[
            "randomstring = rndstr.app:main",
        ]
    },
)