# -*- coding:utf-8 -*-
"""
节点
"""
class LNode(object):
    def __init__(self, elem, next_):
        self.elem = elem
        self.next = next_


class DNode(LNode):
    """
    包含一个前驱和一个后继
    """
    def __init__(self, elem, prev=None, next_=None):
        super().__init__(elem, next_)
        self.prev = prev