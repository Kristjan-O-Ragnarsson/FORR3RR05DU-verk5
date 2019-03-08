import sys


class Node:
    """
    Node in a  double linked list
    :var self._next: reference to the next Node in the list
    :var self._prev: reference to the previous Node in the list
    """
    def __init__(self, _item: int, __prev=None, __next=None) -> None:
        """
        :var self.data: int value to be stored in this node
        :param _item:
        """
        self.data = _item
        self._prev = __prev
        self._next = __next

    def append(self, _item: int) -> bool:
        """
        Recursive function to append _item to the back of a linked list
        Time complexity: O(n)
        :param _item:
        :return boolean: true if succeeds in appending _item
        """
        if self._next:
            return self._next.append(_item)
        else:
            curr = Node(_item)
            self._next = curr
            curr._prev = self
            return True

    def print_list(self) -> None:
        """
        recursively prints the whole double linked list
        Time complexity: O(n)
        :return None:
        """
        if self._next:
            sys.stdout.write(str(self.data)+',')
            return self._next.print_list()
        else:
            sys.stdout.write(str(self.data) + '\n')
            return None

    def find(self, _item: int) -> bool:
        """
        A Linear serch function
        Time complexity: O(n)
        :param _item:
        :return Boolean: based on if _item is found in the list
        """
        if self.data == _item:
            return True
        else:
            return self._next.find()

    def delete(self, _item: int) -> bool:
        """
        A Delete function
        :param _item: item to delete
        :return: bool based on if the item was deleted
        """
        sys.stdout.write(str(self.data) + "," + str(_item) + "\n")
        if self.data == _item:
            sys.stdout.write("a")
            sys.stdout.write("a")

            try:
                self._prev._next = self._next
                self._next._prev = self._prev
            except AttributeError:
                self._prev._next = self._next
            return True

        else:
            return self._next.delete(_item)



if __name__ == '__main__':
    n = Node(2)
    n._next = Node(3)
    n.print_list()
