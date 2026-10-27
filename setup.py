from setuptools import find_packages, setup

setup(
    name="hrbai",
    version="0.1.0",
    packages=find_packages(),
    package_data={
        "hrbai": ["*.pyc"],
    },
    include_package_data=True,
)
