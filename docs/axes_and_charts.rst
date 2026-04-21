Axes and chart helpers
========================

SignalPlot keeps drawing in Matplotlib. Helpers in ``signalplot.axes``
tidy frames, tune common chart types, and enforce honest scales where
that matters.

Typical order
-------------

1. Build the figure with ``plt.subplots``, :func:`signalplot.figure`, or
   :func:`signalplot.small_multiples`.
2. Plot data with ordinary ``ax.plot``, ``ax.bar``, and so on.
3. Optionally call **style** helpers such as :func:`signalplot.style_line_plot`,
   :func:`signalplot.style_scatter_plot`, or :func:`signalplot.style_bar_plot`
   when you want consistent line weights, marker restraint, or bar
   treatment without repeating kwargs.
4. Call :func:`signalplot.tidy_axes` or :func:`signalplot.finish` for spine
   cleanup and light layout polish (see API docs for exact behavior).
5. Save with :func:`signalplot.save`.

Bar charts and zero baselines
------------------------------

For magnitude comparisons, bar charts should read from a **zero**
baseline. :func:`signalplot.force_bar_zero` helps enforce that when an
axis range has drifted.

Small multiples
---------------

:func:`signalplot.small_multiples` returns a figure and a flat list of
axes with ``tidy_axes`` already applied, sized for a simple grid. Use it
when you want comparable panels without hand-rolling ``subplots`` every
time.

Uncertainty bands
-------------------

:func:`signalplot.band` is a thin ``fill_between`` wrapper for intervals
or envelopes. It stays on the same axes as your main series.
