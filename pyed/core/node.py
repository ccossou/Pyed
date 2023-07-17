import logging
import xml.etree.ElementTree as ET
from abc import ABCMeta, abstractmethod

from . import constants
from ..elements.label import Label
from .xml_item import XmlItem
from . import utils

LOG = logging.getLogger(__name__)


class Node(XmlItem, metaclass=ABCMeta):
    node_type = None

    default_title_style = dict(alignment="center", font_family="Dialog",
                               underlined_text="false", font_style="plain", font_size="12", )

    def __init__(self, name, title_style={}, background="#ffffff", transparent="false", border_color="#000000",
                 border_type="line", border_width="1.0", height=False, width=False, x=False, y=False, description="",
                 url="", **kwargs):
        """

        :param str name: Node name (title)
        :param dict title_style: See Label parameters for more information about possible values
        :param str background: Background color as RGB (e.g. '#ffffff') or None if no color
        :param bool transparent: Is the node transparent?
        :param str border_color: Border color as RGB (e.g. '#ffffff') or None if no color
        :param str border_type: Border type (e.g. line, the default)
        :param str border_width: Border width in pixel (e.g. '1.0')
        :param str height:
        :param str width:
        :param str x:
        :param str y:
        :param str description: Node description (not displayed in Yed, so I don't know how usefull this is)
        :param str url: Node url (not displayed in Yed, so I don't know how usefull this is)
        :param dict kwargs: Extra arguments are passed to parent class (developer only)
        """
        super().__init__(**kwargs)

        self.list_of_labels = []  # initialize list of labels

        # Use default dict as base, and overwrite by custom parameter if conflict
        self.title_style = self.default_title_style.copy()
        self.title_style.update(title_style)

        self.add_label(name, **self.title_style)

        self.name = name

        # shape fill
        self.background = background
        self.transparent = transparent

        # border options
        self.border_color = border_color
        self.border_width = border_width

        utils.check_value("border_type", border_type, constants.line_types)
        self.border_type = border_type

        # geometry
        self.geom = {}
        if height:
            self.geom["height"] = height
        if width:
            self.geom["width"] = width
        if x:
            self.geom["x"] = x
        if y:
            self.geom["y"] = y

        self.description = description
        self.url = url

        # Future storage for xml object nodes
        self._ET_node = None
        self._ET_data = None
        self._ET_shape = None


    def add_label(self, label_text, **kwargs):
        """
        Add label to Node

        :param str label_text:
        :param dict kwargs: Extra label parameters
        """
        self.list_of_labels.append(Label(label_text, tag="y:NodeLabel", **kwargs))
        return self

    @abstractmethod
    def to_xml(self):
        """
        Init in the parent class all XML items that are common to all child classes

        Create:
        * self._ET_node
        * self._ET_data
        * self._ET_shape
        """
        self._ET_node = ET.Element("node", id=str(self.id))
        self._ET_data = ET.SubElement(self._ET_node, "data", key="data_node")
        self._ET_shape = ET.SubElement(self._ET_data, "y:" + self.node_type)

        if self.geom:
            ET.SubElement(self._ET_shape, "y:Geometry", **self.geom)

        ET.SubElement(self._ET_shape, "y:Fill", color=self.background,
                      transparent=self.transparent)

        ET.SubElement(self._ET_shape, "y:BorderStyle", color=self.border_color, type=self.border_type,
                      width=self.border_width)

        for label in self.list_of_labels:
            label.to_xml(self._ET_shape)

        if self.url:
            url_node = ET.SubElement(self._ET_node, "data", key="url_node")
            url_node.text = self.url

        if self.description:
            description_node = ET.SubElement(self._ET_node, "data", key="description_node")
            description_node.text = self.description
