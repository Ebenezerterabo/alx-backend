#!/usr/bin/env python3
""" 0-simple_helper_function.py """


def index_range(page: int, page_size: int) -> tuple:
    """ return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for
    pagination
    """

    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return start_idx, end_idx
