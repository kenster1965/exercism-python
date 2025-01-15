"""Tree Building"""

class Record:
    """Record class"""
    def __init__(self, record_id, parent_id):
        """Record constructor"""
        self.record_id = record_id
        self.parent_id = parent_id
        print(f"** {self.record_id=} {self.parent_id=}")


class Node:
    """Node class to represent a tree node."""
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

    def __repr__(self):
        return f"Node({self.node_id})"


def BuildTree(records):
    """
    Build a tree from a list of records.

    :param records: list: A list of records, each containing `record_id` and `parent_id`.
    :return: Node: The root node of the tree.
    """
    if not records:
        return None

    # Sort
    records.sort(key=lambda r: r.record_id)
    for i, record in enumerate(records):
        if record.record_id != i:
            raise ValueError("Record id is invalid or out of order.")

    # Check root
    root_record = records[0]
    if root_record.record_id != 0 or root_record.parent_id != 0:
        raise ValueError("Node parent_id should be smaller than it's record_id.")

    # Made nodes
    nodes = {record.record_id: Node(record.record_id) for record in records}
    for record in records:
        if record.record_id < record.parent_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")
        if record.record_id != 0 and record.record_id == record.parent_id:
            raise ValueError("Only root should have equal record and parent id.")

        if record.record_id != 0:  # Skip the root
            parent = nodes[record.parent_id]
            parent.children.append(nodes[record.record_id])

    return nodes[0]  # Root node
