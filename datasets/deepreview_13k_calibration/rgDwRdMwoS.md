# A Unified Approach to Routing and Cascading for LLMs

- Decision: Reject
- Avg Score: 5.20
- Scores: 6, 3, 6, 8, 3

## Abstract
\vspace{-2mm}
    The widespread applicability of large language models (LLMs) has increased the availability of many fine-tuned models of various sizes targeting specific tasks. Given a set of such specialized models, to maximize overall performance, it is important to figure out the optimal strategy for selecting the right model for a given user query. An effective strategy could drastically increase overall performance and even offer improvements over a single large monolithic model. Existing approaches typically fall into two categories: routing, where a single model is selected for each query, and cascading, which runs a sequence of increasingly larger models until a satisfactory answer is obtained. However, both have notable limitations: routing commits to an initial model without flexibility, while cascading requires executing every model in sequence, which can be inefficient. Additionally, the conditions under which these strategies are provably optimal remain unclear. In this work, we derive optimal strategies for both routing and cascading. Building on this analysis, we propose a novel approach called \emph{cascade routing}, which combines the adaptability of routing with the cost-efficiency of cascading. Our experiments demonstrate that cascade routing consistently outperforms both routing and cascading across a variety of settings, improving both output quality and lowering computational cost, thus offering a unified and efficient solution to the model selection problem.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores the challenges of efficiently using large language models (LLMs) by evaluating existing model selection strategies: routing and cascading. Routing selects a single model per query, while cascading runs models sequentially until a satisfactory answer is found. However, routing lacks flexibility, and cascading is inefficient.

The paper contributes by deriving optimal strategies for both routing and cascading. Building on this analysis, the authors introduce "cascade routing," which combines the adaptability of routing with the cost-efficiency of cascading. Experiments demonstrate that cascade routing consistently outperforms existing methods across various scenarios, enhancing output quality and reducing computational costs. This approach offers a more unified and efficient solution to the model selection problem.

### Strengths
1. The paper frames routing and cascading as linear optimization problems, deriving optimal strategies for both. This provides a strong theoretical foundation lacking in prior work, which often relied on heuristics or simplifying assumptions. The theoretical framing allows for provable optimality under certain conditions.

2. Experimental evaluations on RouterBench consistently demonstrate improved performance, yielding a 1-4% increase in AUC across various noise levels and model set sizes, for both routing and cascading tasks.

3. Overall, the paper is well-written, clearly presented, and easy to follow, making it readily accessible to readers.

### Weaknesses
1. The core idea is an incremental approach that combines two existing methods, which somewhat limits the paper's novelty.

2. The effectiveness of cascade routing depends on precise quality and cost estimations. The paper acknowledges this limitation, demonstrating that performance gains decrease with less accurate estimates. Although various estimation methods are explored, further research is necessary to enhance their robustness in real-world scenarios.

### Questions
1. How does the computational cost of cascade routing, including the pruning strategy, scale with the number of available models? Have you tested this with significantly larger model sets, such as dozens or hundreds of models? Are there further optimizations that could enhance scalability?

2. The paper acknowledges the limitations of current quality estimation methods. Could you elaborate on potential future directions for improving these estimations? Are there specific features or model architectures that you find promising? Additionally, how does the choice of quality metric, such as accuracy versus user preference, impact the performance of cascade routing?

3. I suggest that the authors provide a more detailed error analysis of the results across different benchmarks. This analysis could offer insights into the types of queries where cascade routing excels or underperforms, guiding future improvements.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces cascade routing, a framework that unifies and generalizes two common LLM model selection strategies: routing (which selects one model per query) and cascading (which tries progressively larger models). The authors provide theoretical proofs for optimal strategies in both routing and cascading, then use these insights to develop cascade routing. Their approach allows dynamic model selection and sequencing based on both query difficulty and model specialization. Empirical results show 1-4% improvements over baselines across multiple benchmarks. The work's main contribution is providing a theoretical framework that unifies these previously separate approaches to model selection.

### Strengths
* The paper provides rigorous proofs for optimality conditions in both routing and cascading, establishing a solid mathematical framework for model selection.
* The paper combines two previously separate approaches (routing and cascading) into a single coherent framework, showing how they can complement each other.

### Weaknesses
 * The paper shows only 1-4% accuracy improvements, which may not justify the significant complexity, computation and latency overhead of running multiple models sequentially. The practical value proposition needs stronger motivation.
* There is no discussion of end-to-end inference latency when running multiple models in sequence. While API costs are analyzed, total response time - a critical metric for real-world applications that affect users' experienc - is completely ignored.
* Simply using perplexity and uncertainty features to measure the models' response quality is not fair.
* Additionally, Chain-of-thought methods should be another baseline to compare with the cascading methods.

