.. include:: <s5defs.txt>

=====================
 Python basic course
=====================


.. contents::
    :class: handout

Overall course agenda:

 * Python reasons and basics;
 * standard library, basic operations;
 * Python data model, OOPing with Python;
 * other things that might be useful.

\ 
===============

.. class:: center

   :huge:`Python basics`

History of glorious Python
==========================

.. class:: small

     * Guido van Rossum - Benevolent Dictator For Life (BDFL)
     * CWI, Centre for Mathematics and Computer Science (Dutch)
     * Dec '89 - start, Feb '91 - first public release
     * new system arch needs new sysadmin tools, C is too complex,
       sh is too tied to system
     * ABC, revised and fixed 
     * Monty Python’s Flying Circus, no snakes 
     * Jun '94, "If Guido was hit by a bus?"
     * around Oct '96, Python code stuck deep inside Windows
     * Mar '01, Python Software Foundation
     * Dec '08, backward compatibility breaking Python 3.0

Python vs. ABC vs. C++
======================

.. class:: tiny

    +-----------------------------------------+----------------------------------------+
    | :small:`Python`                         | :small:`ABC`                           |
    |                                         |                                        |
    | .. class:: tiny                         | ::                                     |
    |                                         |                                        |
    |  ::                                     |                                        |
    |                                         |                                        |
    |   def words(document):                  |  HOW TO RETURN words document:         |
    |      collection = []                    |     PUT {} IN collection               |
    |      for line in document:              |     FOR line IN document:              |
    |          for word in line.split():      |        FOR word IN split line:         |
    |              if word not in collection: |           IF word not.in collection:   |
    |                 collection.append(word) |              INSERT word IN collection |
    |      return collection                  |     RETURN collection                  |
    +-----------------------------------------+----------------------------------------+
    | :small:`C++`                                                                     |
    | ::                                                                               |
    |                                                                                  |
    |   vector<string>                                                                 |
    |   words(istream &document) {                                                     |
    |       vector<string> res;                                                        |
    |       string word;                                                               |
    |       while (!document.eof()) {                                                  |
    |           document >> word;                                                      |
    |           if (find(res.begin(), res.end(), word) == res.end()) {                 |
    |               res.push_back(word);                                               |
    |           }                                                                      |
    |       }                                                                          |
    |       return res;                                                                |
    |   }                                                                              |
    +----------------------------------------------------------------------------------+

Arithmetic Python
=================

.. class:: small incremental

    * ``a = b = c = 5`` - assignment can be sequenced, but i's not a usual operator, so
      ``a = (b = 5)`` will fail with syntax error.
    * ``a = (3 + 6 * 7) / 5`` # ``a`` will be 9, nothing special here, except:
    * ``5/2 == 2``, but ``5/2.0 == 5.0/2 == 2.5`` - types are adjusted automagically.
    * ``123**123`` # 123 to the power of 123  will be very long (258 digits), but integer.
    * bitwise operations: ``|``- or, ``&``- and, ``^``- xor, ``~``- not, ``<< >>``- shifts

    ========= ============== ============================ =====================================
     Type      C type         Limits/precision             Comment
    ========= ============== ============================ =====================================
     int       long           -(2^63-1) \.. 2^63           fast and precise
     long      it's too cool  any integer of any size      slower, but unlimited and as precise
     float     double         1.7*10^308 (~15 digits)  
     complex   no such        two float parts              complex(1,2) == 1+2j
    ========= ============== ============================ =====================================
     
Sequence types
===============

.. class:: small incremental

    * strings: ``'abc\n'``, ``"abc\n"``, ``r'a\b\c'``, immutable
    * lists: ``[]``, ``[1,2,3,4,5]``
    * tuples: ``()``, ``(1,2,3,4,5)``, immutable

    Operations:

    * indexing: if ``a==[0,1,2,3,4]``; then ``a[2]==2``; ``a[2:4]==[2,3]``; ``a[1:4:2]==[1,3]``
    * negative indexing: ``a[-2]==3``; ``a[1:-1]=[1,2,3,4]``; ``a[-1:-4:-2]==[4,2]``
    * inclusion: ``2 in a == True``; ``12 in a == False``; ``5 not in a == True``
    * arithmetic: ``[2,4]+[3,5]==[2,4,3,5]``; ``[1,2]*3==[1,2,1,2,1,2]``
    * ``len(a)==5``; ``min(a)==0``; ``max(a)==4``; ``a.index(3)==3``; ``a.count(4)==1``

