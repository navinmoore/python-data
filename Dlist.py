# -*- coding:utf-8 -*-
from Llist import LList
from node import DNode
from error import LinkedListUnderflow

class DLList(LList):
    def __init__(self):
        super().__init__()
    
    def prepent(self, elem):
        p = DNode(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p
        
    def append(self, elem):
        p = DNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop of DLList")
        s = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise 
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e

        