from pyed.core import dict_parser
import pytest


def test_dict_parser():
    """
    Test dict_to_graph function
    """
    indict = {1: {'1a': None},
              2: None,
              3: {'3a': {'3aa': None}}}

    graph = dict_parser.dict_to_graph(indict)

    n1, n1a, n2, n3, n3a, n3aa = list(graph.nodes.values())
    e1, e2, e3 = list(graph.edges.values())

    assert n1.name == "1"
    assert n1a.name == "1a"
    assert n2.name == "2"
    assert n3.name == "3"
    assert n3a.name == "3a"
    assert n3aa.name == "3aa"

    assert e1.node1.name == n1.name
    assert e1.node2.name == n1a.name

    # Due to the recursive nature of the function, edge3 is created before edge2
    assert e3.node1.name == n3.name
    assert e3.node2.name == n3a.name

    assert e2.node1.name == n3a.name
    assert e2.node2.name == n3aa.name
