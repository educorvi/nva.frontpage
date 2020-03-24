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


class JumbofluidIntegrationTest(unittest.TestCase):

    layer = NVA_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_jumbofluid_schema(self):
        fti = queryUtility(IDexterityFTI, name='Jumbofluid')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('Jumbofluid')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_jumbofluid_fti(self):
        fti = queryUtility(IDexterityFTI, name='Jumbofluid')
        self.assertTrue(fti)

    def test_ct_jumbofluid_factory(self):
        fti = queryUtility(IDexterityFTI, name='Jumbofluid')
        factory = fti.factory
        obj = createObject(factory)


    def test_ct_jumbofluid_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Jumbofluid',
            id='jumbofluid',
        )


        parent = obj.__parent__
        self.assertIn('jumbofluid', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('jumbofluid', parent.objectIds())

    def test_ct_jumbofluid_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Jumbofluid')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_jumbofluid_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Jumbofluid')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'jumbofluid_id',
            title='Jumbofluid container',
         )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type='Document',
            title='My Content',
        )
        self.assertTrue(
            obj,
            u'Cannot add {0} to {1} container!'.format(obj.id, fti.id)
        )
