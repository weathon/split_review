# A transfer learning framework for weak to strong generalization

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Modern large language model (LLM) alignment techniques rely on human feedback, but it is unclear whether these techniques fundamentally limit the capabilities of aligned LLMs. In particular, it is unknown if it is possible to align (stronger) LLMs with superhuman capabilities with (weaker) human feedback \emph{without degrading their capabilities}. This is an instance of the weak-to-strong generalization problem: using feedback from a weaker (less capable) model to train a stronger (more capable) model. We prove that weak-to-strong generalization is possible by eliciting latent knowledge from pre-trained LLMs. In particular, we cast the weak-to-strong generalization problem as a transfer learning problem in which we wish to transfer a latent concept prior from a weak model to a strong pre-trained model. We prove that a naive fine-tuning approach suffers from fundamental limitations, but an alternative refinement-based approach suggested by the problem structure provably overcomes the limitations of fine-tuning. Finally, we demonstrate the practical applicability of the refinement approach in
multiple LLM alignment tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work studies weak-to-strong generalization where labels from a weaker model are used to improve the capabilities of a stronger model. Unlike prior works which explain this with the superior extrapolation capabilities, or the ability of stronger models to self-correct incorrect labels, this work assumes a latent concept model as in Xie et al. (2021). Under this model, they re-state the weak-to-strong generalization problem as a transfer learning problem in which one wishes to transfer a prior over a latent concept from the weaker model to the stronger model. In the same model, they show that naive finetuning on weak labels leads to a predictor with poor expected risk, but their refined finetuning approach based on Yang et. al. (2024) runs an implicit Bayesian inference procedure that is able to illicit latent knowledge from the stronger model.

### Strengths
- To study weak-to-strong generalization, the paper proposes a transfer learning problem. Here, the model for Y|X induced by a strong unaligned LLM, and the model for Y|X induced by an aligned but weaker LLM (that produces labels) share a latent structure that allows for a cleaner analysis of the predictor returned by the alignment process. 
- The result in Theorem 3.2 clearly shows that naively finetuning on labels from a biased weaker model can lead to performance no better than that of the weaker model. 
- A large chunk of the analysis relies on the following assumption: the aligned Q(Y|X) and unaligned P(Y|X) models sharing the same orthonormal basis, and this ensures that the optimal predictor $E_Q[Y|X]$ is contained in the convex hull of the source distribution. While this assumption is limiting and unclear if true in practice, it presents a clean explanation of how recovering the latent structure from Y|X can fix the labels from the weaker LLM, and thus provably providing a way to generalize from weaker models, as illustrated in an idealized setting in Section 3.2.
- Using ICL to correct weaker labels is a simple and empirically effective way to correct weak labels, as demonstrated by their experiments on math, tinyAlpacaEval, and tinyTruthfulQA.

### Weaknesses
 - The connection between the theoretical model and practical analysis is weak.
  - E.g., it is unclear if ICL is actually performing implicit Bayesian inference under the assumed model. In fact, this is assumed almost 
     directly from the claims in Xie et. al. (2021).
  - The assumptions (Assm 2.1) made to model the bias in weakly aligned models is not well motivated. They may be amenable for 
     theoretical convenience, but there is no reason to believe that the biases behave as nicely as assumed by the model. 
  - The analysis assumes that the source (unaligned LLM) and target (aligned and correct LLM) distributions share the same convex hull 
     realized by the fixed set of $\beta$s. It is unclear if this is true in practice, since this is equivalent to saying that the weaker LLM learns 
     almost all concepts equally well during pre-training, and any errors in the weaker LLM are covered by Assumption 2.1.
- The empirical results are missing some key baselines. If we ignore the labels from the weak model, and directly use the stronger model to label data, e.g. with CoT prompting for MATH, would that curate a good dataset too? Currently, it is unclear if the weaker model is actually enabling implicit Bayesian inference. 
- As the performance of the weak model improves (still subpar compared to stronger model), naive finetuning outperforms their ICL version of finetuning in multiple tasks. This makes their approach effective only when the labels are highly biased. In this case, I wonder if we can throw away the weaker model, and simply self-train on the stronger one.

