import pandas as pd
import itertools
from collections import Counter
import json
from dotenv import load_dotenv
import os
import openai
import os
import matplotlib.pyplot as plt
import requests
import azure
from azure.identity import DefaultAzureCredential
from openai import AzureOpenAI
import evaluate
import urllib.request
import ssl
import os
import json
import urllib.request
import time
from azure.identity import DefaultAzureCredential
import glob
import pandas as pd


def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.


def submit_tasks(query, id, max_retries=5):
    data = {
    "messages": query,
    "max_tokens": 4096,
    "temperature": 0.1
    }


    batch_file_path = os.path.join(test_src_dir, f"batch_{id}.json")
    # Save the batch request data to a JSON file
    with open(batch_file_path, "w") as f:
        json.dump(data, f, indent=4)

    body = str.encode(json.dumps(data))
    #print(f"Batch request data saved to: {batch_file_path}")

    url = ''

    # Authenticate using AAD (Azure Active Directory)
    credential = DefaultAzureCredential()
    token = credential.get_token("https://cognitiveservices.azure.com/.default").token

    # Set up the headers with AAD token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    retries = 0
    while retries < max_retries:
        response = requests.post(
            url=f"",
            headers=headers,
            json=data
        )
        # Check if the response is rate limited (status code 429)
        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 32))  # Default to 32 seconds if not provided
            print(f"Rate limit exceeded. Retrying in {retry_after} seconds...")
            time.sleep(retry_after)
            retries += 1
        else:
            # If successful or another error occurred, break out of the retry loop
            break

    # Check if the request was successful after retrying
    if response.status_code == 200:
        result = response.json()
        output = result["choices"][0]["message"]["content"]
    else:
        print(f"Request failed after {retries} retries. Status code: {response.status_code}, Response: {response.text}")

    response_file_path = os.path.join(response_src_dir, f"response_{id}.json")

    # Save both input and response data
    with open(response_file_path, "w") as f:
        json.dump({
            "input_data": query,  # Use query here
            "response_data": output  # Ensure result is JSON serializable
        }, f, indent=4)

    print(f"Result for batch {id} saved to: {response_file_path}")



def batch_data(data, batch_size):
    """Split data into batches of given size."""
    return [data[i:i + batch_size] for i in range(0, len(data), batch_size)]

rouge_df = pd.DataFrame(columns=["ROUGE-1", "ROUGE-2", "ROUGE-L", "ROUGE-Lsum"])
test_src_dir = "./gpt4-inference-test"
response_src_dir = "./gpt4-inference-responses"
batch_size = 1

# Define the path for saving the real request file
os.makedirs(test_src_dir, exist_ok=True)
real_data_path = os.path.join(test_src_dir, "test_data.json")

#preprocess data
df = pd.read_csv("../analysis_and_tools_only.csv")

input_string = []

# Iterate through the rows of the dataframe
for index, row in df.iterrows():
    # 'content' is the column with the user questions
    user_content = row['content']
    # 'answer content' is the column with the ground truth answers
    assistant_content = row['answer_content']

    # Append only user content to the input_data
    input_string.append({"role": "user", "content": user_content})

# Define the parameters for the model
params = {
    "temperature": 0.1,
    "max_new_tokens": 4096, #output
    "do_sample": True,
    "return_full_text": False
}

# Combine input data and parameters into the final test data structure
test_data = {
    "input_data": input_string,
    "parameters": params
}

# Save the JSON output to a file
with open('test_data.json', 'w') as json_file:
    json.dump(test_data, json_file, indent=4)

# Save the real request data to a JSON file
with open(real_data_path, "w") as f:
    json.dump(test_data, f, indent=4)

# Create batches
batches = batch_data(test_data["input_data"], batch_size)




for j in range(100):

    print(f"Iteration {j}")

    ## loop through batches
    for i, batch in enumerate(batches):
        submit_tasks(batch,i)

    file_pattern = "./gpt4-inference-responses/*.json"

    questions = []
    answers = []

    for file_name in glob.glob(file_pattern): #glob lists all the text files in the current working dir.
        with open(file_name, 'r') as file:
            data = json.load(file)


        if "input_data" in data: #retrieves list of dictionaries
            for item in data["input_data"]: #iterates over each dictionary in the list
                if "content" in item:
                    questions.append(item["content"])

        if "response_data" in data:
            response = data["response_data"]
            answers.append(response)

    final_df = pd.DataFrame({"Question": questions, "Answer": answers})

    # Save DataFrame to a CSV file (optional)
    final_df.to_csv('combined_questions_answers.csv', index=False)

    final_df.head()

    predictions = final_df["Answer"].to_list()
    references = df["answer_content"].to_list()

    rouge = evaluate.load('rouge') #https://huggingface.co/spaces/evaluate-metric/rouge


    results = rouge.compute(predictions=predictions,
                            references=references,
                            use_aggregator=True)
    rouge_df.loc[j] = [
        round(results["rouge1"], 3),
        round(results["rouge2"], 3),
        round(results["rougeL"], 3),
        round(results["rougeLsum"], 3)
    ]
 
rouge_df.to_csv('./rouge_results.csv', index=False)

