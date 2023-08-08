import logging
import os.path

import yaml
import textwrap
from .. import elements

LOG = logging.getLogger(__name__)


def _parse_graph(x, g, parent_node=None):
    """
    Recursive function to parse the whole dictionnary

    :param x: Input dict
    :param g: Input Pyyed Graph
    :param parent_node: parent object

    :return: Output Pyed graph
    """
    node_kwargs = dict(background="#99cdff")
    edge_kwargs = dict(color="#0101cf")
    for k, v in x.items():

        # automatic line wrap at 23 characters.
        nodename = textwrap.fill(str(k), width=22)

        current_node = g.add_node(elements.ShapeNode, nodename, **node_kwargs)

        if isinstance(v, dict):
            g = _parse_graph(v, g, parent_node=current_node)

        # relations needs to be created after, because for some reason it will create the node if it doesn't exist yet.
        if parent_node is not None:
            g.add_edge(parent_node, current_node, **edge_kwargs)

    return g


def yaml_to_graph(filename):
    """
    Read a Yaml file dictionnary and make a graphML out of it.

    Though we expect a strict format, you can look in pyed/core/dict_parser.py to derive your own parser

    Example input file:
    1:
        1a:
            1aa:
        1b:
    2:
    3:
        3a:

    :param str filename: Input Yaml file with a dictionnary. Each element must end with ":" with no other argument
    """
    basename, in_ext = os.path.splitext(filename)
    out_filename = f"{basename}.graphml"

    with open(filename, 'r') as stream:
        graph_dict = yaml.safe_load(stream)

    dict_to_graph(graph_dict, out_filename)


def dict_to_graph(indict, outfilename=None):
    """
    Process a dictionnary to write the corresponding graph.

    Mainly used to parse a Yaml file, you can use this function directly. This is the format we expect:
    {1: {'1a': {'1aa': None}, '1b': None},
    2: None,
    3: {'3a': None}}

    :param str indict: Leaf of the graph is designed by "leaf: None" in the dict tree
    :param str outfilename: [optional] Filename for .graphml output file

    :return: Object created out of the dictionnary
    :rtype: Pyed.Graph
    """
    g = elements.Graph()
    g = _parse_graph(indict, g=g)

    if outfilename is not None:
        g.write_graph(outfilename)

    return g
