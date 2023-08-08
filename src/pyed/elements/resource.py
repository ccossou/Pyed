import logging
import xml.etree.ElementTree as ET

from ..core.xml_item import XmlItem

LOG = logging.getLogger(__name__)


class Resource(XmlItem):

    def __init__(self, resource, **kwargs):
        """

        :param resource: SVG content as text
        """
        super().__init__(**kwargs)

        self.resource = resource
        self.hash = hash(resource)  # Hash to ensure each resource is unique

    def to_xml(self):
        """
        Create the corresponding XML object.

        The main creation is done in the parent class Node. Only extra steps are done here.

        :return: child object created
        :rtype: xml.etree.ElementTree.Element
        """
        res_item = ET.Element("y:Resource", id=str(self.id))
        res_item.set("xml:space", "preserve")

        res_item.text = self.resource

        return res_item
