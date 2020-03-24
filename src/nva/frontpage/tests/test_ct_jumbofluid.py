# -*- coding: utf-8 -*-
from nva.frontpage.content.jumbofluid import IJumbofluid  # NOQA E501
from nva.frontpage.testing import NVA_FRONTPAGE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




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
        self.assertEqual(IJumbofluid, schema)

    def test_ct_jumbofluid_fti(self):
        fti = queryUtility(IDexterityFTI, name='Jumbofluid')
        self.assertTrue(fti)

    def test_ct_jumbofluid_factory(self):
        fti = queryUtility(IDexterityFTI, name='Jumbofluid')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IJumbofluid.providedBy(obj),
            u'IJumbofluid not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_jumbofluid_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Jumbofluid',
            id='jumbofluid',
        )

        self.assertTrue(
            IJumbofluid.providedBy(obj),
            u'IJumbofluid not provided by {0}!'.format(
                obj.id,
            ),
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
