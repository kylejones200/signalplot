Labels, events, and notes
=========================

SignalPlot favors **direct labels** and light annotation over heavy
legends. Helpers in ``signalplot.labels`` are meant to be called **after**
you have plotted data so positions and limits are known.

Direct labels
-------------

:func:`signalplot.direct_label` places a short text near a point on a
series—useful for the last observation or a representative point instead
of a legend entry.

Events and emphasis
---------------------

:func:`signalplot.event_line` draws a vertical marker with optional text
for policy changes, releases, or interventions.

:func:`signalplot.accent_point` and :func:`signalplot.emphasize_last`
highlight individual observations using the single restrained accent
color (``signalplot.ACCENT``).

Notes
-----

:func:`signalplot.note` adds a small text box for caveats or units. Keep
copy short; long notes belong in captions or prose outside the figure.

Finish before save
------------------

Call :func:`signalplot.finish` (or ensure you have applied the tidy/finish
pattern you want) **before** saving so labels and spines are in their
final state.
