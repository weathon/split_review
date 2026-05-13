# ChEF: A Comprehensive Evaluation Framework for Standardized Assessment of Multimodal Large Language Models

- Decision: Reject
- Scores: 3, 8, 6, 6

## Abstract
Multimodal Large Language Models (MLLMs) have shown impressive abilities in interacting with visual content with myriad potential downstream tasks.
However, even though a list of benchmarks has been proposed, the capabilities and limitations of MLLMs are still not comprehensively understood, due to a lack of a standardized and holistic evaluation framework.
To this end, we present the first \textit{Comprehensive Evaluation Framework} (ChEF) that can holistically profile each MLLM and fairly compare different MLLMs. 
First, we structure ChEF as four modular components, \emph{i.e.}, \textit{Scenario} as scalable multimodal datasets, \textit{Instruction} as flexible instruction retrieving formulae, \textit{Inferencer} as reliable question-answering strategies, and \textit{Metric} as indicative task-specific score functions. 
Based on them, ChEF facilitates versatile evaluations in a standardized framework, and new evaluations can be built by designing new \textit{Recipes} (systematic selection of these four components).
Notably, current MLLM benchmarks can be readily summarized as recipes of ChEF.
Second, we introduce 6 new recipes to quantify competent MLLMs' desired capabilities (or called desiderata, \textit{i.e.}, calibration, in-context learning, instruction following, language performance, hallucination, and robustness) as reliable agents that can perform real-world multimodal interactions.
Third, we conduct a large-scale evaluation of 9 prominent MLLMs on 9 scenarios and 6 desiderata. Our evaluation summarized over 20 valuable observations concerning the generalizability of MLLMs across various scenarios and the composite capability of MLLMs required for multimodal interactions.io}}}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes ChEF, a framework for evaluating Multimodal Large Language Models (MLLMs). The main idea is to instantiate a “Recipe”, called “desiradata”, consisting of Scenarios (datasets), Instruction (how to pose questions such as in-context learning (ICE)), Inferencer (how an MLLM answers questions including Perplexity (PPL), Chain of Thought (CoT), and Multi-Turn), and Metrics.

They evaluate 9 MLLMs using 6 desiderata (9 Scenarios) that target measuring Calibration, In-context Learning, Instruction Following, Language Performance, Hallucination, and Robustness. See page 3 and Section 2.3 for more details.

### Strengths
- S1: The proposed ChEF framework is sound.

- S2: The experimental results are conducted on multiple models and settings and quite comprehensive.

### Weaknesses
- W1: Significance, Related work, and Execution. While I generally like the work that attempts to connect the dots and organize previous work, this work falls short. I do not think that the ChEF framework itself is a significant contribution as the 4 components of the Recipes are normally what people usually think about when it comes to evaluation. Thus, IMO, the main contributions lie in the instantiations of these Recipes or desiderata and their experimental results. However, the significance of this part is unclear due to two reasons. 

  - W1.1: First, it is unclear both in the main text and in the supplement how this work is better than existing work in terms of “scalability” and “comprehensiveness” (cf. the first paragraph of the intro). The paper has to put more emphasis on the discussion of related work in order for the reader to understand the significance.

  - W1.2: Second, the desiderata in Section 2.3 themselves need more rationales/justification. Why do we care about these capabilities? Why do we instantiate them this way? For example, Hallucination consists of asking binary questions about the existence/absence of objects. Yet, this is not the only kind of hallucination. In general, it is unclear why the desiradata is what it is. 

- W2: Clarity: related to W1, the paper would benefit from better presentation of desiradata. Perhaps having a table that lists down the 4 components. Justify why this is “versatile” evaluation.

### Questions
Please clarify as much as you can on my comments in Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a comprehensive evaluation framework for Multimodal Large Language Models (MLLMs). The newly proposed framework has four modules, Scenario, Instruction, Inferencer, and Metric; and existing evaluation benchmarks can be summarized as recipes of the proposed framework. The authors conduct large-scale evaluations and presents valuable observations in the paper.

After rebuttal: I have read the rebuttal and I'd like to keep my scores.

### Strengths
This paper introduces a comprehensive evaluation framework for Multimodal Large Language Models (MLLMs). The newly proposed evaluation framework has a modular design, which allow it to recover various existing benchmarks with different recipes. Interesting observations are also presented in the paper.

### Weaknesses
Since the main contribution of this paper is introducing this new evaluation framework. I suggest the authors to add a section describing the system design/implementation of this framework in detail. It seems that such information is missing in the current draft.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a comprehensive assessment framework for large multimodal models using  four modular components and six "recipes" that stem from desiderata. They then apply the proposed framework to several state of the art large models and present many interesting insights on their performance.

### Strengths
1. The authors demonstrate a good understanding of the problem and lay out a comprehensive framework.
2. The overall proposed framework is wide ranging and thus leads to interesting insights.
3. The authors have been thorough in their implementation and experiments.

### Weaknesses
1. The paper does not justify its choices in a principled manner. The overall framework has an ad-hoc feel to it. While the reference are comprehensive, there is not enough logic to back up why those six desiderata for example are chosen and why some others are not. The work comes across as an engineering requirements style work rather than a scientific paper. I am open to being convinced otherwise. The field is moving very fast so just seemingly brute force evaluation of a bunch of models is not going to be helpful.
2. The writing needs to tone down the claims to being pioneering etc. Or at least back up such claims.

### Questions
1. What are the insights that drive your work? Please see the comments above on weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a comprehensibe evaluation framework ChEF for evaluating Multimodal Large Language Models.  ChEF consists of four modular components and allows for versatile evaluations in a standardized manner by designing new "recipes". The authors conduct evaluation of nine MLLMs  across various scenarios.

### Strengths
1. ChEF is modularly designed with four components, Scenario, Instruction, Inferencer, and Metric, which facilitates versatile evaluations in a standardized framework and easy set up pf new evaluations.
2. ChEF evaluates six capabilities that a competent MLLM model should possess, through constructing corresponding evaluation pipelines from a ChEF Recipe. These capabilities have not been systematically evaluated in exisiting MLLM Benchmarks.
3. The authors evaluate the generalizability of nine MLLMs across various scenarios and their composite capability for multimodal
interactions, and summarize valuable observations.

### Weaknesses
1. I am not certain if it is fair to incorporate current MLLM benchmarks into ChEF. These benchmarks have taken a significant amount of time to develop, so what is the core contribution of ChEF?
2. Besides in-context learning, ChEF only evaluates single-image input. However, the comprehension of multi-image input is also an important assessment dimension for MLLMs.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
