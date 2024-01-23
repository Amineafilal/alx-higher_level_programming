#!/usr/bin/python3
"""This module contains a class Node and a class SinglyLinkedList"""


class Node:
    """Represents a Node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a Node with data and an optional next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data attribute"""
        return self._data

    @data.setter
    def data(self, value):
        """Setter for data attribute with type validation"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Getter for next_node attribute"""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node attribute with type validation"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """Represents a Singly Linked List"""

    def __init__(self):
        """Initialize an empty Singly Linked List with a head"""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position"""
        new_node = Node(value)

        # Insert at the beginning if the list is empty
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        # Find the correct position to insert the new node
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        # Insert the new node into the sorted position
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list"""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
