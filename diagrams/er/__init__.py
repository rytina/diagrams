"""
ER provides a set of classes for creating entity relationship diagrams.
"""

from diagrams import Node, Edge


class Entity(Node):
    _provider = "er"
    _icon_dir = "resources/er"
    _type = "entity"

    def __init__(self, name: str, **attrs):
        super().__init__(name, **attrs)


class Relationship(Edge):
    _provider = "er"
    _icon_dir = "resources/er"
    _type = "relationship"

    def __init__(self, name: str, **attrs):
        super().__init__(name, **attrs)


class Attribute(Node):
    _provider = "er"
    _icon_dir = "resources/er"
    _type = "attribute"

    def __init__(self, name: str, **attrs):
        super().__init__(name, **attrs)
