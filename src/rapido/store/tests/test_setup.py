# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from rapido.store.testing import RAPIDO_STORE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that rapido.store is properly installed."""

    layer = RAPIDO_STORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if rapido.store is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('rapido.store'))

    def test_uninstall(self):
        """Test if rapido.store is cleanly uninstalled."""
        self.installer.uninstallProducts(['rapido.store'])
        self.assertFalse(self.installer.isProductInstalled('rapido.store'))

    def test_browserlayer(self):
        """Test that IRapidoStoreLayer is registered."""
        from rapido.store.interfaces import IRapidoStoreLayer
        from plone.browserlayer import utils
        self.assertIn(IRapidoStoreLayer, utils.registered_layers())
