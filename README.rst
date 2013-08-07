``checkin.py``
==============
Dead simple time tracking tool I have been using for the last 2 years.

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


                            Total balance: -153h 26m

"Total balance" indicates how many more hours you should work this month
(configurable using the ``HOURS_PER_MONTH`` variable, defaults to 160).
Balance is carried over to the next month.

To fix up things (e.g. you forgot to check in/out), you can also pass in a time argument::

   check in 8:15
   check out 19:45  # 24 hour time format!
