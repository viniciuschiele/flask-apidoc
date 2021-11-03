import subprocess
from click import Command


class GenerateApiDoc(Command):
    """
    GenerateApiDoc is a command to generate the apidoc files.
    """
    def __init__(self,
                 input_path="./",
                 output_path="static/docs",
                 template_path=None):
        super(GenerateApiDoc, self).__init__(name="GenerateApiDoc")
        self.input_path = input_path
        self.output_path = output_path
        self.template_path = template_path
        self.callback = self.run

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
