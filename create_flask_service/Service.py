import os
import subprocess
import shutil
import sys
import stat

import requests

from create_flask_service.GlobalEnum import GlobalEnum


class Service:
    def __init__(self, service_name: str, root_dir: str):
        self.service_name = service_name
        self.root_dir = root_dir
        self.executable = "/bin/bash" if os.name == "posix" else None
        self.template_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), GlobalEnum.TEMPLATE_DIR.value
        )

        # Check if service directory already exists, if it does then prompt for overwrite
        self.cwd = os.path.abspath(os.path.join(self.root_dir, self.service_name))
        if os.path.exists(self.cwd):
            proceed = input("Directory already exists, overwrite? [y/N]: ")
            if proceed.lower() == "y":
                try:
                    shutil.rmtree(self.cwd)
                except (PermissionError, WindowsError):
                    for root, dirs, files in os.walk(self.cwd):
                        for directory in dirs:
                            os.chmod(os.path.join(root, directory), stat.S_IWUSR)
                        for file in files:
                            os.chmod(os.path.join(root, file), stat.S_IWUSR)
                    shutil.rmtree(self.cwd)
            else:
                print("Stopping")
                exit()

    def create_tree(self):
        # Copy file structure
        shutil.copytree(
            self.template_dir, self.cwd, ignore=shutil.ignore_patterns("__pycache__")
        )

        return self

    def generate_venv(self):
        # Generate venv
        subprocess.run([sys.executable, "-m", "venv", os.path.join(self.cwd, "venv")])

        return self

    def __version_requirements(self):
        # Read requirements
        req_path = os.path.join(self.cwd, "requirements.txt")
        with open(req_path, "r") as f:
            requirements = [req.rstrip() for req in f.readlines()]

        # Get latest requirement version
        # Make this check cross-dependencies in the future?
        versioned_requirements = []
        for requirement in requirements:
            resp = requests.get(f"https://pypi.org/pypi/{requirement}/json")
            if resp.ok:
                version = resp.json().get("info", {}).get("version")
                versioned_requirements.append(f"{requirement}=={version}")
            else:
                versioned_requirements.append(requirement)

        # Write back to requirements
        with open(req_path, "w") as f:
            f.writelines([f"{req}\n" for req in versioned_requirements])

    def install_requirements(self):
        # Replace requirements with versioned ones
        self.__version_requirements()

        # Install requirements
        subprocess.Popen(
            " && ".join(
                [
                    f"source {self.cwd}/venv/bin/activate"
                    if os.name == "posix"
                    else fr"{self.cwd}\venv\Scripts\activate.bat",
                    f"pip install -r {self.cwd}{os.path.sep}requirements.txt",
                    "deactivate",
                ]
            ),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            shell=True,
            executable=self.executable,
        ).communicate()

        return self

    def initialize_git(self):
        subprocess.Popen(
            f"cd {self.cwd} && git init && git add .",
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            shell=True,
            executable=self.executable,
        ).communicate()

        return self

    def __placeholder(self, file_name: str):
        file_path = os.path.join(self.cwd, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().replace(GlobalEnum.PLACEHOLDER.value, self.service_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)

    def personalize(self):
        self.__placeholder("README.md")
        self.__placeholder(os.path.join("controller", "__init__.py"))
