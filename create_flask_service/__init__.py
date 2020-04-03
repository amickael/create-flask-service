import os
import subprocess
import shutil
import sys


__author__ = "Andrew Mickael"
__version__ = "0.0.1"


class CreateService:
    def __init__(self, service_name: str, root_dir: str):
        self.service_name = service_name
        self.root_dir = root_dir
        self.template_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "template"
        )
        self.cwd = os.path.join(root_dir, service_name)

    def create_tree(self):
        # Check if directory already exists, if it does then prompt for overwrite
        if os.path.exists(self.cwd):
            proceed = input("Directory already exists, overwrite? [y/N]: ")
            if proceed.lower() == "y":
                shutil.rmtree(self.cwd)
            else:
                print("Stopping")
                exit()

        # Copy file structure
        shutil.copytree(
            self.template_dir, self.cwd, ignore=shutil.ignore_patterns("__pycache__")
        )

        return self

    def generate_venv(self):
        # Generate venv
        subprocess.run([sys.executable, "-m", "venv", f"{self.cwd}{os.sep}venv"])

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
        ).communicate()

        return self

    def initialize_git(self):
        subprocess.Popen(
            f"cd {self.cwd} && git init && git add .",
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            shell=True,
        ).communicate()

        return self


def main():
    # Collect inputs
    svc_name = "-".join(input("Service name: ").split(" "))
    root_dir = input("Root directory (Blank for current directory): ")

    # Get working directory and check if already exists. If it does then prompt the user for overwrite
    cwd = os.path.join(root_dir, svc_name)
    if os.path.exists(cwd):
        proceed = input("Directory already exists, overwrite? [y/N]: ")
        if proceed.lower() == "y":
            shutil.rmtree(cwd)
        else:
            print("Process terminated")
            return None

    # Copy file structure
    print("\U0001F6E0", "Creating file structure", sep="\t")
    resource_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "template")
    shutil.copytree(resource_dir, cwd, ignore=shutil.ignore_patterns("__pycache__"))

    # Generate venv
    print("\U0001F3DE", "Generating virtual environment", sep="\t")
    subprocess.run(["python3", "-m", "venv", f"{cwd}/venv"])

    # Activate venv and install requirements
    print("\U0001F4E6", "Installing requirements", sep="\t")
    activate_cmd = (
        f"source {cwd}/venv/bin/activate"
        if os.name == "posix"
        else fr"{cwd}\Scripts\activate.bat"
    )
    install_cmd = f"pip install --upgrade -r {cwd}/requirements.txt"
    deactivate_cmd = "deactivate"
    subprocess.Popen(
        "; ".join([activate_cmd, install_cmd, deactivate_cmd]),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        shell=True,
    ).communicate()

    # Initialize git
    print("\U0001F680", "Initializing git repository", sep="\t")
    os.rename(os.path.join(cwd, ".gitignore"), os.path.join(cwd, "..gitignore"))
    subprocess.Popen(
        f"cd {cwd}; git init; git add .",
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        shell=True,
    ).communicate()

    # Done!
    print("\U0001F382", "All done!", sep="\t")
    print("Your new project is located in:", os.path.abspath(cwd), sep="\t")


if __name__ == "__main__":
    main()
