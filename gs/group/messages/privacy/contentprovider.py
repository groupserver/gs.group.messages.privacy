# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013, 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import absolute_import, unicode_literals
from zope.contentprovider.interfaces import UpdateNotCalled
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('groupserver')
from zope.pagetemplate.pagetemplatefile import PageTemplateFile
from gs.group.base import GroupContentProvider
from .privacy import MessagesPrivacy


class GSPostPrivacyContentProvider(GroupContentProvider):
    def __init__(self, context, request, view):
        super(GSPostPrivacyContentProvider, self).__init__(context, request,
                                                           view)
        self.__updated = False

    def update(self):
        messagesPrivacy = MessagesPrivacy(self.context)
        self.visibility = messagesPrivacy.visibility

        if messagesPrivacy.anon:
            self.webVisibility = _('<strong>Anyone</strong> &#8213; including '
                            'search engines and people who are not logged in '
                            '&#8213;')
            self.emailVisibility = _('<strong>group</strong> members')
        elif messagesPrivacy.site:
            self.webVisibility = _('<strong>Group</strong> members and '
                                    '<strong>site</strong> members')
            self.emailVisibility = _('<strong>group</strong> members')
        else:
            self.webVisibility = _('<strong>Group</strong> members')
            self.emailVisibility = ''

        self.__updated = True

    def render(self):
        if not self.__updated:
            raise UpdateNotCalled
        pageTemplate = PageTemplateFile(self.pageTemplateFileName)
        retval = pageTemplate(visibility=self.visibility,
                                webVisibility=self.webVisibility,
                                emailVisibility=self.emailVisibility)
        return retval
