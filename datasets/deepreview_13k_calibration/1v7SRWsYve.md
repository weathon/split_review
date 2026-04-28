# MAP: Low-compute Model Merging with Amortized Pareto Fronts via Quadratic Approximation

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 6, 5

## Abstract
Model merging has emerged as an effective approach to combine multiple single-task models into a multitask model. This process typically involves computing a weighted average of the model parameters without any additional training. Existing model-merging methods focus on enhancing average task accuracy. However, interference and conflicts between the objectives of different tasks can lead to trade-offs during the merging process. In real-world applications, a set of solutions with various trade-offs can be more informative, helping practitioners make decisions based on diverse preferences. In this paper, we introduce a novel and low-compute algorithm, \textbf{Model Merging with Amortized Pareto Front (MAP)}. MAP efficiently identifies a Pareto set of scaling coefficients for merging multiple models, reflecting the trade-offs involved. It amortizes the substantial computational cost of evaluations needed to estimate the Pareto front by using quadratic approximation surrogate models derived from a pre-selected set of scaling coefficients. Experimental results on vision and natural language processing tasks demonstrate that MAP can accurately identify the Pareto front, providing practitioners with flexible solutions to balance competing task objectives. We also introduce Bayesian MAP for scenarios with a relatively low number of tasks and Nested MAP for situations with a high number of tasks, further reducing the computational cost of evaluation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
When merging models (generally finetuned on different tasks), many techniques boil down to a weighted sum (generally of "task vectors", the difference between the finetuned model and the pre-trained model) include _per-model_ scaling parameters. This creates an exponential number of settings and makes it intractable to try all the different possible merges.

Normally, merging methods are evaluated based on their average performance across many tasks, but they point out that this setting ignores the idea that a user may care more about performance on some subset of tasks than others. To capture this, they introduce the metric of the "win rate" how often a model on one method's Pareto frontier outperforms the models on another methods frontier.

They find that by sampling several _per-model_ scaling hyperparameters, they can use a quadratic approximation to create a better Pareto frontier with less computational resources.

### Strengths
The paper does a good job explaining the motivating the idea of using a Pareto frontier when evaluating model merging and a good job explaining their win-rate metric.

The paper gives a good overview of the quadratic approximation of the Pareto frontier.

### Weaknesses
The Pareto frontier based metric they use (win rate) is explained well, but during the comparisons to other common merging methods, it would have been nice to see another experiment that used their approach to set merging hyperparameters for those methods to see if greater average performance could be achieved. For example, comparing the avg performance of TIES with the hyperparameters from the original paper vs parameters found by their method. Specifically, it's unclear if the proposed method is only useful for the specific merging approach they propose, or if it can be used to improve other merging methods as well. It would be useful to see if the hyperparameter selection method could be applied to other methods like TIES, and if that leads to improved performance.

Often merging methods are also evaluated on if they retain the ability to generalize to new tasks, it would be nice to see some experiments to test the generalization abilities of models merged with hyperparameters found using their method. It is important to understand if the hyperparameters found using the proposed method lead to models that generalize well, or if they overfit to the training tasks. The paper should include experiments that evaluate the generalization performance of the merged models on unseen tasks.

They include some talk of using Bayesian optimization for the sampling of hyperparameters and of using nested model merging, but their discussion (intro, methods, results, etc.) for these are so sparse they should probably be cut. The paper mentions these advanced techniques, but does not provide sufficient details or experimental results to justify their inclusion. The lack of depth makes these sections feel incomplete and detracts from the overall focus of the paper.

MAP is already a very common acronym for Maximum a Posteriori estimation. This collision will hurt adoption of their approach and is distracting as you need to keep reminding yourself is something else when you see MAP in their paper. The use of an existing acronym creates confusion and makes the paper harder to read. A different name should be chosen to avoid this conflict.

Figure 5 is designed to demonstrate the exponential growth of having _per-model_ hyperparameters. This growth is explained well enough in the paper that such a large figure is not the most effective use of space. The figure is not necessary given the explanation in the text, and it takes up valuable space that could be used for more important information.

Nit: Lots of places where references appear to be part of the text, where they shouldn't be, i.e., it is Author (year) instead of (Author, year).

### Questions
N/A

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
4

### Summary
The paper introduces a new model merging method that aims to approximate the pareto front of the performance of various model merging scaling factors by a quadratic approximation of the metric that is used for performance evaluation.
By not requiring a full search over possible scaling factors, the amount of computation that is needed is drastically reduced.
The authors show that this approach is favorable especially for a larger number of tasks, where the number of possible scaling factor combinations increases exponentially.

### Strengths
- The idea of focusing on trade-offs between tasks for which models are merged and Pareto fronts instead of only a single model merging solution is interesting and a useful reframing of model merging.

- The method is derived from sound theory and can reduce the cost of model merging.

- The method can be used as a plug-in addition to Task-Arithmetic-based merging schemes.

