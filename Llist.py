# -*- coding:utf-8 -*-
from node import LNode
from error import LinkedListUnderflow


class LList(object):
    """
    单链表
    """
    def __init__(self):
        self._head = None 
        
    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        # 表头添加
        self._head = LNode(elem, self._head)

    def pop(self):
        # 删除表头节点
        if self._head is None:
            raise LinkedListUnderflow("in pop") 
        e = self._head.elem 
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self.next)
            return 
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
    
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head 
        if p.next is None:
            e = p.elem 
            self._head = None 
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None 
        return e
            

    