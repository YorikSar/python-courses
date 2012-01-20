.. include:: <s5defs.txt>

=====================
 Python basic course
=====================

:Author: Yuriy Taraday
:Contact: yorik.sar@gmail.com; ytaraday@mirantis.com

.. contents::
    :class: handout

Overall course agenda:

 * Python reasons and basics;
 * standard library, basic operations;
 * Python data model, OOPing with Python;
 * other things that might be useful.

\
===============

.. class:: center huge

   Python basics

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

    * indexing: if ``a==[0,1,2,3,4]``: then ``a[2]==2``; ``a[2:4]==[2,3]``; ``a[1:4:2]==[1,3]``
    * negative indexing: ``a[-2]==3``; ``a[1:-1]=[1,2,3]``; ``a[-1:-4:-2]==[4,2]``
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
   * comparsions can be chuncked: ``a < b < c < d < e`` ~ ``(a<b) and (b<c) and (c<d) and (d<e)``

String formatting
=================

.. class:: tiny

   ..

    ``"Where is my %dth %s?" % (10, "shoe")``

   Oldschool string formatting looks very much like formatting in C:

    ``%<mapping><flags><width><precision><type>``

   Where:

   * ``<mapping>`` can be reference to a key in mapping (if there is one after ``%`` operator)
     like ``"%(a)d %(b)s" % {'a': 1, 'b': "as"}``
   * ``<flags>`` is zero or more flags:

     * ``0`` fills empty space to the right side of value with zeroes or spaces
     * ``-`` ajusts value to the left hand
     * ``+`` adds sign before numeral value
     * `` `` adds space before positive numeral
   * ``<width>`` is field width
   * ``<precision>`` is dot folowed by number of meaningful digits after the decimal point
   * ``<type>`` is one of ``s``, ``d``, ``o``, ``h``, etc. Just like in C, but you'll need anything
     but ``s`` very rarely.

   Examples:

   .. class:: borderless

   =========================== ====== =============
   ``"%05s" % ("abc",)``       ``=>`` ``"  abc"``
   ``"%-+7.2f" % (10.34567,)`` ``=>`` ``"+10.35 "``
   =========================== ====== =============

If operator
===========

.. class:: small borderless

  Python has no operator brackets. Neither {} from C nor begin..end from Pascal
  survived. Blocks are distinguised by indent (spaces or tabs, tabs are bad).
  Colon is for clearness only.

  There is no switch operator in Python, it can be modeled by if..elif.

  +------------------------+------------------------+------------------------+
  | .. class:: incremental | .. class:: incremental | .. class:: incremental |
  |                        |                        |                        |
  |  .. container::        |  .. container::        |  .. container::        |
  |                        |                        |                        |
  |   Basic:               |   switch-like:         |   False conds are:     |
  |                        |                        |                        |
  |   ::                   |   ::                   |   * None               |
  |                        |                        |   * False              |
  |    if cond1:           |    if a == 1:          |   * 0, 0L, 0.0, 0+0j   |
  |      op1               |      op1               |   * (), [], {}, set()  |
  |    elif cond2:         |    elif a == 2:        |   * any other object   |
  |      op2               |      op2               |     that can tell us   |
  |    elif cond3:         |    elif a == 3:        |     that it's false or |
  |      op3               |      op3               |     empty or zero      |
  |    else:               |    else:               |                        |
  |      op4               |      op4               |                        |
  +------------------------+------------------------+------------------------+

Loops
=====