### Weaknesses
 - The paper overall is not easy to follow. Many details are left to the reader and there is not always a clear flow in writing, requiring the reader to jump back-and-forth. In particular, the following points could be improved:

- Section 2.3: it is not immediately clear why these norms are calculated, because the fact that the method uses taylor approximations is only introduced at the end of it but even then it is unclear how it ties in with the bigger picture, esp. how closeness of parameters may be related to a taylor approximation of the evaluation metric. This could be clarified. In particular, it is directly showing empirical evidence that Assumption 1 may be valid but this only comes in the section afterwards.

- Section 3.1 (the main description of the method) is not written very well. For example, case 2 and 3: why is the "warping" by a sigmoid benificial and why does a softplus help in Case 3? Many details are left for the reader to figure out. Also, it is mentioned that you optimize Eq.5 in L252 but that you do it with gradient descent is loosely thrown in in L283. Overall, Eq.5 could be discussed more, too.

- The nested MAP (nMAP) is only described in Fig. 4 of the main paper and I can not seem to find any description of bMAP at all. Could you please clarify this? While I agree that how nested merging is done is very intuitive a better description would be helpful.

- It would be helpful to discuss related works more, in particular, Rame et al. 2023, who also seek to use Task-Arithmetic-based merging for Pareto fronts of multiple objectives

### Questions
- In Fig 2 it is not immediately clear to me why the brute force approach of finding the best multitask scaling factor performs worst, also since you call it gold standard. Could you please explain this a bit further? What does the direct search look for exactly? Is it just over Task Arithmetic scaling factors, and if so, what grid is used?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Model Merging with Amortized Pareto Front (MAP), a low-compute algorithm that merges multiple single-task models into a multitask model by efficiently identifying a Pareto set of scaling coefficients. MAP uses quadratic surrogate models to reduce evaluation costs while providing flexible solutions to balance competing task objectives.

### Strengths
1. This is the first algorithm to estimate the Pareto front for task-vector-based model merging without relying on gradient descent, which is often computationally expensive.
  
2. The Nested MAP variant reduces computational complexity, making it suitable for large-scale problems.

### Weaknesses
1. The motivation for applying Multi-Objective Optimization Problems (MOOP) in model merging needs further clarification. While this work represents a direct application of MOOP in this area, it lacks an in-depth explanation of why MOOP would be advantageous over traditional gradient descent-based methods. Specifically, the paper should elaborate on the specific scenarios where MOOP offers a distinct advantage, such as when dealing with non-differentiable objectives or when a full Pareto front exploration is desired, which may not be achievable with gradient-based methods that focus on a single, potentially suboptimal, solution based on a weighted sum of losses. 

2. To enhance the clarity and impact of the paper, consider including a direct comparison with gradient descent-based optimization. Specifically, the authors could discuss MOOP’s potential benefits in terms of computational efficiency, ability to handle non-differentiable objectives, flexibility in exploring trade-offs, and its capacity to fully explore the Pareto front, which gradient-based methods may not achieve. This comparison would help elucidate the unique value of MOOP for model merging. The discussion should include a detailed analysis of the computational costs associated with each approach, considering factors such as the number of evaluations required, the complexity of the optimization process, and the hardware resources needed.

3. The paper would benefit from a more thorough comparative analysis with recent relevant works, particularly "Knowledge Fusion by Evolving Weights of Language Models" and "It's Morphing Time: Unleashing the Potential of Multiple LLMs via Multi-objective Optimization." Both studies propose innovative methods for model merging with evolutionary approaches. A direct comparison with these methods could clarify the specific advancements and trade-offs associated with the MAP approach, such as variations in fusion strategies, optimization techniques, or performance across diverse benchmarks. Discussing how MAP aligns or diverges in terms of methodology, effectiveness, or scope will provide readers with a more complete understanding of its contribution to the field.

### Questions
1. The paper lacks comparative experiments with other established MOOP algorithms, such as MOEA/D and NSGA-II. Including these comparisons would enhance the evaluation of both solution quality and computational efficiency, providing a clearer context for assessing the performance of the proposed method. Additionally, brute force may not be the most appropriate baseline for this type of analysis and could be replaced by a simple MOOP method like MOEA/D.

2. The experiments related to large language models are somewhat limited. Typically, mainstream model fusion effectiveness is tested on benchmarks like math and code tasks, as seen in recent work such as DARE (arXiv: 2311.03099). Including comparisons on these types of benchmarks would lend stronger support to the method’s effectiveness relative to established model fusion approaches.

3. The paper would benefit from additional results or comparative analysis with other state-of-the-art model merging methods, such as Adamerging (ICLR 2024) and DELLA-Merging (arXiv: 2406.11617v1). Adding these would help situate the proposed method within the current landscape and highlight any unique strengths or trade-offs.

### Soundness
3

### Presentation
3

### Contribution
2
