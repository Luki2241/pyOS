from setuptools import setup, find_packages

setup(
    name="pyos",
    version="1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pyos=pyos.main:main"
        ]
    },
)
