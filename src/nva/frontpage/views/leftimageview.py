# -*- coding: utf-8 -*-

from nva.frontpage import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Leftimageview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('leftimageview.pt')



    def kategorie(self):
        kategorie = self.context.kategorie
        return kategorie

    def bild(self):
        url = ''
        bild = self.context.bild
        if bild:
            url = '%s/@@images/bild/large' %self.context.absolute_url()
            #url = self.context.absolute_url()+'/@@images/druckerbild'
        return url 



    def buttontitle(self):
        buttontitle = self.context.buttontitle
        return buttontitle



    def link(self):
        link = self.context.link
        return link
