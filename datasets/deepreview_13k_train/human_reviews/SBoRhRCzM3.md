# THOUGHT PROPAGATION: AN ANALOGICAL APPROACH TO COMPLEX REASONING WITH LARGE LANGUAGE MODELS

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Large Language Models (LLMs) have achieved remarkable success in reasoning tasks with the development of prompting methods. 
However, existing prompting approaches cannot reuse insights of solving similar problems and suffer from accumulated errors in multi-step reasoning, since they prompt LLMs to reason \textit{from scratch}.
To address these issues, we propose \textbf{\textit{Thought Propagation} (TP)}, which explores the analogous problems and leverages their solutions to enhance the complex reasoning ability of LLMs.
These analogous problems are related to the input one, with reusable solutions and problem-solving strategies.
Thus, it is promising to propagate insights of solving previous analogous problems to inspire new problem-solving. 
To achieve this, TP first prompts LLMs to propose and solve a set of analogous problems that are related to the input one. 
Then, TP reuses the results of analogous problems to directly yield a new solution or derive a knowledge-intensive plan for execution to amend the initial solution obtained from scratch.
TP is compatible with existing prompting approaches, allowing plug-and-play generalization and enhancement in a wide range of tasks without much labor in task-specific prompt engineering. 
Experiments across three challenging tasks demonstrate TP enjoys a substantial improvement over the baselines by an average of 12\% absolute increase in finding the optimal solutions in Shortest-path Reasoning, 13\% improvement of human preference in Creative Writing, and 15\% enhancement in the task completion rate of LLM-Agent Planning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Current prompt-based methods limit LLMs from using past knowledge, making complex tasks difficult. This work alleviates this issue and improving the reasoning performance of LLMs on complex problems with a novel Thought Propagation (TP) framework, which is rooted in the fundamental analogical reasoning ability of human cognition. Given an input problem, TP prompts LLMs to seek for its analogous problems. Then, it initializes the solutions to the input problem and its analogous counterparts with existing prompting methods such as standard prompt, CoT etc. Finally, TP instantiates analogical reasoning to update the initial solution to the input problem in two ways: 1. directly develops a refined solution to the input problems and 2. devise a knowledge-intensive plan to improve input problem solving. All these steps are automated with LLMs by prompting. Thus, TP teach LLMs to reason in an analogical way and achieves plug-and-play enhancement to current prompt methods without extensive labor in task-specific prompt engineering. Experiments on three challenging tasks validate the generality and significant performance gain of the proposed TP framework.

### Strengths
* Originality: This work introduces the novel TP framework to enhance LLMs' reasoning by reusing experience in solving similar problems. While previous research explored analogical reasoning on knowledge graphs, a generalized analogical reasoning framework for LLMs was missing until TP. It includes three automated modules: LLM Propose, LLM Solve, and LLM Aggregate, providing a plug-and-play advantage over existing "reason-from-scratch" methods. TP also extends the success of neighborhood propagation in Graph Neural Networks to analogical problem-solving, an innovative and non-trivial generalization, sparking new directions in LLM reasoning. 

* Clarity: This paper is overall well-structured and easy to follow. The general setup in the section of methodology helps readers to understand the proposed TP framework. Additionally, the detailed information on TP for task instantiation in the Experiment and Appendix sections facilitates implementation and reproducibility.

* Evaluation: Extensive evaluation across three tasks demonstrates TP's substantial performance improvement compared to baseline methods across various LLM backbones.

* Significance: TP's modular design exhibits impressive generality across various tasks. It has great chances to benefit researches in diverse directions.

### Weaknesses
Authors should enhance the related work section for a more thorough comparison.

* The authors are encouraged to compare TP with Self-refined LLM reasoning methods [1,2] since TP also manages to refine the solution to the input problems in LLM Aggregation module.
* In shortest path reasoning tasks, does TP sometimes deteriorate the solutions to some testing instances instead of improving them?

