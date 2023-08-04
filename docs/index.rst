Welcome to Pyed's documentation!
================================
This package is yet another tool to help generate graph using Python + `Yed <https://www.yworks.com/products/yed>`_.

Other packages that exists (that took the best names):

* `Pyyed <https://github.com/jamesscottbrown/pyyed>`_ (My package is loosely based on this one)
* `Pygraphml <https://github.com/hadim/pygraphml>`_
* `NetworkX <https://networkx.org/documentation/stable/reference/readwrite/graphml.html>`_

My package focus on drawing simple graph to quickly visualise relations between informations. It's a crude subset of what graphs are capable of. My intent is to have a kind of `Inkscape <https://inkscape.org/release>`_, but for graph. `Yed <https://www.yworks.com/products/yed>`_ is that, but I don't want to add and draw manually dozen of nodes when trying to understand a datastructure or a code.

These pages are thought to provide quick documentation on what you can do with this package, especially the different types of nodes and the parameter and values available.

Why another package?
--------------------
I wanted functionalities that do not exist in those packages. I wanted a way to create package with enhanced data visualisation, in particular node with list of information (GenericNode in Pyed) and node with table of data (TableNode in Pyed) and custom nodes with any .svg file as a shape (SvgNode in Pyed).

Principle
-----------
This package will not create finalized graph on its own. You'll have to use `Yed <https://www.yworks.com/products/yed>`_ or another GUI that support .graphml to render the graph correctly. By default, node size is not adapted to its content, and all nodes are on top of eachother.


Check :ref:`installation` the project.

Contents
--------

.. toctree::

   source/intro
   source/sub-package
