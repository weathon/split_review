# Attention layers provably solve single-location regression

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Attention-based models, such as Transformer, excel across various tasks but lack a comprehensive theoretical understanding, especially regarding token-wise sparsity and internal linear representations. To address this gap, we introduce the \textit{single-location regression} task, where only one token in a sequence determines the output, and its position is a latent random variable, retrievable via a linear projection of the input. To solve this task, we propose a dedicated predictor, which turns out to be a simplified version of a non-linear self-attention layer. We study its theoretical properties, by showing its asymptotic Bayes optimality and analyzing its training dynamics. In particular, despite the non-convex nature of the problem, the predictor effectively learns the underlying structure. This work highlights the capacity of attention mechanisms to handle sparse token information and internal linear structures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new theoretical approach to understand attention mechanisms by considering a task called single-location regression. The authors consider a simplified model that's related to self-attention layer and shows that the model can achieves asymptotic Bayes optimality, while linear regressors fail. The authors also use PGD to show that the non-convex loss function still converge.

### Strengths
1. The paper is well-written and easy to follow. For example, the step-by-step illustration of how to connect the construction to the attention mechanism in Section 3 is helpful for understanding.
2. The choice of model is good, like using [CLS] property which is observed in empirical study in (5) is natural and reasonable, and using erf as nonlinear weight function is also reasonable. In general, the theoretical result is solid.
3. Also contain some empirical result for showing the convergence of constructed model

### Weaknesses
1. The setting is restricted to single position token, although it focus on the sparse attention settings and it's already difficult to analyze, it's still far from the real-world case. Besides, the authors haven't done experiments on real-world experiments (like sentimental tasks as shown in Figure 1) to support some claims in the paper, this may kind of reduce the impact of the theoretical analysis. But in general it's already good as a theoretical-centric paper.

### Questions
1. What's the function of input in Figure 1 (a)? It seems that the Y label just depends on the output and the input is not related to the sentimental label?

### Soundness
3

### Presentation
4

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
This paper studies the ability of attention mechanisms to deal with token-wise sparsity and internal linear representations. In order to demonstrate the capability, the paper proposes a simplified version of a self-attention layer to solve the single-location regression task, showing an asymptotic Bayes optimality and analyzing training dynamics.

### Strengths
The paper is well-written and easy to follow. A novel task called "single-location regression task" is introduced to satisfy the sparsity of the token and model real-world tasks to some extent. Despite the non-convexity and non-linearity, the paper is able to analyze the training dynamics and show the asymptotic Bayes optimality.

### Weaknesses
1. The proposed task may be over-simplified and lack generality. For instance, it assumes that the tokens other than $X_{J_0}$ have zero mean and only one token contains information. This is a significant limitation as real-world data often exhibits more complex relationships and dependencies between tokens, where multiple tokens may contribute to the final output and have non-zero means. The single-location regression task, while useful for initial analysis, does not fully capture the nuances of practical applications.
2. The paper shows the connection to a single self-attention layer by using the assumption that $p=1$. Although the low-rank property may come true after the training process, it is so strong to make this assumption directly. This assumption drastically simplifies the analysis but may not hold in practice, where the attention matrix is unlikely to be strictly rank-1. The authors should provide more justification or empirical evidence to support this assumption, or at least discuss the potential impact of relaxing it.
3. It is uncommon to use the function $erf$ to replace the softmax function. To demonstrate the feasibility of this simplification, more explanations or theoretical backups should be provided. The $erf$ function has different properties than softmax, particularly in terms of its saturation behavior and gradient characteristics. The paper needs to rigorously justify why this substitution is valid and how it affects the training dynamics and the final solution.
4. The paper shows the asymptotic results of $k_t, v_t$, while a non-asymptotic result is needed to investigate the convergence rates of these two parameters. The asymptotic analysis, while insightful, does not provide information on how quickly the parameters converge to their optimal values. A non-asymptotic analysis would be crucial to understand the practical implications of the theoretical results, especially in scenarios with limited training data or computational resources.
5. The initialization is limited to the specific manifold, which is better to extend to a more general one. The restriction of initialization to a specific manifold limits the applicability of the theoretical results. A more general initialization scheme would make the analysis more robust and relevant to practical scenarios where the initial parameters are not constrained to such a specific manifold.
6. The current experiments only validate the theoretical results on synthetic datasets. It is recommended that the authors consider adding some experiments on real datasets to test the effects. The lack of experiments on real-world datasets makes it difficult to assess the practical relevance of the proposed model and analysis. Experiments on real datasets would provide valuable insights into the model's performance and limitations in more realistic settings.

### Questions
See weaknesses.

### Soundness
3

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
This paper introduces a new task, the single location regression task, showing it is solvable by a predictor resembling an attention layer, when a linear predictor fails. The result is theoretically well grounded and of good significance given the limited theory on attention layers and their striking efficacy. This task relates to key famous NLP problems known in the existing literature, serving as a good testbed for studying Transformers through a theoretical lens. The statistical performance of this attention-like optimal predictor is shown to exceed the one of an optimal linear predictor, under minimal assumptions. (projected) Gradient descent, is demonstrated to reach the optimal solution, wiith experiments provided to support the theory.

