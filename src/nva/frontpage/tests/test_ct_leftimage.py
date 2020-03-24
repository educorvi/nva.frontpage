# -*- coding: utf-8 -*-
from nva.frontpage.content.leftimage import ILeftimage  # NOQA E501
from nva.frontpage.testing import NVA_FRONTPAGE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
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
        self.parent = self.portal

    def test_ct_leftimage_schema(self):
        fti = queryUtility(IDexterityFTI, name='leftimage')
        schema = fti.lookupSchema()
        self.assertEqual(ILeftimage, schema)

    def test_ct_leftimage_fti(self):
        fti = queryUtility(IDexterityFTI, name='leftimage')
        self.assertTrue(fti)

    def test_ct_leftimage_factory(self):
        fti = queryUtility(IDexterityFTI, name='leftimage')
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
            container=self.portal,
            type='leftimage',
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

    def test_ct_leftimage_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='leftimage')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_leftimage_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='leftimage')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'leftimage_id',
            title='leftimage container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
