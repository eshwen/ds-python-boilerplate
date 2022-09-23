"""Test file."""
import numpy as np
import pandas as pd


def hello_world() -> str:
    """Returns "Hello World!" when called.

    Returns:
        str: The string 'Hello world!'.

    Example:
        ```python
        >>> hello_world()
        'Hello World!'
        ```

    Note:
        This is an example of a note.

    Warning:
        This is an example of a warning.

    """
    return "Hello World!"


def do_a_dataframe_thing(df: pd.DataFrame, arr: np.ndarray | None = None) -> pd.DataFrame:
    """An example of documentation with references to external libraries.

    Args:
        df: Input dataframe.
        arr: Input array.

    See Also:
        An explicit reference to a dataframe: [pandas.DataFrame][] for an explicit reference.
        Or a numpy array: [numpy.array][].

    Returns:
         A dataframe with some magical operation applied to it.

    """
    if arr is not None and arr.size > 0:
        return df[arr]
    return df