### Questions
- It is unclear how $\kappa$ or the strength of the aligned LLM changes the error lower bound in the second part of Theorem 3.2. Can the authors please expand on the discussion here?
- What does “labels from one source” mean in L216?
- How does the separability assumption on the latent clusters sidestep the lower presented in Theorem 3.2 (L217)?
- How tight is the result in Theorem 4.2? It seems that $n_{ICL} = o(1/\rho)$ for the result to be non-trivial. Is ICL or some form of Bayesian inference on latent concepts, the best one can do in the worst case?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This submission studies weak-to-strong generalization, where a weaker but aligned model is used to align a stronger but unaligned model. It is commonly assumed that weak-to-strong generalization is possible because the weak model supervision elicits knowledge that is already captured by the strong model but is possibly not expressed with desired frequency. In a similar spirit, the authors consider a theoretical setting, where both weak and strong models are assumed to have conditional probability density (of scalar output Y given a prompt X) that is of the following form:
$$
p(Y|X) = \sum_{k} \alpha_k \mathcal{N}(y; \beta_k^T \phi^*(X), \sigma^2),
$$
where $\phi^*(X)$ is some *observed* representation that is assumed to be the same for both models, while $\alpha_k$ and $\beta_k$ are *unobserved*, with $\beta_k$ representing concepts and $\alpha_{1:k}$ being a prior distribution over concepts. In this framework, the authors formulate weak-to-strong generalization as transferring weak teacher’s prior probabilities $\alpha_{1:k}$, while assuming one of the following conditions:
* Noisy weak model: $\beta_k$ are shared by the strong and weak models, but the labels of the weak model are noisy.
* Biased weak model: $\beta_k$ of the weak model are corrupted versions of target aligned strong model’s $\beta_k$.

One of the main contributions of this submission is demonstrating that naively fine-tuning the strong model with labels sampled from the weak model can lead to quality degradations (Theorem 3.2). Furthermore, with experiments persona learning, mathematical reasoning, and explanation technique learning, the authors show that this simple fine-tuning strategy leads to content quality drop, even though alignment (i.e., style transfer in case of personal/explanation tehncique learning) is often successful.

To improve weak-to-strong generalization, the authors propose a method that uses in-context learning capabilities of the strong model to refine the weak model’s labels (e.g., make them factually more correct) while adhering to the “style” presented to the strong model with a few in-context examples. These refined labels are then used to fine-tune the strong model. Within the proposed theoretical framework, the authors prove that under certain assumptions, this procedure can lead to a successful weak-to-strong generalization. Empirically, the proposed algorithm often manages to retain the strong model's quality, while transferring the style of the aligned weak model significantly, although not as well as the naive fine-tuning does.

### Strengths
* The paper is generally well-written and the presentation is clear. See my comments below for minor suggestions.
* The proposed theoretical framework captures some essential aspects of weak-to-strong generalization, while being amenable to analysis. The theoretical results proved in this framework are good contributions to the theory of weak-to-strong generalization.
* The authors explore a few techniques to improve upon fine-tuning with weak model’s labels. The proposed method and the alternative variants presented in appendices B and C are practical enough and can be helpful for designing better methods in the future.

### Weaknesses
 **Strong assumptions that are sometimes not elaborated enough.**
* Most importantly, the authors make strong assumptions on the form of the weak model, unaligned strong model, and the target (aligned) strong model. Specifically, the assumption that both the weak and strong models can be represented as a mixture of Gaussians with shared feature representations $\phi^*(X)$ is quite restrictive and lacks justification. This assumption needs further discussion, especially regarding its applicability to complex models like large language models.
* It is assumed that the weak model is perfectly aligned (i.e., its $\alpha_k$ are perfect)? This is a strong assumption that needs to be explicitly stated and justified. In practice, weak models are often not perfectly aligned, and this assumption could limit the theoretical analysis's relevance.
* Why do betas have to be orthonormal at Line 104? Also, as I understand, unit norm is not assumed for target distributions. Similarly, why is orthogonality needed in the second case of Assumption 2.1. The need for orthonormal $\beta_k$ is not clear, and the implications of this assumption on the results should be discussed. The authors should also clarify if this assumption is necessary or merely a simplification for the analysis.
* It would be helpful to provide some intuition on the two cases of Assumption 2.1. The two cases of Assumption 2.1 are not well-motivated, and it is unclear what scenarios they are intended to represent. A more detailed explanation of these cases and their relevance to the problem is needed.
* Line 138: How important is it to assume identity covariance for features $\phi^*(X)$? The assumption of identity covariance for the feature representation $\phi^*(X)$ is also quite strong and lacks motivation. The authors should discuss how this assumption affects the results and whether it can be relaxed.

