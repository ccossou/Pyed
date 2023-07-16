import logging
import xml.etree.ElementTree as ET

from ..core import constants
from .label import Label
from ..core.xml_item import XmlItem
from ..core import utils

LOG = logging.getLogger(__name__)


class Edge(XmlItem):

    default_clabel_style = dict(alignment="center", backgroundColor=None, borderColor="",
                                modelName="centered", modelPosition="center", preferred_placement=None)
    default_slabel_style = dict(alignment="center", backgroundColor=None, borderColor="",
                                modelName="six_pos", modelPosition="shead",
                           preferred_placement="source_on_edge",)  # source
    default_tlabel_style = dict(alignment="center", backgroundColor=None, borderColor="",
                                modelName="six_pos", modelPosition="thead",
                           preferred_placement="source_on_edge",)  # target

    def __init__(self, node1, node2, label=None, arrowhead="standard", arrowfoot="none",
                 color="#000000", line_type="line", width="1.0", label_style={},
                 source_label=None, target_label=None,
                 description="", url="", **kwargs):
        super().__init__(**kwargs)
        self.node1 = node1
        self.node2 = node2

        self.list_of_labels = []  # initialize list of labels

        if label:
            self.clabel_style = self.default_clabel_style.copy()
            self.clabel_style.update(label_style)
            self.add_label(label, **self.clabel_style)

        if source_label is not None:
            self.slabel_style = self.default_slabel_style.copy()
            self.slabel_style.update(label_style)
            self.add_label(source_label, **self.slabel_style)

        if target_label is not None:
            self.tlabel_style = self.default_tlabel_style.copy()
            self.tlabel_style.update(label_style)
            self.add_label(target_label, **self.tlabel_style)

        utils.check_value("arrowhead", arrowhead, constants.arrow_types)
        self.arrowhead = arrowhead

        utils.check_value("arrowfoot", arrowfoot, constants.arrow_types)
        self.arrowfoot = arrowfoot

        utils.check_value("line_type", line_type, constants.line_types)
        self.line_type = line_type

        self.color = color
        self.width = width

        self.description = description
        self.url = url


    def add_label(self, label_text, **kwargs):
        self.list_of_labels.append(Label(label_text, tag="y:EdgeLabel", **kwargs))
        # Enable method chaining
        return self

    def to_xml(self):
        edge = ET.Element("edge", id=str(self.id), source=str(self.node1.id), target=str(self.node2.id))
        data = ET.SubElement(edge, "data", key="data_edge")
        pl = ET.SubElement(data, "y:PolyLineEdge")

        ET.SubElement(pl, "y:Arrows", source=self.arrowfoot, target=self.arrowhead)
        ET.SubElement(pl, "y:LineStyle", color=self.color, type=self.line_type,
                      width=self.width)

        for label in self.list_of_labels:
            label.to_xml(pl)

        if self.url:
            url_edge = ET.SubElement(edge, "data", key="url_edge")
            url_edge.text = self.url

        if self.description:
            description_edge = ET.SubElement(edge, "data", key="description_edge")
            description_edge.text = self.description

        return edge
