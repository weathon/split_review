# MolTextQA: A Curated Question-Answering Dataset and Benchmark for Molecular Structure-Text Relationship Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 8, 3

## Abstract
Recent advancements in AI have significantly enhanced molecular representation learning, which is crucial for predicting molecule properties and designing new molecules. Despite these advances, effectively utilizing the vast amount of molecular data available in textual form from databases and scholarly articles remains a challenge. Recently, a large body of research has focused on utilizing Large Language Models (LLMs) and multi-modal architectures to interpret textual information and link it with molecular structures. Nevertheless, existing datasets often lack specificity in evaluation, as well as direct comparisons and comprehensive benchmarking across different models and model classes. In this work, we construct a dataset specifically designed for evaluating models on structure-directed questions and textual description-based molecule retrieval, featuring over 500,000 question-answer pairs related to approximately 240,000 molecules from PubChem. Its structure enhances evaluation specificity and precision through the use of multiple-choice answers. Moreover, we benchmark various architectural classes fine-tuned using this dataset, including multi-modal architectures, and large language models, uncovering several insights. Our experiments indicate that the Galactica and BioT5 models are the top performers in Molecule QA and Molecule Retrieval tasks respectively, achieving about 70% accuracy. We have made both the dataset and the fine-tuned models publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a question-answer (QA) dataset containing over 500,000 QA pairs associated with 240,000 unique small molecules. The dataset is derived from the PubChem textual corpus and includes multiple-choice questions about chemical structures, physical and biological properties, applications, and manufacturing information. The questions and answers are generated using various large language models (LLMs), including Llama3 and ChatGPT. A subset of the dataset is human-annotated to enable evaluation. The authors also present an evaluation of existing molecule-text multimodal models and LLMs on the proposed dataset.

### Strengths
- Textual data can play a valuable role in enhancing molecular prediction tasks. This paper introduces a large-scale dataset to advance the molecule-text research, providing a benchmark for molecule-related question-answering (QA) tasks, where comprehensive resources are currently lacking.
- The dataset is generated using a combination of multiple large language models (LLMs) and includes a subset with human annotation. This approach aims to enhance the dataset’s quality and usability, potentially offering the community a resource to explore QA tasks related to molecular data.

### Weaknesses
 - The dataset consists solely of multiple-choice questions with sentence-level descriptions, potentially limiting the depth and complexity of the tasks. It is unclear whether the dataset effectively tests cross-modal reasoning between text and molecules, as many examples seem to involve only simple references to the molecule in the text.

- Additionally, the paper does not provide a strong justification for how advancements in this benchmark would lead to meaningful improvements in molecular prediction models. Consequently, it remains uncertain how this dataset would contribute to real-world molecular applications or enhance the predictive capabilities of existing models.

- As noted by another reviewer, the validation process lacks clarity, raising concerns about the quality of the dataset.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a large, structured question-answering (QA) benchmark for studying the relationship between molecular structures and text descriptions. It contains 500,000 QA pairs of about 240,000 molecules from PubChem, designed to enhance model evaluation by offering specific, multiple-choice questions across categories like chemical, physical, and biological properties.

### Strengths
1. The dataset’s structured QA approach and validation process ensure a reliable and robust QA dataset.

2. Evaluation across multiple architectures enables direct comparisons in molecular QA.

3. The paper is generally well-written and clear in describing the dataset construction, with well-organized figures and tables.

### Weaknesses
1. The QA generation process relies heavily on LLMs, which may introduce non-factual content if not properly validated.

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work is a benchmarking effort on the topic of molecular structure-text data. The paper presents MolTextQA, a dataset and benchmark for evaluating models on molecular structure-text relationship learning. The dataset contains approximately 500,000 question-answer pairs related to 240,000 molecules from PubChem, specifically curated for structured-directed questions and molecule retrieval tasks. The paper benchmarks various architectural approaches including multi-modal models and large language models, with reporting the finding that Galactica and MoleculeSTM perform best on Molecule QA and Molecule Retrieval tasks respectively, alongside other analyses and highlighting challenges.

### Strengths
- the data size is substantial with 500k pairs and as shown, comes from diverse categories.
- the benchmark emphasizes specificity by using targeted questions with multiple-choice answers.
- the details on the data curation process is sufficiently included in the paper as well as in the README of the code repo. the types of information included in the schema are also reasonable and easy to follow.
- although llm generations during the curation process may be not 100% factual, the posed challenges are attempted to be addressed and corresponding validation are shown.

### Weaknesses
 - in the context of LLM being used in the process, although validation efforts are made, questions about long-term scalability and manual validation persist. 
- while the validation steps adopted shows high accuracy (around 96%), the remaining error rate could potentially complicate model training, as acknowledged in the paper.
- some questions might be straightforward questions or redundant, such as on the polarity questions

### Questions
na

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper introduces a dataset of approximately 500,000 question-answer pairs centered on **molecule structure-based questions** and **textual description-based molecule retrieval**, derived from around 240,000 molecules in PubChem. The authors utilize this dataset to benchmark multiple models, including multi-modal architectures and large language models. Notably, they highlight the high performance of Galactica and MoleculeSTM in molecule QA and retrieval tasks, respectively.

### Strengths
The paper contributes a novel dataset focused on **molecule structure-based questions** and **textual description-based molecule retrieval** tasks. Additionally, several scientific large language models are evaluated on this new dataset, providing initial benchmarks.

### Weaknesses
- The writing of the paper requires significant improvement, as it is currently challenging to follow. The paper includes redundant sections while lacking clarity and justifications in key areas.
  - Acronyms are defined multiple times throughout the paper; for example, "QA" is defined **five** times and "LLMs" **four** times.
  - Several statements lack clarity and justification. For example, in line 042, "deep learning methods" is vague in context. Lines 044-046 lack justification, and line 053 references "a surge in the development of models to decipher the complex relationships between molecular structures and textual descriptions" without specifying which models are being referred to.
- The motivation is unclear. Line 073 mentions, "Many existing datasets are based on free-form text generation or molecule/text retrieval, complicating the assessment of a model’s capability to infer specific molecular properties." However, it is unclear which datasets are being referenced. Although the authors mention that section 2.2 elaborates on current methodological shortcomings, the motivation for proposing a new QA dataset should be explicitly outlined in the introduction. The motivation behind introducing a new QA dataset is currently missing from the introduction.
- The authors state, "commonly used evaluation metrics such as the BLEU score are not entirely reliable for this context." However, BLEU scores are typically not used for molecule/text retrieval tasks, which brings into question the relevance of this statement.
- The benchmarking experiments need to add several recent baselines, such as **BioT5**, **BioT5+**, and **MolecularGPT**.
- The authors claim to have conducted "a comprehensive validation process that includes human annotation of a small subset to evaluate data accuracy." However, **no details are provided on the human annotation process.**
- The paper asserts that it provides "valuable insights into the advantages and limitations of current models," but these insights are not clearly presented.

### Questions
- Please clarify the statements mentioned above.
- How were the human annotations conducted?
- What specific advantages and limitations of current models does the analysis reveal?

### Soundness
1

### Presentation
1

### Contribution
1
