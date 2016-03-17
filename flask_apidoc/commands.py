# Copyright 2015 Vinicius Chiele. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


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
        super(Command, self).__init__()
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

        return subprocess.call(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
