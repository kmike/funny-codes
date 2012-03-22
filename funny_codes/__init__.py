# -*- coding: utf-8 -*-
from __future__ import absolute_import
from random import choice

class FunnyCodes(object):
    """
    Class for generating random strings of a given pattern
    and measuring some metrics.
    """

    LETTER_GROUPS = [
        u"AEIOUY",
        u"BCDFGHJKLMNPQRSTVXZ",
        u"123456789",
    ]

    def __init__(self, pattern):
        self.pattern = pattern

    def next(self):
        """ Returns next random string """
        return u"".join(self._get())

    def __iter__(self):
        return self

    def variants_count(self):
        """
        Returns the maximum number of unique strings that
        can be generated using this pattern.
        """
        num = 1
        for letter, group in self._pattern_groups():
            num *= len(group) if group else 1
        return num

    def collision_prob(self, n):
        """
        Returns the approximate probability of collision within ``n``
        generated strings for this pattern.

        See http://en.wikipedia.org/wiki/Birthday_problem#Generalizations
        """
        d = self.variants_count()
        return 1.0 - ((d-1.0)/d)**(n*(n-1)/2)

    def expected_collisions(self, n):
        """
        Returns the expected number of collisions when
        ``n`` strings are generated.
        """
        d = float(self.variants_count())
        return n - d + d*((d-1)/d)**n

    def _pattern_groups(self):
        for letter in self.pattern:
            for group in self.LETTER_GROUPS:
                if letter in group:
                    yield letter, group
                    break
            else:
                yield letter, None

    def _get(self):
        for letter, group in self._pattern_groups():
            yield choice(group) if group else letter



class RuFunnyCodes(object):
    """
    Класс для генерации случайных номеров по шаблону.
    """
    LETTER_GROUPS = [
        u"АЕИОУЫЭЮЯ",
        u"БВГДЖЗКЛМНПРСТФХЦЧ",
        u"123456789",
    ]

