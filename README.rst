``checkin.py``
==============
Dead simple time tracking tool I have been using for the last 4 years.

Keeps track of your hours in a JSON file (``hours.json``). A human-readable version
of that database is stored in ``hours.txt``.

Use like this::

   check in
   # worky worky ...
   check out

Now have a look at ``~/hours.txt``::

   August 2013
   ====================
   Wed, 07. Aug    08:00 - 15:26 = 7:26:09

                            Total: 7h 26m


                            Total missing: 153h 26m

"Total missing" indicates how many more hours you should work this month
(configurable using the ``HOURS_PER_MONTH`` variable, defaults to 160).
Balance is carried over to the next month.

To fix up things (e.g. you forgot to check in/out), you can also pass in a time argument::

   check in 8:15
   check out 19:45  # 24 hour time format!

You could pass in an optional message for each record. The message may be a project name, specific ticket or tags list.::

   check in "working on ticket #7777"

Result::

   November 2017
   ====================
   Thu, 16. Nov	20:00 -  NOW  = 0:00:00  'working on ticket #7777'

                         Total: 0h 0m


   Total missing: 160h 0m

You could correct the message on check out if you like.::

   check out "working on ticket #8888"
Result::

   November 2017
   ====================
   Thu, 16. Nov	20:00 - 20:02 = 0:01:44  'working on ticket #8888'

                           Total: 0h 1m


   Total missing: 159h 58m

It works simlesly with specific time.::

   check in 19:00 "working on ticket #3333"

Result::

   November 2017
   ====================
   Thu, 16. Nov	20:00 - 20:02 = 0:01:44  'working on ticket #8888'
   Thu, 16. Nov	19:00 -  NOW  = 1:06:00  'working on ticket #3333'

                         Total: 1h 7m


   Total missing: 158h 52m

So you could correct the message with specific time as well.::

   check out 19:40 "working on ticket #4444"

Result::

    November 2017
    ====================
    Thu, 16. Nov	20:00 - 20:02 = 0:01:44  'working on ticket #8888'
    Thu, 16. Nov	19:00 - 19:40 = 0:39:28  'working on ticket #4444'

                         Total: 0h 41m


    Total missing: 159h 18m

