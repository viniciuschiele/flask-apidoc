from .views import app
from flask_apidoc.commands import GenerateApiDoc

app.cli.add_command(GenerateApiDoc(), "apidoc")

if __name__ == "__main__":
    pass
