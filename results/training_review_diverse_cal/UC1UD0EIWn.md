Now I have a thorough understanding of the paper and can verify all the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes MoE-KD, a knowledge distillation method that reformulates the classification objective by treating the teacher's predictions as latent variables in a mixture-of-experts framework. This decomposes the classification task into subtasks handled by specialized experts, with the teacher classifier serving as a gating function. The method is formalized as an EM algorithm with a convergence guarantee and achieves strong empirical results across many benchmarks (CIFAR-100, ImageNet, fine-grained datasets) and teacher-student pairs.

## Strengths

1. **Principled reformulation of KD as a mixture-of-experts problem with theoretical grounding.** The introduction of teacher predictions as latent variables (Eq. 4) and derivation of an ELBO (Eq. 9) leading to a formal EM algorithm (E-step Eq. 12, M-step Eqs. 13–14) with a convergence proof (Eq. 15) goes beyond heuristic logit-matching and provides a clear optimization framework.

2. **Consistent state-of-the-art performance across diverse settings.** In Tables 1 and 2 (CIFAR-100, 11 teacher-student pairs), MoE-KD surpasses all prior methods including the recent WTTM, with gains up to 2.10% for WRN-40-2/ShuffleNetV1. On ImageNet (Table 3), it outperforms DiffKD by 0.82% Top-1 for ResNet34/ResNet18. On fine-grained datasets (Table 6) and with stronger teachers (Table 7), it again achieves the best results.

3. **Theoretical connection to existing work.** Section 4.4 proves that SRRL is a special case of MoE-KD's ELBO when the expert projector collapses (Lemma 1), subsuming a known approach and explaining why MoE-KD can outperform it.

4. **Effective handling of the teacher-student capacity gap.** Table 7 shows that with a stronger teacher, MoE-KD improves Top-1 accuracy by 1.5% and 1.0% over baseline for ResNet34 and EfficientNet-B0 respectively, outperforming DiffKD (1.3% and 0.8%).

5. **Feature transferability validated on downstream tasks.** Linear probing results (Table 5) on STL-10 and Tiny-ImageNet show that features learned by MoE-KD generalize beyond the original classification task, achieving higher accuracy than features from other KD methods.

## Weaknesses

### Fatal
None.

### Major

1. **The inference procedure as stated is non-standard and lacks justification.** Section 4.3 states: "inference with the optimized parameters $\hat{\pmb\theta}$ for a test-time sample $\mathbf{x}$ requires to compute $\arg\max_{k}\mathcal{R}_{\mathrm{MoE-KD}}(\mathbf{x},k;\hat{\pmb\theta})$." Here $\mathcal{R}_{\mathrm{MoE-KD}}$ is the ELBO-based objective (Eq. 11). This means evaluating the ELBO for every possible label $k$ and picking the highest — not computing the student's marginal predictive distribution $P_{\theta}^{S}(Y^{S}=y|x)=\sum_{k}P_{\theta}^{S}(Y^{S}=y|Y^{T}=k,x)P_{\theta}^{S}(Y^{T}=k|x)$, which would be the natural inference rule. Moreover, the ELBO depends on the variational distribution $\hat{P}$, which during training is set in the E-step using the known label $y_i$ (Eq. 12). At test time, no label is available to condition on, but the paper does not specify what $\hat{P}$ is used or how the ELBO is evaluated. The paper must either (a) clarify that inference actually uses the marginal distribution (and correct the text), or (b) justify why ELBO-based inference is valid and specify the test-time variational distribution. The current ambiguity undermines reproducibility and understanding of what the trained model actually outputs. This is the most significant unresolved issue in the paper.

### Minor

1. **Variational distribution notation conflates dependencies.** Eq. (9) writes the variational distribution as $\hat{P}(Y^{T}=k|\mathbf{x}_{i})$, which suggests it conditions only on the input. However, the E-step computation (Eq. 12) uses $P_{\theta_{t}}^{S}(Y^{T}=k|Y^{S}=y_{i},\mathbf{x}_{i})$, which depends on the true label $y_i$ through the expert terms in both numerator and denominator. The notation should make this explicit (e.g., $\hat{P}(Y^{T}=k|\mathbf{x}_{i},y_{i})$). This is a clarity issue, not a mathematical error — the actual computation is correct — but it could confuse readers attempting to reproduce or extend the work.

