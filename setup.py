from setuptools import setup, find_packages

import create_flask_service

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="create-flask-service",
    version=create_flask_service.__version__,
    description="Create a Flask microservice with a few keystrokes",
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
    install_requires=["halo"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires=">=3.6",
)
