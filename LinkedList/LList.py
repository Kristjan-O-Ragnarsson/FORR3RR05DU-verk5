import sys

from LinkedList import Node


class LList:
    """
    Linked list class using the node class
    """

    def __init__(self) -> None:
        """
        :var self._head: the root of the Linked List
        """
        self._head = None

    def push(self, _item: int) -> None:
        """
        Push _item to head
        :param _item:
        :return None:
        """
        x = self._head is not None
        new_node = Node(_item)
        new_node._next = self._head
        self._head = new_node
        try:
            self._head._next._prev = self._head
        except AttributeError:
            pass

    def append(self, _item: int) -> bool:
        """
        Append item to the back of Linked List
        :param _item:
        :return: Bool based on if it succeded adding item to the back of list
        """
        if self._head:
            return self._head.append(_item)
        else:
            self.push(_item)
            return True

    def print_list(self) -> None:
        """
        Printing function for Linked List
        :return: None
        """
        if self._head:
            self._head.print_list()
        else:
            sys.stdout.write("Empty list")

    def delete(self, _item: int) -> bool:
        """
        A function that should make the garbage bollector delet the node
        :param _item:
        :return: bool
        """
        #sys.stdout.write("00\n")
        if self._head is None:
            #sys.stdout.write("11\n")
            return False
        elif self._head.data == _item:
            #sys.stdout.write("20\n")
            if self._head._next is None:
                #sys.stdout.write("21\n")
                self._head = None
            else:
                #sys.stdout.write("22\n")
                self._head = self._head._next
                self._head._prev = None
            return True
        else:
            #sys.stdout.write("31\n")
            return self._head.delete(_item)

    def find(self, _item: int) -> bool:
        """
        find function for linked list
        :param _item:
        :return: bool
        """
        if self._head:
            return self._head.find(_item)
        else:
            return False


if __name__ == '__main__':
    _l = LList()
    _l.push(2)
    _l.push(3)
    _l.push(4)
    _l.push(5)
    _l.push(6)
    _l.print_list()
    _l.delete(2)
    _l.append(1)
    _l.delete(6)
    _l.print_list()
    sys.stdout.write(str(_l.find(1)))
    #sys.stdout.write("err")
