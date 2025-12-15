Usage guide
===========

Installation
------------

Install SignalPlot into your environment:

.. code-block:: bash

   pip install signalplot

Or, from a clone of the repository in editable mode:

.. code-block:: bash

   pip install -e .


Quick start
-----------

The basic pattern is:

1. Import Matplotlib and SignalPlot.
2. Call :func:`signalplot.apply` once.
3. Use plain Matplotlib to create figures.
4. Save with :func:`signalplot.save` or ``plt.savefig`` (after patching).

.. code-block:: python

   import matplotlib.pyplot as plt
   import signalplot as sp

   sp.apply()

   x = [1, 2, 3, 4]
   y = [2, 3, 2.5, 4]

   fig, ax = plt.subplots()
   ax.plot(x, y)
   ax.set_title("Example series")

   sp.finish(ax)
   sp.save("example.png")
   plt.show()


Direct labels and events
------------------------

SignalPlot prefers direct labels and simple, explicit event markers over
heavy legends and decorations.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   import signalplot as sp

   sp.apply()

   x = np.arange(0, 36)
   y = np.cumsum(np.random.default_rng(0).normal(size=x.size))

   fig, ax = plt.subplots()
   ax.plot(x, y)

   sp.direct_label(ax, x[-1], y[-1], "Series A", dx=0.5)
   sp.event_line(ax, x=18, text="Policy change")
   sp.finish(ax)

   sp.save("direct_label_event.png")
   plt.show()


Honest bar charts
-----------------

Bar charts should start at zero to preserve scale honesty. Use
``force_bar_zero`` to enforce this when needed.

.. code-block:: python

   import matplotlib.pyplot as plt
   import signalplot as sp

   sp.apply()

   categories = ["Residential", "Commercial", "Industrial"]
   values = [120, 150, 95]

   fig, ax = plt.subplots()
   ax.bar(categories, values, color="0.6")
   ax.set_title("Average demand by sector")

   sp.force_bar_zero(ax)
   sp.finish(ax)

   sp.save("bar_honest_scale.png")
   plt.show()


