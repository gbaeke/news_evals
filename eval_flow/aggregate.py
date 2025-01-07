# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from typing import List

from promptflow.core import log_metric, tool


@tool
def aggregate(scores: List[int]):
    """
    This tool aggregates the processed result of all lines and calculates a percentage score.

    :param scores: List of the output of line_process node.
    """

    # Add your aggregation logic here
    # Aggregate the results of all lines and calculate the accuracy
    avg_score = (sum(scores) / len(scores)) * 10 if scores else 0
   

    # Log metric the aggregate result
    log_metric(key="grade", value=avg_score)

    return avg_score
