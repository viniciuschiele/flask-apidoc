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

from os.path import join


class ApiDoc(object):
    def __init__(self, folder_path=None, url_path=None, app=None):
        self.folder_path = folder_path
        self.url_path = url_path

        if self.folder_path is None:
            self.folder_path = 'apidoc'

        if self.url_path is None:
            self.url_path = '/apidoc'

        self.app = None

        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        url = self.url_path

        if not self.url_path.endswith('/'):
            url += '/'

        app.add_url_rule(url, 'apidoc', self.__apidoc_view)
        app.add_url_rule(url + '<path:path>', 'apidoc', self.__apidoc_view)

    def __apidoc_view(self, path=None):
        if not path:
            path = 'index.html'

        response = self.app.send_static_file(join(self.folder_path, path))

        # TODO: replace url
        # if path == 'api_project.js' or path == 'api_project.json':
        #     self.__replace_url(response)

        return response