.. class:: tiny borderless

  +-----------------------------------------------+---------------------------------------------------+
  | There are just two loops:                     | .. class:: incremental                            |
  |                                               |                                                   |
  | .. class:: incremental                        |  .. container::                                   |
  |                                               |                                                   |
  |  .. container::                               |   ``for`` loop is way more powerfull: ::          |
  |                                               |                                                   |
  |   ``while`` loop is as simple as ::           |    for name in sequence:                          |
  |                                               |      ops                                          |
  |    while cond1:                               |                                                   |
  |      op1                                      |   ``name`` iterates over each element of          |
  |                                               |   sequence. Sequence can be string, tuple,        |
  |   Nothing special                             |   list, set, dict or of any other type that       |
  +-----------------------------------------------+   defines itself as iterable. If you iterate over |
  | .. class:: incremental                        |   dict, you iterate over its keys.                |
  |                                               +---------------------------------------------------+
  |  .. container::                               | .. class:: incremental                            |
  |                                               |                                                   |
  |   If you want to mimic ordinal C for loop: :: |  .. container::                                   |
  |                                               |                                                   |
  |    for (i=0; i<5; i++)                        |   To iterate over sequence with index, use        |
  |                                               |   ``enumerate`` function: ::                      |
  |   You should use ``range`` func: ::           |                                                   |
  |                                               |    for i,e in enumerate(seq):                     |
  |    for i in range(5):                         |                                                   |
  |                                               |   Here ``i`` will be zero-based index of element  |
  |   ``range`` can take up to 3 args like slice  |   in ``e`` while ``e`` iterates over sequence as  |
  |   operator: ::                                |   usual                                           |
  |                                               |                                                   |
  |    range(3) == [0,1,2]                        |  .. container::                                   |
  |    range(2,4) == [2,3]                        |                                                   |
  |    range(1,4,2) == [1,3]                      |   Note that you can use this comma trick in       |
  |                                               |   assignment:                                     |
  |                                               |                                                   |
  |                                               |   =============== = ===================           |
  |                                               |   ``a,b = (1,2)`` ~ ``a=1; b=2``                  |
  |                                               |   ``a,b = b,a``   ~ ``_t=a; a=b; b=_t``           |
  |                                               |   =============== = ===================           |
  |                                               |                                                   |
  |                                               |   It's named packing (on the left side) and       |
  |                                               |   unpacking (on the right one).                   |
  +-----------------------------------------------+---------------------------------------------------+

Functions
=========

.. class:: tiny borderless

  .. list-table::

   * - Functions are defined like this: ::

        def f(param1, param2, param3):
          op1
          op2
          return value

       .. class:: incremental

        .. container::

         Note that you can use packing to return several
         values at a time: ::

          def f(a,b,c):
            return a+b, b+c

          x, y = f(1,2,3) # x==3; y==5

        .. container::

         You can set a default values to arguments and
         pass only necessary ones: ::

          def f(a,b,c=4,d=5):
            pass

          f(a,b,d=8)

        .. container::

         Note that you should use ``global`` to modify global vars::

          a, b = 1, 2
          def f():
            global a
            a, b = 3, 4
          f() # a==3, b==2

     - .. class:: incremental

        .. container::

         You even can pass all parameters at once: ::

          args = [1,2,3,4]
          f(*args) # => f(1,2,3,4)

        .. **

        .. container::

         Or receive variable number of parameters: ::

          def f(*args):
            pass

          f(1,2,3,4) # => args == (1,2,3,4)

         .. **
        .. container::

         You can do bulk passing with skipped args
         too: ::

          args = [1,2,3,4]
          kwargs = {'d': 5, 'e': 6}
          f(*args,**kwargs) # ~ f(1,2,3,4,d=5,e=6)

         .. **

        .. container::

          And receive them too: ::

           def f(a,b,**kwargs): pass
           f(1,2,f=5,z=4) # => a==1,b==2,
                          # kwargs=={'f':5,'z':4}

Modules
=======

.. class:: small borderless

  Every ``.py`` file is a module in Python. You can use it from outside easily:

  .. list-table::

   * - a.py ::

        def f(a,b):
          return a**2 + b**2
        C = 25

     - b.py ::

        import a
        assert a.f(2,3) == a.C

  Modules are looked for in directories in ``sys.path`` list:

  .. list-table::

   * - ::

        import sys
        sys.path.append('path/to/my/modules')
        import mymodule

  Note that module's body is executed on import.

Evals in Python
===============

