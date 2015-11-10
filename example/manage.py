from example.views import app
from flask_apidoc.commands import GenerateApiDoc
from flask_script import Manager

manager = Manager(app)
manager.add_command('apidoc', GenerateApiDoc())

if __name__ == "__main__":
    manager.run()
