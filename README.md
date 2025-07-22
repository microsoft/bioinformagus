# Bioinformagus


This repository is an example of running the multiagent bioinformatics analysis<br/>

Here, you can find the jupyter-notebooks for benchmarking and examples of a mutliagent system

## Directory Overview

- **Evaluation/**
  
  Directory exists for evaluation purposes of different language models such as (GPT-4, GPT-4o, Phi3, Phi3.5 and Phi3.5MOE) against the Biostart
  benchmark questions/answers as provided by [analysis_and_tools_only.csv](Evaluation/analysis_and_tools_only.csv). Each subdirectory has a notebook
  or python code on how to run the evauluations and when availble provided example benchmarks.
  
- **Fine-tune/**
  
  Contains resources for formating data for fine-tuning with Phi-3, including example notebooks. Reference: [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook/tree/main).

  The main notebook [fine_tuning_data_format.ipynb](Fine-tune/input_data/format_input_data/fine_tuning_data_format.ipynb), converts [Software Tools and Description](Fine-tune/input_data/format_input_data/biocontainers_1.jsonl) and [Biocontainers Tool commandline options](Fine-tune/input_data/format_input_data/biocontainers_help.jsonl) to the correct jsonl format respectivley [FT_tools.jsonl](Fine-tune/input_data/format_input_data/FT_tools.jsonl) and [FT_docs.jsonl](Fine-tune/input_data/format_input_data/FT_docs.jsonl).

  - The note book also splits the data into test and train.
    - Software Tools Descriptions (Biocontainers and Software Ontology)
        - Test: [Test_1.jsonl](Fine-tune/input_data/test_1.jsonl)
        - Train: [Train_1.jsonl](Fine-tune/input_data/train_1.jsonl)
    - Biocontainer Commlandline options
        - Test: [Test_2.jsonl](Fine-tune/input_data/test_2.jsonl)
        - Train: [Train_2.jsonl](Fine-tune/input_data/train_2.jsonl)
    - Final data is combined into:
        - Train: [train.jsonl](Fine-tune/train.jsonl)
        - Eval: [eval.jsonl](Fine-tune/eval.jsonl)
  

- **RAG/**  

  Contains resources for Retrieval-Augmented Generation (RAG) using Azure Cognitive Search, with instructions for indexing available [here](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overviewg).

  Example of nf-core modules converted to to JSONL [nfc.jsonl](RAG/nfc.jsonl)

- **Mutli-Agent/**  

The notebooks in this folder demonstrate workflows, experiments, and benchmarking using multi-agent systems for bioinformatics tasks. These examples are intended to help users understand how to leverage agent-based approaches for complex data analysis and automation in bioinformatics.

- Evaluation against user questions: [Multiagent_response.ipynb](Multi-Agent/Multiagent_response.ipynb)
- Evaluation against Biostarts questions[Multiagent_biostars.ipynb](Multi-Agent/Multiagent_biostars.ipynb)


## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
