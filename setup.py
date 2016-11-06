from setuptools import setup

with open("README.md") as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="python_project_generator",
    version='0.0.1',
    description='generate a python project',
    long_description=readme,
    author="slumber1122",
    author_email="slumber1122@gmail.com",
    url="https://github.com/slumber1122/python_project_generator",
    license=license,
    packages='python_project_generator',
    keywords='structure of python project',
    include_package_data=True,
    zip_safe=False
)
