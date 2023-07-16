import logging
import xml.etree.ElementTree as ET

from .label import Label
from ..core.node import Node

LOG = logging.getLogger(__name__)


class GenericNode(Node):
    node_type = "GenericNode"

    default_title_style = dict(backgroundColor="#b7c9e3", modelName="internal", modelPosition="t",
                               verticalTextPosition="bottom",
                               configuration="com.yworks.entityRelationship.label.name")

    default_desc_style = dict(alignment="left", configuration="com.yworks.entityRelationship.label.attributes",
                              verticalTextPosition="top", modelName="custom", modelPosition=None,
                              backgroundColor=None)

    def __init__(self, name, description, background="#e8eef7", title_style={}, desc_style={}, **kwargs):
        """

        :param name:
        :param dict style_params: common parameters passed to Node.
        """

        t_style = self.default_title_style.copy()
        t_style.update(title_style)
        super().__init__(name, title_style=t_style, background=background, **kwargs)

        # Use default dict as base, and overwrite by custom parameter if conflict
        d_style = self.default_desc_style.copy()  # Default title
        d_style.update(desc_style)  # custom for description

        self.description_label = Label(description, tag="y:NodeLabel", **d_style)

    def to_xml(self):
        """
        Create the corresponding XML object.

        The main creation is done in the parent class Node. Only extra steps are done here.

        :return: child object created
        :rtype: xml.etree.ElementTree.Element
        """
        # Generic Node conversion
        super().to_xml()

        # Add attribute to node type
        self._ET_shape.set("configuration", "com.yworks.entityRelationship.big_entity")

        desc_label_node = self.description_label.to_xml(self._ET_shape)
        tmp = ET.SubElement(desc_label_node, "y:LabelModel")
        ET.SubElement(tmp, "y:ErdAttributesNodeLabelModel")
        tmp = ET.SubElement(desc_label_node, "y:ModelParameter")
        ET.SubElement(tmp, "y:ErdAttributesNodeLabelModelParameter")

        style_element = ET.SubElement(self._ET_shape, "y:StyleProperties")
        ET.SubElement(style_element, "y:Property", attrib={"class": "java.lang.Boolean",
                                                           "name": "y.view.ShadowNodePainter.SHADOW_PAINTING",
                                                           "value": "false"})

        return self._ET_node
