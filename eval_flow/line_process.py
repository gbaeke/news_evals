# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow.core import tool
import json


@tool
def line_process(score: str):
    """
    This tool processes the prediction of a single line and returns the processed result.

    :param score: a JSON string containing additional scoring information.
    """
    
    # Parse the JSON string to extract score field
    score_json = json.loads(score)
    score = int(score_json.get("score"))
    

    return score
