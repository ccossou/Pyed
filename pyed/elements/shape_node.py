import logging
import xml.etree.ElementTree as ET

from ..core import utils
from ..core.node import Node

LOG = logging.getLogger(__name__)


class ShapeNode(Node):
    node_type = "ShapeNode"

    validShapes = ["rectangle", "rectangle3d", "roundrectangle", "diamond", "ellipse",
                   "fatarrow", "fatarrow2", "hexagon", "octagon", "parallelogram",
                   "parallelogram2", "star5", "star6", "star6", "star8", "trapezoid",
                   "trapezoid2", "triangle", "trapezoid2", "triangle"]

    def __init__(self, name, shape="rectangle", **style_params):
        """

        :param str name: Node title
        :param str shape: Shape for the current node. By default: rectangle
        :param dict kwargs: extra parameters passed to Node.
        """
        super().__init__(name, **style_params)

        # node shape
        utils.check_value("shape", shape, Node.validShapes)
        self.shape = shape

    def to_xml(self):
        """
        Create the corresponding XML object.

        The main creation is done in the parent class Node. Only extra steps are done here.

        :return: child object created
        :rtype: xml.etree.ElementTree.Element
        """

        # Generic Node conversion
        super().to_xml()

        ET.SubElement(self._ET_shape, "y:Shape", type=self.shape)

        return self._ET_node
