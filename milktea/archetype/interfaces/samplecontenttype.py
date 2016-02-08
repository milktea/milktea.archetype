from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from milktea.archetype import archetypeMessageFactory as _



class ISampleContentType(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    newfield = schema.TextLine(
        title=_(u"Field Label"),
        required=False,
        description=_(u"Field Desc"),
    )
#
