Defaults and saving
====================

Call :func:`signalplot.apply` **once** near the start of your script or
notebook. It updates Matplotlib ``rcParams`` with SignalPlot’s figure,
axes, typography, and ``savefig`` defaults. It does not replace
``pyplot``; you keep using normal Matplotlib calls afterward.

When to call ``apply()``
------------------------

- **Do** call it before creating figures if you want the style contract
  (white background, hidden top/right spines, restrained type, save
  defaults).
- **Skip** it only when you intentionally want an unstyled or
  third-party-styled figure in the same process; mixing styles in one
  session is possible but easy to get wrong.

Saving figures
--------------

:func:`signalplot.save` writes the current figure using the same keyword
arguments as ``matplotlib.pyplot.savefig``, but fills in dpi,
``bbox_inches``, and colors from ``rcParams`` (which ``apply()`` set).
Override any parameter per call when you need an exception::

    sp.save("figure.png")
    sp.save("poster.png", dpi=600)

``savefig`` is an alias for ``save`` for people who prefer Matplotlib’s
name.

``SaveDefaults`` and ``apply()``
--------------------------------

You can pass a custom :class:`signalplot.SaveDefaults` into ``apply()`` to
change the defaults that later flow into ``save()`` and into
``rcParams["savefig.*"]``::

    from signalplot import SaveDefaults, apply

    apply(save=SaveDefaults(dpi=400))

Patching ``plt.savefig``
------------------------

:func:`signalplot.patch_pyplot` wraps ``matplotlib.pyplot.savefig`` so
plain ``plt.savefig("x.png")`` picks up the same defaults. Use this only
if you control the whole process; it is a global monkey patch. Tests run
this in a **subprocess** to avoid cross-test pollution.

Escape hatches
--------------

- Adjust one-off parameters on ``ax`` or ``fig`` after plotting; ``apply()``
  does not block that.
- Call ``matplotlib.rcParams.update({...})`` after ``apply()`` for
  targeted overrides (accept that you are leaving the strict style
  contract).
- Pass explicit ``dpi``, ``facecolor``, and so on to ``save()`` when a
  single export needs different settings than the rest of the document.
