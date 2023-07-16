import logging

import xml.etree.ElementTree as ET

from .edge import Edge
from .group import Group

LOG = logging.getLogger(__name__)


class Graph:
    def __init__(self, directed="directed", graph_id="G"):
        """

        :param str directed: No idea what this does in practice, I leave the default because I don't need it.
        :param str graph_id: Graph object index. Must be unique. This is not an issue for one object but will be
                             when multiple graphes are created.
        """

        self.nodes = {}
        self.edges = {}
        self.groups = {}

        self.directed = directed
        self.id = graph_id
        self.existing_entities = {self.id: self}

        # a graph object is its own graph reference.
        self.parent_graph = self
        self.parent = None

        self.graphml = None

    def _construct_graphml(self):
        """
        Create the self.graphml object as an XML.Element
        """
        graphml = ET.Element("graphml", xmlns="http://graphml.graphdrawing.org/xmlns")
        graphml.set("xmlns:java", "http://www.yworks.com/xml/yfiles-common/1.0/java")
        graphml.set("xmlns:sys", "http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0")
        graphml.set("xmlns:x", "http://www.yworks.com/xml/yfiles-common/markup/2.0")
        graphml.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        graphml.set("xmlns:y", "http://www.yworks.com/xml/graphml")
        graphml.set("xmlns:yed", "http://www.yworks.com/xml/yed/3")
        graphml.set("xsi:schemaLocation",
                    "http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd")

        node_key = ET.SubElement(graphml, "key", id="data_node")
        node_key.set("for", "node")
        node_key.set("yfiles.type", "nodegraphics")

        # Definition: url for Node
        node_key = ET.SubElement(graphml, "key", id="url_node")
        node_key.set("for", "node")
        node_key.set("attr.name", "url")
        node_key.set("attr.type", "string")

        # Definition: description for Node
        node_key = ET.SubElement(graphml, "key", id="description_node")
        node_key.set("for", "node")
        node_key.set("attr.name", "description")
        node_key.set("attr.type", "string")

        # Definition: url for Edge
        node_key = ET.SubElement(graphml, "key", id="url_edge")
        node_key.set("for", "edge")
        node_key.set("attr.name", "url")
        node_key.set("attr.type", "string")

        # Definition: description for Edge
        node_key = ET.SubElement(graphml, "key", id="description_edge")
        node_key.set("for", "edge")
        node_key.set("attr.name", "description")
        node_key.set("attr.type", "string")

        edge_key = ET.SubElement(graphml, "key", id="data_edge")
        edge_key.set("for", "edge")
        edge_key.set("yfiles.type", "edgegraphics")

        graph = ET.SubElement(graphml, "graph", edgedefault=self.directed,
                              id=self.id)

        for node in self.nodes.values():
            graph.append(node.to_xml())

        for grp in self.groups.values():
            graph.append(grp.to_xml())

        for edge in self.edges.values():
            graph.append(edge.to_xml())

        self.graphml = graphml

    def write_graph(self, filename):
        """
        Write current graph object to file (Syntax is GraphML, compatible with Yed)

        :param str filename: absolute or relative path for output file (expect .graphml extension).
        """
        self._construct_graphml()

        tree = ET.ElementTree(self.graphml)
        tree.write(filename)

    def get_graph(self):
        """
        Render current object as xml code

        :return: XML code
        :rtype: str
        """
        self._construct_graphml()

        return ET.tostring(self.graphml, encoding='UTF-8').decode()

    def add_node(self, NodeClass, node_name, **kwargs):
        """
        Add node of type NodeClass to self.

        :param NodeType NodeClass: Node class must be child class of Node (e.g. ShapeNode, GenericNode, TableNode, UmlNode)
        :param str node_name: node title
        :param kwargs: Extra parameter to the Node class

        :return: child node created
        :rtype: instance of type NodeClass
        """
        node = NodeClass(node_name, parent=self, **kwargs)

        self.nodes[node.id] = node
        self.existing_entities[node.id] = node
        return node

    def add_edge(self, node1, node2, **kwargs):
        """
        Add an edge between both input nodes

        :param Node node1: First node object
        :param Node node2: Second node object
        :param kwargs: Extra parameters for the Edge object.

        :return: edge object
        :rtype: Edge
        """

        edge = Edge(node1, node2, parent=self, **kwargs)
        self.edges[edge.id] = edge
        return edge

    def add_group(self, name, **kwargs):
        """
        Add group to current object.

        :param str name: child group name
        :param kwargs: Extra parameters for the Group object

        :return: child group created
        :rtype: Group
        """
        group = Group(name, parent=self, **kwargs)
        self.groups[group.id] = group
        self.existing_entities[group.id] = group
        return group
