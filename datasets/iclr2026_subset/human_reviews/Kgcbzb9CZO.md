## Human Reviewer 1

### Summary
The authors proposed to improve the robustness and generalization performance by adding Gaussian noise to the intermediate representations. Some general theoretical analysis and preliminary experimental results partially demonstrate the claims.

### Strengths
Not clear.

### Weaknesses
* Idea is not completely new. The idea is quite similar to [1], although [1] may not be well recognized. 

[1] Yu, Xiaowei, et al. "Noisynn: Exploring the impact of information entropy change in learning systems." arXiv e-prints (2023): arXiv-2309.

* So many random assumptions appeared in the derivation. First of all, what's the advantage for introducing $\eta$ in (1). This is a quite specific parameterization with a strong assumption on $\eta$. The variational inference part is only used to approximate the log-likelihood but if at the very beginning there are no points to introduce $\eta$, there are no support for this method. 

* So many tuning parameters ($\alpha, \beta, \lambda$). And the stability constraint has no theoretical support. In practice these parameters are competing with each other so how can we find the optimal setup and is this optimal setup over-fitting to specific problems?

* Training cost is significantly high, as we need to do multi-pass for each data sample.

* Theorem are basically meaningless and requires implicit assumptions. For example, probability density is not guaranteed to be smooth but Theorem 1 implicitly requires this. Theorem 2 and 3 only shows there exists some probability measure $\mathcal{P}$, but how can we guarantee the $\mathcal{P}$ used in the proposed methods really improves? The proof only means we 

* Proof is not rigorous. For example, in proof of Theorem 2 and 3, we focus on norm square which should be related to $b^2$ and $s^2$. Also, this $\eta$ is very likely to condition on $x$ (hidden in the claim that let $\mathcal{P}$ as a uniform distribution with support measurement $\zeta C$). This is far away from the claim in the methodology.

* Experiments is only on CIFAR-100 and GSM-8K, which is quite small-scale. The authors does not mention if this evaluation is fair under the same training budget. And I'm also wondering if these are orthogonal to the known methods, say if we already apply different kinds of augmentation methods, does this method still work?

### Questions
Just echo the weakness part:

* Relationship to the existing work.
* More rigorous justification of the method.
* More convincing experimental results.

### Soundness
1

### Presentation
1

### Contribution
1

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper introduces Distributional Input Projections, where Gaussian perturbations are injected at intermediate layers and their parameters are learned. The goal is improved generalization through smoother representations.

### Strengths
The paper is generally well-written and easy to follow. The authors run experiments on multiple architectures and tasks (MLPs, CNN/ViT, a language model), indicating an effort toward broader validation. Some empirical gains are visible, suggesting the idea could have regularization benefits. The attempt to connect generalization behavior to smoothness properties is conceptually aligned with robust learning literature.

### Weaknesses
1. Misrepresentation of randomized smoothing literature. The manuscript repeatedly refers to “random smoothing” and incorrectly attributes adversarial training to Cohen et al. (2019). Cohen et al. established Gaussian randomized smoothing certificates using Neyman–Pearson and did not perform adversarial training. Salman et al. later connected smoothing to Lipschitz control, but this distinction is blurred or incorrect in multiple places. Example: Line 239: “and adversarial training (Cohen et al., 2019)”, this is factually wrong. Line 330: RS reduced to just adding noise; this misses the certified robustness objective.
2. Limited novelty and unclear conceptual contribution. Adding learnable Gaussian noise inside networks is close to existing stochastic regularization methods (variational dropout, noisy layers, Bayesian features). Without a formal guarantee or structural insight, the contribution appears incremental. Distillation ablates the sampling at inference, which suggests much of the benefit may stem purely from stochastic training effects.
3. Theory is not rigorous enough for the claims. Theorems rely on smoothness assumptions that do not reflect practical deep nets (non-smooth activations, unknown Lipschitz constants). No certified robustness or provable Lipschitz improvement is established, unlike in the proper RS literature. Consequently, the theoretical section does not convincingly support the narrative.
4. Empirical evidence is insufficient. Results are limited to small-scale datasets. For generalization claims, ImageNet-level evaluation is expected. Variance across seeds is missing, and LLM results show minimal gains under a single training regime. There is no adversarial evaluation, despite repeatedly referencing adversarial robustness.

### Questions
Please address the weaknesses

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper introduces Distributional Input Projection Networks (DIPNet), a framework that projects inputs at each layer into learnable distributions rather than fixed feature vectors. This induces smoother loss landscapes with respect to inputs and improves generalization. The authors provide theoretical analysis showing reductions in local smoothness measures and the Lipschitz constant. DIPNet is evaluated across diverse architectures—ViTs, LLMs, ResNets, and MLPs—and shows consistent gains in test accuracy, robustness to adversarial attacks, out-of-distribution data, and reasoning tasks. The method is modular and can be integrated into existing networks without major architectural changes.

### Strengths
1. Comprehensive experiments across state-of-the-art vision and language models.
2. Strong theoretical grounding linking distributional projection to smoothness and generalization.
3. Improves not only standard generalization but also robustness to adversarial, OOD, and reasoning benchmarks.

### Weaknesses
1. Although motivated by smoothness, the intuition behind why distributional projection helps over simpler regularization is not fully disentangled.
2. The method introduces substantial computational overhead, and its effectiveness appears to rely heavily on distillation, raising concerns about efficiency and practicality in large-scale training.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper proposes DIPNet, which turns each layer’s deterministic input into a learnable Gaussian distribution 
the model samples per-layer “particles” and averages forward trajectories to make predictions. The authors claim this distributional input projection smooths the loss landscape, lowers Lipschitz/smoothness measures, and thereby improves generalization. They provide analyses showing bounded Lipschitz and reduced smoothness for the distributionally smoothed function, add a stability penalty on output variance, and report gains across vision (ViTs on CIFAR-100 under various training-time attacks) and LLM reasoning

### Strengths
- The per-layer Gaussian projection with k-trajectory averaging integrates cleanly; the implementation steps are clearly stated.
- Proofs that smoothing can bound the Lipschitz constant and reduce second-order smoothness support the generalization narrative (I have not fully verified the proofs).
- The paper includes comprehensive setups and supportive ablation studies.

### Weaknesses
- The paper is poorly written and needs reorganization. Please add informative captions to all tables/figures and avoid pasting raw W&B screenshots; re-plot with consistent styling and legible axes/legend.
- The method is computationally expensive, which requires m forward passes per example.
- Reported fine-tuned results appear lower than widely reported pretrained baselines on GSM8K (e.g., Qwen2.5-3B ≈ 79.1; Llama-3.1-8B ≈ 84.5, per the Qwen 2.5 paper).
- Marginal improvements over other simple baselines (<1% ViT-Small/ViT-Base/LM experiment) while being much more expensive

### Questions
- Please report FLOPs and wall-clock time (training and inference) versus baselines, for several k values. Include memory usage and throughput.
- There appears to be a mismatch between your reported GSM8K accuracy and official/commonly reported numbers. Please double-check evaluation protocols.
- Ensure comparisons against strong, compute-matched baselines (e.g., single-pass counterparts with similar wall-clock) and clarify whether any baseline benefits from additional augmentation or ensembling.

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
3