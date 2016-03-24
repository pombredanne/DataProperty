# encoding: utf-8

'''
@author: Tsuyoshi Hombashi
'''


from __future__ import absolute_import

from ._align import Align
from ._typecode import Typecode


class AlignGetter(object):

    @property
    def typecode_align_table(self):
        raise NotImplementedError()

    @typecode_align_table.setter
    def typecode_align_table(self, x):
        self.__typecode_align_table = x

    def get_align_from_typecode(self, typecode):
        return self.__typecode_align_table.get(typecode, Align.LEFT)

    def __init__(self):
        self.typecode_align_table = {
            Typecode.STRING: Align.LEFT,
            Typecode.INT: Align.RIGHT,
            Typecode.FLOAT: Align.RIGHT,
        }

align_getter = AlignGetter()