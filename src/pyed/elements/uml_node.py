import logging
import xml.etree.ElementTree as ET

from ..core.node import Node

LOG = logging.getLogger(__name__)


class UmlNode(Node):
    node_type = "UMLClassNode"

    def __init__(self, name, stereotype="", attributes="", methods="", **style_params):
        """

        :param str name: Class name
        :param str stereotype: class stereotype
        :param str attributes: class attributes
        :param str methods: Class methods
        :param kwargs: Title label extra parameters
        """

        super().__init__(name, **style_params)
        self.stereotype = stereotype
        self.attributes = attributes
        self.methods = methods


    def to_xml(self):
        """
        Create the corresponding XML object.

        The main creation is done in the parent class Node. Only extra steps are done here.

        :return: child object created
        :rtype: xml.etree.ElementTree.Element
        """
        # Generic Node conversion
        super().to_xml()

        UML = ET.SubElement(self._ET_shape, "y:UML", use3DEffect="false")

        attributes = ET.SubElement(UML, "y:AttributeLabel")
        attributes.text = self.attributes

        methods = ET.SubElement(UML, "y:MethodLabel")
        methods.text = self.methods

        UML.set("stereotype", self.stereotype)

        return self._ET_node
