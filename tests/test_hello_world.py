import numpy as np
import pandas as pd

from my_project import hello_world


def test_hello_world():
    assert hello_world.hello_world() == "Hello World!"


def test_do_a_dataframe_thing():
    df_in = pd.DataFrame({"foo": ["bar", "baz"]})
    df_out_bare = hello_world.do_a_dataframe_thing(df_in)
    pd.testing.assert_frame_equal(df_in, df_out_bare)

    arr_in = np.array([])
    df_out_with_arr = hello_world.do_a_dataframe_thing(df_in, arr_in)
    pd.testing.assert_frame_equal(df_in, df_out_with_arr)

    arr_in_len = np.array([True, False])
    df_out_with_arr_len = hello_world.do_a_dataframe_thing(df_in, arr_in_len)
    pd.testing.assert_frame_equal(df_out_with_arr_len, pd.DataFrame({"foo": ["bar"]}))
