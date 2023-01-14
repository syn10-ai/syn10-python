import os
from pathlib import Path
from setuptools import find_packages, setup

parent_dir = Path(__file__).resolve().parent

version_contents = {}
version_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "syn10/version.py"
)
with open(version_path, "rt") as f:
    exec(f.read(), version_contents)

setup(
    name="Syn10",
    description="Python SDK for Syn10",
    version=version_contents["VERSION"],
    author="Syn10",
    author_email="support@syn10.ai",
    url="https://github.com/syn10-ai/syn10-python.git",
    license="MIT",
    entry_points={
        "console_scripts": [
            "syn10=syn10._syn10_scripts:main",
        ],
    },
    packages=find_packages(exclude=["tests", "tests.*", "docs", "examples"]),
    data_files=[("", ["requirements.txt"])],
    install_requires=parent_dir.joinpath("requirements.txt").read_text().splitlines(),
    python_requires=">=3.8.15",
)
