# OpenWebMath: An Open Dataset of High-Quality Mathematical Web Text

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 5

## Abstract
There is growing evidence that pretraining on high quality, carefully thought-out tokens such as code or mathematics plays an important role in improving the reasoning abilities of large language models. For example, Minerva, a PaLM model finetuned on billions of tokens of mathematical documents from arXiv and the web, reported dramatically improved performance on problems that require quantitative reasoning. However, because all known publicly released web datasets employ preprocessing that does not faithfully preserve mathematical notation, the benefits of large scale training on quantitive web documents are unavailable to the research community. We introduce OpenWebMath, an open dataset inspired by these works containing 14.7B tokens of mathematical webpages from Common Crawl. We describe in detail our method for extracting text and \LaTeX{} content and removing boilerplate from HTML documents, as well as our methods for quality filtering and deduplication. Additionally, we run small-scale experiments by training 1.4B parameter language models on OpenWebMath, showing that models trained on 14.7B tokens of our dataset surpass the performance of models trained on over 20x the amount of general language data. We hope that our dataset, \href{https://huggingface.co/datasets/open-web-math/open-web-math}{openly released on the Hugging Face Hub}, will help spur advances in the reasoning abilities of large language models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a large scale dataset of mathematical text (14.7B tokens, 6.3M documents) filtered from the Common Crawl dataset: OpenWebMath. The paper primarily describes the extensive pre-processing applied to obtain this dataset. To indicate the value of the dataset the paper trains a 1.4B Pythia model on the gathered data and reports perplexity on GSM8k and MATH datasets and task accuracy on MATH and LILA-multiarch. The results indicate that a model trained on OpenWebMath sees improved perplexity and better task accuracy.

### Strengths
- The paper presents a well documented dataset.
- The dataset seems to be useful for training LLMs of small-medium scale.

### Weaknesses
 - The paper presents no special insight on the dataset or the effect of the processing steps applied - it only describes the pre-processing pipeline. A key aspect that would strengthen this paper is a description of the overlap (computed in some apt way: eg overlap of urls, text overlap, others) between OpenWebMath and the benchmark datasets it evaluates on - computing overlap other popular reasoning benchmarks would also be a welcome addition.

 - It seems like the MATH dataset was gathered from aops.com/community/c3158_usa_contests. Is this a part of Common Crawl? What is the overlap between OpenWebMath and MATH? This is important given concerns of dataset contamination with web scale datasets: https://arxiv.org/abs/2310.10628
- How does OpenWebMath differ from ProofPile? Are there obvious reasons why using OpenWebMath results in significantly better performance than ProofPile?
	- The citation for ProofPile ("Proofnet: Autoformalizing and formally proving undergraduate-level mathematics.") seems incorrect. Please consider adding a note of what the dataset is and its source.
- What exactly is LILA-multiarith? It seems the LILA benchmark contains multiple different datasets, why did the evaluation here only use this one dataset in the benchmark? 
	- In similar vein to the above comments, does the data here overlap with OpenWebMath?
	- Please consider citing the original source of the multiarith dataset in addition to the benchmark, its not clear what the original data is. The citation chain to the original dataset seems to be: https://arxiv.org/pdf/2210.17517.pdf (LILA) -> https://arxiv.org/pdf/1608.01413.pdf (methodological paper using the data?) -> https://aclanthology.org/Q15-1001.pdf (original data) - please verify this.
- Please consider describing the tasks of Table 2 in more detail.
- Please place a table or figure closer to the texts discussing it.

### Questions
- It seems like the MATH dataset was gathered from aops.com/community/c3158_usa_contests. Is this a part of Common Crawl? What is the overlap between OpenWebMath and MATH? This is important given concerns of dataset contamination with web scale datasets: https://arxiv.org/abs/2310.10628
- How does OpenWebMath differ from ProofPile? Are there obvious reasons why using OpenWebMath results in significantly better performance than ProofPile?
	- The citation for ProofPile ("Proofnet: Autoformalizing and formally proving undergraduate-level mathematics.") seems incorrect. Please consider adding a note of what the dataset is and its source.
- What exactly is LILA-multiarith? It seems the LILA benchmark contains multiple different datasets, why did the evaluation here only use this one dataset in the benchmark? 
	- In similar vein to the above comments, does the data here overlap with OpenWebMath?
	- Please consider citing the original source of the multiarith dataset in addition to the benchmark, its not clear what the original data is. The citation chain to the original dataset seems to be: https://arxiv.org/pdf/2210.17517.pdf (LILA) -> https://arxiv.org/pdf/1608.01413.pdf (methodological paper using the data?) -> https://aclanthology.org/Q15-1001.pdf (original data) - please verify this.
- Please consider describing the tasks of Table 2 in more detail.
- Please place a table or figure closer to the texts discussing it.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes OpenWebMath, an open dataset of 14.7B high-quality mathematical documents from web text. The authors highlight the importance of pretraining on mathematical content to improve the reasoning abilities of large language models. They mention the success of the Minerva model, which was trained on a curated dataset of mathematical documents. However, existing open-source web datasets do not preserve mathematical notation accurately, limiting their usefulness. OpenWebMath aims to address this gap by providing a dataset of 14.7 billion tokens of mathematical web pages extracted from Common Crawl. The authors describe their method for extracting and filtering web pages for high-quality English mathematical documents. They also conduct experiments showing that models trained on OpenWebMath outperform models trained on larger general language datasets.

### Strengths
1. This paper proposes an open high-quality mathematical dataset, which can let models get a good reasoning ability in a lower computation.
2. This paper proposes a new method for extracting and filtering mathematical text from web pages. This method is worth deeper research.

### Weaknesses
1. The authors should provide an example of a dataset in the paper.
2. The order in which the table appears is inconsistent with the logic of the text.
3. There are invisible Unicode characters and some text in other languages in the data.

### Questions
Why there are some invisible Unicode characters and other language text in sample_dataset.jsonl? For instance the  40th and 43th lines of sample_dataset.jsonl.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the author introduces OpenWebMath, a new large-scale dataset for language model mathematical problem-solving. A comprehensive illustration of the dataset construction pipeline is provided and some further analysis of the dataset is conducted.

### Strengths
1. The paper provides an opensource large-scale mathematical web text dataset which can benefit the following research.
2. The detailed dataset construction pipeline is provided.

### Weaknesses
1. The paper provides an opensource large-scale mathematical web text dataset which can benefit the following research.
2. The detailed dataset construction pipeline is provided.

1. The advance of OpenWebMath compared with existing datasets such as Proof-Pile is not provided.
2. My main concern here is that the paper is a dataset construction paper without novel technique contribution provided. I’m not very sure if this kind of paper is suitable for ICLR.

### Questions
What is the advance of OpenWebMath compared with existing datasets such as Proof-Pile?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
