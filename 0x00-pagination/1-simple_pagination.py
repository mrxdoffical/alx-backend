#!/usr/bin/env python3
"""
this module is simple helper
"""

import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for a given

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """server class
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """cached database"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reading = csv.reader(f)
                dataset = [row for row in reading]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> list[list]:
        """Get paginated data"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
