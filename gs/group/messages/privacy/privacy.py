# -*- coding: utf-8 -*-
############################################################################
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
############################################################################
from __future__ import unicode_literals, absolute_import
from zope.cachedescriptors.property import Lazy
from gs.group.privacy import (get_visibility, PERM_ANN, PERM_GRP, PERM_SIT)
from Products.XWFMailingListManager.interfaces import IGSMessagesFolder
from . import GSMessageFactory as _


class MessagesPrivacy(object):

    def __init__(self, messages):
        if not IGSMessagesFolder.providedBy(messages):
            m = '{0} does not provide the IGSMessagesFolder interface'
            msg = m.format(messages)
            raise TypeError(msg)
        self.context = self.messages = messages

    @classmethod
    def from_group(cls, group):
        messages = getattr(group.aq_explicit, 'messages')
        retval = cls(messages)
        return retval

    @Lazy
    def permission(self):
        retval = get_visibility(self.messages)
        return retval

    @property
    def anon(self):
        return self.permission == PERM_ANN

    @property
    def site(self):
        return self.permission == PERM_SIT

    @Lazy
    def visibility(self):
        d = {PERM_ANN: _('public'),
             PERM_GRP: _('private'),
             PERM_SIT: _('restricted'), }
        retval = d.get(self.permission, _('odd'))
        return retval


def from_group(grp):
    'A factory-function for the ZCML'
    return MessagesPrivacy.from_group(grp)
