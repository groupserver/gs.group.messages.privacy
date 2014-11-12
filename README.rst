=============================
``gs.group.messages.privacy``
=============================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Privacy information about posts in a group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2014-11-12
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

Introduction
============

The product is responsible for providing human-readable summaries
of the privacy of posts made do a group. The information is
mostly displayed by the ``groupserver.PostPrivacy`` `content
provider`_, while the `MessagesPrivacy`_ class does the actual
summarising.

Content provider
================

The content provider looks for the ``messages`` object in the
current context [#context]_:

.. code-block:: xml

  <div tal:content="structure provider:groupserver.PostPrivacy">
    Privacy statement
  </div>

``MessagesPrivacy``
===================

The ``gs.group.messages.privacy.MessagesPrivacy`` class provides
a one-word summary of the privacy setting:

* ``public``: Everyone can see the post.
* ``restricted``: Only site members can see the post.
* ``private``: Only group members can see the post.
* ``odd``: None of the above.

This summary is made available through the ``visibility``
property of the content provider:

.. code-block:: xml

    <span class="vis"
          tal:content="view/privacy/visibility">lurid</span></span>

An adaptor from both the group-folder and messages object to the
messages-privacy class is available. For example

.. code-block:: python

    from gs.group.messages.privacy.interfaces import IMessagesPrivacy

    ...

        @Lazy
        def privacy(self):
          retval = IMessagesPrivacy(self.context)
          return retval

Resources
=========

- Code repository: https://github.com/groupserver/gs.group.messages.privacy
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. [#context] The content provider just assumes that the current
              context is the ``messages`` instance for a
              group. This is a bug.

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

..  LocalWords:  PostPrivacy MessagesPrivacy tal groupserver http
