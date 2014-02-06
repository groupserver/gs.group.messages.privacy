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
from AccessControl.PermissionRole import rolesForPermissionOn


class MessagesPrivacy(object):

    def __init__(self, messages):
        self.context = self.messages = messages

    @Lazy
    def roles(self):
        retval = rolesForPermissionOn('View', self.messages)
        return retval

    @Lazy
    def anon(self):
        retval = 'Anonymous' in self.roles
        assert type(retval) == bool
        return retval

    @Lazy
    def site(self):
        retval = 'DivisionMember' in self.roles
        assert type(retval) == bool
        return retval

    @Lazy
    def group(self):
        retval = 'GroupMember' in self.roles
        assert type(retval) == bool
        return retval

    @Lazy
    def visibility(self):
        retval = (self.anon and 'public') or 'private'
        return retval