### Questions
Please refer to weaknesses part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This text introduces Thought Propagation (TP), an approach to enhance Large Language Models' (LLMs) reasoning abilities. TP leverages insights from solving analogous problems to improve complex reasoning. It prompts LLMs to propose and solve related analogous problems, reusing their solutions and problem-solving strategies. Experiments show that, TP outperforms existing methods such as Chain-of-Thought and Tree-of-Thought on three challenging tasks by large margins.

### Strengths
1. The idea that exploring analogous problems and leveraging the solutions to prompt the reasoning task of LLMs is interesting and with broad interests to the research and application of LLMs. The authors provide many analyses and examples to show the efficacy of the proposed thought propagation (TP), which are convicing.

2. The method does not require to train the LLMs with sophisticated strategy or careful design of datasets in some previous works, but is a plug-and-play approach in inference, which is efficient and environment friendly, and can be generalize to various LLMs.

3. The performance improvements are significant.

### Weaknesses
1. TP is training-free, but compared to train-of-thought, it requires more action steps to propose, solve, and aggregate analogous problems, which is more computationally-costly and complex.

2. Some typos: in page 9, the last sentence of section 6, the quotation marks should be `` ''.

### Questions
1. Can we combine TP with CoT to achieve further performance improvements?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new LLM prompting strategy, Thought Propagation (TP), which generates analogies to the input problem, generates solutions to them, evaluates the solutions (using the LLM itself), and then uses the correct solutions either to directly solve the input problem, or to derive a high-level plan to solve the input problem. TP is evaluated against relevant baseline methods on three tasks:  shortest-path reasoning, creative writing, and planning in ALFWorld. The results show that TP consistently obtains higher scores than the baseline methods tested.

### Strengths
The surprising and potentially exciting finding is that this reasoning-through-generated-analogies helps solve the input problem even without ground-truth validation of the correctness of the solutions to the analogies. It's surprising because of the counterintuitive nature of the finding; one might have expected ToT to outperform TP since ToT spends its compute on the input problem rather than on analogies which are, by definition, somewhat different than the input problem.

The work deals with an important topic, is carefully motivated, and the results are analyzed in detail.

### Weaknesses
Since TP outperforms ToT by a surprising and counterintuitive amount, it is critical to compare the two methods in terms of token cost, which is a controllable quantity for both TP and ToT. The authors acknowledge the importance of comparing token cost in their discussion of Figure 5:  “1-layer TP outperforms ToT by a large margin in different LLM backends but shares similar token expenses.” However, this figure applies only to the shortest-path task, which is highly problematic for evaluating LLMs. The task is contrived in the sense that one would never actually use an LLM to solve a shortest-path task, and one would not expect much LLM training data to be relevant to solving such tasks. Even more importantly, the results of this evaluation are likely to depend very sensitively on the details of how the graph definition is represented in natural language for insertion into the prompt. Therefore one would expect that making subtly different choices in representation could make very large differences in performance, and some of those choices would just happen to favor certain prompt approaches (like TP) over others (like ToT). For these reasons, it seems hard to conclude much from the shortest-path experiments. Unfortunately, no token costs are provided for the other two experiments. This leads me to doubt the validity of the paper’s central finding.

I still question the relevance of the shortest-path experiments. In rebuttal, the authors argued that the shortest-path task is a good testbed for evaluating LLM reasoning for 3 reasons:
- It is a challenging task, requiring many steps to solve over a variety of graphs.  
- Some concurrent work has applied LLMs to graphs. 
- Generated graphs avoid data contamination.

I agree that application of LLMs to graphs is an interesting line of investigation, where these 3 reasons make sense. But the goal of this work, as staked out in the title and abstract, is to compare different prompting techniques across a broader range of LLM applications. If the paper’s claims were confined to the graph domain, the significance of the work would be greatly limited.

### Questions
None

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