.. class:: small borderless incremental

 .. container::

   Function ``eval`` evaluates string of Python code in some context::

    globals = {'a': 1}
    locals = {'b': 2}
    eval("a,b = 3,4", globals, locals)
        # globals=={'a': 1}, locals=={'b': 4}

 .. container::

   You can access global and local dicts of curren block with ``globals()`` and
   ``locals()`` functions. ``a = 1`` is equivalent of ``locals()['a'] = 1``.

 .. container::

   So ``import <name>`` process looks like this::

    filename = find_module("<name>")
    body = open(filename).read()
    <name> = module("<name>")
    eval(compile(body, filename, 'exec'), {}, <name>.__dict__)

Evals in Python 2
=================

.. class:: small borderless

 .. list-table::

  * - .. class:: incremental 
       
       .. container::
          
        And you can use it to argument your module depending on some external
        conditions:
         
        .. list-table::
         :class: borderless

         * - a.py::

              if we_got_windows:
                def do_it():
                  do_it_windows_style()
              else:
                def do_it():
                  do_it_easy_way()
         * - b.py::
             
              import a
              do_it() # Will do it right way 
                      # on any OS

    - .. class:: incremental

       .. container::
         
        By the way, functions can use this dynamic too::
     
         def get_f(zero, value):
           if zero:
             def f(a):
               return 0
           else:
             def f(a):
               return a*value
           return f
         f1 = get_f(True, 5)
         f2 = get_f(False, 5)
         f1(4) # => 0
         f2(4) # => 20

Packages
========

.. class:: small

   .. container::

      Modules can be grouped into modules - directories with special
      ``__init__.py`` file. Contents of this file are attached to package and
      all modules inside this package become accessible through the dot after
      package name:

      .. list-table::
        :class: borderless

        * - a/__init__.py::

             CC = 5

          - a/bb.py::

             ZZ = 6

          - main.py::

             import a
             a.CC # works
             a.bb # error - a.bb is not imported yet
             import a.bb
             a.bb.ZZ # works

\
=========

:huge:`Standard Library`

 There is about 200 standard modules and packages in Python. We'll look into
 some of them.

Module: sys
===========

.. class:: small

   Contains lots of OS-agnostic runtime interpretator's stuff

   ================================= ==================================
   ``argv``                          like (argc, argv) in C
   ``exit(n)``                       exit with status n (default 0), like ``return`` from ``main`` in C
   ``platform``                      current platform (linux, windows, darwin)
   ``stdin``, ``stdout``, ``stderr`` standard i/o streams
   ``version``                       Python's version
   ================================= ==================================

Module: os
==========

.. class:: small

   OS-specific stuff, partly available on all OS's

   =================== ==============================
   ``environ``         dict containing all OS environment variables
   ``curdir``          symbol for current dir (dot)
   ``sep``, ``altsep`` path separator (``\`` or ``/`` or even ``:``)
   ``pathsep``         paths list separator (``:`` or ``;``)
   ``linesep``         line separator (``\n`` or ``\n`` or ``\r\n``)
   =================== ==============================
   
   ====================== =========================================
   ``chdir(dir)``         change current dir
   ``getcwd()``           get current dir
   ``chmod(path[,mode])`` change file access flags (n/a on Windows)
   ``listdir(dir)``       contents of dir
   ``mkdir(dir[,mode])``  create dir with access flags
   ``remove(path)``       delete file
   ``rmdir(path)``        delete dir
   ``rename(src,dst)``    rename path
   ====================== =========================================

Module: os.walk()
=================

.. class:: small

   Function ``os.walk(dir)`` allows you to walk around directory tree. ::

    for root, dirs, files in os.walk(dir):
      print "In dir %s:" % (root,)
      print "Dirs:"
      for d in dirs:
        print d
      print "Files:"
      for f in files:
        print f

Module: zipfile
===============

.. class:: small

   Everything for your zip file management::

    import zipfile

    f = zipfile.ZipFile('myfile.zip','a')
                            # can be 'r' or 'w'
    f.write('myfile.txt')
    f.write('theirfile.txt', 'othername.txt')
    print f.open('somefile.txt').read()
    f.close()

