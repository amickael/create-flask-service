import os

from halo import Halo

from create_flask_service.Service import Service


__author__ = "Andrew Mickael"
__version__ = "0.1.1"


def main():
    try:
        # Prompt input
        service_name = input("Service name: ")
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
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == "__main__":
    main()
