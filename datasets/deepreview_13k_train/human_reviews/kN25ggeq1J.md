# Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment

- Decision: Accept
- Scores: 5, 6, 6

## Abstract
The reasoning abilities are one of the most enigmatic and captivating aspects of large language models (LLMs). Numerous studies are dedicated to exploring and expanding the boundaries of this reasoning capability. However, tasks that embody both reasoning and recall characteristics are often overlooked. In this paper, we introduce such a novel task, code reasoning, to provide a new perspective for the reasoning abilities of LLMs.
We summarize three meta-benchmarks based on established forms of logical reasoning, and instantiate these into eight specific benchmark tasks. Our testing on these benchmarks reveals that LLMs continue to struggle with identifying satisfactory reasoning pathways.
Additionally, we present a new pathway exploration pipeline inspired by human intricate problem-solving methods. This Reflective Hypothesis Decomposition and Amendment (RHDA) pipeline consists of the following iterative steps: (1) Proposing potential hypotheses based on observations and decomposing them; (2) Utilizing tools to validate hypotheses and reflection outcomes; (3) Revising hypothesis in light of observations. Our approach effectively mitigates logical chain collapses arising from forgetting or hallucination issues in multi-step reasoning, resulting in performance gains of up to $3\times$. Finally, we expanded this pipeline by applying it to simulate complex household tasks in real-world scenarios, specifically in VirtualHome, enhancing the handling of failure cases. We release our code and all of results at https://anonymous.4open.science/r/code_reasoning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This article presents a dynamic prompting method that automatically adjusts the number of prompting steps based on task complexity and model performance in real time.

### Strengths
The approach taken has significant potential. The provided benchmark can be instrumental in understanding the boundaries between reasoning and recall.

### Weaknesses
The paper contains  arguments that "are a bit loose or controversial". I request that the authors make their arguments more precise, and address the ICLR audience rather than assuming that this audience knows cognitive science, and terms like System 1 and System 2 tasks.

It is helpful to learn that System 1 and System 2 tasks have been explored technically, but the authors must introduce these tasks from the ML perspective and provide the references  [5, 6, 7] to ensure readers have the proper context.

From a computer science point of view, an LLM can be viewed either as performing a mathematical function or as a software artifact.  Claims made about LLMs thus need to be validated either mathematically or empirically. The responses in the rebuttal help significantly to make things more precise.

Further, the goal to "explore the boundaries of LLM capabilities" can be presented in a more precise way. Many ML practitioners don't care about whether an LLM corresponds to some theoy of mind or human reasoning, but want to know in a precise sense what it's capabilities are.

The paper starts off in line 42 with "From the perspective of human cognitive psychology, reasoning can be viewed as a process of memory retrieval," and this is the perspective taken. There is insufficient mathematical theory or implementation to show results relevant to ICLR.

There are several claims made without defintion and/or validation. Some of these issues have been addressed in the rebuttal, but the authors must revise the article paying attention to ensuring clarity for an ML researcher.

### Questions
Can you provide any empirical evidence to back up the many claims made in the article?

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
The paper presents "code reasoning" as a novel task requiring both reasoning and memory to explore the capabilities and boundaries of LLMs. The authors propose three new meta-benchmarks based on different forms of logical reasoning, namely: inductive code reasoning (predicting program from input-output pairs), deductive code reasoning (predicting output from input-program), and abductive code reasoning (predicting input from output-program). They instantiate these meta-benchmarks into eight concrete benchmarks: List Function, MiniARC, RobustFill, and DeepCoder for inductive reasoning, and CRUXEval and LiveCodeBench for both deductive and abductive reasoning. They propose a novel pipeline, "RHDA" (Reflective Hypothesis Decomposition and Amendment), that iteratively decomposes complex problems into simpler steps, verifies the results, and based on this feedback proposes amendments. This pipeline leads to as much as 3× performance gains over baseline models.

### Strengths
1. Novel formulation and pipeline:
    - The paper introduces an intermediate task between reasoning and recall, giving us the ability to understand LLMs more deeply
    - RHDA pipeline demonstrates robustness in handling complex reasoning tasks
    
2. Comprehensive Evaluation: 
    - Three types of meta-framework with 8 specific benchmarks
    - Evaluation across different model types (GPT-4o and Claude 3.5)
    - Thorough ablation studies show the importance of each component.
3. Strong Results:
    - On inductive reasoning: RHDA outperforms baselines by 18.45% (List Function), 5.89% (MiniARC), 33.31% (RobustFill), and 12.02% (DeepCoder)
    - On deductive reasoning: Achieves 90.62% on CRUXEval and 84.16% on LiveCodeBench
    - On abductive reasoning: Achieves 83.75% on CRUXEval and 71.57% on LiveCodeBench
4. Extensibility: Successfully demonstrated application to VirtualHome environment, showing the framework can handle real-world complex scenarios like household tasks.

