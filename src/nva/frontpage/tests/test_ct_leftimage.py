# -*- coding: utf-8 -*-
from nva.frontpage.content.leftimage import ILeftimage  # NOQA E501
from nva.frontpage.testing import NVA_FRONTPAGE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class LeftimageIntegrationTest(unittest.TestCase):

    layer = NVA_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Landingpage',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_leftimage_schema(self):
        fti = queryUtility(IDexterityFTI, name='Leftimage')
        schema = fti.lookupSchema()
        self.assertEqual(ILeftimage, schema)

    def test_ct_leftimage_fti(self):
        fti = queryUtility(IDexterityFTI, name='Leftimage')
        self.assertTrue(fti)

    def test_ct_leftimage_factory(self):
        fti = queryUtility(IDexterityFTI, name='Leftimage')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ILeftimage.providedBy(obj),
            u'ILeftimage not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_leftimage_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Leftimage',
            id='leftimage',
        )

        self.assertTrue(
            ILeftimage.providedBy(obj),
            u'ILeftimage not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('leftimage', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('leftimage', parent.objectIds())

    def test_ct_leftimage_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Leftimage')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
