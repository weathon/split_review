# AutoCast++: Enhancing World Event Prediction with Zero-shot Ranking-based Context Retrieval

- Decision: Accept
- Scores: 8, 3, 6

## Abstract
Machine-based prediction of real-world events is garnering attention due to its potential for informed decision-making. Whereas traditional forecasting predominantly hinges on structured data like time-series, recent breakthroughs in language models enable predictions using unstructured text. In particular, \citep{zou2022forecasting} unveils AutoCast, a new benchmark that employs news articles for answering forecasting queries. Nevertheless, existing methods still trail behind human performance.
The cornerstone of accurate forecasting, we argue, lies in identifying a concise, yet rich subset of news snippets from a vast corpus. With this motivation, we introduce AutoCast++, a zero-shot ranking-based context retrieval system, tailored to sift through expansive news document collections for event forecasting. Our approach first re-ranks articles based on zero-shot question-passage relevance, honing in on semantically pertinent news. Following this, the chosen articles are subjected to zero-shot summarization to attain succinct context. Leveraging a pre-trained language model, we conduct both the relevance evaluation and article summarization without needing domain-specific training. Notably, recent articles can sometimes be at odds with preceding ones due to new facts or unanticipated incidents, leading to fluctuating temporal dynamics. To tackle this, our re-ranking mechanism gives preference to more recent articles, and we further regularize the multi-passage representation learning to align with human forecaster responses made on different dates.
Empirical results underscore marked improvements across multiple metrics, improving the performance for multiple-choice questions (MCQ) by 48\% and true/false (TF) questions by up to 8\%.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present AutoCast++, a system for world event prediction relying on three components: a task-aligned retrieval module; a news summarisation module (text summarisation on retrieved news); a fusion-in-decoder model that is aligned to perform the event predictions.
They evaluate the system on the AutoCast dataset by grouping the tasks in numerical, multiple choice and true/false; considering as baselines a collection of methodologies suggested by the benchmark.
The results show that the proposed system is able to outperform the considered baselines considering different model sizes.

### Strengths
The proposed system shows remarkable performance presenting a limited impact from the model size.
The only tasks where it does not excel are the numerical ones, but it's anyway a close call with a baseline that is almost two times larger.

### Weaknesses
While the exclusion of baselines relying on new LLMs including data post mid 2021 is understandable, the ablation studies seem to suggest that relying on LLM for retrieval reranking and summarisation play a huge role in the performance of the system.
What would be convincing is to build/revamp the baselines considered using the GPT3 pre-trained version that the authors leverage in their experiments.
This would surely make the submission much stronger and convincing.

### Questions
Which GPT3 version was considered in the work?
What is the impact of binning numerical questions? Is the binning applicable also to the baselines? If yes how would results change?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces AutoCast++, an event prediction system designed to address forecasting questions by analyzing news documents. AutoCast++ comprises three key components: the Task-Aligned Retrieval Module, which re-ranks news documents based on relevance (using GPT-3 in a zero-shot manner) and recency; the Enhanced Neural Article Reader, which summarizes pertinent news content; and the Human-Aligned Loss Function, aligning system confidence with human forecaster accuracy. These components collectively led to improvements in addressing various forecasting question types in the AutoCast dataset, notably achieving a 48% enhancement in handling multiple-choice questions.

### Strengths
- Ablation study is done to evaluate the effectiveness of different components of the system.

- Their proposed system achieved 48% improvement on multiple choice forecasting questions, which is significant.

- Even the smaller version of their proposed system (with 0.2 and 0.8 billion parameters) outperforms larger baselines (with 2.8 billion parameters).

### Weaknesses
 - Limited reproducibility: The source code associated with the research paper is unavailable, so it is not possible to reproduce the results.

- In ablation study, no specific experiment has been conducted to demonstrate the isolated effectiveness of the Alignment Loss component.

### Questions
Please see the weakness section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a zero-shot ranking-based retriever-reader model for event forecasting. The model can generate the effective answers by the proposed task-aligned retrieval module and enhanced neural article reader. Experimental results on a public dataset verify the effectiveness of the proposed method.

### Strengths
1.The logic of the paper is sound.  
2.The description of the methodology is relatively clear.

### Weaknesses
1.The writing of the paper needs to be further improved and all the symbols need to be interpreted.  
2.The work focuses on a single textual modality, so why mention multiple data sources, multiple modalities in the introduction section?  
3.N_q is a subset of D. Why are the elements in N_q n and not d?  
4.The dataset used is too small and results on more as well as larger datasets are needed to be validated.

### Questions
See above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
