# Agent Skill Acquisition for Large Language Models via CycleQD

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Training large language models to acquire specific skills remains a challenging endeavor.
Conventional training approaches often struggle with data distribution imbalances and inadequacies in objective functions that do not align well with task-specific performance.
To address these challenges, we introduce \implname, a novel approach that leverages the Quality Diversity framework through a cyclic adaptation of the algorithm, along with a model merging based crossover and an SVD-based mutation.
In \implname, each task's performance metric is alternated as the quality measure while the others serve as the behavioral characteristics.
This cyclic focus on individual tasks allows for concentrated effort on one task at a time, eliminating the need for data ratio tuning and simplifying the design of the objective function.
Empirical results from AgentBench indicate that applying \implname to \textsc{Llama3-8B-Instruct} based models not only enables them to surpass traditional fine-tuning methods in coding, operating systems, and database tasks, but also achieves performance on par with \textsc{gpt-3.5-turbo}, which potentially contains much more parameters, across these domains.
Crucially, this enhanced performance is achieved while retaining robust language capabilities, as evidenced by its performance on widely adopted language benchmark tasks.
We highlight the key design choices in \implname, detailing how these contribute to its effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This paper presents CycleQD, a novel framework for making llm acquire specific skills through Quality Diversity (QD) optimization. CycleQD addresses challenges in skill training, such as data imbalance and inadequate objective functions, by cyclically alternating quality measures for different tasks.  CycleQD shows competitive results, achieving performance on par with GPT-3.5-TURBO.

### Strengths
The paper presents an innovative approach to LLM skill acquisition, uniquely applying the Quality Diversity paradigm to cycle through task-specific optimizations, which is quite novel. 
The experimental results on the proposed CycleQD framework show a substantial performance gain, validating the model’s effectiveness and overall performance.
Overall, CycleQD introduces a scalable method to merge agent skills into LLMs, addressing critical challenges in agent-based LLM design.

### Weaknesses
Although the CycleQD  is designed for the agent skill acquirment of LLMs, the experiments predominantly focus on computer science tasks, such as OS and DB. Its applicability to other fields as agents will futher strength this paper.

The methodology, though effective, involves a multi-step process (crossover, mutation, cyclic quality alternation) that may be complex. The author may need to provide a clearer illustration of the methodology, such as an overview figure of the method pipeline.

The ablation study does not provide substantial evidence of the proposed method's effectiveness, as the performance gains of each component are minimal.

### Questions
I am also curious about any real-world application tests using the proposed method across different scenarios, given that the scenarios in the experiments are quite similar.

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
This paper introduces evolutionary approaches for merging large language models (trained on individual skills), as an alternative to fine-tuning (jointly on multiple skills). This is the first work to merge models using Quality Diversity (QD) algorithms. This work introduces a cyclic adaptation for QD: the optimization is conducted for one task at a time (in a cycle). Models are merged in the crossover operation by linearly combining task vectors. Finally, the mutation function modifies the "child" (from crossover) by sampling perturbations from the SVD components of its task vector.

This approach is tested using coding, OS, and DB skills. This evolutionary approach for model merging outperforms both fine-tuning based methods (by +5.4 pts) and other model merging methods (by +5.5 pts). The ablations show that each component of this method (cycle adaptation, SVD-based mutation, and elite sampling) lead to gains (on average). This method also generalizes to out-of-distribution coding tasks (more than fine-tuned, single-task experts) while also retaining performance on language skills. On the other hand, the merged model produced by this approach underperforms on individual tasks compared to fine-tuned experts for the domain of image segmentation.

### Strengths
This work appears to be very original: (1) it is different from conventional fine-tuning and even model merging methods, and (2) it alleviates certain design decisions, like data mixing ratios and different objectives, when fine-tuning on multiple tasks.

I understand that previous evolutionary approaches don't update the weights directly and this method proposes to do so (using the framing of model merging). I think this is a significant contribution. I think the specific adaptations they propose are also positive contributions.

From what I can see, this method establishes sufficient gains over the alternative methods in the computer science tasks. Since this paper introduces several components, I was looking for (and was satisfied to find) the ablations in Table 3.

### Weaknesses
I think the writing is mostly clear, but this paper assumes some extra background knowledge about evolutionary methods. I would really appreciate it if the authors (briefly) introduce such approaches and terminology from first principles, before the details of their augmentations.

It would also be great if the authors could again motivate the need for evolutionary approaches (rather than fine-tuning) in training or merging models. Is it just the avoidance of design decisions that I mentioned above? Are there more fundamental motivations (like the diversity of skills captured by this method, which was briefly mentioned)? Or is this direction of work primarily exploratory?

I am not already familiar with evolutionary approaches, so no significant methodological weaknesses are obvious to me. I will wait to see what other reviewers have to say, but generally hold a positive opinion for now.

### Questions
Formatting: I see that a couple half-column figures are used (concatenated horizontally with text). Please make sure that this abides by the formatting rules and correct if not.

Is it normal for model merging approaches to test using just 2-3 tasks?

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
3

### Summary
The paper proposed CycleQD to achieve superior performance on multiple agent skills while retaining robust language capabilities.

