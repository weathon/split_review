# The Last Iterate Advantage: Empirical Auditing and Principled Heuristic Analysis of Differentially Private SGD

- Decision: Accept
- Scores: 5, 5, 8, 5

## Abstract
We propose a simple heuristic privacy analysis of noisy clipped stochastic gradient descent (DP-SGD) in the setting where only the last iterate is released and the intermediate iterates remain hidden. Namely, our heuristic assumes a linear structure for the model.

We show experimentally that our heuristic is predictive of the outcome of privacy auditing applied to various training procedures. Thus it can be used prior to training as a rough estimate of the final privacy leakage. We also probe the limitations of our heuristic by providing some artificial counterexamples where it underestimates the privacy leakage.

The standard composition-based privacy analysis of DP-SGD effectively assumes that the adversary has access to all intermediate iterates, which is often unrealistic.
However, this analysis remains the state of the art in practice. 
While our heuristic does not replace a rigorous privacy analysis, it illustrates the large gap between the best theoretical upper bounds and the privacy auditing lower bounds and sets a target for further work to improve the theoretical privacy analyses. We also empirically support our heuristic and show existing privacy auditing attacks are bounded by our heuristic analysis in both vision and language tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a heuristic privacy analysis for DP-SGD when only the final model is released, and intermediate updates are hidden. This heuristic assumes linear loss functions and, when the assumption holds, provides a more accurate estimate of privacy leakage than standard composition-based analyses, which often overestimate privacy loss by assuming adversaries have access to all training iterates. The authors experimentally demonstrate that their heuristic closely predicts the outcomes of privacy auditing tools, serving as a practical upper bound on privacy leakage in deep learning settings (where auditing is usually expensive). They also discuss counterexamples where the heuristic underestimates privacy leakage, highlighting its limitations. By bridging the gap between theoretical upper bounds and empirical lower bounds from privacy auditing, the heuristic sets a more realistic target for both theoretical improvements and practical attacks. It offers a computationally efficient way to estimate privacy leakage, aiding in tasks like hyperparameter selection before training without the overhead of extensive privacy audits.

### Strengths
* The paper presents a new heuristic privacy analysis for DP-SGD when only the final model is released. 
* The heuristic allows practitioners to estimate privacy leakage before training, aiding in hyperparameter selection without the computational cost and complexity of running privacy audits.
* The heuristic can serve as a benchmark for future improvements in both theoretical privacy analyses and practical attack methods, encouraging the development of stronger privacy attacks against ML models
* The authors provide a good amount of examples and intuition when the heuristic does not hold

### Weaknesses
* The reliance on linear loss functions is a simplification. This mismatch may limit the applicability of the heuristic to real-world models as a valid upper bound. (see the questions)
* The paper could position itself within the existing body of work on privacy auditing, particularly recent methods that perform effective audits under similar threat models. A deeper comparison would clarify the novelty and contribution of this work. (see the questions)
* While formalising the heuristic is helpful, it can be seen as a natural extension of existing observations that independent gradients are optimal for tight auditing when only the last iterate is revealed. The paper may not fundamentally add new knowledge to privacy auditing beyond this formalisation. (see the questions)

### Questions
* How does this work relate to other recent results in privacy auditing that perform effective audits under similar threat models? Specifically, could the authors elaborate on the novelty of their approach compared to methods presented in papers [1], [2], and [3], which make assumptions about the adversary and not the loss itself?
* Could the authors comment on the strength of the linearity assumption compared to other assumptions or heuristics used in privacy auditing? For instance, in [4], an auditing procedure for one-shot auditing is designed under the assumption that the adversary can insert a known random gradient, which can easily be extended to the blacbox setting. How does the linearity assumption compare?
* Are there practical scenarios or specific types of models where the linearity assumption approximately holds? 
* Theoretical work also addresses this threat model for the non-convex case (see [5]). Is there any connection or similarity between the works?

