import logging
import xml.etree.ElementTree as ET

from ..core import utils
from ..core.node import Node

LOG = logging.getLogger(__name__)


class ShapeNode(Node):
    custom_properties_defs = {}

    node_type = "ShapeNode"

    validShapes = ["rectangle", "rectangle3d", "roundrectangle", "diamond", "ellipse",
                   "fatarrow", "fatarrow2", "hexagon", "octagon", "parallelogram",
                   "parallelogram2", "star5", "star6", "star6", "star8", "trapezoid",
                   "trapezoid2", "triangle", "trapezoid2", "triangle"]

    def __init__(self, node_name, shape="rectangle", **style_params):
        """

        :param node_name:
        :param dict style_params: common parameters passed to Node.
        """
        super().__init__(node_name, **style_params)

        # node shape
        utils.check_value("shape", shape, Node.validShapes)
        self.shape = shape

    def to_xml(self):
        # Generic Node conversion
        Node.to_xml(self)

        ET.SubElement(self._ET_shape, "y:Shape", type=self.shape)

        return self._ET_node
