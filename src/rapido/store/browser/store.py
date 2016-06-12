from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import requests
import yaml

GITHUB_REPOSITORY = 'plomino/rapido.store'


class RapidoStore(BrowserView):
    """Manage the Rapido app store."""

    template = ViewPageTemplateFile("store.pt")

    def display(self):
        store_url = 'https://api.github.com/repos/%s/contents/plugins' % GITHUB_REPOSITORY
        headers = {'Accept': 'application/vnd.github.v3+json'}

        req = requests.get(store_url, headers=headers)
        root = req.json()
        plugins = [content['name'] for content in root
            if content['type'] == 'dir']

        data = []
        for plugin in plugins:
            yaml_url = 'https://raw.githubusercontent.com/%s/master/plugins/%s/settings.yaml' % (
                GITHUB_REPOSITORY, plugin)
            req = requests.get(yaml_url)
            data.append({
                'id': plugin,
                'settings': yaml.load(req.text),
                'url': 'https://github.com/%s/tree/master/plugins/%s' % (GITHUB_REPOSITORY, plugin),
            })

        self.plugins = data

        return self.template()

    def install(self, plugin_id):
        folder_url = 'https://api.github.com/repos/%s/contents/plugins/%s' % (
            GITHUB_REPOSITORY,
            plugin_id)
        headers = {'Accept': 'application/vnd.github.v3+json'}

    def __call__(self):
        if self.request.get('install'):
            plugin_id = self.request.get('plugin_id')
            self.install(plugin_id)


        return self.display()
