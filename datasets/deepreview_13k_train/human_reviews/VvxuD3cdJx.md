# AutoScale: Combining Multi-Task Optimization with Linear Scalarization

- Decision: Reject
- Scores: 6, 5, 6

## Abstract
Multi-task learning is favored due to its efficiency and potential transfer learning achieved by sharing networks across tasks. While a series of multi-task optimization algorithms (MTOs) have been proposed to solve MTL optimization challenges and enhance performance, recent research claims that simple linear scalarization, which sums per-task loss with a carefully searched weight set, is sufficient, casting doubt on the added value of more complex MTO algorithms. In this paper, we provide a novel perspective that linear scalarization and MTOs are closely related and can be combined to yield high performance and efficiency. We show, for the first time, that a well-performing linear scalarization exhibits specific characteristics of certain optimization metrics proposed by MTOs, such as high task gradient magnitude similarity and low condition number, via an extensive empirical study. We then propose AutoScale, an efficient pipeline that leverages these influential metrics to guide the search for optimal linear scalarization weights. AutoScale shows superior performance than prior MTOs and performs close to the searched weight performance consistently across different datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the connection between multi-task optimization (MTO) and linear scalarization, proposing the use of multi-task learning metrics such as gradient magnitude similarity and condition number to guide the determination of weights in linear scalarization. The proposed approach, named AutoScale, includes detailed discussions on the initial multi-task learning phase and various strategies for optimizing the weights, which gives insights into its implementation.

### Strengths
Multi-task optimization and learning is essential in machine learning. The approach of using multi-task learning metrics to determine the weights in the linear scalarization seems novel. The proposed method is computationally more feasible than an exhaustive grid search of weights.

### Weaknesses
1. While using MTL metrics to estimate the optimal weight appears reasonable based on the results shown in Figure 2, it is unclear whether these findings would hold consistently across other datasets. Additionally, the evaluation metric—a single average of the accuracy of multiple tasks—may not fully capture the nuanced definition of "good" and "bad" results, especially in a multi-task learning context. More careful discussions are needed to justify the use of MLT metrics. Specifically, the paper lacks a rigorous analysis of how sensitive the chosen MTL metrics (gradient magnitude similarity, condition number, and balanced loss scale) are to variations in task difficulty and dataset characteristics. The paper should include a more comprehensive analysis of the correlation between these metrics and the final performance across a wider range of datasets and task combinations. Furthermore, the use of a simple average of task accuracies might mask significant performance variations across individual tasks, which is a critical aspect of multi-task learning.
2. The paper could benefit from more comparisons with linear scalarization approaches that directly use predictive performance metrics as criteria for determining weights. The current comparison is limited to unitary and grid-searched weights, which are not representative of state-of-the-art methods. The paper should include comparisons with methods that adaptively adjust weights based on validation performance, such as Bayesian optimization or reinforcement learning-based approaches. This would provide a more robust benchmark for evaluating the effectiveness of the proposed method.
3. Beyond the unitary and grid-searched weights discussed, the authors might consider exploring other weight determination methods, such as those surveyed by Royer et al. (2024), to provide a broader context and benchmark for AutoScale. The paper should also discuss the limitations of the proposed method in comparison to other weight determination methods, particularly in terms of computational cost and sensitivity to hyperparameter settings. A more thorough discussion of the trade-offs between different weight determination strategies would be beneficial.

### Questions
In Table 1, the iteration time is reported. Could the authors also provide the total computational time? Additionally, what is the computational time for each method shown in Table 2?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work studies the relationship between MTO and linear scalarization, which is over debate in the literature. Authors use some metrics to demonstrate the positive relationship. Based on this observation, a new two-phase pipeline for MTL is proposed and demonstrated in multiple datasets.

### Strengths
This work is the first to explore relationship between MTO and linear secularization.

Experiments show the benefit of AutoScale in terms of evaluation metrics and running time.

### Weaknesses
Notations are not given before their formal definitions, which creates barriers of reading.

Some explanations are not given, for example, why are those cost functions defined in that way?

Results (figure/table) are not clearly explained.

What are G1, G2, G3, …, B1 in Figure 2?

I feel the whole structure needs to be rewritten. For example, Delta m is in Figure 3 and authors wrote on Line 257 that Figure 3 shows clear correlations. However, Delta m is not defined until Section 5. Key definitions need to be given in the main text.

In Section 4.1, authors propose three cost functions. Are these cost functions related to the literature. Are there any reasonings on choosing these? Why are these functions helpful to the problem? Authors should explain the intuitions.

In Section 4.2, what is the fifth method? Exponential fit? What are the conclusions from Figure 4?

Is Time s/iter the running time? For example, the last column of Table 1. This should be defined clearly.

Authors show the running time, different values of alpha (Figure 6) etc. If these are to demonstrate the generalization or robustness, authors should show them in all datasets.

### Questions
What are G1, G2, G3, …, B1 in Figure 2?
 
I feel the whole structure needs to be rewritten. For example, Delta m is in Figure 3 and authors wrote on Line 257 that Figure 3 shows clear correlations. However, Delta m is not defined until Section 5. Key definitions need to be given in the main text.
 
In Section 4.1, authors propose three cost functions. Are these cost functions related to the literature. Are there any reasonings on choosing these? Why are these functions helpful to the problem? Authors should explain the intuitions.
 
In Section 4.2, what is the fifth method? Exponential fit? What are the conclusions from Figure 4?

Is Time s/iter the running time? For example, the last column of Table 1. This should be defined clearly.

Authors show the running time, different values of alpha (Figure 6) etc. If these are to demonstrate the generalization or robustness, authors should show them in all datasets.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes AutoScale, a new approach that combines MTO with linear scalarization for efficient and effective MTL. The authors explore the synergy between MTOs and linear scalarization, proposing that certain MTO metrics can guide weight selection to improve scalarization efficiency. AutoScale operates in two stages: an exploration phase to gather gradient and loss data using an MTO method, and a scalarization phase that leverages optimized weights derived from key MTO metrics. Extensive experiments demonstrate that AutoScale outperforms prior MTO methods and nearly matches the performance of grid-searched scalarization weights, without the associated search costs.

### Strengths
The paper is well-organized and the idea is clear.
The presentation is overall clear, and the experiments seem extensive and convincing.

### Weaknesses
1. The technical contributions seem limited since the proposed methodology is pretty straightforward.
2. In the experiments, the number of tasks are too small (i.e. up to 4 tasks), which are not common in multi-task learning settings. The experiments should include more tasks to demonstrate the scalability of the proposed method.
3. The code is unavailable, and it is impossible to reproduce the results. This significantly hinders the verification of the claims made in the paper.
4. Some typos. For example, Line 306 Exploration -> exploration
Line 311: Linear Scalarization -> linear scalarization

### Questions
1. Can authors discuss why linear scalaization correlates with some MTO metrics while is independent of others. What are commonality of these correlated MTO metrics?

2. What are benefits of Autoscale compared with traditional MTO algorithms?

### Soundness
3

### Presentation
3

### Contribution
2
