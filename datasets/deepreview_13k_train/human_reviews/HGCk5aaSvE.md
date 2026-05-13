# Pareto Prompt Optimization

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Natural language prompt optimization, or prompt engineering, has emerged as a powerful technique to unlock the potential of Large Language Models (LLMs) for various tasks. While existing methods primarily focus on maximizing a single task-specific performance metric for LLM outputs, real-world applications often require considering trade-offs between multiple objectives. In this work, we address this limitation by proposing an effective technique for multi-objective prompt optimization for LLMs. Specifically, we propose **ParetoPrompt**, a reinforcement learning~(RL) method that leverages dominance relationships between prompts to derive a policy model for prompts optimization using preference-based loss functions. By leveraging multi-objective dominance relationships, ParetoPrompt enables efficient exploration of the entire Pareto front without the need for a predefined scalarization of multiple objectives. Our experimental results show that ParetoPrompt consistently outperforms existing algorithms that use specific objective values. ParetoPrompt also yields robust performances when the objective metrics differ between training and testing.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the multi-objective prompt optimization challenge through a novel method called ParetoPrompt. In particular, ParetoPrompt introduces a reinforcement learning from human feedback (RLHF) approach that utilizes dominance preference data, enabling it to efficiently explore optimal trade-offs across multiple objectives. This approach is both innovative and promising, as it allows for nuanced optimization without relying on rigid scalarization functions.

### Strengths
- Introducing reinforcement learning from human feedback (RLHF) into Pareto optimization is a novel and inspiring approach, adding a valuable dimension to multi-objective optimization.
- The final results are promising, demonstrating the method's potential to achieve balanced and effective trade-offs across objectives.

### Weaknesses
 - The motivation for using RLHF in Pareto optimization, as opposed to standard Pareto algorithms, could be further elaborated to strengthen the case for this approach.
- The paper lacks a detailed report on querying budgets (or optimization efficiency), which is critical for assessing practical performance in prompt optimization.
- The learning procedure for the reward model appears complex and may be challenging to implement or adapt across diverse applications.
- Including more results with a greater number of objective functions would enhance the evaluation and demonstrate broader applicability.

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces ParetoPrompt, a reinforcement learning method designed for multi-objective prompt optimization.

### Strengths
The reported experiments show the proposed algorithm outperform the baseline methods under a variety of metrics

### Weaknesses
1. More recent baseline methods should be compared. For example: https://arxiv.org/abs/2406.12845
2. Any theoretical justifications that the proposed training process (in the end of section 3) is Pareto-optimal?
3. In the proposed training process, how to estimate the objectives of the corresponding outputs y1 and y2?

### Questions
see above

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a Pareto prompt optimization algorithm. Instead of considering a single objective, this paper considers multi-objective in a real prompt optimization scenario and proposes an RL-based algorithm to find the Pareto optimal prompts in the Pareto front and achieve better performance than other algorithms.

### Strengths
1. The Pareto prompt optimization problem proposed by the author is novel and practical for me
2. The presentation of the algorithm design is great
3. The experimental results shows that the Pareto prompt optimization algorithm outperforms other methods.

### Weaknesses
1. This paper did not provide enough discussion on the related works of prompt optimization, [1,2,3,4] are some of the works that I think should be included.

2. In the comparison, the author did not provide any comparison with existing prompt optimization works like [1,2,3,4]. More justification of comparison on this is needed to position this paper in the area of prompt optimization.

### Questions
1. How does the approach proposed in this work different from [5]? Since [5] also considers the human preference in prompt optimization (in this paper's case, dominance relationship). Could the author provide some explanation? If indeed, there are some similarity, is it possible to compare this work as one of the baseline in the paper?

[5] Lin, X., Dai, Z., Verma, A., Ng, S. K., Jaillet, P., & Low, B. K. H. (2024). Prompt Optimization with Human Feedback. arXiv preprint arXiv:2405.17346.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors proposed a prompt optimization method relying on the pareto dominance relationships between prompts. This avoids a predefined aggregation among the multiple objectives. Instead, a loss containing separate components for dominance and non-dominance data is designed, optimizing for pareto optimal prompts on the pareto frontier. Experiments are conducted on real-world datasets and language models, showing the method’s capability of producing well-performing prompts across multiple objectives.

### Strengths
1. Studies an important practical problem of multi-objective metric design when the explicit structure is unknown.
2. The special treatment for non-dominated prompts contributes to the novel design of the overall loss function.
3. Clear visual illustration of the results lying on the pareto front.

### Weaknesses
1. The experiments are not extensive enough, e.g., no experiment beyond 3 objectives, and only models like BERT and GPT2 are used.
2. The experiment design on the choice of objectives can be improved. Having prompt fluency as the objective makes less sense as compared to output fluency, conciseness, informativeness, style alignment, etc.

3. Since non-dominated prompts consist of the majority of the sampled prompts, will they also dominate the loss function? For example, if most of the prompts are non-dominated, optimizing the loss function basically gives the same reward for almost all prompts. Please clarify.
4. Clarify how having the loss in equation (4) encourages “diversifying non-dominated prompts” as stated in line 257?
5. In the experiments, the fluency of the prompt is used as an objective. This is counterintuitive: I would imagine the fluency of the output/generation to be much more important than the fluency of the prompt itself. This makes the experiment results less convincing.
6. From Figure 3, I can see that ParetoPrompt produces many prompts that lie on the “pareto front”. If I need to choose one of them eventually to use in the system, how should I choose the prompt?
7. It seems strange to me that the percentage of non-dominated samples increases with training, but the loss also keeps increasing.
8. When the number of objectives increases, it is expected to have much more conflicts (non-dominant pairs) as compared to dominant ones. Though this is discussed as a limitation in the last section, I always have this doubt in mind while reading the paper, do consider bringing this comment to an earlier section of the paper for clarity. On a side note, I would like to know the rough maximum number of objectives that ParetoPrompt can handle in practice?
9. A missing related work [1] on using preference optimization for prompt optimization.
10. [Typo] Line 404, “ouput” → “output”

### Questions
1. Since non-dominated prompts consist of the majority of the sampled prompts, will they also dominate the loss function? For example, if most of the prompts are non-dominated, optimizing the loss function basically gives the same reward for almost all prompts. Please clarify.
2. Clarify how having the loss in equation (4) encourages “diversifying non-dominated prompts” as stated in line 257?
3. In the experiments, the fluency of the prompt is used as an objective. This is counterintuitive: I would imagine the fluency of the output/generation to be much more important than the fluency of the prompt itself. This makes the experiment results less convincing.
4. From Figure 3, I can see that ParetoPrompt produces many prompts that lie on the “pareto front”. If I need to choose one of them eventually to use in the system, how should I choose the prompt?
5. It seems strange to me that the percentage of non-dominated samples increases with training, but the loss also keeps increasing.
6. When the number of objectives increases, it is expected to have much more conflicts (non-dominant pairs) as compared to dominant ones. Though this is discussed as a limitation in the last section, I always have this doubt in mind while reading the paper, do consider bringing this comment to an earlier section of the paper for clarity. On a side note, I would like to know the rough maximum number of objectives that ParetoPrompt can handle in practice?
7. A missing related work [1] on using preference optimization for prompt optimization. 
8. [Typo] Line 404, “ouput” → “output”

References:

[1] Prompt Optimization with Human Feedback. In ICML 2024 Workshop on Models of Human Feedback for AI Alignment.

### Soundness
2

### Presentation
3

### Contribution
3
