# Bayesian Optimization via Continual Variational Last Layer Training

- Decision: Accept
- Avg Score: 7.25
- Scores: 5, 8, 8, 8

## Abstract
Gaussian Processes (GPs) are widely seen as the state-of-the-art surrogate models for Bayesian optimization (BO) due to their ability to model uncertainty and their performance on tasks where correlations are easily captured (such as those defined by Euclidean metrics) and their ability to be efficiently updated online. However, the performance of GPs depends on the choice of kernel, and kernel selection for complex correlation structures is often difficult or must be made bespoke. While Bayesian neural networks (BNNs) are a promising direction for higher capacity surrogate models, they have so far seen limited use due to poor performance on some problem types. In this paper, we propose an approach which shows competitive performance on many problem types, including some that BNNs typically struggle with. We build on variational Bayesian last layers (VBLLs), and connect training of these models to exact conditioning in GPs. We exploit this connection to develop an efficient online training algorithm that interleaves conditioning and optimization. Our findings suggest that VBLL networks significantly outperform GPs and other BNN architectures on tasks with complex input correlations, and match the performance of well-tuned GPs on established benchmark tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose VBLL networks as a surrogate for Bayesian optimization and identify a relationship between optimizing the variational posterior and recursive Bayesian linear regression. They demonstrate competitive BO results with VBLL on diverse single and multi-objective benchmarks.

### Strengths
- The method is well-explained and is theoretically justified, and there are additional modifications which can be made to increase the efficiency such as feature re-use and sparse full model retraining. This flexibility enables practitioners to balance the tradeoff between model performance and computational cost.
- The authors use a diverse setting of test objectives, specifically demonstrating performance on instances with high-dimensionality and non-stationarity. 
- VBLL appears to be robust to hyperparameter choices and can be used as a drop-in surrogate model, unlike typical GPs which require careful kernel selection.

### Weaknesses
 - Although it appears that one of the primary motivations behind this work is the increased efficiency compared to other BNN surrogates, there is no measure of runtime or computational cost within the paper. It would be helpful to understand how these methods perform as a function of computational budget, specifically the wall-clock time for surrogate fitting and optimization. This could also help clarify the difference in performances between VBLL and VBLL CL, as the continual learning approach should theoretically reduce fitting times, but this is not explicitly shown.
- There is also currently no demonstration of why this approximation would be preferred over the using the exact marginal likelihood with approaches like DNGO [1]. Without these baselines, there is minimal evidence that the proposed method has practical merit over existing work. Furthermore, it would also be useful to compare last-layer methods like VBLL to more expensive BNN surrogates like deep ensembles so we can assess the tradeoff between computation and performance. The lack of comparison to deep ensembles is a significant gap, as they are a strong baseline for Bayesian neural network surrogates.


### Questions
- Could you further elaborate on the differences between LLLA and VBLL? LLLA outperforms VBLL on many of the non-stationary benchmarks, and from line 530, it appears that VBLL-based approaches may be less flexible than last-layer Laplace approximations.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a combination of two ideas: (!) Bayesian last-layer training of neural networks with (2) using a parametric Bayesian linear model for black-box function optimization. Using natural parameterization of the last layer Gaussian and assuming independent Gaussian noise, it is possible to use a continual update which is only $O(N^2)$ in the last-layer number of neurons $N$. As with every parametric Bayesian function model, the acquisition function can be directly and analytically optimized using Thompson sampling. The empirical results on a wide variety of Bayesian Optimization tasks are promising.

### Strengths
The paper combines two well studied ideas in an elegant way and the presentation is (relatively) easy to follow (though I would have wished a bit more emphasis on the natural parameterization of the Normal distributions as this is key to the computational efficiency). The empirical studies are extensive and well discussed.

### Weaknesses
One aspect that is disregarded by the paper is how to chose the network architecture for all but the last-layer; I have no idea how sensitive the quality of the proposed approach is to this. In essence, the complexity of choosing a kernel function for GPs has been shifted to the network architecture of the underlying neural network. This is not discussed in sufficient detail. Also, only at the end the difference to Laplace approximation of the last layer is discussed; I would have expected this in the Related Work section.

### Questions
* In line 110 und 111 it helps to point out that $\mathbf{w} = S^{-1} \mathbf{q}$ is the vector of precision-means (for those unfamiliar with natural parameters of the Normal distribution)
* The proof of Theorem 1 in the appendix relies on the simple observation that the approximating family contains the true distribution. I would have preferred to see this in the main body of the text; it's less "mechanical" than I expected and key to the reasoning of the paper (line 178-189 can be significantly shortened b/c it uses the well known Cholesky decomposition for approximating the inverse and log-determinant of the precision)
* Line 217: Where is the parameter $V$ (Wishart prior scale) necessary?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Although Gaussian processes (GPs) are widely used for Bayesian Optimisation (BO), they are not always well suited to modelling functions with complex correlations across inputs, and are often limited by the choice of kernel function. On the other hand, Bayesian neural networks (BNNs) can better handle complex non-Euclidean data, but are computationally expensive and challenging to condition on new data. In this work, the authors extend recent work on Variational Bayesian Last Layer (VBLL) models specifically for BO. They show how VBLLs can be adapted as efficient surrogate models for BO tasks through modified training procedures, which enable continual, online training with recursive conditioning, improving scalability. Additionally, the authors demonstrate how VBLL’s parametric structure enables effective Thompson sampling for both single- and multi-objective acquisition functions, offering more stability and numerical efficiency compared to GPs. Experiments compare VBLL’s performance against other techniques such as baseline GPs, and BNNs, and show that VBLL performs especially well on complex tasks, such as the Oil Sorbent benchmark, where other approaches struggle due to numerical instability.

