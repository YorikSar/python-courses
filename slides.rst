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
   ``linesep``         line separator (``\r`` or ``\n`` or ``\r\n``)
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

\ 
===============

 :huge:`Object Oriented Programming in Python`

Basic types hierarchy
=====================

.. class:: small

 * ``object``
  
  - ``NoneType`` - singletone ``None``
  - ``NotImplementedType`` - singletone ``NotImplemented``
  - ``numbers.Number``
 
   * ``numbers.Integral`` - ``int``, ``long``, ``bool``
   * ``numbers.Real`` - ``float``
   * ``numbers.Complex`` - ``complex``
 
  - ``basestring``
   
   * ``str`` (``types.StringType``)
   * ``unicode`` (``types.UnicodeType``)

Old-style classes
=================

.. class:: center incremental big

  `Forget about them`

New-style classes
=================

.. class:: tiny

 .. list-table::
  :class: borderless

  * - .. class:: incremental

       .. container::

        Classes are declared like this:: 

         class C(object):
           cls_var = 123
           def __init__(self, param):
             self.obj_var = param
             self.cls_var += 1
           def f(self):
             print self.cls_var, self.obj_var

       .. container::

        Objects are created by calling a class::

         c = C(123)
         # ~
         c = C.__new__(123)
         c.__init__(123)

       .. container::

        Inheritance can be done as usual::
         
         class A(object):
           a = 1
         class B(A):
           b = 2
         class C(B):
           b = 3

    - .. class:: incremental

       .. container::

        Note that Python is very dynamic::

         class WeGetSignal(all_your_base()):
           """How are you gentlemen"""
           if are_belong_to_us():
             def make_your_time(self):
               move_zig()
           else:
             def make_your_time(self):
               for_greate_justice()

       .. container::

        In fact, class declaration equals to something like this::

         bases = (object,)
         body = "cls_var=123\ndef __init__(self, param):......"
         _attrs = {}
         eval(compile(body,__name__,'exec'),globals(),_attrs)
         C = type("C", bases, _attrs)

       .. container::

        You can not hide a name inside class, but you can::

         class C(object):
           _hint_to_hide = 0
               # polite programmers will not touch it
           def __obscure_hide():
               # will be converted to _C__obscure_hide
             pass

Special methods
===============

.. class:: small incremental

 All that ``__methods__`` are special methods, they are used instead of 
 operator overloading and lots of other class tuning. Examples:

 * ``__new__`` - create object or fine-tune object creation, mostly used in
   metaclasses;
 * ``__init__`` - constructor, object's variables declaration;
 * ``__del__`` is called when object is destroyed, but not necessary;
 * ``__str__``, ``__repr__`` are used to convert object to string like
   ``str(obj)`` or ``repr(obj)``, remember ``%s`` and ``%r`` formatting
 * ``__lt__``, ``__le__``, ``__gt__``, ``__ge__``, ``__eq__``, ``__ne__`` are
   used by all that comparsion operators, so that for example ``a<b`` is
   equivalent to ``a.__lt__(b)`` or ``b.__gt__(a)`` if the first one is not
   implemented or returns ``NotImplemented``
 * ``__cmp__`` does all what the previous ones does, returning negative,
   positive values or zero if object is less, greater or equals the parameter
   respectively.


Protocols
=========

.. class:: small

 There is number of so called protocols in Python. Protocol is some rules about
 class or object that must be met to make built-in functions work. 

 .. list-table::
  :class: borderless

  * - .. class:: incremental

       .. container::

        For example, ``for`` loop::
  
         for v in obj:
           do_it(v)
  
        equals to ::
         
         _it = obj.__iter__()
         while True:
           try:
             v = _it.next()
           except StopIteration:
             break
           do_it(v)

    - .. class:: incremental

       So, iterator protocol requires:
    
       * container to have ``__iter__`` method (which can be called throgh
         ``iter(obj)`` built-in) that returns iterator;
       * iterator to have ``next`` method which returns next element or raises
         ``StopIteration`` exception when passed through the end of container;
       * iterator to have ``__iter__`` method that returns iterator itself,
         just for completeness.

Decorators
==========