2. **No discussion of inference computational cost.** The paper does not analyze the inference cost of the method. Even if one uses the marginal distribution (the natural approach), inference requires evaluating $K$ expert outputs and combining them with the gating weights — more expensive than a standard single-classifier student. If the ELBO is actually used for inference as stated, the cost would be even higher (roughly $K$ times a forward pass). The paper should acknowledge this trade-off and ideally report wall-clock times or FLOPs.

3. **Overstated simplicity regarding hyper-parameters.** The paper claims "the only hyper-parameter in our method" is the temperature $\tau$ (Section 5, Settings). However, the architectures of the projectors $\mathcal{G}$ (three-layer bottleneck) and $\Psi$ (two-layer MLP) — including their layer counts and hidden dimensions — are also design choices that affect performance. A brief study of sensitivity to these architectural choices would strengthen the claim of simplicity.

4. **No specification of how expert prototypes $\mu_k$ are computed during training.** Eq. (7) defines $\mu_k$ via a soft aggregation over the entire dataset in the teacher embedding space. The paper does not specify whether this aggregation is performed as a pre-processing step (pre-computed once) or updated online (e.g., via moving average), and what additional time/memory cost this incurs beyond the "less than 3%" reported for the projector $\mathcal{G}$.

### Trivial
- The convergence proof (Eq. 15, the sequence is non-decreasing and bounded) is a standard EM argument. The paper does not over-claim here, but the proof is not deep.

## Nice-to-Haves

- **Show that the experts actually specialize.** The paper claims the gating partitions the dataset into subtasks and that each expert becomes specialized. Direct evidence (e.g., visualizing gating weights for test examples, measuring how different experts fire on different classes) would strengthen this central narrative. Currently it is backed only by the uniform-gating ablation.
- **Sensitivity analysis of the number of experts $K$.** The method sets $K$ equal to the number of classes. It would strengthen the contribution to show whether smaller $K$ works (e.g., on datasets with many classes) or whether a fixed $K$ could be used across datasets.
- **A limitations section** would help delineate the method's scope, particularly the inference cost and the dependency on teacher prototypes.
- **The connection to label-noise learning** in Section 4.4 is interesting but is mentioned only briefly and not exploited further. It could be shortened or moved to extended discussion without loss to the main KD contribution.

## Removed Points

- **"The convergence proof is a standard EM argument"** — This is a descriptive observation, not a weakness. The paper does not claim a novel convergence proof, and a standard proof is appropriate for this type of paper.
- **"The label-noise learning connection feels bolted on"** — This is a subjective stylistic opinion, not a substantive weakness. The connection is presented as an observation, not a core contribution.
- **"Requiring the authors to add X (various suggestions)"** — Several reviewer suggestions (limitations section, expert specialization visualization, K sensitivity) are moved to Nice-to-Haves above as they are not core weaknesses but would strengthen the paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the inference procedure.** State explicitly whether the marginal distribution or the ELBO is used at test time. If the marginal is used, correct the text in Section 4.3. If the ELBO is used, (a) specify what variational distribution $\hat{P}$ is used at test time and why, (b) justify why $\arg\max_k \text{ELBO}(x,k)$ is a valid surrogate for $\arg\max_k P(Y^S=k|x)$, and (c) discuss the computational cost.
2. **Fix the variational distribution notation** in Eq. (9) to reflect the dependency on $y_i$, e.g., $\hat{P}(Y^T=k|\mathbf{x}_i,y_i)$.
3. **Add a brief discussion of inference cost** (FLOPs or wall-clock time) compared to standard KD students.
4. **Specify how $\mu_k$ prototypes are computed** — pre-computed once or updated online — and report the associated cost.
5. **Add a limitations section** discussing inference cost, the need for teacher prototypes, and sensitivity to projector architectures.

## Score and Decision

This paper makes a genuine contribution: a novel, theoretically grounded reformulation of KD as an MoE problem with an EM training algorithm, backed by strong and extensive experimental results. The core ideas are creative and well-motivated. The main unresolved issue is the ambiguity around the inference procedure, which needs to be clarified or corrected. This is fixable and not a fatal flaw. The notation issue and missing computational discussion are minor. Overall, the contribution is solid and the paper warrants publication.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>