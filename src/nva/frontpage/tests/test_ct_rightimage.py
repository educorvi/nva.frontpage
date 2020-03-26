# -*- coding: utf-8 -*-
from nva.frontpage.testing import NVA_FRONTPAGE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class RightimageIntegrationTest(unittest.TestCase):

    layer = NVA_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_rightimage_schema(self):
        fti = queryUtility(IDexterityFTI, name='rightimage')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('rightimage')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_rightimage_fti(self):
        fti = queryUtility(IDexterityFTI, name='rightimage')
        self.assertTrue(fti)

    def test_ct_rightimage_factory(self):
        fti = queryUtility(IDexterityFTI, name='rightimage')
        factory = fti.factory
        obj = createObject(factory)


    def test_ct_rightimage_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='rightimage',
            id='rightimage',
        )


        parent = obj.__parent__
        self.assertIn('rightimage', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('rightimage', parent.objectIds())

    def test_ct_rightimage_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='rightimage')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
