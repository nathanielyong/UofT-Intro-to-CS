"""CSC111 Winter 2021 Assignment 1: Linked Lists, Part 1

Instructions (READ THIS FIRST!)
===============================

Please write your tests for Part 1 in this module. Make sure to review the assignment
instructions carefully for this part! You may find it helpful to consult this
section of the Course Notes:
https://www.teach.cs.toronto.edu/~csc110y/fall/notes/B-python-libraries/02-pytest.html

While you must include unit tests, you may also use property-based tests in your test suite.

We will *not* be running PythonTA on this file; however, you should follow good programming
design and style in this file anyway, just like you would for all other work.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu and Isaac Waller.
"""
import pytest
from a1_part1 import MoveToFrontLinkedList, SwapLinkedList, CountLinkedList


# --------------- MoveToFrontLinkedList (mtfll) tests -------------------------
def test_mtfll_zero_nodes_false() -> None:
    """Test __contains__ method for MoveToFrontLinkedList when linked list has zero nodes.
    Check that the function returns false."""
    lst = MoveToFrontLinkedList([])
    expected = False
    actual = lst.__contains__(1)
    assert expected == actual


def test_mtfll_one_node_true() -> None:
    """Test __contains__ method for MoveToFrontLinkedList when linked list has one node.
    Check that the function returns true when item is in the linked list."""
    lst = MoveToFrontLinkedList([1])
    expected = True
    actual = lst.__contains__(1)
    assert expected == actual


def test_mtfll_one_node_false() -> None:
    """Test __contains__ method for MoveToFrontLinkedList when linked list has one node.
    Check that the function returns true when item is in the linked list."""
    lst = MoveToFrontLinkedList([1])
    expected = False
    actual = lst.__contains__(0)
    assert expected == actual


def test_mtfll_many_nodes_true_first_node() -> None:
    """Test __contains__ method for MoveToFrontLinkedList when linked list has multiple nodes.
    Check that the function returns true when item to be found is the first node"""
    lst = MoveToFrontLinkedList([1, 2, 3, 4, 5])
    expected = True
    actual = lst.__contains__(1)
    assert expected == actual


def test_mtfll_many_nodes_true_interior_node() -> None:
    """Test __contains__ method for MoveToFrontLinkedList when linked list has multiple nodes.
    Check that the function returns true when item to be found is an interior node (not the first or last node)"""
    lst = MoveToFrontLinkedList([1, 2, 3, 4, 5])
    expected = True
    actual = lst.__contains__(3)
    assert expected == actual


def test_mtfll_many_nodes_true_last_node() -> None:
    """Test __contains__ method for MoveToFrontLinkedList when linked list has multiple nodes.
    Check that the function returns true when item to be found is the last node"""
    lst = MoveToFrontLinkedList([1, 2, 3, 4, 5])
    expected = True
    actual = lst.__contains__(5)
    assert expected == actual


def test_mtfll_many_nodes_false() -> None:
    """Test __contains__ method for MoveToFrontLinkedList when linked list has multiple nodes.
    Check that the function returns false when item is not found."""
    lst = MoveToFrontLinkedList([1, 2, 3, 4, 5])
    expected = False
    actual = lst.__contains__(0)
    assert expected == actual


def test_mtfll_zero_nodes_no_mutation() -> None:
    """Test __contains__ method for MoveToFrontLinkedList.
    Check that the function does not mutate a zero node linked list."""
    lst = MoveToFrontLinkedList([])
    lst_copy = lst.to_list()
    lst.__contains__(0)
    assert lst.to_list() == lst_copy


def test_mtfll_one_node_no_mutation() -> None:
    """Test __contains__ method for MoveToFrontLinkedList.
    Check that the function does not mutate a one node linked list that contains the item."""
    lst = MoveToFrontLinkedList([1])
    lst_copy = lst.to_list()
    lst.__contains__(1)
    assert lst.to_list() == lst_copy