**Insufficient exploration of simpler weak-to-strong generalization techniques than the proposed one summarized above.** Besides the main approach (label refinement with ICL and then fine-tuning on refined labels), the authors propose two simpler strategies in appendices B and C. Furthermore, another simple strategy is to not fine-tune the strong model, but just use its in-context learning ability (possibly with a suitable system prompt) to produce a prediction on a query given a few in-context demonstrations from the weak teacher. To better understand whether the complexity of the proposed approach is needed, it would be great to explore these simpler approaches more (e.g., better prompt engineering)  and compare them to the main proposed technique explicitly in a joint future or table.

### Questions
* Line 117: $X_q$ should be just $X$. Also, one of the $\sigma^2$ is extra.
* Lines 139-141: It would be helpful to state the excess loss explicitly as MSE between $\mathbb{E}_Q[Y|X]$ and $\hat{\beta}^T\phi^*(x)$.
* Line 142: “The subsequent output is an example of source and target priors over the concepts and a weakly supervised sample” – this sentence is unclear.
* Lines 200-204: It should be $\alpha_1$ instead of $\alpha$.
* Theorem 3.2. Would be helpful to comment why there is no $\eta$ on the right hand side.
* Lines 303-308: This part needs more elaboration. It would be helpful to add a derivation of the first line.
In figures 1, 2, and 4, do the 4 weak models on the “Strong model content score vs Weak model content score” and “Strong model style score vs Weak model style score” subplots align with each other. In other words, are the weak models on both plots the same as we scan left to right?

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
This paper mainly studies the problem of weak-to-strong generalization, that is, how to use the feedback from relatively weaker models to train and align more powerful language models without compromising their capabilities.

### Strengths
The paper proposes a theoretical framework that transforms the weak-to-strong generalization problem into a transfer learning problem, and proves that weak-to-strong generalization is feasible under this framework.

### Weaknesses
The framework assumes a convex hull relationship between the source model and target distribution, which may be too idealistic in practical applications. This convex hull assumption implies that the target distribution (the distribution that the strong model aims to achieve) must be covered by a combination of the source model's distributions. This is a strong theoretical assumption because in practice, stronger models may produce outputs that are completely beyond the capabilities of weaker models. Furthermore, the paper does not provide a clear methodology for verifying this assumption in real-world scenarios. The assumption also does not account for the possibility that the target distribution might require a fundamentally different representation or reasoning process that is not present in the source model, even in a latent form. This is a significant limitation as it restricts the applicability of the proposed framework to cases where the target task is essentially a refinement of the source task, rather than a qualitatively different one.

### Questions
1. In practical applications, how can we determine whether there truly exists a convex hull relationship between the source model and target distribution?
2. If we find that the source model cannot fully cover the target distribution, what are some feasible solutions?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a method to improve weak-to-strong generalization using labels from the strong model provided ICL examples from the weak model. They also provide a theoretical analysis of weak-to-strong generalization on a regression task.

### Strengths
The idea of using ICL examples to refine labels for weak to strong generalization is novel, and the paper provides theoretical analysis and motivation for the method. They also perform experiments on multiple common benchmarks and find improvements over naive fine-tuning on weak labels.

### Weaknesses
For baselines, there are other existing methods beyond naive fine-tuning such as using an auxiliary confidence loss or using intermediate models as presented in the weak to strong paper (Burns et al., 2023) that aim to address similar issues. It is unclear how this method compares to these existing methods given that they have the same goal. It would be helpful if comparisons to using the auxiliary confidence loss are added.

### Questions
1. How does this method compare to existing methods for weak to strong that aim to address limitations of naive fine-tuning?

### Soundness
2

### Presentation
3

### Contribution
2
