# py_euclidea
Python version of the Euclidea game for possible reinforcement learning agents (https://euclidea.xyz)

## Interactive mode
$ ./euclidea.py [series]/[level].py
for example
$ ./euclidea.py 02_beta/04_Angle30.py

Mouse:
* middle button: shift view
* wheel: zoom
* left button: use tool

Keyboard:
* Backspace: undo
* Tab: change goal (if there are more goal options)
* 'r': random level instance, recommended with the initial zoom and shift and without any constructions
* 'm': Move tool -- move any movable point (not recommended to move them in a way it would make the construction illegal)
* 'x': Point Tool -- click to an intersection, to a curve, or to the empty space
* 'c': Circle Tool X Y -- circle with center X passing through Y
* 'l': Line Tool X Y -- line passing through X and Y
* 'i': Intersection Tool a b -- all the intersections of curves a and b
* 'b': Bisector Tool X Y -- perpendicular bisector of the segmetn XY
* 't': Perp Tool l X -- line passing through X perpendicular to l
* 'h': Parallel Tool l X -- line passing through X parallel to l
* 'g': Compass Tool X Y Z -- circle with center Z and radius XY
* 'a': Angle Bisector Tool X Y Z -- bisector of the pair of rays YX, YZ.

## Files
* [number]_[greek_letter]/[something].py -- levels
* geo_object.py -- classes for geometrical types (Point, Line, Circle + drawing them)
* constructions.py -- helper functions for numerical constructions -- e.g. intersection of two lines
* tools.py -- implementation of the tools (Point, Compass, Intersection, ...)
* environment.py -- loading level, putting tools and goals together
* euclidea.py -- interactive program
* multi_level.py -- environment keeping multiple levels inside, intended for reinforcement learning agents, not tested yet
* level_guessing.py -- generation of pairs (picture, level index), intended for basic experiments with image recognition
* bruteforce.py -- experiments with finding short solutions of certain levels by examining all posibilities (not related to most of the previous)
