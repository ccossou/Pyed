import logging
import xml.etree.ElementTree as ET

from .label import Label
from ..core.node import Node

LOG = logging.getLogger(__name__)


class UmlNode(Node):
    node_type = "UMLClassNode"

    def __init__(self, node_name, stereotype="", attributes="", methods="", **style_params):
        """

        :param node_name:
        :param UML:
        :param dict style_params: common parameters passed to Node.
        """
        super().__init__(node_name, **style_params)
        self.stereotype = stereotype
        self.attributes = attributes
        self.methods = methods

    def add_label(self, label_text, **kwargs):
        self.list_of_labels.append(Label(label_text, tag="y:NodeLabel", **kwargs))
        return self

    def to_xml(self):
        # Generic Node conversion
        Node.to_xml(self)

        UML = ET.SubElement(self._ET_shape, "y:UML", use3DEffect="false")

        attributes = ET.SubElement(UML, "y:AttributeLabel")
        attributes.text = self.attributes

        methods = ET.SubElement(UML, "y:MethodLabel")
        methods.text = self.methods

        UML.set("stereotype", self.stereotype)

        return self._ET_node
