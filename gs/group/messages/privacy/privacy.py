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
from __future__ import unicode_literals
from zope.cachedescriptors.property import Lazy
from gs.group.privacy import get_visibility, PERM_ANN, PERM_GRP, PERM_SIT


class MessagesPrivacy(object):

    def __init__(self, messages):
        print messages
        self.context = self.messages = messages

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
        d = {PERM_ANN: 'public',
            PERM_GRP: 'private',
            PERM_SIT: 'restricted to site members', }
        retval = d.get(self.permission, 'odd')
        return retval
