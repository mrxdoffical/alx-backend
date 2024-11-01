#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.

This module provides a Server class to paginate a dataset of popular
baby names in a way that is resilient to deletions.
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): Path to the dataset file.
        __dataset (List[List]): Cached dataset.
        __indexed_dataset (Dict[int, List]): Indexed dataset.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server class.
        """
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0.

        Returns:
            Dict[int, List]: The indexed dataset.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: truncated_dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict:
        """
        Get paginated data with deletion-resilient hypermedia pagination
        info.

        Args:
            index (int): The current start index of the return page.
            page_size (int): The number of items per page (default is 10).

        Returns:
            Dict: A dictionary containing pagination metadata and the
            dataset page.

        Raises:
            AssertionError: If index is out of range.
        """
        assert index is not None and 0 <= index < len(self.dataset())

        indexed_dataset = self.indexed_dataset()
        data = []
        next_index = index

        while len(data) < page_size and next_index < len(indexed_dataset):
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