### Weaknesses
1. Limited Theoretical Analysis: 
  - While the paper positions code reasoning between memory and reasoning tasks, it lacks a deeper theoretical analysis of why this intermediate position is beneficial or how it relates to existing theories of reasoning. Specifically, the paper does not explore the information-theoretic properties of code as a representation for reasoning, nor does it connect its findings to established cognitive models of problem-solving. A more rigorous analysis of how code representation facilitates or hinders reasoning compared to other forms of representation would be valuable.
2. Limited Real-World Validation: 
 - While they show the program is capable of performing in VirtualHome, having quantitative benchmarks and more complex scenarios would be helpful to understand real-world applicability. The current evaluation in VirtualHome lacks standardized metrics, making it difficult to compare the performance of RHDA with other methods in a controlled setting. Furthermore, the complexity of the tasks evaluated in VirtualHome seems limited, and it is unclear how the method would scale to more intricate real-world scenarios with multiple agents and dynamic environments.
3. Incomplete Error Analysis: 
- Additional discussion on the failure modes of the RHDA pipeline would be helpful. Analysis of whether failures occur due to incorrect hypothesis formation, ineffective amendment etc is missing. The paper should include a detailed breakdown of error types, categorizing them based on the stage of the RHDA pipeline where they occur (e.g., initial hypothesis, decomposition, verification, or amendment). A qualitative analysis of specific failure cases, illustrating the limitations of the amendment process, would also be beneficial.
4. Complexity Overhead: 
- The paper doesn't analyze the computational cost of running multiple iterations of RHDA compared to single-pass methods like CoT or PoT. This is particularly important given the iterative nature of the approach. The analysis should include metrics such as the number of API calls, the total inference time, and the memory footprint of the RHDA pipeline, compared to baseline methods. Furthermore, the paper should investigate the relationship between the number of iterations and the performance gains, to determine the optimal trade-off between accuracy and computational cost.

### Questions
1. Example analysis is said to be shown in Appendix E, but Appendix E is empty. 
2. How sensitive is the method to the quality of the initial decomposition? Are there cases where poor initial decomposition cannot be recovered through amendments?
3. When and why does the RHDA pipeline fail - are the failures primarily due to poor initial decompositions, ineffective amendments, or do different tasks exhibit different failure patterns?
4. The computational overhead analysis is missing:
 -  What is the computational cost compared to baseline methods? 
 -  What is the trade-off between the number of iterations and performance gains?
5. While VirtualHome examples demonstrate RHDA's potential for real-world tasks, can you provide quantitative metrics and more complex scenarios (e.g., handling multiple interdependent tasks or recovering from failures) to better evaluate its practical capabilities?

### Soundness
3

### Presentation
3

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
This paper evaluates LLMs on code reasoning tasks, which require both recall and reasoning capabilities. The authors also propose a method RDHA which generally improves their performance in these tasks.

### Strengths
originality: RDHA is a novel method. It is interesting to see such a method to be applied to code reasoning and even planning tasks (e.g., Virtual Home).

quality: the paper conducts a systematic investigation of code reasoning tasks and an additional planning task, which is a very comprehensive task setting.

clarity: the paper is generally easy to follow.

significance: it is important to understand LLMs' capabilities and limitations.

### Weaknesses
Generally, the contributions of this paper are not strong enough.

1. If the main contribution is the evaluation of LLMs on code reasoning, it is not enough to test only two LLMs. Plus, it is not surprising that LLMs fail in complex reasoning tasks as widely testified in many existing works [1,2].

2. If the strongest contribution is RHDA, I wonder how it compares to other prompting methods such as self-refine [3].

2. Some arguments are a bit loose or controversial. For instance, the authors "...position the code reasoning task between memory and reasoning" because it requires memory of syntax from pre-training and reasoning about current question and context. In this sense, most, if not all of the reasoning tasks can be put in the middle of the Figure 1 spectrum, which has one extreme of reasoning and another extreme of recall. For instance, math, which the authors put on the reasoning extreme of the spectrum, requires the LLM to understand what operators mean as well (i.e., syntax, which also needs to come from training memory). The authors are encouraged to be more cautious in statements.

### Questions
1. What is the difference between Sub-Hyp and Chain of Thought?

2. I didn't get the rationale of why the IO prompt is the best in terms of accuracy. More specifically, what does it mean when you say this? On page 6, the end of the paragraph preceding the ablation study says "This may be a misunderstanding... than RHDA."?

3. At the bottom of page 7, "...we present a quantitative...", did you mean qualitative?

4. Did you conduct a full-scale experiment on Virtual Home? It seems that you only present two examples in the paper, which I'm not sure can generalize to the conclusion that RHDA is scalable and flexible.

5. What is the cost of RHDA? Does it generalize to other non-symbolic domains?

6. How does your method compare to self-refine?

### Soundness
2

### Presentation
3

### Contribution
3
