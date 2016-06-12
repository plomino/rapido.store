from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import requests


class RapidoStore(BrowserView):
    """Manage the Rapido app store."""

    template = ViewPageTemplateFile("store.pt")

    def __call__(self):
        store_url = 'https://api.github.com/repos/plomino/rapido.store/contents/plugins'
        headers = {'Accept': 'application/vnd.github.v3+json'}

        r = requests.get(store_url, headers=headers)
        data = r.json()
        plugins = [content['name'] for content in data
            if content['type']=='dir']
        import pdb; pdb.set_trace()

        return self.template()
