# Subtle Errors Matter: Preference Learning via Error-injected Self-editing

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Large Language Models (LLMs) have exhibited strong mathematical reasoning and computational prowess, tackling tasks ranging from basic arithmetic to advanced competition-level problems. However, frequently occurring subtle errors, such as miscalculations or incorrect substitutions, limit the models' full mathematical potential. Existing studies to improve mathematical ability typically involve distilling reasoning skills from stronger LLMs or applying preference learning to step-wise response pairs. 
Although these methods leverage samples of varying granularity to mitigate reasoning errors, they overlook the frequently occurring subtle errors. A major reason is that sampled preference pairs involve differences unrelated to the errors, which may distract the model from focusing on subtle errors. 
In this work, we propose a novel preference learning framework called eRror-Injected Self-Editing (RISE), which injects predefined subtle errors into partial tokens of correct solutions to construct hard pairs for error mitigation. In detail, RISE uses the model itself to edit a small number of tokens in the solution, injecting designed subtle errors. Then, pairs composed of self-edited solutions and their corresponding correct ones, along with pairs of correct and incorrect solutions obtained through sampling, are used together for subtle error-aware DPO training. 
Compared with other preference learning methods, RISE further refines the training objective to focus on predefined errors and their tokens, without requiring fine-grained sampling or preference annotation. 
Extensive experiments validate the effectiveness of RISE, with preference learning on Qwen2-7B-Instruct yielding notable improvements of 3.0\% on GSM8K and 7.9\% on MATH.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a preference learning framework called RISE for DPO training. The key idea is to inject carefully created noise in the correct-incorrect answer pairs to guide the model which mistakes to avoid.

### Strengths
The paper studies how to optimize preference learning, a timely and important topic. The proposed method RISE is easy to understand, and showcases empirical performance gains on two commonly used open-source models, qwen and llama.

### Weaknesses
My major concern is the scope of the performance evaluation. Across all experiments in this paper, the models are trained on a single dataset extracted from Lai et al 2024. It is not clear if the results are cherry-picked or not. For example, how about other DPO training datasets for Math and other datasets? In addition, it is not clear how RISE affects the models' quality on other tasks. The authors classify the 6 evaluation datasets used in this paper as either "in-distribution" or "out-of-distribution", but they are all indeed math-related questions. It would be more desired to see evaluation on real out-of-distribution datasets, such as physics or logic heavy datasets (e.g., ZebraLogic or ARC corpus).

### Questions
See my weakness comment.

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
4

### Summary
The paper presents a novel preference learning framework known as eRror-Injected Self-Editing (RISE), which is designed to enhance the mathematical reasoning capabilities of Large Language Models (LLMs). The core contribution of RISE is its innovative approach to error mitigation by injecting subtle, predefined errors into correct solutions, creating hard pairs for training that help the model focus on common mistake patterns.
The framework operates by using the LLM to generate correct multi-step solutions and then intentionally introducing errors into these solutions to form self-edited pairs. These pairs, along with correctly and incorrectly solved samples, are used for subtle error-aware Direct Preference Optimization (DPO) training. The paper reports improvements on mathematical reasoning tasks when RISE is applied to LLMs like Qwen2-7B-Instruct, and shows improvement on the GSM8K and MATH dataset. These results demonstrate the effectiveness of RISE in refining the training objective to target subtle error tokens and in improving the model's ability.

### Strengths
1. Originality: The paper introduces RISE, a novel preference learning framework that addresses the subtle error problem in LLMs, which is not commonly seen in other works.
2. Quality: The paper compares RISE with other preference learning methods and shows that it outperforms them, which shows the quality of the approach.
3. Significance: The paper makes a significant contribution to the field of LLMs by providing a method to improve their mathematical reasoning capabilities, which is a critical area for LLM development.

### Weaknesses
1. Generalizability and Domain-Specificity: The paper focuses exclusively on mathematical reasoning tasks. It would be beneficial to see how RISE performs in other domains, such as reasoning and coding, where subtle errors also play a significant role. The current evaluation lacks a comparative analysis of RISE's performance across diverse tasks, making it difficult to assess its broad applicability. For example, the types of errors common in mathematical problem-solving might not translate directly to coding or logical reasoning, where syntax, logical flow, and algorithmic errors are more prevalent.
2. Diversity of Error Types: While the paper addresses common error types in mathematical reasoning, it may not cover all possible error categories. For instance, it might be worth exploring errors related to the interaction of different error types. The current approach seems to focus on isolated error injections, potentially missing the complex interplay of errors that can occur in real-world scenarios. For example, a single mathematical problem might involve both a misapplication of a formula and an arithmetic error, and the model's ability to handle such combined errors is not evaluated.
3. Experiments: The authors should evaluate the performance of RICE on more open-source models (such as Mistral-7B-Instruct-v0.3, qwen 2.5 series). And the influence of hyperparameter $\alpha$ should also be explored. The lack of experiments on a wider range of open-source models limits the generalizability of the findings. The current evaluation is limited to a single model architecture, and it's unclear whether the observed improvements would hold for other models with different architectures and training methodologies. Furthermore, the sensitivity of the method to the hyperparameter $\alpha$ needs to be thoroughly investigated to determine the optimal range and its impact on performance.