Mutable sequence operations
===========================

.. class:: small borderless

   We assume that ``a==[0,1,2,3,4]`` before each operation.

   +------------------------------------------------+----------------------------------------------+
   | .. class:: incremental                         | .. class:: incremental                       |
   |                                                |                                              |
   |  .. container::                                |  .. container::                              |
   |                                                |                                              |
   |   assignment:                                  |   deletion:                                  |
   |                                                |                                              |
   |   ================== ===================       |   ==================== =============         |
   |   ``a[3]=5``         ``[0,1,2,5,4]``           |   ``del a[2]``         ``[0,1,3,4]``         |
   |   ``a[2:4]=[9,8,7]`` ``[0,1,9,8,7,4]``         |   ``del a[2:4]``       ``[0,1,4]``           |
   |   ``a[1:4:2]=[9,8]`` ``[0,9,2,8,4]``           |   ``del`` ``a[1:4:2]`` ``[0,2,4]``           |
   |   ================== ===================       |   ==================== =============         |
   +------------------------------------------------+----------------------------------------------+

   +------------------------------------------------+----------------------------------------------+
   | .. class:: incremental                         | .. class:: incremental                       |
   |                                                |                                              | 
   |  .. container::                                |  .. container::                              | 
   |                                                |                                              | 
   |   extending:                                   |   =============== ===============            |
   |                                                |   ``a.remove(2)`` ``[0,1,3,4]``              |
   |   =================== ===================      |   ``a.pop(2)==2`` ``[0,1,3,4]``              |
   |   ``a.append(5)``     ``[0,1,2,3,4,5]``        |   ``a.reverse()`` ``[4,3,2,1,0]``            | 
   |   ``a.extend([5,6])`` ``[0,1,2,3,4,5,6]``      |   ``a.sort()``    ``[0,1,2,3,4]``            | 
   |   ``a.insert(3,9)``   ``[0,1,2,9,3,4]``        |   =============== ===============            | 
   |   =================== ===================      |                                              |
   +------------------------------------------------+----------------------------------------------+

Sets and frozensets
===================

.. class:: small borderless
   
    Sets can be created like this: ``set()``; ``set(1,2,3)``; ``{1,2,3}``.
    Frozensets are immutable sets: ``frozenset()``; ``frozenset(1,2,3)``.

    * membership: ``x in s``; ``x not in s``
    * sets relations: ``s1 <= s2``; ``s1 < s2``; ``s1 >= s2``; ``s1 > s2``
    * arithmetic: ``{1,2} | {2,3} == {1,2,3}``; ``{1,2} & {2,3} == {2}``; ``{1,2}-{2,3}=={1}``; ``{1,2}^{2,3}=={1,3}``

    Set, but not frozensets support:
    * operators ``|=``; ``&=``; ``-=``; ``^=``
    * methods ``add``; ``remove``; ``discard``; ``pop``; ``clear``

Dictionaries
============

.. class:: small

    ``dict()`` is mapping of some objects to some other objects. Also can be constructed
    with ``{}`` or ``{'a':2,3:(1,2)}``

    * ``len(d)``, ``d['a']``, ``del d['a']`` work just like with lists
    * ``'a' in d``, ``2 not in d`` work on the set of keys
    * ``d.get(2)`` returns ``None`` instead of error if key is not found

Logical operations
==================

.. class:: small

   * False values are: ``None``; ``False``; all zeros (``0``, ``0.0``, ``0L``);
     empty collections (``()``, ``[]``, ``{}``, ``set()``)
   * operators: ``and``, ``or``, ``not``
   * comparsions: ``<``, ``<=``, ``>``, ``>=``, ``==``, ``!=``, ``is``, ``is not``
   
