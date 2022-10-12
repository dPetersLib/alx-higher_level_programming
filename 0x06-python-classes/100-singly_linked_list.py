#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node
    
    @property
    def data(self):
        return self.__data
    
    @property
    def next_node(self):
        return self.__next_node
    
    @data.setter
    def data(self, value):
        if type(value) == int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")
    
    @next_node.setter
    def next_node(self, value):
        if type(value) == None or type(value) == Node:
            self.__next_node = value
        else:
            raise TypeError("ext_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.__head = None
    
    def sorted_insert(self, value):
        node = Node(value)
        if self.__head == None:
            self.__head = node
        else:
            current_node = self.__head
            while current_node.next_node != None:
                current_node = current_node.next_node
            current_node.next_node = node
    
    def print_list(self):
        current_node = self.__head
        while current_node.next_node != None:
            print("{}".format(current_node.data))
            current_node = current_node.next_node
