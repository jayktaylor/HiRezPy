.. currentmodule:: hirezpy

API Reference
=============

The following section outlines the API of HiRezPy.

Client
------

.. autoclass:: Client
    :members:

Enums
-----

There are several enums used within HiRezPy to make it easier for you to configure the library for use how you like.

.. class:: Language

    Specifies the language being used within the library or per function.

    .. attribute:: english
    .. attribute:: german
    .. attribute:: french
    .. attribute:: spanish
    .. attribute:: spanish_latin
    .. attribute:: portuguese
    .. attribute:: russian
    .. attribute:: polish
    .. attribute:: turkish

.. class:: Endpoint

    Specifies the endpoint being used within the library or per function.

    .. attribute:: smitepc
    .. attribute:: smitexbox
    .. attribute:: smiteps
    .. attribute:: paladinspc

Data Classes
------------

These are the classes created by API responses. You shouldn't create these yourself. They hold the data that is responded from the API server in an easy to use way.

HrpObject
~~~~~~~~~

.. autoclass:: HrpObject
    :members:

Limits
~~~~~~

.. autoclass:: Limits
    :members:

Match
~~~~~

.. autoclass:: Match
    :members:

Player
~~~~~~

.. autoclass:: Player
    :members:

Rank
~~~~

.. autoclass:: Rank
    :members:

Character
~~~~~~~~~

.. autoclass:: Character
    :members:

God
~~~

.. autoclass:: God
    :members:

Ability
~~~~~~~

.. autoclass:: Ability
    :members:

GodAbility
~~~~~~~~~~

.. autoclass:: GodAbility
    :members:

Champion
~~~~~~~~

.. autoclass:: Champion
    :members:

ChampionAbility
~~~~~~~~~~~~~~~

.. autoclass:: ChampionAbility
    :members:
