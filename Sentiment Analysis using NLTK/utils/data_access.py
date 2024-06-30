from typing import List
from snowflake.snowpark.context import get_active_session

import pandas as pd
import streamlit as st

session = get_active_session()


@st.cache_data
def get_dataframe_from_raw_sql(query: str) -> pd.DataFrame:
    """Executes the given query in the Snowflake database
    and converts the result to a pandas dataframe.

    Args:
        query (str): The query to be run against the database.

    Returns:
        pd.DataFrame: The query result as a pandas dataframe.
    """
    pandas_df = session.sql(query).to_pandas()
    return pandas_df


@st.cache_data
def execute_query_with_params(query: str, params: List) -> pd.DataFrame:
    """Executes query with given parameters and returns the result as a pandas dataframe.

    Args:
        query (str): The query to be executed.
        params (List): The queries' parameters.

    Returns:
        pd.DataFrame: The result as a pandas dataframe.
    """
    return session.sql(query, params=params).to_pandas()
