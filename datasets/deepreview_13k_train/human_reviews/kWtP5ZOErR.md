# EvoPress: Towards Optimal Dynamic Model Compression via Evolutionary Search

- Decision: Reject
- Scores: 8, 8, 6, 3

## Abstract
\looseness=-1
The high computational costs of large language models (LLMs) have led to a flurry of research on LLM compression, via methods such as quantization, sparsification, or structured pruning. A new frontier in this area is given by \emph{dynamic, non-uniform} compression methods, which adjust the compression levels (e.g., sparsity) per-block or even per-layer in order to minimize accuracy loss, while guaranteeing a global compression threshold. 
Yet, current methods rely on heuristics for identifying the ``importance'' of a given layer towards the loss, based on assumptions such as \emph{error monotonicity}, i.e. that the end-to-end model compression error is proportional to the sum of layer-wise  errors.  
In this paper, we revisit this area, and propose a new and general approach for dynamic compression that is provably optimal in a given input range. 
We begin from the motivating observation that, in general, \emph{error monotonicity does not hold for LLMs}:  
compressed models with lower sum of per-layer errors can perform \emph{worse} than models with higher error sums. To address this, we propose a new general evolutionary framework for dynamic LLM compression called \methodname{}, which has provable convergence, and low sample and evaluation complexity. 
We show that these theoretical guarantees lead to highly competitive practical performance for dynamic compression of Llama, Mistral and Phi models. Via \methodname{}, we set new state-of-the-art results across all compression approaches: structural pruning (block/layer dropping), unstructured sparsity, as well as quantization with dynamic bitwidths.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper introduces a new general framework for dynamic LLM compression. Building on the observation that error monotonicity does not generally hold for LLM compression, the paper proposed evolutionary search approach. The proposed approach is provably convergent and has low sample and evaluation complexity when the fitness function is linear. Experiments show that the proposed methods improve dynamic compression of Llama, Mistral, and Phi models.

### Strengths
The proposed method shows strong empirical performance. It is flexible, as it can be applied to unstructured pruning, structured pruning/layer dropping, and quantization. Theoretical analysis of the proposed methods is also provided,

### Weaknesses
1. I think it would be better if the average and standard deviation of the performance metrics across different runs were reported, as it can demonstrate the significance of the improvement. But I understand it could be expensive to do and might not be possible for baseline methods.


2. The theoretical results are somewhat disconnected from other parts. I think having the theoretical results is a bonus and it can be of interest beyond the LLM context. But some exploration of the function form of $f$ in real experiments or some simple simulation example might better demonstrate the significance of the results

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a meta-heuristic for non-uniform model compression that is largely independent of specific model architectures and compression methods. The method is demonstrated on three compression approaches—depth pruning, unstructured sparsity, and quantization—with ample numerical results and a supporting analytical convergence analysis.

### Strengths
The strength of the approach is its simplicity and the fact that it is somewhat agnostic to model architecture and compression techniques.
While it doesn’t introduce entirely novel algorithms, its design effectively minimizes computational costs when working with larger models. Overall, the paper is quite well-written and presents compelling arguments for the proposed approach.

### Weaknesses
The manuscript does not, however, discuss much about the scalability of the approach in more complex scenarios, and to what extent the evolutionary search is useful compared to more basic derivative-free optimization techniques or the like.
While presented as evolutionary, the algorithm leans heavily on an elitist, exploitation-focused strategy. This approach could limit exploration, potentially trapping the algorithm in local minima and risk of poor generalization in more complex compression scenarios.

This approach appears to be effective as long as the manifold remains relatively convex. However, with multi-modal compression techniques or non-convex landscapes, there are concerns about whether this computationally efficient method will generalize well beyond the controlled benchmarking environments, especially when handling mixed or complex compression strategies.

### Questions
1) The scheme is presented as an evolutionary search, but the update mechanism uses an elitist strategy (focused on exploitation) based on single-offspring selection. The number of mutations is also kept minimal, with one mutation shown to be nearly optimal, as demonstrated in SI B. In this regime, the scheme resembles a form of random coordinate descent or derivative-free optimization, with the added twist that perturbation occurs on a manifold with constant overall compression (referred to as switching). Could you clarify which properties of an evolutionary algorithm are essential to the results achieved, as opposed to a simpler perturbative approach?

2) In the current setting, how much variability is there in the optimal compression profile found after one run of the evolutionary search? Does it appear the search get stuck in local minima in any of the benchmarks? 

3) Can you predict if the hypothesis that smooth dynamic model compression results in a smooth fitness landscape with few local optima still hold in multi-modal cases? 

Additional Questions/comments:

4) How is the step size in a single dimension determined (e.g., the 1M weights for unstructured sparsity)? Is the step size fixed or adaptive?

5) In the selection process, only two stages are shown (see SI B.2). Was this approach tested with more stages, and if so, were additional stages found to be ineffective?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work proposes an algorithm to perform dynamic compression (different layers can be compressed to various levels) of large language models. Previous works assign importance to each layer and assume end-to-end model compression error is proportional to the sum of layer-wise errors. This work observes that error monotonicity does not hold for LLM, and proposes an evolutionary search algorithm to achieve better compression quality.

In EvoPress, multiple heuristics, including mutation operation and the selection step are proposed to achieve efficient sampling for LLM. Experimental results show better compression quality compared to previous work on multiple applications.

### Strengths
LLM compression is an important topic. This work proposes a new optimization algorithm, and better performance has been presented on multiple applications, including pruning, introducing sparsity, and quantization.

### Weaknesses
1. It would be good to introduce an algorithm overview figure to illustrate the steps in EvoPress. In addition, the algorithm contains mulitple heuristics to make the sampling efficient. It would be good to also summarize these heuristics in the figure.
2. It's not clear whether the hyperparameters used in the heuristics (mutation operation & multi-step selection) can transfer well across tasks/datasets/models. Further illustration would be very useful.

### Questions
Please see above

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a new evolutionary framework for dynamic LLM compression.

### Strengths
This paper proposes an evolutionary algorithm within an optimization framework, for sparse structure selection for LLMs.

### Weaknesses
1. The theoretical justification in Theorem 1 appears irrelevant to the algorithm proposed in the paper. Theorem 1 is established for linear fitness functions; however, it’s difficult to see how this applies, as LLMs likely do not have linear fitness functions. The fitness landscape of LLMs is known to be highly non-convex and complex, with numerous local minima, making the assumption of linearity a significant oversimplification. The theorem's applicability is further weakened by the fact that the evolutionary algorithm operates on a discrete search space of possible compression configurations, whereas the theorem seems to assume a continuous space. This discrepancy between the theoretical setup and the practical algorithm raises concerns about the theorem's relevance.

2.  The comparison lacks systematic rigor. For instance, Table 2 presents results only at the sparsity level 70%. What about results at other sparsity levels? The lack of a comprehensive evaluation across different sparsity levels makes it difficult to assess the robustness and generalizability of the proposed method. It is unclear if the performance gains observed at 70% sparsity hold true at other levels, particularly at lower sparsity levels where the compression challenge may be less pronounced. Furthermore, the absence of results at multiple sparsity levels makes it difficult to compare the proposed method with other compression techniques that may exhibit different performance characteristics across the sparsity spectrum.

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
2
