# Large Language Models Are Not Strong Abstract Reasoners

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Large Language Models have shown tremendous performance on a large variety of natural language processing tasks, ranging from text comprehension to common sense reasoning. 
However, the mechanisms responsible for this success remain opaque, and it is unclear whether LLMs can achieve human-like cognitive capabilities or whether these models are still fundamentally circumscribed.
Abstract reasoning is a fundamental task for cognition, consisting of finding and applying a general pattern from few data. Evaluating deep neural architectures on this task could give insight into their potential limitations regarding reasoning and their broad generalisation abilities, yet this is currently an under-explored area.
In this paper, we introduce a new benchmark for evaluating language models beyond memorization on abstract reasoning tasks. We perform extensive evaluations of state-of-the-art LLMs, showing that they currently achieve very limited performance in contrast with other natural language tasks, even when applying techniques that have been shown to improve performance on other NLP tasks.
We argue that guiding LLM generation to follow causal paths could help improve the generalisation and reasoning abilities of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to evaluate the abstract reasoning ability of LLMs by curating a set of datasets. Overall the authors show that the performance of current LLMs are limited and various techniques do not help.

### Strengths
- The paper is well written and easy to follow  
- The curated benchmark seems high quality
- The experiments are extensive and demonstrate the main point.
- The observation that basic techniques do not improve performance is significant.

### Weaknesses
 - This new benchmark introduced are largely existing datasets thus with limited novelties. There are also existing works on evaluating the inductive reasoning ability of LLMs such as https://arxiv.org/pdf/2306.09841.pdf.
- This paper does not evaluate slightly more complicated prompting methods, such as simply generating more samples of code and filter by number of training examples passed. Existing papers proposing more complicated pipelines: https://arxiv.org/pdf/2212.10923.pdf, https://arxiv.org/abs/2309.05660 ,https://arxiv.org/abs/2310.08559

### Questions
n/a

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the abstract reasoning abilities of LLMs. The authors propose a benchmark for evaluating language models in order to comprehensively assess their abstract reasoning capabilities. Their experiments reveal that current LLMs struggle with abstract reasoning tasks and techniques that have previously improved performances on other NLP tasks do not result in significant enhancements for abstract reasoning.

### Strengths
1. The paper investigates abstract reasoning abilities of Large Language Models by creating a new benchmark combining existing datasets with novel datasets adapted from vision tasks for language models, which has not been extensively studied before.
2. The evaluation is pretty extensive including a wide range of models and tried a few techniques beyond just simple prompting. 
3. The paper is well-written and organized.
4. The proposed task has not yet been solved by LLMs.

### Weaknesses
1. this task will be automatically solved when models of better reasoning capabilities become available.
2. The authors frame abstract reasoning as "a potential task for effective measurement of the cognitive abilities of neural models", so the utility of this benchmark is mostly evaluation of LLMs. One concern is that there isn't an actual application that would benefit from studying this kind of reasoning capabilities.

### Questions
1. Have authors considered fine-tuning?  It would be nice to show even fine-tuning Llama2 is not enough for solving the abstract reasoning tasks.
2. Curious to see how zephyr-7b-beta (https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) performs on the proposed benchmark.
3. How is open-ended QA evaluated?
4. Do the authors have plans to maintain a leaderboard for this task? Will there be a held out test set?
5. What is the data releasing plan for this benchmark?
6. Also curious about human performance on this benchmark. For example, I couldn't figure out the example in Figure 6.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an evaluation of Large Language Models (LLMs) on abstract reasoning tasks. The authors introduce a new benchmark for evaluating LLMs on abstract reasoning and conduct extensive experiments on language models. The results show that LLMs currently achieve limited performance on abstract reasoning tasks compared to other natural language tasks. The authors also explore the impact of fine-tuning and prompt design techniques on abstract reasoning performance.

### Strengths
1. This article attempts to address a topic of great interest - whether large models possess the capacity for abstract reasoning.
2. The authors provide a comprehensive evaluation and conduct extensive experiments on various language models.

### Weaknesses
1. Similar conclusion has been explored by previous studies [1][2].

[1] "Reasoning or reciting? exploring the capabilities and limitations of language models through counterfactual tasks." arXiv preprint arXiv:2307.02477 (2023).

[2] "Large Language Models are In-Context Semantic Reasoners rather than Symbolic Reasoners." arXiv preprint arXiv:2305.14825 (2023)

2. Lack of experiment with larger models or advanced models. Fine-tuned on smaller models cannot sufficiently draw the conclusion.

### Questions
1. Can you experiment with more advanced models Llama-2, with better performance than Llama1, Alpaca, or fine-tune with larger models (13B, 70B)? 
2. The details of fine-tuning experiments, such as training data, training steps. Do you consider incorporating the instruction about “how to induce”, “how to deduce” into supervision?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
