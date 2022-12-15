import os

from setuptools import find_packages, setup

version_contents = {}
version_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "syn10/version.py"
)
with open(version_path, "rt") as f:
    exec(f.read(), version_contents)

setup(
    name="syn10",
    description="Python client library for the syn10 API",
    version=version_contents["VERSION"],
    install_requires=[
        "requests>=2.28.1",
    ],
    python_requires=">=3.8.15",
    entry_points={
        "console_scripts": [
            "syn10=syn10._syn10_scripts:main",
        ],
    },
    packages=find_packages(exclude=["tests", "tests.*"]),
    author="syn10",
    author_email="syn10.ai@gmail.com",
    url="https://github.com/syn10-ai/syn10-python.git",
)