.. class:: tiny borderless
 
 .. list-table::

  * - .. class:: incremental

       .. container::

        ::

         @decorate
         def f(): pass

        equals to::

         def f(): pass
         f = decorate(f)

       .. container::

        you can do some function call::

         @decorate('like this')
         def f(): pass

       .. container::

        and you can decorate classes::

         @shiny
         class C(object): pass
    - .. class:: incremental

       .. container::

        decorators usually look like this::

         def decorate1(f):
           def _wrapped(*args,**kwargs):
             print "%s(*%s,**%s)" % \
                 (f.__name__,args,kwargs)
             return f(*args,**kwargs)
           return _wrapped

        .. **
       .. container::
        
        or like this::

         def decorate2(kind):
           def __inner(f):
             def _wrapped(*args,**kwargs):
               print "%s %s(*%s,**%s)" % \
                   (kind,f.__name__,args,kwargs)
               return f(*args,**kwargs)
             return _wrapped
           return __inner

        .. **

 .. list-table::

  * - .. class:: incremental

       .. container::

        so that:

        .. list-table::
         :class: borderless

         * - ::

              @decorate1
              def f1(a): return a+1

              @decorate2('Cute')
              def f2(a): return a-1
           - ::

              @decorate2('Shiny')
              def f3(a): return a*2
    - .. class:: incremental

       .. container::

        .. list-table::
         :class: borderless

         * - will cause::
              
              print f1(1)
              print f2(a=2)
              print f3(3,a=3)

           - to print::
              
              f1((1,),{})
              2
              Cute f2((),{'a':2})
              1
              Shiny f3((3,),{'a':3})
              ### ERROR!!!! ###

Class and static methods
========================

.. class:: tiny

 Of course you want to have methods bound not to object, but to class, or even
 unbound method encapsulated into class namespace.

 .. list-table::
  :class: borderless

  * - .. class:: incremental
    
       .. container::

        Class methods are bound to current class::

         class A(object):
           @classmethod
           def f(cls):
             return "%s.f" % (cls.__name__,)

         class B(A): pass

         A.f(), B.f() # => "A.f", "B.f"

       .. container::

        Static methods are totally unbound::

         class C(object):
           @staticmethod
           def f(): # No cls, no self
             pass

       Bound methods are methods which already have first argument substituted.
    - .. class:: incremental
      
       .. container::

        Let's say, you have::

         class A(object):
           def m(self): pass
           @classmethod
           def cls_m(cls): pass
           @staticmethod
           def st_m(): pass
         
         class B(A): pass

         a = A(); b = B()

       .. container::

        Then methods will be bound like this:

        .. list-table::
         :header-rows: 1
         :class: center

         * - f
           - ``A.f``
           - ``B.f``
           - ``a.f``
           - ``b.f``
         * - ``m``
           - no
           - no
           - ``a``
           - ``b``
         * - ``cls_m``
           - ``A``
           - ``B``
           - ``A``
           - ``B``
         * - ``st_m``
           - no
           - no
           - no
           - no

       .. container::

        To access overloaded method, you should use built-in method ``super``::

         super(C,obj).meth # => meth bound to a parent of C

       Yes, I'm lying again.

Properties
==========

.. class:: small
 
 .. list-table::
  :class: borderless

  * - .. class:: incremental
      
       .. container::
       
        Sometimes you want some syntax sugar to make your life easier and access
        computed values as object's fields, not as method result::
       
         class C(object):
           def getx(self):
             return self._x
           def setx(self,value):
             self._x = value
           def delx(self):
             del self._x
           x = property(getx, setx, delx)

       .. container::

         So that::

          c.x       # ~ c.getx()
          c.x = 123 # ~ c.setx(123)
          del c.x   # ~ c.delx()
     
    - .. class:: incremental
    
       .. container::
          
        Note that all arguments except the first one are optional, so ``property`` can
        be used as decorator::
       
         class C(object):
           @property
           def x(self):
             return self._x
           @x.setter
           def x(self,value):
             self._x = value
           @x.deleter
           def x(self):
             del self._x

Attribute lookup
================

