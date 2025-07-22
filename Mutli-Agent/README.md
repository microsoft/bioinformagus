# Multiagent Setup Guide

This guide describes how to set up and use the `.ipynb` notebook in the [Mutli-Agent](../).

## Overview

The notebooks demonstrates a multi-agent bioinformatics solution using multiple language models and retrieval systems. It orchestrates:
- A fine-tuned LLM agent
- A Retrieval-Augmented Generation (RAG) agent using Azure Cognitive Search and Phi-3
- A reasoning agent (Phi-3)
to solve and explain bioinformatics problems with code and logic, and includes quality rating of responses.

## Prerequisites

- Python 3.12 or above (recommended: Anaconda environment)
- Jupyter Notebook (`pip install notebook` or via Anaconda)
- Access to AzureML endpoints, Azure Cognitive Search, and required API keys

## Required Python Packages

Install the required packages by running the following in a notebook cell or your terminal:

```python
%pip install langchain_community
%pip install azure-ai-ml
%pip install -qU langchain-openai
%pip install json5
```

Additional dependencies may be needed, per the notebook logic (e.g., `requests`, `numpy`, etc.), but these are the core packages for interacting with AzureML and language model endpoints.

## Environment Configuration

You need to provide your Azure credentials and endpoint URLs for the notebook to work:
- AzureML endpoint URLs and API keys
- Azure AI Search service name and API key

Update the following variables in the notebook:
```python
endpoint_url = "<YOUR_AZUREML_ENDPOINT_URL>"
endpoint_api_key = "<YOUR_AZUREML_API_KEY>"
AZURE_AI_SEARCH_SERVICE_NAME = "<YOUR_AZURE_SEARCH_SERVICE_NAME>"
AZURE_AI_SEARCH_API_KEY = "<YOUR_AZURE_SEARCH_API_KEY>"
```
Replace the placeholders above with your actual credentials.

## Usage

1. **Install dependencies:**  
   Run the first code cell to install all required Python packages.

2. **Configure endpoints:**  
   Enter your Azure endpoint URLs and API keys in the appropriate places in the notebook.

3. **Run cells sequentially:**  
   Execute the notebook cells in order. The notebook will:
   - Set up agents for solving, coding, and reasoning
   - Accept bioinformatics questions
   - Retrieve relevant documentation
   - Generate code and explanatory responses
   - Perform quality assessment of each answer

4. **Review outputs:**  
   The notebook prints responses and quality ratings. Results are optionally saved to a text file for later analysis.

## Troubleshooting

- If you see errors related to missing packages, rerun the installation cell or install them manually.
- If API calls time out, check your endpoint configuration and network connectivity.
- Ensure you have access rights to the Azure resources you specify.

## Customization

- You can modify the queries and agent logic to suit other bioinformatics workflows.
- Adjust the prompt templates and quality rating logic as needed for your specific use case.

---

For more information, see the [Bioinformagus README](../../README.md) or open an issue in the repository for help.