def test_mtfll_one_node_no_mutation2() -> None:
    """Test __contains__ method for MoveToFrontLinkedList.
    Check that the function does not mutate a one node linked list that does not contain the item."""
    lst = MoveToFrontLinkedList([1])
    lst_copy = lst.to_list()
    lst.__contains__(0)
    assert lst.to_list() == lst_copy


def test_mtfll_many_nodes_mutation_interior_node() -> None:
    """Test __contains__ method for MoveToFrontLinkedList.
    Check that the function mutates linked list with multiple nodes,
    when the item to be found is an interior node (not the first or last node),
    by moving it to the front of the list"""
    lst = MoveToFrontLinkedList([1, 2, 3, 4, 5])
    lst.__contains__(3)
    assert lst.to_list() == [3, 1, 2, 4, 5]


def test_mtfll_many_nodes_mutation_last_node() -> None:
    """Test __contains__ method for MoveToFrontLinkedList.
    Check that the function mutates linked list with multiple nodes,
    when the item to be found is the last node, by moving it to the front of the list"""
    lst = MoveToFrontLinkedList([1, 2, 3, 4, 5])
    lst.__contains__(5)
    assert lst.to_list() == [5, 1, 2, 3, 4]


def test_mtfll_many_nodes_no_mutation() -> None:
    """Test __contains__ method for MoveToFrontLinkedList.
    Check that the function does not mutate a linked list with multiple nodes if the item is not found."""
    lst = MoveToFrontLinkedList([1, 2, 3, 4, 5])
    lst_copy = lst.to_list()
    lst.__contains__(0)
    assert lst.to_list() == lst_copy


def test_mtfll_many_nodes_no_mutation_first_node() -> None:
    """Test __contains__ method for MoveToFrontLinkedList.
    Check that the function does not mutate a linked list with multiple nodes
    if the first node contains the item to be found"""
    lst = MoveToFrontLinkedList([1, 2, 3, 4, 5])
    lst_copy = lst.to_list()
    lst.__contains__(1)
    assert lst.to_list() == lst_copy


# --------------- SwapLinkedList (sll) tests -------------------------
def test_sll_zero_nodes_false() -> None:
    """Test __contains__ method for SwapLinkedList when linked list has zero nodes.
    Check that the function returns false."""
    lst = SwapLinkedList([])
    expected = False
    actual = lst.__contains__(1)
    assert expected == actual


def test_sll_one_node_true() -> None:
    """Test __contains__ method for SwapLinkedList when linked list has one node.
    Check that the function returns true when item is in the linked list."""
    lst = SwapLinkedList([1])
    expected = True
    actual = lst.__contains__(1)
    assert expected == actual


def test_sll_one_node_false() -> None:
    """Test __contains__ method for SwapLinkedList when linked list has one node.
    Check that the function returns true when item is in the linked list."""
    lst = SwapLinkedList([1])
    expected = False
    actual = lst.__contains__(0)
    assert expected == actual


def test_sll_many_nodes_true_first_node() -> None:
    """Test __contains__ method for SwapLinkedList when linked list has multiple nodes.
    Check that the function returns true when item to be found is the first node."""
    lst = SwapLinkedList([1, 2, 3, 4, 5])
    expected = True
    actual = lst.__contains__(1)
    assert expected == actual


def test_sll_many_nodes_true_interior_node() -> None:
    """Test __contains__ method for SwapLinkedList when linked list has multiple nodes.
    Check that the function returns true when item to be found is an interior node (not first or last node)."""
    lst = SwapLinkedList([1, 2, 3, 4, 5])
    expected = True
    actual = lst.__contains__(3)
    assert expected == actual


def test_sll_many_nodes_true_last_node() -> None:
    """Test __contains__ method for SwapLinkedList when linked list has multiple nodes.
    Check that the function returns true when item to be found is the last node."""
    lst = SwapLinkedList([1, 2, 3, 4, 5])
    expected = True
    actual = lst.__contains__(5)
    assert expected == actual