.. class:: small incremental
 
 .. container::
  
  You may wonder how ``.`` "operator" works. Here are few easy steps:
 
  #. look in obj.__dict__
  #. look in type(obj) and its parents
  #. call ``__getattr__``, ``__setattr__`` or ``__delattr__``
 
 .. container::
  
  So default behaviour can be mimiced like this::
   
   class C(object):
     def __getattr__(self,name):
       try:
         return self.__dict__[name]
       except KeyError:
         raise AttributeError
     def __setattr__(self,name,value):
       self.__dict__[name] = value
     def __delattr__(self,name):
       del self.__dict__[name]

Exceptions
==========

.. class:: small incremental

 Python supports very common exception handling process: if comewhere some
 error occurs, exception is raised at that level, then stack is unwinded to
 find first sutable exception handler, which is then executed.

 Raised exception consists of type, value and traceback. They can be retrieved
 with ``sys.exc_info()`` call.

 .. container::

  Whole syntax of ``raise`` statement is::

   raise [<type>[,<value>[,<traceback>]]]]
 
 When called without arguments, it reraises last raised exception (or raises
 ``TypeError`` if there isn't one).

 When called with one argument, it can be either exception type (which is
 instantiated and raised)or exception object (which is just raised).

 Traceback is set to current location in stack or to the third argument, if it
 is present.

Exception handling
==================

.. class:: small

 .. container::

  Exception can be handled using try..except block::
 
   try:
     do_something()
   except ExceptionType:
     handle_exception()
   except (ExceptionType1, ExceptionType2) as exc:
     handle(exc)
   else:
     hail_somebody_for_clean_execution()
   finally:
     do_cleanup_anyway()

Exception hierarchy
===================

.. class:: tiny

 * ``BaseException``

  * ``SystemExit``
  * ``KeyboardInterrupt``
  * ``Exception``
   
   * ``StandardError``

    * ``ArithmeticError``
     
     * ``ZeroDivisionError``
     * ``OvervlowError``

    * ``LookupError``

     * ``IndexError``
     * ``KeyError``

\ 
===

 :huge:`Useful stuff`

Generators
==========

.. class:: tiny
 
 Let's say, you want to create some sequence of elements that require some
 computation, e.g. sequence of logarithms of counting numerals.

 .. list-table::
  :class: borderless

  * - .. class:: incremental
       
       .. container::
        
        You can create a function returning list of necessary length::
      
         def logs(n):
           res = []
           for i in range(1,n+1):
             res.append(math.log(i))
           return res

       But it consumes a lot of memory for big ``n`` and a very lot of time to
       compute the whole thing

       .. container::

        Remember iterator protocol? You can use it::

         class logs(object):
           def __init__(self, n):
             self.i = 0
             self.n = n
           def __iter__(self):
             return self
           def next(self):
             if self.i >= self.n:
               raise StopIteration
             else:
               self.i += 1
               return math.log(self.i)

    - .. class:: incremental
       
       It doesn't consume more memory for bigger ``n`` and computes values as
       they needed, but it looks *ugly*.

       .. container::

        So they decided to make life easier and let ugly iterators look like
        cute functions::

         def logs(n):
           for i in range(1,n+1):
             yield math.log(i)

        It almost equivalent to previous class, but uses 3 lines.

       .. container::

        Since such logic is very popular, there is even shorter option::
        
         (math.log(i) for i in range(1,n+1))

       Or if you want a list, just use ``[]`` instead of ``()``.

       .. container::

        Generator expressions support filtering too::

         (math.log(i) for i in range(1,n+1) if i%2==1)

       .. container::

        This ``for``\-``if``\s can even be nested (just like usual ``for``\s
        and ``if``\s::
         
         (a+b for a in range(5) if a%2==0 \
              for b in range(2*a) if b%4==1)

Generator functions
===================

.. class:: tiny

 .. list-table::
  :class: borderless

  * - .. class:: incremental

       .. container::

        Look at this generator function::

         def gen(param):
           startup()
           yield start_value
           while main_loop():
             do_logic()
             yield intermediate
             if do_more_logic():
               yield something_other

       .. container::

        It looks very much like coroutine, so after a lot of efforts they made
        coroutines almost clear in Python::

         def player(game):
           collect_chips()
           yield READY
           while True:
             try:
               compute_bet()
               their_bets = (yield our_bet)
             except TableFolded:
               gather_chips()
               move_to_next_table()
             except GeneratorExit:
               exchange_chips()
               break

    - .. class:: incremental

       .. container::

        Note that ``yield``\s now can expect some return values, and even can
        be source of exceptions. This is achieved through this methods of
        generators produced by this functions:

        .. list-table::

         * - ``next()``
           - old one, does nothing special
         * - ``send(value)``
           - injects ``value`` as result of ``yield``
         * - ``throw(t[,v[,tb]])``
           - raises exception at the point of ``yield``
         * - ``close()``
           - raises ``GeneratorExit``

       Every call resumes generator at the point it was paused and returns
       value gathered by next ``yield`` or propagates any unhandled exception
       occured inside generator. ``close`` is special since it silently eats
       ``StopIteration`` and ``GeneratorExit`` exceptions and raises
       ``RuntimeError`` if generator tries to return something more to caller.

Context managers
================

.. class:: tiny

 .. list-table::
  :class: borderless

  * - .. class:: incremental

       .. container::

        You might remember that parrern that appeared around file handling
        (archives in our case)::

         fil = open('thefile', 'w')
         fil.write(smth)
         process(fil)
         fil.close()

       .. container::

        But what will happen if we get come error e.g. in ``process()``?
        ``fil`` will remain open with proper consequences. So we should use
        ``finally``::

         fil = open('thefile', 'w')
         try:
           fil.write(smth)
           process(fil)
         finally:
           fil.close()

       .. container::

        Here is inconsistence: we have to remember what cleanup operations
        should be done after the work with object is done. Here come context
        managers::

         with open('thefile', 'w') as fil:
           fil.write(smth)
           process(fil)

    - .. class:: incremental

       .. container::
          
        Context manager protocol consists of two methods:

        ============= =========================================================
        ``__enter__`` called at ``with``, returned value goes to variable after
                      ``as``
        ``__exit__``  called when block ends with exception's triplet (or
                      ``None``\s)
        ============= =========================================================

       Note that variable after ``as`` gets not context manager itself, but
       some other value returned by ``__enter__`` (well, in case of ``file``,
       it is ``self``).

       There is couple of handy methods in ``contextlib`` (in number of 2):
       
       * ``closing`` closes everything that can be closed::

          with closing(socket()) as sock:
            sock.connect(....)
            ....

       * ``contextmanager`` decorator allows you to create a context manager
         without all that ``__`` burden::

          @contextlib.contextmanager
          def closing(obj):
            try:
              yield obj
            finally:
              obj.close()

Slots
=====

.. class:: small incremental
 
 .. container::

  You may have noted that every object requires a dictionary instance for its
  ``__dict__``, which doesn't looks good for classes that contains one or two
  fields.

 .. container::

  For such types you can list all possible attributes in ``__slots__`` and then
  no dict will be created::

   class Slots(object):
     __slots__ = ('a', 'b', 'c')
     def __init__(self):
       self.a = 1
       self.b = 2
       self.cc = 3  # AttributeError!

 Couple of facts:

 * if you need to add not listed attribute, add ``__dict__`` to ``__slots__``
   list;
 * if one of base classes already have ``__dict__``, slots definition is
   meaningless;
 * derived classes will have ``__dict__`` by default;
 * you can not set default values for slots in class level, it'll overwrite
   slot's meaning.

Metaclasses
===========

.. class:: small incremental

 .. container::

  Remember class creation process? You can tweak even this part! ::

   bases = (object,)
   body = "cls_var=123\ndef __init__(self, param):......"
   _attrs = {}
   eval(compile(body,__name__,'exec'),globals(),_attrs)
   C = type("C", bases, _attrs)

 .. container::

  After this code, ``C`` becomes an object of class ``type``. And you can
  inherit from class ``type`` just like from any other class.

 .. container::

  ::

   class my_type(type):
     def __new__(mcs, name, bases, attrs):
       # do anything you want with attrs, for example
       return super(my_type,mcs).__new__(mcs, name, bases, attrs)

 Frameworks use this to add custom getters/setters to this class or some
 classes connected to it, you can replace or tweak any method of new class.
