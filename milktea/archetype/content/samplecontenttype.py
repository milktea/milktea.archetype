"""Definition of the Sample Content Type content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from milktea.archetype import archetypeMessageFactory as _

from milktea.archetype.interfaces import ISampleContentType
from milktea.archetype.config import PROJECTNAME

SampleContentTypeSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'newfield',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Field Label"),
            description=_(u"Field Desc"),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

SampleContentTypeSchema['title'].storage = atapi.AnnotationStorage()
SampleContentTypeSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(SampleContentTypeSchema, moveDiscussion=False)


class SampleContentType(base.ATCTContent):
    """Description of the Example Type"""
    implements(ISampleContentType)

    meta_type = "SampleContentType"
    schema = SampleContentTypeSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    newfield = atapi.ATFieldProperty('newfield')


atapi.registerType(SampleContentType, PROJECTNAME)
