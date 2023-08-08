import logging
import xml.etree.ElementTree as ET

from ..core.node import Node

LOG = logging.getLogger(__name__)


class SvgNode(Node):
    node_type = "SVGNode"

    def __init__(self, name, svg_filename, **style_params):
        """

        :param str name: Class name
        :param str svg_filename: relative or absolute path to a .svg file to be used as a Node
        :param dict kwargs: extra parameters passed to Node.
        """

        super().__init__(name, **style_params)

        with open(svg_filename, 'r') as obj:
            svg_content = obj.read()

        self.res_id = self.parent_graph.add_resource(svg_content)

    def to_xml(self):
        """
        Create the corresponding XML object.

        The main creation is done in the parent class Node. Only extra steps are done here.

        :return: child object created
        :rtype: xml.etree.ElementTree.Element
        """
        # Generic Node conversion
        super().to_xml()

        ET.SubElement(self._ET_shape, "y:SVGNodeProperties", usingVisualBounds="true")
        svg_model = ET.SubElement(self._ET_shape, "y:SVGModel", svgBoundsPolicy="0")
        ET.SubElement(svg_model, "y:SVGContent", refid=self.res_id)  # Ref to the corresponding resource

        return self._ET_node