### Questions
* Given the significant latency overhead of running multiple models sequentially, could you provide a comprehensive analysis of end-to-end response times? How does this compare to simpler approaches like routing-only or ensemble methods?
* For quality estimation of model responses, have you considered more sophisticated evaluation methods beyond perplexity and uncertainty features? For example, using LLM-as-Judge to better evaluate the response's quality?
* The 1-4% accuracy improvement seems modest given the additional complexity and latency. Could you elaborate on specific use cases or scenarios where this trade-off would be clearly beneficial? Perhaps certain domains or applications where even small accuracy gains are highly valuable?

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Given the current landscape, where numerous fine-tuned models of varying sizes are tailored to specific tasks, this paper introduces a solution for selecting the most suitable model for a given user query, called Cascade Routing. This approach combines the adaptability of routing with the cost-efficiency of cascading, resulting in improved output quality while reducing computational costs, outperforming existing methods.
Furthermore, the paper offers a theoretical analysis of both existing routing and cascading methods, as well as the proposed Cascade Routing approach. Both theoretical analysis and experimental results consistently demonstrate the superiority of the proposed method over current alternatives.

### Strengths
1. This paper presents a theoretical analysis of existing LLM selection strategies and introduces a new cascading strategy that outperforms current methods under specific conditions.
2. The paper is generally well-articulated and easy to understand.

### Weaknesses
1. The paper lacks experimental results for other routing and cascade methods, such as [1] and the existing routing and cascading methods mentioned in the related work. These methods can also reduce the cost of LLMs without compromising response quality.

2. The strength of this paper's approach lies in achieving higher accuracy at the same computational cost, though it comes at the expense of longer runtime. Given that the accuracy improvement ranges are only between 1% to 4%, the authors need to demonstrate that the additional runtime is sufficiently minimal to justify the practicality of this approach.
Specifically, the authors should clearly state the runtime of different methods in the experiments presented in Figure 2 and Table 2 and include the runtime and AUC for the three methods: Linear Interpolation, Routing, and Cascade (Baseline) in Table 3.

3. The method proposed in this paper does not change the model order compared to the existing cascade approach, nor does it alter the methods for estimating cost and output quality. It simply expands the search space, resulting in limited contributions.

### Questions
1. As mentioned in the paper, the proposed method performs poorly when the quality and cost estimates are inaccurate, which raises concerns about its practical application.
 
2. I would like to know how much training data is required for the hyperparameter training of this method compared to existing routing and cascading approaches. I hope the authors can provide some comparative results.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents cascade routing, a novel model selection strategy for large language models (LLMs) that unifies the strengths of traditional routing and cascading methods. Routing directs queries to a specific model, optimizing for task-specific expertise but lacks flexibility to adjust once selected, while cascading processes queries sequentially through models, which can be inefficient. Cascade routing addresses these limitations by combining adaptability with cost-efficiency, dynamically routing queries across models until a high-quality response is reached. The authors theoretically derive optimal strategies for both routing and cascading, integrating them into the cascade routing framework, which is shown to significantly outperform existing methods in accuracy and cost-effectiveness across diverse benchmarks.

### Strengths
* Cascade routing effectively combines the strengths of routing and cascading for improved query handling in LLMs.

* The paper provides a solid theoretical basis, with optimal strategies derived for both routing and cascading.

* Experimental results confirm significant performance gains, especially under low-noise settings.

### Weaknesses
 * Cascade routing's effectiveness is limited by the accuracy of quality and cost estimates, which can be noisy.

* Cascade routing requires multiple hyperparameters, making it challenging to tune effectively without extensive data.

### Questions
1. The cascade routing method heavily relies on precise estimates of quality and computational cost for each model. In practical scenarios, these estimates can be noisy, especially since they are typically derived from previous outputs or simple statistical models. When these estimates contain high levels of noise, cascade routing's decision-making becomes less effective. How can this issue be addressed especially for real-time or adaptive applications where quality and cost estimates are challenging to maintain with high accuracy?

2. Cascade routing involves tuning multiple hyperparameters to balance cost, quality, and routing decisions. This includes setting parameters for each model’s cost-quality tradeoff, which adds complexity to the optimization process. Would the optimization be time-consuming and computationally expensive?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The widespread applicability of large language models (LLMs) has increased the availability of many fine-tuned models of various sizes targeting specific tasks. An effective strategy can increase overall performance and even offer improvements over a single large monolithic model. Existing model selection strategies, such as routing and cascading, have their drawbacks. Routing commits to an initial model without flexibility, while cascading requires running every model in sequence, which can be inefficient. The paper proposes a novel approach called cascade routing, which combines the adaptability of routing with the cost-efficiency of cascading to improve output quality and reduce computational cost.

### Strengths
1. Good writing.
2. The research topic is valuable.
3. A formal proof is given.

### Weaknesses
1. The strategies proposed in the paper produced little improvement.
2. More solid experimentation is needed.

### Questions
1. The minor performance improvement (1%~4%) with the proposed scheme in the paper raises doubts about whether this enhancement is simply due to experimental uncertainty.  For greater conviction, I would advocate for more rigorous experimental designs that demonstrate substantial and statistically significant performance improvements.
2. What criteria should guide the decision on which models are assigned to the same cascade level? Additionally, what is the optimal number of models to be considered at each cascade level within the routing strategy？
3. Does combining cascading and routing hold the key to solving this problem, or would factors like quality estimation approaches be more promising topics for research?

### Soundness
2

### Presentation
2

### Contribution
2
