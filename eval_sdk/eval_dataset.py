import os
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
from azure.ai.evaluation import evaluate


# load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize Azure AI project and Azure OpenAI conncetion with your environment variables
azure_ai_project = {
    "subscription_id": os.environ.get("AZURE_SUBSCRIPTION_ID"),
    "resource_group_name": os.environ.get("AZURE_RESOURCE_GROUP"),
    "project_name": os.environ.get("AZURE_PROJECT_NAME"),
}

model_config = {
    "azure_endpoint": os.environ.get("AZURE_OPENAI_ENDPOINT"),
    "api_key": os.environ.get("AZURE_OPENAI_API_KEY"),
    "azure_deployment": os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
    "api_version": os.environ.get("AZURE_OPENAI_API_VERSION"),
    "type": "azure_openai"  # this is required when you use evaluate
}

# import the headline evaluator
from title_score import HeadlineEvaluator

headline_eval = HeadlineEvaluator(model_config)

def main():
    current_dir = os.path.dirname(__file__)
    articles_path = os.path.join(current_dir, "articles.jsonl")

    result = evaluate(
        data=articles_path, # provide your data here
        evaluators={
            "headline": headline_eval
        },
        # column mapping
        evaluator_config={
            "headline": {
                "column_mapping": {
                    "article": "${data.content}",
                    "headline": "${data.title}"
                } 
            }
        },
        # Optionally provide an output path to dump a json of metric summary
        output_path="./myevalresults.json"
    )
    return result

if __name__ == "__main__":
    result = main()
    print(result)
