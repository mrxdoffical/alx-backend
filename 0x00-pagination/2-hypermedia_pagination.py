#!/usr/bin/env python3
"""
Module for pagination and hypermedia pagination of a dataset of popular
baby names.

This module provides functions and classes to paginate a dataset and to
provide hypermedia information for pagination.
"""

import csv
from typing import List, Dict
import math


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for a given pagination page and
    page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): Path to the dataset file.
        __dataset (List[List]): Cached dataset.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server class.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset.

        Reads the dataset from the CSV file if not already cached and
        caches it.

        Returns:
            List[List]: The dataset excluding the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get paginated data.

        Args:
            page (int): The current page number (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            List[List]: A list of rows corresponding to the paginated
            data.

        Raises:
            AssertionError: If page or page_size are not positive
            integers.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get paginated data with hypermedia pagination info.

        Args:
            page (int): The current page number (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            Dict: A dictionary containing pagination metadata and the
            dataset page.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
