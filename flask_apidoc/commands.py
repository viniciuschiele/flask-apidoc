"""
Provides an integration with flask_script to generate the ApiDoc files.
"""


try:
    import flask_script
except ImportError:
    raise ImportError('Missing flask-script library (pip install flask-script)')


import subprocess

from flask_script import Command


class GenerateApiDoc(Command):
    """
    GenerateApiDoc adds to Flask-Script a command to generate the apidoc files.
    """

    def __init__(self, input_path=None, output_path=None, template_path=None):
        super(GenerateApiDoc, self).__init__()
        self.input_path = input_path
        self.output_path = output_path or 'static/docs'
        self.template_path = template_path

    def run(self):
        cmd = ['apidoc']

        if self.input_path:
            cmd.append('--input')
            cmd.append(self.input_path)

        if self.output_path:
            cmd.append('--output')
            cmd.append(self.output_path)

        if self.template_path:
            cmd.append('--template')
            cmd.append(self.template_path)

        p = subprocess.Popen(cmd)

        p.communicate()

        return p.returncode
