from setuptools import setup, find_packages

setup(
    name="quick",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["colorama", "questionary"],
    entry_points={
        "console_scripts": [
            "quick=quick.main:main",
        ],
    },
)
