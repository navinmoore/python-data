# -*- coding:utf-8 -*-

from node import LNode
from error import LinkedListUnderflow

class LCLick:
    def __init__(self):
        self._rear = None 
    
    def is_empty(self):
        return self._rear is None 
    
    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
        else:
            p.next = self._rear.next
            self._rear.next = p
            
    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):
        # 删除前端
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CList")
        p = self._rear.next
        if self._rear is p:
            self._rear = None 
        else:
            self._rear.next = p.next
        return p.elem
