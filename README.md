# Mole PDF Dataset for Data Extraction Benchmarking

<img src="./mole.png" alt="data-mole" width="400"/>

We present a synthetic pdf dataset across 10 different categories.
Run your extraction algorithms and compare your results with the table data available.

While building data extraction tools many customers raise the question on how performant our algorithms for extractions are.
However to label a dataset by itself is really diffiuclt and time consuming therefore we present Ankathete Benchmark which
reversed the data creation. GPT-4 is used to create first the tables and then the PDF hence the data extraction will be there.
This procedure can be scalled to thousands of documents and gives a good starting point to claim your algorithms are good.
If you are not able to extract that data into a correct dataframe you do not have to start with cluttered data.

## Installation and Generation

1. **Set up the environment:**  
   Add an `.env` file in the root directory containing your `OPENAI_API_KEY`.

2. **Install the required tools:**  
   Install the [UV package manager](https://docs.astral.sh/uv/getting-started/installation/).

3. **Synchronize dependencies:**  
   Run the following command in the root directory:

   ```bash
   uv sync
   ```

4. **Generate the dataset**
   Run the following command in the root directory:
   ```bash
   uv sync
   ```

Run the script `uv run main.py`

## Folder, file and environment structure

The data can be found in the `./data` folder. Choose your batch.
The code for the generation is in the root folder. Entry point is the `main.py` file.

## Deterministic vs Ambivalent and Non-deterministc

When working with extraction values form pdfs you will encounter 3 different versions of possible extractable values:

- Deterministic Extraction: Extracts clear, fixed figures (e.g., revenue) reliably from structured data in PDFs.
- Ambivalent Extraction: Encounters ambiguity with no single clear value, leading to potential variability.
- Non-Deterministic Extraction: Extracts free-flowing text (e.g., summaries), with unique output each time due to interpretive variability.

We have focused here solely on deterministic values since all others are not well testable.

## Available categories

You can find pdfs from 10 different sectors:

- consulting
- education
- finance
- government
- healthcare
- legal
- manufacturing
- marketing
- publishing
- realestate

You can add more in the `instructions.py` file.

## For citations

```bibtex
@dataset{pdf_benchmark,
title = {Mole PDF Benchmark - A Dataset for Data Extraction and Benchmarking},
author = {Marc Willhaus and Andrea Zelic},
year = {2024},
publisher = {Ankathete},
url = {https://github.com/Ankathete/pdf-benchmark},
note = {An open-source dataset for benchmarking PDF-to-table data extraction algorithms.}
}
```

## MIT licence

```
Copyright (c) 2024 Marc, Andrea, and Ankathete

Permission is hereby granted, free of charge, to any person obtaining a copy of this dataset and associated documentation files (the "Dataset"), to deal in the Dataset without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Dataset, and to permit persons to whom the Dataset is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Dataset.

THE DATASET IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE DATASET OR THE USE OR OTHER DEALINGS IN THE DATASET.
```