def test_sll_many_nodes_false() -> None:
    """Test __contains__ method for SwapLinkedList when linked list has multiple nodes.
    Check that the function returns false when item is not found."""
    lst = SwapLinkedList([1, 2, 3, 4, 5])
    expected = False
    actual = lst.__contains__(0)
    assert expected == actual


def test_sll_zero_nodes_no_mutation() -> None:
    """Test __contains__ method for SwapLinkedList.
    Check that the function does not mutate a zero node linked list."""
    lst = SwapLinkedList([])
    lst_copy = lst.to_list()
    lst.__contains__(0)
    assert lst.to_list() == lst_copy


def test_sll_one_node_no_mutation() -> None:
    """Test __contains__ method for SwapLinkedList.
    Check that the function does not mutate a one node linked list that contains the item."""
    lst = SwapLinkedList([1])
    lst_copy = lst.to_list()
    lst.__contains__(1)
    assert lst.to_list() == lst_copy


def test_sll_one_node_no_mutation2() -> None:
    """Test __contains__ method for SwapLinkedList.
    Check that the function does not mutate a one node linked list that does not contain the item."""
    lst = SwapLinkedList([1])
    lst_copy = lst.to_list()
    lst.__contains__(0)
    assert lst.to_list() == lst_copy


def test_sll_many_nodes_mutation_interior_node() -> None:
    """Test __contains__ method for SwapLinkedList.
    Check that the function mutates linked list with multiple nodes,
    when the item to be found is an interior node, by swapping it with the node before."""
    lst = SwapLinkedList([1, 2, 3, 4, 5])
    lst.__contains__(3)
    assert lst.to_list() == [1, 3, 2, 4, 5]


def test_sll_many_nodes_mutation_last_node() -> None:
    """Test __contains__ method for SwapLinkedList.
    Check that the function mutates linked list with multiple nodes,
    when the item to be found is the last node, by swapping it with the node before."""
    lst = SwapLinkedList([1, 2, 3, 4, 5])
    lst.__contains__(5)
    assert lst.to_list() == [1, 2, 3, 5, 4]


def test_sll_many_nodes_no_mutation() -> None:
    """Test __contains__ method for SwapLinkedList.
    Check that the function does not mutate a linked list with multiple nodes if the item is not found."""
    lst = SwapLinkedList([1, 2, 3, 4, 5])
    lst_copy = lst.to_list()
    lst.__contains__(0)
    assert lst.to_list() == lst_copy


def test_sll_many_nodes_no_mutation2() -> None:
    """Test __contains__ method for SwapLinkedList.
    Check that the function does not mutate a linked list with multiple nodes
    if the first node contains the item to be found"""
    lst = SwapLinkedList([1, 2, 3, 4, 5])
    lst.__contains__(1)
    assert lst.to_list() == [1, 2, 3, 4, 5]


# --------------- CountLinkedList (cll) tests -------------------------
def test_cll_zero_nodes_false() -> None:
    """Test __contains__ method for CountLinkedList when linked list has zero nodes.
    Check that the function returns false."""
    lst = CountLinkedList([])
    expected = False
    actual = lst.__contains__(1)
    assert expected == actual


def test_cll_one_node_true() -> None:
    """Test __contains__ method for CountLinkedList when linked list has one node.
    Check that the function returns true when item is in the linked list."""
    lst = CountLinkedList([1])
    expected = True
    actual = lst.__contains__(1)
    assert expected == actual


def test_cll_one_node_false() -> None:
    """Test __contains__ method for CountLinkedList when linked list has one node.
    Check that the function returns true when item is in the linked list."""
    lst = CountLinkedList([1])
    expected = False
    actual = lst.__contains__(0)
    assert expected == actual


def test_cll_many_nodes_true_first_node() -> None:
    """Test __contains__ method for CountLinkedList when linked list has multiple nodes.
    Check that the function returns true when item to be found is the first node."""
    lst = CountLinkedList([1, 2, 3, 4, 5])
    expected = True
    actual = lst.__contains__(1)
    assert expected == actual