[1]: https://arxiv.org/pdf/2405.14106
[2]: https://arxiv.org/pdf/2405.14457
[3]: https://arxiv.org/pdf/2407.06496
[4]: https://arxiv.org/pdf/2302.03098
[5]: https://arxiv.org/pdf/2305.09903

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper tackles a fundamental problem in DP-SGD: the privacy analysis of the last iterate. It is well known that DP-SGD (in the centralized case) makes an artificial assumption that all intermediate iterates are published which can be observed by adversary to ease the privacy analysis through composition. New heuristic auditing methods are presented to approximate the leakage from the last-iterate. Disadvantage and failure cases of proposed methods are discussed.

### Strengths
The paper is well motivated and organized. Interesting examples are presented with good intuitions.

### Weaknesses
My primary concern is with the meaningfulness of the main result in Theorem 1.

In the proof, the authors appear to use $v_i$ to represent the $i$-th per-sample gradient, assuming $v_i$ is constant. First, I am not aware of any real-world loss function, even in the case of linear regression, that yields or can be framed to yield a constant gradient independent of model weight. Second, in practice, when $v_i$  is treated as a random variable, it is important to note that (a) the variable $v_i$  at different iterations is correlated with $v_j$  , and (b) the distribution of $v_i$ ​  changes when it is derived from a pair of adjacent datasets. Thus, when 
$v_i$  is random, the proof no longer holds, as the divergence cannot simply be reduced to that between the two Gaussian mixtures derived.

This simplification also leads to non-monotonicity, as discussed by the authors. Although they propose taking the worst-case estimate across all parameter selections, this approach feels somewhat ad hoc. The absence of results demonstrating, at a minimum, the conditions under which the model in Theorem 1 can serve as a provable upper bound for the estimate makes it challenging to evaluate and fully understand this auditing method. 

Additionally, can the authors elaborate on their statement about the justification for focusing on linear losses which stems from the observation that existing auditing techniques achieve the highest epsilon values? The observation itself makes sense as if every time is worst case, the privacy loss seems to be the maximal. But I do not get why this supports the reduction to the linear function,  

Moreover, I believe a ground truth for the last-iterate privacy loss is missing.

### Questions
In general, I think there is some interesting results in the paper but more work seems to be needed.

1. Can the author comment or empirically get the truly last-iterate in some practical tasks (it is ok to just run two or three iterations) and then compare it with the estimate from the heuristic auditing proposed? 

2. Can the author explain how to generalize the analysis to capture the practical random $v_i$ scenario?


minors:
1. There is overlap in the figures in Fig.1.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper derives an exact privacy analysis of DP-SGD for linear models (referred to as the heuristic) when only the last iterate is released. The authors also compare existing empirical privacy auditing methods with the exact heuristic across different regimes, including image classification tasks and language models.

### Strengths
This paper introduces a novel approach (named heuristic) to assess the performance of existing empirical evaluations of DP-SGD's privacy guarantees. While empirical evaluation provides a lower bound on the privacy budget of DP mechanisms, it may underestimate the true privacy loss. By comparing it with the heuristic bound for linear models, if the empirical audit bound is loose, it is unreasonable to expect it to hold tightly for more complicated non-linear (or even non-convex) models.

### Weaknesses
The main weakness of this paper is its limited theoretical contribution. In my view, the heuristic bound (Theorem 1) offers a simplified analysis of existing convergence privacy analysis for (strongly) convex loss functions (cf., the literature referenced in the introduction of this paper, which uses both RDP and $f$-DP). Additionally, the linear model is relatively simple, as the last-iterate output has a closed-form representation. Therefore, I propose the following questions or modifications:

1. $\textbf{Linear Probing as a Benchmarking Method:}$ Linear probing is commonly used for benchmarking when privately fine-tuning a foundation model. Therefore, the proposed heuristic for linear models could be beneficial when fine-tuning the last layer (linear probing) of a foundation model. Besides the well-known paper by De et al., the following recent studies may provide strong support for the utility of linear models in private fine-tuning, potentially strengthening the story for using heuristics for linear models.

