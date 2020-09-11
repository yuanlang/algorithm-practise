# Task
# A Node class is provided for you in the editor. A Node object has an 
# integer data field, data, and a Node instance pointer, next, pointing 
# to another node(i.e.: the next node in a list).
# A removeDuplicates function is declared in your editor, which takes a 
# pointer to the head node of a linked list as a parameter. 
# Complete removeDuplicates so that it deletes any duplicate nodes 
# from the list and returns the head of the updated list.
# Note: 
# The head pointer may be null, indicating that the list is empty. 
# Be sure to reset your  pointer when performing deletions to avoid breaking the list.

#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    if head == None:
        head = new_node
        return head
    node = head
    while node != None and node.next != None:
        node = node.next
    node.next = new_node
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
