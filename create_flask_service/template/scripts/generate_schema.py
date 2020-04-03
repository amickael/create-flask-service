import os
import subprocess


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv("../.env")
    db_uri = os.environ["YOUR_CONN_STR_GOES_HERE"]
    subprocess.run(
        [
            "sqlacodegen",
            db_uri,
            "--schema",
            "dbo",
            "--noinflect",
            "--outfile",
            "../model/DataModel.py",
        ]
    )
