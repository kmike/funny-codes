===========
funny-codes
===========

This is a small module for generating randoms strings of a given pattern.
It is also capable of estimating various metrics for this pattern
(probability of collision, estimated collision count and total variants count).

Installation
============

::

    $ pip install funny-codes

Usage
=====

::

    >>> from funny_codes import FunnyCodes
    >>> my_codes = FunnyCodes('TATAN-76')
    >>> my_codes.next() # the following is a random code matching the pattern
    HIPAS-12

    >>> my_codes.next()
    MOVER-87

    >>> my_codes.variants_count()
    20000844

    >>> my_codes.collision_prob(1000)
    0.024664677603280283

    >>> my_codes.expected_collisions(10000)
    2.499235797673464

