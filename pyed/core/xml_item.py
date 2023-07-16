import logging
from abc import ABCMeta

LOG = logging.getLogger(__name__)

class XmlItem(metaclass=ABCMeta):
    """
    Generic class to whom all graph object derive (node, group and edges)
    """
    # Variable to ensure unique ID of all nodes/groups/etc...
    identifier = None
    _class_counter = 0

    def __init__(self, parent):
        self.__class__._class_counter += 1
        self.counter = self.__class__._class_counter

        self.__class__.identifier = self.__class__.__name__

        self.parent = parent  # direct parent object (usually a graph or a group in which a node or edge is defined
        self.parent_graph = parent.parent_graph  # Graph object (i.e top level object of the xml structure)

    @property
    def id(self):
        return f"{self.identifier}_{self.counter}"
