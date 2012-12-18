# coding=utf-8
from zope.interface import Interface
from zope.schema import ASCIILine


class IGSPostPrivacyContentProvider(Interface):
    pageTemplateFileName = Text(title=u"Page Template File Name",
        description=u"""The name of the ZPT file
        that is used to render the post.""",
        required=False,
        default="browser/templates/dialog.pt")
