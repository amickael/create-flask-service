import os
import subprocess
import shutil
import sys

from halo import Halo


__author__ = "Andrew Mickael"
__version__ = "0.0.11"

TEMPLATE_DIR = "template"
PLACEHOLDER = "{{ %SERVICE_NAME% }}"


class CreateService:
    def __init__(self, service_name: str, root_dir: str):
        self.service_name = "-".join(service_name.split(" "))
        self.root_dir = root_dir
        self.template_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), TEMPLATE_DIR
        )

        # Check if service directory already exists, if it does then prompt for overwrite
        self.cwd = os.path.join(self.root_dir, self.service_name)
        if os.path.exists(self.cwd):
            proceed = input("Directory already exists, overwrite? [y/N]: ")
            if proceed.lower() == "y":
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
        subprocess.run([sys.executable, "-m", "venv", f"{self.cwd}{os.sep}venv"])

        return self

    def install_requirements(self):
        # Install requirements
        subprocess.Popen(
            " && ".join(
                [
                    f"source {self.cwd}/venv/bin/activate"
                    if os.name == "posix"
                    else fr"{self.cwd}\Scripts\activate.bat",
                    f"pip install -r {self.cwd}{os.path.sep}requirements.txt",
                    "deactivate",
                ]
            ),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            shell=True,
            executable="/bin/bash" if os.name == "posix" else None,
        ).communicate()

        return self

    def initialize_git(self):
        subprocess.Popen(
            f"cd {self.cwd} && git init && git add .",
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            shell=True,
            executable="/bin/bash" if os.name == "posix" else None,
        ).communicate()

        return self

    def __placeholder(self, file_name: str):
        file_path = os.path.join(self.cwd, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().replace(PLACEHOLDER, self.service_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)

    def personalize(self):
        self.__placeholder("README.md")
        self.__placeholder(os.path.join("controller", "__init__.py"))


def main():
    try:
        # Prompt input
        service_name = input("Service name: ")
        root_dir = input("Root directory (blank for current directory): ")
        service = CreateService(service_name, root_dir)

        # Create file structure
        spinner = Halo(text="Creating file structure")
        spinner.start()
        service.create_tree()
        spinner.succeed()

        # Generate venv
        spinner.start("Generating virtual environment")
        service.generate_venv()
        spinner.succeed()

        # Activate venv and install requirements
        spinner.start("Installing requirements")
        service.install_requirements()
        spinner.succeed()

        # Initialize git
        spinner.start("Initializing git repository")
        service.initialize_git()
        spinner.succeed()

        # Personalize
        spinner.start("Personalizing")
        service.personalize()
        spinner.succeed()

        # Done!
        spinner.stop_and_persist("🎂".encode("utf-8"), "All done!")
        print("Your new project is located in:", os.path.abspath(service.cwd), sep="\t")
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == "__main__":
    main()
