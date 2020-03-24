# -*- coding: utf-8 -*-
from nva.frontpage.content.textbox import ITextbox  # NOQA E501
from nva.frontpage.testing import NVA_FRONTPAGE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class TextboxIntegrationTest(unittest.TestCase):

    layer = NVA_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_textbox_schema(self):
        fti = queryUtility(IDexterityFTI, name='textbox')
        schema = fti.lookupSchema()
        self.assertEqual(ITextbox, schema)

    def test_ct_textbox_fti(self):
        fti = queryUtility(IDexterityFTI, name='textbox')
        self.assertTrue(fti)

    def test_ct_textbox_factory(self):
        fti = queryUtility(IDexterityFTI, name='textbox')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ITextbox.providedBy(obj),
            u'ITextbox not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_textbox_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='textbox',
            id='textbox',
        )

        self.assertTrue(
            ITextbox.providedBy(obj),
            u'ITextbox not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('textbox', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('textbox', parent.objectIds())

    def test_ct_textbox_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='textbox')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
