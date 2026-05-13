# EvidenceBench: A Benchmark for Extracting Evidence from Biomedical Papers

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
We study the task of automatically finding evidence relevant to hypotheses in biomedical papers. Finding relevant evidence is an important stage when humans write systematic reviews about certain scientific hypotheses. We introduce EvidenceBench to measure models performance on this task, which is created by a novel pipeline that consists of hypothesis generation and sentence-by-sentence annotation of biomedical papers for relevant evidence, completely guided by and faithfully following existing human experts judgment. Our pipeline's value and accuracy is validated by teams of human experts. We evaluate a diverse set of language models and retrieval systems on the benchmark and find the performance of the best models still falls significantly short of expert-level on this task. To show the scalability of our proposed pipeline, we create a larger EvidenceBench-100k with 107,461 fully annotated papers with hypotheses to faciliate model training and development. Both datasets are available at https://github.com/EvidenceBench/EvidenceBench

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents EvidenceBench, which is a benchmark for finding arguments supporting or against a hypothesis. They find hypotheses inside survey, and find supporting arguments from the same survey, and the original paper. 
This paper also proposes metrics for the task and compares many LLMs' performance on the task. In addition, this paper also provides the fine-tuning results on the benchmark.

### Strengths
1. Identifying arguments supporting or against an argument is an important task.
2. This paper proposes an annotation pipeline, which might be helpful for future tasks.

### Weaknesses
1. The paper spends too much effort on constructing the benchmark, but not many insights are provided through the experiment section.
2. The writing can be largely improved. There's many places in the writing that are vague and not clear.
For example, the second paragraph in the introduction section: 
"We consider the goal of understanding what is known in the literature about a scientific hypothesis.
This can be broken into several stages: searching for relevant papers; extracting information from
these papers; and aggregating this information. Our work focuses on the second stage."
My questions are:
a). what is precisely the research goal in terms of "understanding what is known in the literature about a scientific hypothesis"?
b). why it can be broken into these three stages?

In line 047~048: "These annotations are judgments which are ordinarily made by domain experts, and the benchmark should be faithful to these judgments": what does it mean by "the benchmark should be faithful to these judgements"?

In line 048~050: "Third, despite the complexity of annotation, the benchmark construction process should be scalable, providing a sufficient number of examples to accurately measure system performance": what does it mean by "should be scalable"? what does it mean by "providing a sufficient number of examples to accurately measure system performance"? what is the relation between these two arguments?

I found it very hard to read through the paper. I would suggest the authors for a major revision at least in terms of the writing.

3. In section 3.2, which is "DATASET PIPELINE OVERVIEW", there's less/none justification on why the design can compose a good and persuading enough pipeline. The only mentioned is what the pipeline is. After reading it, I don't know why the design can warrant a good automation.
4. Expert only check 50 of the analyzed papers, which is not very persuading enough on believing the overall quality of the constructed benchmark.

### Questions
Can you provide more insights or knowledge that we can learn?

### Soundness
3

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
This paper studies the task of finding evidence for a hypothesis. The authors develop a pipeline for annotating biomedical papers for this task. Using the annotation pipeline, the authors build a benchmark of more than 400 papers. Additionally, the authors create a larger dataset containing 100K papers.
The authors also run experiments to evaluate the effectiveness of different approaches to the proposed task.

### Strengths
* The authors propose a practical task and evaluate the effectiveness of existing approaches to the task
* A useful resource for benchmarking LLMs on the proposed task
* The paper is well-structured and easy to follow, although some presentations can be further improved

### Weaknesses
The concept of `study aspect` is confusing, and I am unsure how the evaluation procedure considers it. For example, if a sentence is retrieved for the wrong aspect or multiple aspects.
Based on the task definition, the hypothesis is given. However, this may not be the case in the real world. It would be nice to see these tested models' sensitivity to the modified (paraphrasing) hypothesis.
The difference between `EvidenceBench` and `EvidenceBench-100k` is unclear (seems with or without human validation?)
The authors exclude figure and table, which might be very relevant and important for the proposed task.

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces EvidenceBench, a scalable annotation pipeline designed for extracting and aligning evidence with specific hypotheses in biomedical literature. Study aspects and hypotheses are initially extracted from systematic reviews. A specialized alignment annotator then performs sentence-level annotations to link each piece of evidence directly to the corresponding hypothesis. To validate this approach, the authors use the pipeline to generate the expansive EvidenceBench-100k benchmark. Fine-tuned on this benchmark dataset, embedding models showed improved performance in the 'Result ER@Optimal' task, showing this standardized benchmark and evaluation framework will support the development of tools for automate evidence synthesis and hypothesis testing.

