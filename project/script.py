# -*- coding: utf-8 -*-
"""This is a module demonstrating a script

A collection of functions that print 'script'.

Example:
    This is an example that exemplifies in the ``Example`` section::
        $ python script.py

New Section.

Attributes:
    module_variable (str): A variable mentioned in the ``Attributes`` section:

Todo:
    * Something with your life.

.. _This is a link: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

"""

module_variable = 'script'


def printscript():
    """Prints 'script'

    Args:

    Returns:
        str: The string returned

    """

    print(module_variable)
    return module_variable


def script_generator(n):
    """Generates repeated words.

    Args:
        n(int): The upper limit of the number of the range to generate

    Yields:
        str: the `module_variable`

    Examples:
        Doctest example.

        >>> print([s for s in script_generator(3)])
        ['script', 'script', 'script']

    """
    for i in range(n):
        yield module_variable


if __name__ == "__main__":
    import doctest
    doctest.testmod()
