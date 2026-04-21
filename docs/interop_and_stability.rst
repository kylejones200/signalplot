Interoperability and API stability
===================================

Headless and servers
----------------------

Set the backend to ``Agg`` (or another non-interactive backend) **before**
importing ``pyplot`` if you run without a display::

    import matplotlib
    matplotlib.use("Agg")

    import matplotlib.pyplot as plt
    import signalplot as sp

The documentation build and tests use this pattern. Close figures you no
longer need (``plt.close(fig)`` or ``plt.close("all")``) when generating
many plots in one process to limit memory growth.

Jupyter and Quarto
-------------------

Call ``apply()`` in the first cell of a notebook (or once per Quarto
chunk that defines plotting) so all subsequent cells share the same
defaults. Inline displays use the active backend; ``save()`` still
writes files when you export for publication.

Stability expectations
-----------------------

Names listed in ``signalplot.__all__`` are the **intended public
surface** for semantic versioning: breaking changes should come with a
major version bump. Callers should import from the ``signalplot``
package rather than submodules (``signalplot.style``, ``signalplot.axes``,
and so on), since submodule layout may evolve as long as the top-level
exports remain compatible.

Helpers beyond the short list documented as “stable high-level API” in
the package docstring may still change in minor releases if the README
style contract stays satisfied—when in doubt, pin your dependency
version and read the changelog.
