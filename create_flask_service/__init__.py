import argparse

from halo import Halo
import requests

from create_flask_service.Service import Service


__author__ = "Andrew Mickael"
__version__ = "0.1.6"
__description__ = "Create a Flask microservice with a few keystrokes"


def check_version(verbose: bool = False):
    resp = requests.get("https://pypi.org/pypi/create-flask-service/json")
    if resp.ok:
        latest_version = resp.json().get("info", {}).get("version", "")
        if latest_version != __version__ or verbose:
            print(
                f"A newer version of create-flask-service is available on PyPI ({__version__} => {latest_version})",
                'Run "pip install --upgrade create-flask-service" to update',
                sep="\r\n",
            )


def run():
    # Prompt input
    while True:
        service_name = input("Service name: ").strip().replace(" ", "-")
        if service_name:
            break
        else:
            print("Please enter a service name")
    root_dir = input("Root directory (blank for current directory): ")
    service = Service(service_name, root_dir)

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
    print("Your new project is located in:", service.cwd, sep="\t")


def main():
    # Set up args
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("-V", action="store_true", help="Display version")
    args = parser.parse_args()

    # Run
    if args.V is True:
        print("create-flask-service", __version__, sep="==")
    else:
        try:
            run()
        except (KeyboardInterrupt, SystemExit):
            pass
    check_version()


if __name__ == "__main__":
    main()
