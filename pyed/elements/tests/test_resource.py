import pyed


def test_resource():
    """
    Test Resource constructor
    """
    g = pyed.Graph()

    ref_1 = "resource 1: qdsflkjhqsd fkljhqsd flkqj h"
    ref_2 = "resource 2: qdsflkjhqsd fkljhqsd flkqj h"

    ref_hash_1 = hash(ref_1)
    ref_hash_2 = hash(ref_2)

    # Sanity check to ensure hashes are indeed different
    assert ref_hash_1 != ref_hash_2

    # Ensure that adding the same resource yield the same id and we don't duplicate it in the graphml
    r_id_1 = g.add_resource(ref_1)
    r_id_1b = g.add_resource(ref_1)
    assert r_id_1 == r_id_1b

    # Test resource values
    r1 = g.resources[r_id_1]
    assert r_id_1 == r1.id
    assert r1.hash == ref_hash_1

    # Ensure a different resource is unique and get a different id
    r_id_2 = g.add_resource(ref_2)
    assert r_id_1 != r_id_2

    # Test resource values
    r2 = g.resources[r_id_2]
    assert r2.id == r_id_2
    assert r2.hash == ref_hash_2
