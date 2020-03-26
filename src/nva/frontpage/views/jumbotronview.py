# -*- coding: utf-8 -*-

from nva.frontpage import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Jumbotronview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('jumbotronview.pt')

    def textfield(self):
        textfield = self.context.textfield
        return textfield

    def buttontitle(self):
        buttontitle = self.context.buttontitle
        return buttontitle

    def link(self):
        link = self.context.link
        return link
