# -*- coding: utf-8 -*-
from zope.contentprovider.interfaces import UpdateNotCalled
from zope.pagetemplate.pagetemplatefile import PageTemplateFile
from gs.group.base import GroupContentProvider
from privacy import MessagesPrivacy


class GSPostPrivacyContentProvider(GroupContentProvider):
    def __init__(self, context, request, view):
        super(GSPostPrivacyContentProvider, self).__init__(context, request,
                                                           view)
        self.__updated = False

    def update(self):
        messagesPrivacy = MessagesPrivacy(self.context)
        self.visibility = messagesPrivacy.visibility

        if messagesPrivacy .anon:
            self.webVisibility = u'<strong>Anyone</strong> &#8213; '\
              u'including search engines and people who are not '\
              u' logged in &#8213;'
            self.emailVisibility = u'<strong>group</strong> members'
        elif messagesPrivacy .site:
            self.webVisibility = u'<strong>Group</strong> members '\
              u'and <strong>site</strong> members'
            self.emailVisibility = u'<strong>group</strong> members'
        else:
            self.webVisibility = u'<strong>Group</strong> members'
            self.emailVisibility = u''

        assert type(self.visibility) == unicode
        assert type(self.webVisibility) == unicode
        assert type(self.emailVisibility) == unicode
        self.__updated = True

    def render(self):
        if not self.__updated:
            raise UpdateNotCalled
        pageTemplate = PageTemplateFile(self.pageTemplateFileName)
        retval = pageTemplate(visibility=self.visibility,
                                webVisibility=self.webVisibility,
                                emailVisibility=self.emailVisibility)
        assert type(retval) == unicode
        return retval