### Strengths
- The paper discussed a critical problem: achieving superior performance on multiple skills while retaining language capabilities. 
- The proposed method is novel.

### Weaknesses
Overall, the major weakness of this paper is its presentation. For the audience not familiar with evolutionary computation, the paper is hard to follow.
1. [Presentation] Problems in understanding the proposed method.
	- Explain the evolution of figure 4 by referring to algorithm 1. The figures are meant to give direct intuitions about how the algorithm works, but the current delivery fails to achieve this purpose. Specifically, the connection between the steps in Algorithm 1 and the visual changes in Figure 4 are not clear. For example, it's unclear how the elite selection process in the algorithm translates to the changes observed in the figure's population distribution.
	- In the elite sampling (line 217), what does the formula intuitively means? Specifically, what is the meaning of $ \gamma$ . It is not clear how the weighting factor, gamma, is derived or what its impact is on the selection of elites. The paper lacks a clear explanation of how this parameter influences the exploration-exploitation trade-off in the algorithm.
	- In the crossover (Sec. 3.2), there are no explanations for why $w$ are sampled from gaussian? From my understanding, $w$ are used to determine component weights for combining task vectors. The component weights should be greater than $0$ . But Gaussian samples has infinite range. The use of Gaussian sampling for weights is not justified, especially when these weights are intended to combine task vectors. The paper should clarify why negative weights are allowed and what their impact is on the resulting model.
	- In the mutation (Sec. 3.3), there are no explanations for why SVD can address the challenge of excessive exploration in parameter space or overfitting. In addition, clarify how the proposed SVD-based mutation allows finer control of $\theta_{child}$ (line 283). The paper does not provide a clear explanation of how SVD helps to mitigate overfitting or excessive exploration. It is unclear how the singular vectors are used to control the mutation process and how this leads to finer control over the child model's parameters.
	- In the model aggregation (Sec. 3.4), there are no explanations for why the proposed convex combination is adopted for obtain the final model. In particular, what is the connection between this design choice and the major goal of this paper, i.e., achieving superior performance on multiple tasks without degradation on other tasks. The paper does not justify the choice of convex combination for model aggregation. It is not clear how this method ensures that the final model maintains high performance across all tasks without degrading performance on any specific task.
2. [Contribution] CycleQD on SAM is irrelevant with the main topic of this paper, which focuses on language models.
3. [Soundness] The current experiments include only three tasks. Including more tasks to support the generality of CycleQD is better.

### Questions
1. Questions on presentation issues: see above. 
2. Is it possible to combine finetuning and CycleQD, e.g., SFT after CycleQD? What would be the result.
3. Computation and time cost comparisons between CycleQD and gradient-based fine-tuning.
4. The number of generations is critical for selecting elites. How sensitive is CycleQD regarding this hyperparameter?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces CycleQD, a framework for enhancing large language models' skill acquisition through cyclical quality diversity optimization. CycleQD first trains expert models for individual skills, then combines them using model merging as crossover operations and SVD-based mutations, while cycling through different task metrics as quality measures. The method alternates between optimizing different skills by maintaining separate archives, each tracking models with diverse behavioral characteristics.

### Strengths
1. Demonstrates strong empirical results by achieving comparable performance to GPT-3.5-TURBO on coding, OS and DB tasks using only an 8B parameter model
2. Avoids the complex tuning of data ratios and objective functions by decomposing multi-skill training into single-skill training followed by model merging
3. Provides full ablation studies validating the necessity of key components including cyclic adaptation, SVD-based mutation, and elite sampling

### Weaknesses
1. Elite sampling strategy lacks theoretical foundation and uses arbitrary hyperparameters (0.5-0.8 range) without clear justification. The selection of elites based on an aggregated score of Q and BC values, while intuitively appealing, lacks a rigorous mathematical basis. The method does not explain why this specific aggregation is optimal or how it relates to established multi-objective optimization principles. The chosen range for hyperparameters is also not justified by any systematic analysis or theoretical argument, making it difficult to reproduce or generalize the results.
2. Computational costs and efficiency not analyzed or compared with baseline methods. The paper does not provide a detailed analysis of the computational resources required by CycleQD, including memory usage and runtime. This omission makes it difficult to assess the practical feasibility of the approach, especially when compared to more established methods like fine-tuning or other multi-objective optimization techniques. A breakdown of the computational cost of each step (expert training, merging, mutation) would be necessary for a comprehensive evaluation.
3. Missing comparison with established multi-objective optimization approaches like NSGA-II or Pareto-based methods. While the authors mention the limitations of NSGA-II, they do not provide a thorough comparison with other Pareto-based methods or alternative multi-objective optimization algorithms. A more comprehensive benchmark against a wider range of established methods would be necessary to fully contextualize the performance of CycleQD and highlight its unique advantages and disadvantages.

### Questions
1. Why is cyclic optimization more effective than simultaneous optimization of multiple objectives?
2. What is the theoretical basis for using SVD decomposition in mutation, how does it help explore the parameter space more effectively?
3. Can this method scale to combining skills from vastly different domains (e.g., math, creative writing, and visual reasoning)? Would it still outperform traditional SFT?

### Soundness
3

### Presentation
3

### Contribution
3
