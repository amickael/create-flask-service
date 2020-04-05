from setuptools import setup, find_packages

import create_flask_service

with open("README.md", "r") as f:
    readme = f.read()

with open("requirements.txt", "r") as f:
    requirements = [i.rstrip() for i in f.readlines()]

setup(
    name="create-flask-service",
    version=create_flask_service.__version__,
    description=create_flask_service.__description__,
    long_description=readme,
    long_description_content_type="text/markdown",
    author=create_flask_service.__author__,
    author_email="andrew.mickael@gmail.com",
    license="MIT",
    platforms=["NT", "POSIX"],
    url="https://github.com/amickael/create-flask-service",
    packages=find_packages(exclude=("create_flask_service.template",)),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": ["create-flask-service = create_flask_service:main"]
    },
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Environment :: Console",
    ],
    python_requires=">=3.6",
)
