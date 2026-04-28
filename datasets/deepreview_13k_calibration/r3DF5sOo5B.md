# Transformers Learn to Implement Multi-step Gradient Descent with Chain of Thought

- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8

## Abstract
Chain of Thought (CoT) prompting has been shown to significantly improve the performance of large language models (LLMs), particularly in arithmetic and reasoning tasks, by instructing the model to produce intermediate reasoning steps. Despite the remarkable empirical success of CoT and its theoretical advantages in enhancing expressivity, the mechanisms underlying CoT training remain largely unexplored. In this paper, we study the training dynamics of transformers over a CoT objective on a in-context weight prediction task for linear regression. We prove that while a one-layer linear transformer without CoT can only implement a single step of gradient descent (GD) and fails to recover the ground-truth weight vector, a transformer with CoT prompting can learn to perform multi-step GD autoregressively, achieving near-exact recovery. Furthermore, we show that the trained transformer effectively generalizes on the unseen data. Empirically, we demonstrate that CoT prompting yields substantial performance improvements.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the single-layer linear self-attention (LSA) model in the context of solving in-context weight prediction problems for linear regression tasks. Unlike standard ICL, where given a query feature $x_q$, the model is trained to predict the label $y=x_q^\top w^*$, this work trains the model to predict the task feature $w^*$ directly. As a result, the loss is evaluated based on the prediction of the task feature, defined as $\ell=||LSA(X,y)_{[:,-1]}-w^*||^2$.

1. Given input $X,y$, gradient descent (GD) with an appropriately chosen learning rate returns task feature predictions $w_0,w_1,\cdots,w_k$. The authors introduce CoT prompting by appending the intermediate GD steps $w_0,w_1,\cdots,w_k$ to the input, demonstrating that this approach reduces the loss compared to scenarios without CoT prompting.

2. Under certain initialization assumptions, the authors present convergence results using gradient flow analysis and further demonstrate that their findings can generalize to out-of-distribution (OOD) settings.

### Strengths
1. The paper is well-organized, and the theoretical analysis appears solid.
2. The paper introduces CoT prompting to enhance the expressivity of single-layer linear attention models in ICL tasks.

### Weaknesses
 1. Limited explanation is provided about the training setting. As described, the ground-truth GD steps $w_0,w_1...$ are assumed to be available. To generate this data, the gradient of the data model, such as the linear model in this case, must be known. While, in standard ICL settings, only input-label pairs are required. Additionally, each $w^*$ is randomly sampled for each prompt, which implies that generating $M$ training samples would require $M$ gradient calculations over an $n\times d$-dimensional dataset, typically where $M\to\infty$. This raises concerns about the practical feasibility of generating the training data, especially given the computational cost of calculating gradients for each sample, and the assumption that the labeler possesses knowledge of the underlying linear model to compute these gradients.

2. The model's performance and loss are highly dependent on the learning rate $\eta$. In this work, $\eta$ is fixed, meaning that optimal losses can only be achieved by setting $\eta=\frac{n}{n+d+1}$. In standard ICL settings, $\eta$ is often implicitly learned. As a result, the definition of global minimization in the paper is somewhat ambiguous. The paper does not adequately address how the fixed learning rate impacts the model's ability to generalize across different tasks or datasets where the optimal learning rate might vary. This fixed learning rate could limit the model's practical applicability.

3. By making $n$ and $k$ dependent on $d$, it is unclear how varying values of $n$ and $k$ affect convergence and evaluation losses. The paper lacks a detailed analysis on how the choice of $n$ and $k$ relative to $d$ influences the model's performance, especially in terms of convergence speed and the final evaluation loss. This dependency makes it difficult to understand the practical implications of these parameters and how they should be chosen in different scenarios.

4. The CoT + one-layer approach in this paper appears closely related to ICL + multi-layer methods. The paper could benefit from a discussion on this connection. The paper does not sufficiently explore the relationship between the proposed CoT approach and existing multi-layer ICL methods, which could provide valuable insights into the relative advantages and disadvantages of each approach. A more detailed comparison would help to clarify the novelty and contribution of the proposed method.

### Questions
1. In some places, the notations are unclear:
    - The dimensions of model output $f$ and $w$ do not seem to align in Lines 199 and 209.
    - Is $\sigma<1/2$ in Assumption 4.1?
    - Could you clarify whether the loss in Theorem 4.1 corresponds to Eq. (7)?

2. Could the authors explain the reasoning behind setting $V_{31}$ and $W_{13}$ to have the same set of eigenvalues in Assumption 4.1?

3. Could the authors clarify in Theorem 3.1 what the model prediction is: $w^*$ or $w_1$?

4. See Weakness section.

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
The authors investigate the training dynamics of transformers trained with a Chain of Thought (CoT) objective, specifically in an in-context weight prediction task for linear regression. Under certain assumptions, it proves that a one-layer transformer without CoT training can only perform a single gradient descent step, resulting in suboptimal recovery of the weight vector. However, with CoT training, the transformer can execute multi-step gradient descent, enabling near-exact recovery and some out-of-distribution generalization. The authors provide theoretical results demonstrating the global convergence of the training via gradient flow and empirical evidence showcasing the superior performance of transformers trained with CoT compared to those without.

