import os
import json
import sys
from promptflow.client import load_flow


class HeadlineEvaluator:
    def __init__(self, model_config):
        current_dir = os.path.dirname(__file__)
        prompty_path = os.path.join(current_dir, "headline.prompty")
        self._flow = load_flow(source=prompty_path, model={"configuration": model_config})

    def __call__(self, *, headline: str, article: str, **kwargs):
        llm_response = self._flow(headline=headline, article=article)
        try:
            response = json.loads(llm_response)
        except Exception as ex:
            response = llm_response
        return response