# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig

import rapido.store


class RapidoStoreLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            rapido.store,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'rapido.store:default')


RAPIDO_STORE_FIXTURE = RapidoStoreLayer()


RAPIDO_STORE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(RAPIDO_STORE_FIXTURE,),
    name='RapidoStoreLayer:IntegrationTesting'
)


RAPIDO_STORE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(RAPIDO_STORE_FIXTURE,),
    name='RapidoStoreLayer:FunctionalTesting'
)


RAPIDO_STORE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        RAPIDO_STORE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='RapidoStoreLayer:AcceptanceTesting'
)