Differentially Private Image Classification by Learning Priors from Random Processes. Tang et al., NeurIPS'23.

Neural Collapse Meets Differential Privacy: Curious Behaviors of NoisyGD with Near-perfect Representation Learning. Wang et al., ICML'24.

2. $\textbf{Extension to Convex Loss Functions:}$ Could this heuristic bound be extended to convex loss functions? I understand that the existing convergence bounds for DP-SGD involve complicated constants that are challenging to specify in practice, but a potential comparison between empirical auditing bounds and the theoretical upper bound under convex loss would be more convincing than in the linear case.

3. $\textbf{Comparison with Privacy Auditing Bound using privacy profiles: }$  It appears that the comparison with the privacy auditing bound is based on a specific value of $(\epsilon, \delta)$. What about examining the entire $(\epsilon, \delta(\epsilon))$-curve (or equivalently, the ROC curve or the type I/II error trade-off curve)? My question arises because, even if the privacy auditing bound might be (nearly) tight for specific values of $(\epsilon, \delta)$, it may not remain tight across the entire curve.

### Questions
See the weakness part.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper computes heuristic differential privacy parameters $\varepsilon$ and $\delta$ for releasing the last iterate of the DP-SGD algorithm. The proposed heuristic relies on computing the DP upper bound under linear loss function, which is always smaller than the DP upper bound under worst-case loss functions.  Numerical experiments show interesting scenarios where the proposed heuristics yield estimates that are significantly smaller than the worst-case DP upper bound. Experiments on image and language datasets confirm that the heuristic estimates lie between the DP upper bound and the lower bounds obtained via privacy auditing. Finally, the authors provide examples where the proposed heuristics underestimate the privacy loss.

### Strengths
- A systematic investigation of using heuristic privacy estimates to study the last-iterate privacy loss of the DP-SGD algorithm, including derivations, numerical experiments, comparison with auditing experiments, and analysis of counterexamples where the proposed heuristics underestimates the privacy loss.

- Numerical experiments show that when the sampling rate is small, the proposed heuristic yields an estimate that is significantly smaller than the standard DP upper bound.

- Auditing experiments illustrated that interestingly, black-box gradient space attacks fail to give tight auditing lower bound for the last-iterate of DP-SGD algorithm under natural datasets, in which case the heuristic estimates and the input-space attack gives more reliable estimates for the privacy loss.

### Weaknesses
- The message of the paper is not fully clear -- why is such a heuristic privacy estimate realistic and useful? Specifically, (1) linear loss is not a commonly used loss function; and (2) the heuristic estimates appear to be roughly the same as DP upper bound in certain auditing experiments (Figure 2). See questions 1 and 2 for more details.


- Several terms and plots in the paper are not explained in detail and the claims require more clarification. See question 3 for more details.

### Questions
1. Could the authors comment on why the proposed heuristics give a realistic privacy risk estimate, given that the linear loss function is not commonly used? That is, whether and how often would the proposed heuristics overestimate the last-iterate privacy loss.

2. Besides the small sampling rate and the pathological counterexamples (as discussed in 4.3), are there other regimes where the proposed heuristic is significantly smaller than the DP upper bound? This is to understand the usefulness of the proposed heuristics.

3. Minor questions regarding clarity:
    - Line 297 - `we expect this looseness to be the result of statistic effects` -- could the authors provide error bars in Figure 3 to validate this hypothesis?
    - Figure 3 and 4: why is the standard epsilon constant under increasing the number of steps?
    - What is the exact definition of a heuristic privacy estimate? It seems to be DP's upper bound over a family of loss functions, rather than all loss functions.

### Soundness
3

### Presentation
2

### Contribution
2