### Strengths
This paper provides some theoretical analysis on CoT, which is lacking and deserves much more attention. These seem to be new results on CoT, albeit in the setting of a one-layer linear transformer.

### Weaknesses
- The comparison between a transformer trained on a Chain of Thought (CoT) objective and one without seems to conflate the training objective with the presence of CoT data in the pretraining corpus. While it's likely that CoT data exists within the vast pretraining datasets of modern LLMs, the core training objective remains next-token prediction. The distinction made in the paper might not accurately reflect the nuances of how CoT reasoning emerges in models trained on large, diverse datasets.

- The restriction to one-layer linear transformers, while common for theoretical analysis, significantly limits the applicability of these results to real-world LLMs. The architectural differences and the non-linearities present in practical models could drastically alter the training dynamics and the efficacy of CoT prompting. It is unclear how well the findings on multi-step gradient descent through CoT training would translate to deeper, non-linear models.

- The assumption that the number of samples (n) is bounded by dlog^5d appears contrived and primarily driven by the need to facilitate the proofs. A more intuitive framing, such as requiring a quadratic number of samples to control evaluation error, might be more insightful. Furthermore, the necessity of this bound for the main results should be clarified. For instance, does Corollary 3.1 truly require this bound, or is it only relevant for the analysis of training dynamics?

- Theorem 4.1 relies on several restrictive assumptions. While the authors acknowledge that these settings are used in prior works, exploring the implications of these assumptions in a more general setting would significantly strengthen the paper. Relaxing these assumptions, even if it leads to weaker bounds, could provide a more realistic understanding of CoT's impact on training dynamics.

- The novelty of the methods employed in the proofs is not clearly articulated. It is difficult to ascertain whether the techniques are straightforward extensions of those used in other works, such as Bai et al., or if they involve genuinely novel ideas. The manuscript should explicitly highlight the unique aspects of the proof techniques and their contributions to the field.

- Theorem 4.2 is not clearly explained. Specifically, the intuition behind the model's out-of-distribution (OOD) generalization within the specified bounds of the spectrum of the covariance matrix is not provided. Additionally, the term L^{eval}_{\Sigma} is not defined, making it difficult to understand the theorem's implications. Providing a clear definition and an intuitive explanation of the OOD generalization behavior would greatly enhance the theorem's impact.

- The manuscript lacks empirical validation for Theorem 4.2. Including experiments that demonstrate the OOD generalization predicted by the theorem would provide strong support for the theoretical claims.

- While a theoretical analysis of CoT is valuable, the current results lack impact due to the restrictive assumptions and the limited scope of the model considered. Providing more intuitive explanations of the assumptions and exploring the implications in a more general setting could significantly enhance the paper's contribution.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
2

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
This paper introduces a novel in-context learning task, termed in-context weight prediction for linear regression. The authors demonstrate that single-layer transformers exhibit limitations in this task when working with limited number of examples, and they show that incorporating a chain-of-thought mechanism significantly enhances performance. Through analysis of gradient dynamics in single-layer transformers using chain-of-thought, they establish convergence results that align well with their empirical findings.

### Strengths
While existing literature always try to understand the expressive power of CoT from a computational complexity perspective, this work offers a fresh analytical framework, and they provide convergence analysis and sufficient  experiments to validate their findings. The approach is both innovative and provides valuable insights for future research directions.

### Weaknesses
Although this work presents interesting findings, the construction and proof techniques largely adapt existing methodologies. Furthermore, similar results might be achievable using looped transformers as demonstrated in [1], where:
$$
Z_0 = \begin{pmatrix}
x_0 & x_n& x_{query} \\
y_0 & y_n& 0
\end{pmatrix}, Z_k = f(Z_{k-1})
$$
where $f$ is a linear transformer with fixed parameters. In other words, while existing work demonstrate looped transformer (inference a (single layer) fixed parameter transformer with $k$ times can get a similar form $w^{k} x_{query}$, where $w^k$  defined like theorem 3.2 in this work, the theoretical contribution that directly analysis $w^k$ seems limited. So a more detailed discussion between this work and analysis in [1], and a meanfull explaination why such a in-context learning task framework is necessary, is desired.

Note that [1] analysis a multilayer transformer with the same parameters as each layer, so I refer this work as looped transformers, other works like [2,3] also analysis similar transformers.

[1] Ding, N., Levinboim, T., Wu, J., Goodman, S., & Soricut, R. (2023). CausalLM is not optimal for in-context learning. arXiv preprint arXiv:2308.06912.

[2] Ahn, K., Cheng, X., Daneshmand, H., & Sra, S. (2023). Transformers learn to implement preconditioned gradient descent for in-context learning. Advances in Neural Information Processing Systems, 36, 45614-45650.

[3] Gatmiry, K., Saunshi, N., Reddi, S. J., Jegelka, S., & Kumar, S. (2024). Can Looped Transformers Learn to Implement Multi-step Gradient Descent for In-context Learning?. arXiv preprint arXiv:2410.08292.

### Questions
Please refer to the weakness section, the reviewer would like to better understand how the authors reconcile the apparent disconnect between CoT steps in practical applications (where more steps don't necessarily yield better performance) and their theoretical analysis. Additionally, how can the insights from this work inform the design of effective step-by-step instructions for improved CoT performance?

### Soundness
3

### Presentation
3

### Contribution
3