### Strengths
- The paper is extremely well written and very easy and pleasant to read. 
- The analysis is theoretically strong and rigorous
- More generally, this work promotes an approach that is worth being acknowledged and valued: looking into a simpler problem than the ones practitioners can face, yet relevant, and solve it completely and rigorously.
- Additionally, the problem is well connected to practical concerns, with the authors made a convincing case for the significance of their analysis.

### Weaknesses
By decreasing order of importance

- The present work’s approach is not so well connected to the existing literature in line 103: "note that our task shares similarities with single-index models (McCulllagh & Nelder, 1983) and mixtures of linear regressions (De Veaux, 1989)". I see the differences between those works and the present one being hightlighted in the following sentence , but the exact nature of these similarities is not clear. Could this connection be elaborated? Specifically, the connection to single-index models seems tenuous, as those models typically involve a single projection of the input, whereas this work involves multiple projections and a more complex non-linear interaction. The mixture of linear regressions connection is also not immediately obvious, as the mixture components in De Veaux (1989) are typically associated with different subpopulations, which is not the case here.
- Minor: In the caption of figure 2, it may be helpful to add a note about the size of the squares, that presumably indicates the level of alignment.
- line 234: "We emphasize that empirically this simplification of softmax using a component-wise nonlinearity has been shown not to degrade performance". The cited paper Wortsman et al, 2023 indeed indicates such behaviour but their experiments include a normalisation. The claim as stated is misleading without explicitly mentioning the normalization step.
- Broadly speaking, the question of whether softmax is needed in attention layers remains an open and unresolved one in the commuinity. To avoid overstating the case, consider rephrasing to reflect this ongoing debate. Note that I don’t think having used erf in your analysis diminushes the value of your work in any way.


### Questions
- Could you point out (and explain) the steps in your proofs that would break if softmax were considered instead of erf. My guess is that preserving the independence  is key (via elementwise application) but could sigmoid or any other nonlinear bounded increasing and differential elementwise activation work as well? It might be helpful to mention early on that the analysis could extend to a broader class of activations if that’s the case (modulo adjustments of the formulae in theorem 1).  
- Linear predictors are shown to fail at solving the task and the comparison to them is much appreciated. Do you have a sense of how non linear predictors would in turn perform, thus this could show how attention layers are to be preferred to fully-connected layers for instance in such contexts (an analogue of proposition 3 in this case may not be true and probably non trivial to show, but in any case, interesting to discuss or to investigate). 
- Are the tokens assumed to be independent (line 74) or independent conditionally on J_0 (line 85)? I did not read the proofs so I couldn’t figure it out  myself but would be good to clarify. More generally, could you explain at which points of your proofs the independence is needed to help readers understand how this assumption could be relaxed for future works concerned with more realistic scenarios.
- Minor: line 1832 "Our code is available at [XXX]" in the appendix. 
- Extra minor: line 469: a space is missing between "Figure 4a" and "(right)"

### Soundness
4

### Presentation
4

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
This work examines the transformer mechanism for solving the single-location regression task within a simplified non-linear self-attention setting. It provides a Bayes optimality guarantee for the oracle network predictor and demonstrates how the training dynamics allow the network to converge to this solution using projected gradient descent.

### Strengths
1. The mathematical analysis from both statistical and optimization perspectives is insightful, offering a comprehensive theoretical guarantee.

2. The paper is well-written and easy to follow.

3. Experiements are provided to support the theoretical findings.

### Weaknesses
My main concern lies in the motivation for studying this specific setting, characterized by token-wise sparsity and internal linear representations.  While these features are relevant to real-world NLP scenarios, the essential mechanism for transformers to succeed in this setting is, first, to identify the underlying structure (the latent sparse pattern in this work) and then to perform a task-specific operation on this structure (linear transformations here). This intrinsic mechanism has been extensively explored across various settings (e.g., [1-3]), even with more realistic softmax attention. Thus, the technical significance of studying a simplified attention model in such a specific setting remains unclear. Could the authors elaborate on the specific technical difficulties encountered in this setting? What are the key technical challenges in extending the analysis to more realistic softmax attention?



[1] How Transformers Learn Causal Structure with Gradient Descent. Nichani et al., 2024

[2] Vision Transformers provably learn spatial structure. Jelassi et al, 2022

[3] Transformers Provably Learn Sparse Token Selection While Fully-Connected Nets Cannot. Wang et al., 2024

### Questions
1. What is the specific convergence rate in Theorem 5? Since this forms a key part of the contribution in characterizing the training dynamics, a more detailed presentation in the main paper would be beneficial.

2. In line 334, why is the entire sum on the order of $\Theta(\lambda \sqrt{L})$?

3. The PGD analysis relies on a relatively strong assumption that the initialization lies on the manifold. Could the authors discuss any possibilities for generalizing the current analysis to accommodate a broader range of initializations?

### Soundness
3

### Presentation
3

### Contribution
2
