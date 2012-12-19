# -*- coding: utf-8 -*-
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
        retval = (self.anon and u'public') or u'private'
        assert type(retval) == unicode
        return retval