### Strengths
The paper is well-written and a pleasure to read. The problem statement is clear from the outset, and the connections to related work are extensive. I also appreciated how the paper’s focus on practical aspects such as improving training efficiency via continual learning. Having the method implemented in BoTorch is also appealing to practitioners wanting to experiment using this method in real-world settings. 

The experiments demonstrate that VBLL performs well in the targeted settings having complex input correlations and non-Euclidean structures. Showing that VBLL outperforms competing techniques on real-world datasets such as the Oil Sorbent and Pest Control datasets adds further credence to how VBLL is suited to multi-objective settings prone to numerical instability.

While the contributions may initially appear incremental, adapting VBLL to BO introduces challenges that require non-trivial solutions. The need for efficient, online training in BO necessitated the development of recursive conditioning and continual learning updates, which are distinct from standard regression tasks. Addressing the requirements of multi-objective and high-dimensional settings also required effective workarounds to address numerical stability issues.

### Weaknesses
1. Deep kernel learning was the first method to come to mind when reading the motivation for this work. While I appreciated its inclusion in the experimental section, I would have liked more discussion in the earlier sections on why DKL might be less ideal than VBLL. To my understanding, DKL’s computational complexity, especially in high-dimensional settings, might be a key differentiator, but additional detail on this would help clarify VBLL’s practical advantages right from the outset.
2. While the experiments are quite extensive, I would appreciate more insight on the cases where the method is expected to underperform compared to other approaches. Although dedicated experiments are provided in the supplementary material, high-level insights on possible sensitivity to hyper-parameters could also be included in the main text.

### Questions
Please refer to comments in "Weaknesses".

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Gaussian Process (GP) models are widely regarded as state-of-the-art surrogates for Bayesian Optimization, thanks to their strong predictive performance, efficient updates for small datasets, and straightforward uncertainty quantification. However, they can be challenging to apply to search problems with non-stationary or complex correlation structures. In contrast, Bayesian Neural Networks (BNNs) are more flexible and can handle such problems with minimal adaptation, but they have traditionally been associated with high computational costs and unreliable uncertainty estimates.

This paper introduces a new method that leverages variational last-layer BNNs, combining advantages of both GPs and BNNs. The proposed approach demonstrates superior performance over GPs and several other BNN architectures in tasks with complex input correlations while achieving comparable results to GPs on standard benchmark problems.

### Strengths
The paper makes a valuable contribution to the field by highlighting the capabilities of a class of BNN models for Bayesian Optimization (BO) and introducing a practical technique for efficient updates in online settings, including BO scenarios. The writing is clear and well-structured, and the findings are substantiated by experiments conducted in both single-objective and multi-objective settings.

### Weaknesses
The presented method appears to perform comparably to Last Layer Laplace Approximations (LLLA) without clearly demonstrating new advantages. The paper emphasises computational concerns — and presumably could provide a favourable runtime-performance trade-off—but that is not empirically validated and the method is seemingly not compared against the baselines in this respect.

The claim that Laplace approximations are more sensitive to noise lacks sufficient support, as there is no accompanying experiment or reference to substantiate it (see Section 6, "Performance and Baselines"). Providing evidence here would strengthen the argument.

The discussion around early-stopping based on training loss (see Section 3.2, "Early Stopping") makes significant claims, such as training "only as long as necessary to achieve optimal performance" and suggesting that applying a similar criterion could benefit training neural network-based surrogate models in BO more broadly. While it is reasonable to argue that stopping training before full convergence improves runtime efficiency and can serve as a regularisation heuristic, the lack of experimental results of the trade-off in the setting when presented as a methodological contribution is a major omission. The effect of early stopping on the quality of the fitted model should be demonstrated through empirical evaluation, such as predictive error on relevant functions or/and assessing its impact on BO performance.

The choice of length scales [0.005, 4] for the GP model (see Section 5.1, "Surrogate Models") appears to be unsuitable for the high-dimensional benchmarks considered. As demonstrated in (1) "Vanilla Bayesian Optimization Performs Great in High Dimensions" (ICML 2024), length scales around \sqrt{D} are generally more effective for Bayesian Optimization in high-dimensional settings. Using more appropriate lengthscales (specifically adopting a suitable lengthscale prior with mass concentrated near \sqrt{D}) could potentially dramatically enhance the model's performance, making it a more informative comparison.


### Questions
1. I think the runtime advantage of the suggested algorithm must be more clearly presented, since it is the motivation of much of the methodology. Specifically, be accompanied by results showcasing a benefit (in e.g. regret/performance per wallclock time), especially compared to LLLA which in terms of regret per iteration performs similarly. 

2. There are a couple of sections in the methodology which I think unjustifiably and unnecessarily make claims without backing (see Weaknesses). I recommend the authors to look over the claims and make sure they have backing; either by adding relevant proofs, experiments or references for claims important to the paper, or lessening/removing claims which may be unnecessary. It is okay that not every design decision in a larger algorithm (or system or model) is fully backed, but then those design decisions should arguably not be presented as central parts of the methodology accompanied by unbacked claims. 

Overall, the paper addresses a meaningful gap in the literature. If the concerns outlined above are addressed, I would be inclined to raise my evaluation score.

### Soundness
1

### Presentation
3

### Contribution
3