### Strengths
o	The original EvidenceBench evaluated the performance of selected LLMs and embedding models on evidence retrieval tasks and compared different prompting strategies, which revealed that GPT-4o is the SOTA LLM, and that embedding models underperform due to a lack of context awareness.

o	The EvidenceBench-100k fine-tuned E5-v2 model and Llama3-8B significantly improved on the result evidence retrieval task but trailed behind larger models, validating the effectiveness of the benchmark dataset.

o	The author presented the topic and their framework well, with detailed descriptions and clear figures illustrating the overall problem and their area.

o	This paper innovatively developed the pipeline for evidence retrieval for a given hypothesis and further annotated biomedical papers at the sentence level for better meta-analysis.

o	The authors conducted comprehensive experiments with both open-sourced and closed-sourced LLMs, and a small language model. Human experts were involved to validate study aspects generation and automate sentence annotation to enhance trustworthiness.

### Weaknesses
o	The authors claimed that their method using the SOTA LLMs reduces construction time from over 3,000 human hours for EvidenceBench to 3 hours. However, there is no evidence provided regarding how the 3 hours were concluded. Additionally, GPT4-0125, GPT4-o-mini, and Claude3-Opus are used during data generation without explanations of when to choose which.

o	No ablation study regarding how topics can influence the study aspect and hypothesis extraction is provided. The subsets used for experiments are randomly selected without considering the distribution of topics.

o	The experiments are conducted on a subset of the test dataset. Although EventBench-100K is comprehensive and large, only 300 data points are used to evaluate LLMs, which is a very small portion.

### Questions
o	How is the 3 human hour for construction using this pipeline concluded? Why are different LLMs (GPT4-0125, GPT4-o-mini, and Claude3-Opus) selected as the tool at different stage of benchmark data creation?

o	The summary extraction from study monographs is performed by LLMs, without human inspection. The summaries are used as input to LLMs for the recovery of hypotheses and decomposition of aspects. Although the aspect decomposition is inspected by humans, how is the summary extraction validated to avoid error propagation?

o	In Task Definition, both versions of the task define the desired sentences as evidence for or against a hypothesis. It is difficult to discern whether sentences classified as counter-evidence in relation to one hypothesis might be more appropriately considered as supportive of an alternative hypothesis. Given the structured nature of the tasks, are there any experiments or human validations conducted to address and clarify these categorizations?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new task of finding evidence for a hypothesis. The authors built a large-scale dataset with reasonable costs using existing survey monographs and LLMs.

### Strengths
- The large-scale datasets are constructed using LLMs with fewer budgets.
- Several evaluations of existing and fine-tuned models are provided and compared, showing the usefulness of the benchmark dataset for evaluating current LLMs' abilities.

### Weaknesses
 - It needs to be clarified how the hypotheses from survey monographs are generally helpful.
- The authors expect to provide immediate value to scientists as the first desiderate of the benchmark (lines 44-45), and the dataset creation involves several experts. Still, no manual analyses are provided for the results, so whether the results benefit scientists is unclear. 
- The proposed task focuses on the limited part of the practical problem; the task expects the candidate pool and needs to consider cases with evidence and with (the retrieval results of) the considerable paper pool (e.g., the entire PubMed database).

Typo:
- Line 509, Figure 3 should be Table 6.

### Questions
- Hypotheses are taken from survey monographs, so they can differ from natural hypotheses the experts consider. Is there any evaluation of the dataset that evaluates the suitableness of the instances for evidence retrieval?
- What happens if the experts think of the hypotheses with no evidence?

### Soundness
3

### Presentation
3

### Contribution
2
