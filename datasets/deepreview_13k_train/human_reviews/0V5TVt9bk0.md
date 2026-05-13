# Q-Bench: A Benchmark for General-Purpose Foundation Models on Low-level Vision

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
The rapid evolution of Multi-modality Large Language Models (MLLMs) has catalyzed a shift in computer vision from specialized models to general-purpose foundation models. Nevertheless, there is still an inadequacy in assessing the abilities of MLLMs on \textbf{low-level visual perception and understanding}. To address this gap, we present \textbf{Q-Bench}, a holistic benchmark crafted to systematically evaluate potential abilities of MLLMs on three realms: low-level visual perception, low-level visual description, and overall visual quality assessment. \textbf{\textit{a)}} To evaluate the low-level \textbf{\textit{perception}} ability, we construct the \textbf{LLVisionQA} dataset, consisting of 2,990 diverse-sourced images, each equipped with a human-asked question focusing on its low-level attributes. We then measure the correctness of MLLMs on answering these questions. \textbf{\textit{b)}} To examine the \textbf{\textit{description}} ability of MLLMs on low-level information, we propose the \textbf{LLDescribe} dataset consisting of long expert-labelled \textit{golden} low-level text descriptions on 499 images, and a GPT-involved comparison pipeline between outputs of MLLMs and the \textit{golden} descriptions. \textbf{\textit{c)}} Besides these two tasks, we further measure their visual quality \textbf{\textit{assessment}} ability to align with human opinion scores. Specifically, we design a softmax-based strategy that enables MLLMs to predict \textit{quantifiable} quality scores, and evaluate them on various existing image quality assessment (IQA) datasets. Our evaluation across the three abilities confirms that MLLMs possess preliminary low-level visual skills. However, these skills are still unstable and relatively imprecise, indicating the need for specific enhancements on MLLMs towards these abilities. We hope that our benchmark can encourage the research community to delve deeper to discover and enhance these untapped potentials of MLLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work introduces a benchmark for low-level perception and understanding. They introduce three tasks for assessing the MLLM. The main focus is low-level, thus they build an evaluation bench from various aspects (low-level attributes, visual distortions, etc.). The experiments are extensive and comprehensive.

### Strengths
1. The motivation is sufficient, and this benchmark is specifically designed for low-level tasks rather than a holistic evaluation of general abilities.
2. The tasks consist of classification and description, as well as probability-based quantitative evaluation, making it well-organized for evaluating the low-level abilities of the current MLLM.
3. The experiments are extensive and comprehensive, which are helpful in diagnosing the strengths and shortcomings of current MLLMs.

### Weaknesses
The main concern is about the trustworthiness of the evaluation.

1. As the ChatGPT also suffers from hallucination, how can we ensure the reliability and confidence of the GPT-assisted evaluation?
2. What is the difference between the proposed metric and perplexity (only considering good/bad)? Is the PPL equivalent to this new metric?
3. As current models typically leverage large amounts of data, how can we avoid contamination of the evaluation dataset in the training set?

### Questions
As questions in weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The rapidly developed Multi-modality Large Language Models (MLLMs) have progressed greatly. However, there is still an inadequacy in assessing the abilities of MLLMs on low-level visual perception and understanding. Accordingly, this paper proposed Q-Bench, a holistic benchmark of MLLMs for low-level visual perception, low-level visual description, and overall visual quality assessment. Q-Bench constructs solid benchmark datasets and reasonable evaluation pipelines, including LLVisionQA for low-level perception ability, LLDescribe for low-level description ability, and a compounded IQA dataset for image quality assessment with an innovative softmax-based strategy. Q-Bench provides a viable solution to reveal the potential of MLLMs for low-level visual understanding.

### Strengths
1. Q-Bench is composed of benchmark datasets and reasonable evaluation pipelines for low-level perception, low-level description, and image quality assessment. The contributions are solid. 
2. The experiments and study are extensive and convincing. 
3. The Q-Bench is well presented, and the details are clear.

### Weaknesses
1. In the evaluation of LLDescribe, the softmax is calculated between good and poor. How about also considering their synonyms, e.g., great, excellent, fine, bad, low, etc? Here is a possible solution: (1) merge the logits of great, excellent, fine into good, and bad, low into poor. (2) calculate the final score with merged logits.
2. As a benchmark paper, the author may update the recent SOTA MLLMs into the leadboards of this paper, e.g., QWen-VL [1], InternLM-XComposer [2], and LLaVA-1.5 [3].

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This is a benchmark paper on the performance of low-level visual perception and understanding of MLLMs. To this end, the paper collected and annotated a new benchmark dataset Q-Bench including 1) LLVisionQA about the low-level perception of 2990 images; 2) LLDescribe about the description of image quality of 499 images; 3) how to align visual quality scores with people perception. The paper evaluated 10 recent public available MLLM on Q-Bench. The evaluation indicates current MLLMs have decent low-level abilities yet still a long way to go for general low-level visual assessment.

### Strengths
The benchmark of current MLLMs’ abilities to access low-level image quality appears a quite interesting topic to me. The paper presented a thorough and in-depth evaluation and the finding may inspire some further research. The evaluation design of Q-Bench makes sense. The paper is well-written.

### Weaknesses
This is a descent benchmark paper on an interesting topic. I would recommend acceptance given the performance of GPT-4V on Q-Bench is provided in the revised version.

### Questions
It is definitely a must-to-ask question that how the performance of GPT-4-Vision on Q-Bench, which shall establish the baseline for commercial SotA MLLM.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
