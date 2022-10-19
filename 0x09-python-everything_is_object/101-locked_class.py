#!/usr/bin/python3
"""LockedClass Module.

This module shows the use of __setattr__().
"""


class LockedClass:
    """LockedClass Class

    This class prevents the user from dynamically creating
    new instance attributes,
    except if the new instance attribute is called first_name.
    """
    def __setattr__(self, key, value):
        """Attribute Setting Method

        Controls what happens when an instance of this class
        wants to set an attribute on itself.

        Args:
            key (str) : the attribute's key.
            valu (any): the attribute's value.
        """
        if key != 'first_name':
            raise AttributeError("'LockedClass' object has \
no attribute 'last_name'")
