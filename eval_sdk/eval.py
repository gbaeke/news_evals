import os
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()

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
}


from azure.ai.evaluation import GroundednessProEvaluator, GroundednessEvaluator

# Initialzing Groundedness evaluator
groundedness_eval = GroundednessEvaluator(model_config)

query_response = dict(
    query="Which tent is the most waterproof?",
    context="The Alpine Explorer Tent is the most water-proof of all tents available.",
    response="The North Face Himalayan tent is the most waterproof tent available on the market today."
)

# Running Groundedness Evaluator on a query and response pair
groundedness_score = groundedness_eval(
    **query_response
)
print(groundedness_score)


# try the headline evaluator
from title_score import HeadlineEvaluator

headline_eval = HeadlineEvaluator(model_config)

headline_data = dict(
    article="A leading tech company has announced the launch of its latest AI assistant, promising to revolutionize daily life and work efficiency. Equipped with advanced natural language processing and real-time adaptability, the assistant is designed to assist with tasks ranging from scheduling to creative writing. Analysts believe this innovation could redefine how businesses and individuals interact with technology, sparking debates over privacy and ethical AI usage.",
    headline="Some company unveils a boring widget that nobody will use",
)

headline_score = headline_eval(**headline_data)

print(headline_score)