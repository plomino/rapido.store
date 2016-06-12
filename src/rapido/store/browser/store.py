from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import requests
import yaml


class RapidoStore(BrowserView):
    """Manage the Rapido app store."""

    template = ViewPageTemplateFile("store.pt")

    def __call__(self):
        store_url = 'https://api.github.com/repos/plomino/rapido.store/contents/plugins'
        headers = {'Accept': 'application/vnd.github.v3+json'}

        req = requests.get(store_url, headers=headers)
        root = req.json()
        plugins = [content['name'] for content in root
            if content['type'] == 'dir']

        data = []
        for plugin in plugins:
            req = requests.get(store_url, headers=headers)
            data.append(yaml.load(req.text()))

        self.plugins = data

        return self.template()