### Questions
1. The interaction of different error types: Will the interaction of different error types improve the performance?
2. Number of self-edited pairs: Why the performance on GSM8K and MATH both decrease with more self-edited pairs? Please further analyse this pheonomenon to pre-define the number of self-edited pairs.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents a model fine-tuning method that aims to solve the math problem of LLMs. Specifically, the paper reuses the existing training paradigm (RLFH or DPO concretely) but pays attention to the training pair generation. The negative sample is generated by prompting LLM with intentional instruction on producing wrong answers (with particular error types described in Section 2.1). The main motivation comes from the hypothesis that the existing fine-tuning solution does not provide targetted training pairs, causing the fine-tuned model to capture subtle errors that are not intended. 

The training objectives are borrowed from previous works, including DPO, step-wise DPO, and negative log-likelihood loss (to stabilize the training). The contribution of this paper is more about how to get better negative samples. Experiments show the proposed approach provides reasonable improvement on small models (7B) but with limited improvement on large models (70B). Compared to the DPO solution previously used, the improvement is also not very significant.

### Strengths
The paper is well-written and easy to understand. The majority of the descriptions are with clear equations or demonstrative figure supports. While some contents are not included in the paper, they are well-known in the literature. 

Actively looking for hard negative examples is always a research topic. The paper focuses on generating regularized negatives (from the list of error types) such as enforcing the fine-tuned model to avoid making similar mistakes. The strategy is letting LLM provide the wrong examples as part of forward passing over steps.  

Experiments included multiple LLMs in comparison. While most of them are not intended to solve math problems, it is good to have more things to compare.

### Weaknesses
The most obvious weakness of this paper is the lack of solid evidence of motivation. While the paper stated that negative samples randomly generated may be unrelated to error, there is no solid evidence on how it impacts the model's math ability. The research gap has yet to be explicitly visible so far. The authors should provide sufficient insight into how those randomly sampled negatives hurt the performance with solid evidence. I am not very convinced this issue is significant. Considering the limited performance improvement on large models (70B), I am concerned if this is indeed a problem of existing works.

Most of the approaches used in this paper are existing training methods. The novelty of this paper is weak, given it is simply proposing a negative sample generation approach. The majority of the training descriptions are optional, given they are well-known. E.g. DPO, step-wise DPO, or NLL. The authors give good justification for why using prompts to generate the wrong sample is an impactful contribution. 

The last point of concern is the performance improvement of large models. The proposed method does not seem to improve the performance of the large models much. Why is that? It seems not an improvement space problem since the large LLMs still suffer from math problems with many errors. However, even after this fine-tuning, the proposed solution fails to take care of them. Any insight? Is it indicating the proposed solution is going in the wrong direction for solving this problem?

### Questions
1. Why does this solution fail to improve the math of large models compared to the models fine-tuned on random negative samples? If someone uses a very simple negative sampling approach by generating random numerical values, is there any performance difference from the proposed solution?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel approach to enhancing the performance of language models in mathematical problem-solving by introducing noise into correct solutions to create subtly incorrect answers. These correct/incorrect answer pairs are then utilized to fine-tune a DPO (Direct Preference Optimization) model. Empirical evidence demonstrates the effectiveness of this approach in improving the model’s accuracy.

### Strengths
1. The paper effectively addresses the challenge of subtle error detection, a common issue faced by large language models (LLMs). The proposed method successfully enhances models, transforming relatively weaker ones into stronger versions.
1. The technique leverages the simplicity of generating incorrect solutions rather than correct ones, making the training process more efficient. By instructing models to produce errors, it harnesses the LLM’s capability to identify likely mistakes based on its own tendencies, leading to a self-improvement mechanism.

### Weaknesses
1. The effectiveness of this method heavily relies on prompt engineering. The quality and specificity of the prompts used to generate incorrect answers significantly influence the quality and subtlety of the generated mistakes.
1. As the approach is based on pre-defined templates, it may not capture the full spectrum of potential errors a language model might make, leaving certain blind spots unaddressed.
1. The scalability of the proposed method remains uncertain, as it primarily focuses on generating diverse incorrect answers rather than ensuring diversity in correct solutions. This might limit its applicability in more complex or varied scenarios.

### Questions
1. Do you think this method can be extended to other domains where subtle mistake detection is crucial, such as logical reasoning and programming? If so, what adaptations would be necessary?

### Soundness
3

### Presentation
3

### Contribution
3
