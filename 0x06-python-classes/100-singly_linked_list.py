#!/usr/bin/python3
"""Singly Linked List

This module implements a singly linked list.
The nodes of this linkedlist is sorted in ascendin order
according to their data.
"""


class Node:
    """Node for a singlylinkedlist

    This class defines a node of a singly linked list.
    As with every singlylinkedlist's node, it has two components:
    A data component and a pointer to the next node.

    """

    def __init__(self, data, next_node=None):
        """This is the constructor method for the Node.

        This constructor method is call just once,
        i.e. when an instance of this class is initiated.

        Args:
            data (int): The data component
            next_node (Node): The pointer to the next node

        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """This returns the data of the node"""
        return self.__data

    @property
    def next_node(self):
        """This returns the pointer to the next_node"""
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) == int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @next_node.setter
    def next_node(self, value):
        if type(value) is None or type(value) == Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """A SinglyLinkedList definition

    This is a class that defines a singly linked list.
    The List has Nodes and the nodes are sorted and printed in
    acending order.

    """

    def __init__(self):
        """This is the constructor method for the SinglyLinkedList.

        This constructor method is call just once,
        i.e. when an instance of this class is initiated.

        """
        self.__head = None

    def sorted_insert(self, value):
        """Sort the List and insert the node

        This method inserts a new Node into the correct sorted position
        in the list (increasing order).
        The purpose of the while loop (in the first else clause) is
        to get the insertion position.
        ie. The node before and after the insertion point
        i.e. the node with be inserted inbtwn prev_node and current_node

        Args:
            value (Node): Node to be inserted.

        """
        node = Node(value)
        if self.__head is None:
            self.__head = node
        else:
            current = self.__head
            prev_node = None
            while current.next_node is not None and node.data > current.data:
                prev_node = current
                current = current.next_node
            if node.data <= self.__head.data:
                self.__head = node
            if node.data <= current.data:
                node.next_node = current
                if prev_node:
                    prev_node.next_node = node
            else:
                current.next_node = node

    def __str__(self):
        """Object Representation definition.

        This method defines how the singlelinkedlist is to be represented
        when used in a print statement and thereabout.

        Return:
            It prints the data of each node
            till it gets to the end of the list,
            thereafter, it returns the data of the last node thereby
            printing it also.

        """
        current_node = self.__head
        if current_node is not None:
            while current_node.next_node is not None:
                print("{}".format(current_node.data))
                current_node = current_node.next_node
            return "{}".format(current_node.data)
        return ""
