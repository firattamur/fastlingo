class Node:
    """A node for a double linked list."""

    def __init__(self, key: str, value: str) -> None:
        """Initialize a node for a double linked list.

        Args:
            key   (str): The key of the node.
            value (str): The value of the node.
        """

        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def to_dict(self) -> dict:
        """Convert the Node object to a dictionary.

        Returns:
            dict: A dictionary representation of the Node object.
        """
        return {
            "key": self.key,
            "value": self.value,
            "next": self.next.to_dict() if self.next else None,
            "prev": self.prev.to_dict() if self.prev else None,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create a Node object from a dictionary.

        Args:
            data (dict): A dictionary containing the Node object data.

        Returns:
            Node: A Node object created from the dictionary.
        """
        node = cls(data["key"], data["value"])
        if data["next"]:
            node.next = cls.from_dict(data["next"])
        if data["prev"]:
            node.prev = cls.from_dict(data["prev"])
        return node


class DoubleLinkedList:
    """A double linked list."""

    def __init__(self) -> None:
        """Initialize a double linked list."""

        self.head = None
        self.tail = None

    def append(self, key: str, value: str) -> None:
        """Append a node to the double linked list.

        Args:
            key   (str): The key of the node.
            value (str): The value of the node.
        """

        node = Node(key, value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def remove(self, node: Node) -> None:
        """Remove a node from the double linked list.

        Args:
            node (Node): The node to remove.
        """

        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    def move_to_end(self, node: Node) -> None:
        """Move a node to the end of the double linked list (tail) to make sure it is the most recently used.

        Args:
            node (Node): The node to move to the end.
        """

        self.remove(node)
        self.append(node.key, node.value)