def test_cll_many_nodes_true_interior_node() -> None:
    """Test __contains__ method for CountLinkedList when linked list has multiple nodes.
    Check that the function returns true when item to be found is an interior node."""
    lst = CountLinkedList([1, 2, 3, 4, 5])
    expected = True
    actual = lst.__contains__(3)
    assert expected == actual


def test_cll_many_nodes_true_last_node() -> None:
    """Test __contains__ method for CountLinkedList when linked list has multiple nodes.
    Check that the function returns true when item to be found is the last node."""
    lst = CountLinkedList([1, 2, 3, 4, 5])
    expected = True
    actual = lst.__contains__(5)
    assert expected == actual


def test_cll_many_nodes_false() -> None:
    """Test __contains__ method for CountLinkedList when linked list has multiple nodes.
    Check that the function returns false when item is not in the linked list."""
    lst = CountLinkedList([1, 2, 3, 4, 5])
    expected = False
    actual = lst.__contains__(0)
    assert expected == actual


def test_cll_zero_nodes_no_mutation() -> None:
    """Test __contains__ method for CountLinkedList.
    Check that the function does not mutate a zero node linked list."""
    lst = CountLinkedList([])
    lst_copy = lst.to_list()
    lst.__contains__(0)
    assert lst.to_list() == lst_copy


def test_cll_one_node_no_mutation() -> None:
    """Test __contains__ method for CountLinkedList.
    Check that the function does not mutate a one node linked list that contains the item."""
    lst = CountLinkedList([1])
    lst_copy = lst.to_list()
    lst.__contains__(1)
    assert lst.to_list() == lst_copy


def test_cll_one_node_no_mutation2() -> None:
    """Test __contains__ method for CountLinkedList.
    Check that the function does not mutate a one node linked list that does not contain the item."""
    lst = CountLinkedList([1])
    lst_copy = lst.to_list()
    lst.__contains__(0)
    assert lst.to_list() == lst_copy


def test_cll_many_nodes_no_mutation() -> None:
    """Test __contains__ method for CountLinkedList.
    Check that the function does not mutate a linked list with multiple nodes if the item is not found."""
    lst = CountLinkedList([1, 2, 3, 4, 5])
    lst_copy = lst.to_list()
    lst.__contains__(0)
    assert lst.to_list() == lst_copy


def test_cll_many_nodes_no_mutation2() -> None:
    """Test __contains__ method for CountLinkedList.
    Check that the function does not mutate a linked list with multiple nodes
    if the first node contains the item to be found"""
    lst = CountLinkedList([1, 2, 3, 4, 5])
    lst.__contains__(1)
    assert lst.to_list() == [1, 2, 3, 4, 5]


def test_cll_many_nodes_mutation_interior_node() -> None:
    """Test __contains__ method for CountLinkedList.
    Check that the function mutates linked list with multiple nodes
    when the item to be found is an interior node, by moving it before all nodes with a smaller access_count."""
    lst = CountLinkedList([1, 2, 3, 4, 5])
    lst.__contains__(3)
    assert lst.to_list() == [3, 1, 2, 4, 5]


def test_cll_many_nodes_mutation_last_node() -> None:
    """Test __contains__ method for CountLinkedList.
    Check that the function mutates linked list with multiple nodes
    when the item to be found is the last node, by moving it before all nodes with a smaller access_count."""
    lst = CountLinkedList([1, 2, 3, 4, 5])
    lst.__contains__(5)
    assert lst.to_list() == [5, 1, 2, 3, 4]


def test_cll_many_nodes_tie_handling() -> None:
    """Test __contains__ method for CountLinkedList.
    Check that the function does not move nodes in front of other nodes with a higher or equal access_count
    In the following test, the 4 should not be moved in front of the 1 because the access_counts are equal."""
    lst = CountLinkedList([1, 2, 3, 4, 5])
    lst.__contains__(1)
    lst.__contains__(4)
    assert lst.to_list() == [1, 4, 2, 3, 5]


if __name__ == '__main__':
    pytest.main(['a1_part1_test.py', '-v'])
