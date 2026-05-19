- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper rethinks knowledge distillation from a mixture-of-experts perspective by treating teacher predictions as latent variables in the classification objective. The student's classifier is decomposed into a gating function (reusing the teacher's classifier on projected student features) and K experts (implemented as a shared weight matrix with prototype-derived biases). The method is formulated as an EM algorithm with a proven convergence guarantee on the ELBO. Experiments across CIFAR-100 (11 teacher-student pairs), ImageNet-1K, fine-grained datasets, and transfer learning settings show consistent improvements over a broad set of baselines including DiffKD, DIST, and WTTM.

## Strengths

- **Theoretically grounded EM formulation with convergence proof.** The paper derives an ELBO (Eq. 9) and proves that the E-step (Eq. 12) and M-step (Eq. 14) produce a non-decreasing sequence of the objective (Eq. 15). This formal theoretical treatment is rare in the KD literature and elevates the work beyond heuristic loss design.

- **State-of-the-art empirical results across diverse settings.** MoE-KD achieves the highest Top-1 accuracy in 11/11 teacher-student pairs on CIFAR-100 (Tables 1, 2), outperforms DiffKD on ImageNet for ResNet34/ResNet18 by 0.82%, and leads on fine-grained datasets CUB and Stanford Dogs (Table 6). Gains hold even with stronger teachers (Table 7), demonstrating robustness to the capacity gap.

- **Principled treatment of the teacher–ground-truth discrepancy.** The paper identifies that classical KD's simultaneous alignment to teacher soft labels and ground-truth labels is ill-posed when the two distributions diverge (Section 1). The MoE reformulation with teacher predictions as latent variables (Eq. 4) provides a clean resolution without ad-hoc loss balancing or extra hyperparameters.

- **Rigorous connection to prior work.** Section 4.4 proves that SRRL (Yang et al., 2021) is a special case of MoE-KD's ELBO under a collapsed projection assumption (Lemma 1), establishing theoretical generality.

- **Well-designed ablation study.** Table 4 systematically isolates each component: uniform gating, learning gating from scratch, learning prototypes from scratch, hard vs. soft aggregation, and replacing Bayes-optimal estimation with direct teacher predictions. Results confirm that every component contributes to the final performance.

## Weaknesses

### Fatal
None.

### Major

- **The expert parameterization is restrictive relative to the "distinct subtask" claim.** All K experts share a single weight matrix **W** and differ only by additive biases **bₖ** derived from prototypes (Eq. 6: *P*<sub>*θ*</sub><sup>*S*</sup>(*Y*<sup>*S*</sup>=*y*<sub>*i*</sub>|*Y*<sup>*T*</sup>=*k*,**x**<sub>*i*</sub>) = softmax<sub>*y*<sub>*i*</sub></sub>[**W**<sup>⊤</sup>**z**<sub>*i*</sub><sup>*S*</sup>+**b**<sub>*k*</sub>]). This means the experts are not independent classifiers but shifts of the same linear decision boundary in logit space. The paper claims experts "learn to solve a distinct subtask" and "tend to be highly specialized" (Section 4.1), but provides no analysis of whether the learned experts actually exhibit specialization (e.g., gate assignment distributions, per-expert accuracy profiles). The implications of tying the number of experts to the number of classes K (rather than allowing a different number of experts) are not explored. This does not invalidate the method's empirical success, but it creates a gap between the claimed MoE narrative and the implemented architecture.

### Minor

- **Prototype computation (Eq. 7) is underspecified.** The prototypes **μ**ₖ are defined as soft aggregations over the *entire* training set with teacher-prediction weights. The paper does not state whether these are computed once at initialization, updated periodically each epoch, or estimated from mini-batches. This matters for both reproducibility and scalability to large datasets like ImageNet (where full-dataset aggregation per iteration would be expensive). The ablation includes a hard-aggregation variant (baseline iv) but does not clarify the online procedure.

- **Main results lack statistical significance measures.** The paper states "The reported results of our method are averaged over 5 runs" only in the ablation context. Tables 1, 2, and 3 (the primary CIFAR-100 and ImageNet results) show only point estimates without standard deviations or confidence intervals. Given the ablation reports variability across runs, the main results would be stronger with error bars.

- **Ablation study is limited to one teacher-student pair.** Table 4 uses only ResNet32x4 → ResNet8x4 (homogeneous CIFAR-100). Repeating key ablations on at least one heterogeneous pair (e.g., WRN-40-2 → ShuffleNetV1) would strengthen the evidence that the design choices generalize across architectural families.

- **Unclear whether baseline numbers are reproduced or cited.** The paper lists many baselines but does not specify whether they were re-implemented in the same codebase or numbers are taken from prior publications. If numbers are from different papers with potentially different training regimens, the comparison may not be perfectly controlled.

- **Convergence analysis addresses only the full-dataset EM, not the stochastic minibatch version.** The proof in Section 4.3 (Eq. 15) shows monotonic ELBO improvement on the full dataset. The practical algorithm uses mini-batches (Eq. 14), which may not preserve this monotonic property. The paper does not discuss this gap.

- **No discussion of limitations or potential failure cases.** The paper does not consider scenarios where the method might underperform (e.g., poorly calibrated teachers, misaligned student feature spaces). A brief limitations paragraph would improve rigor.

### Trivial
None.

## Nice-to-Haves

- Analysis of expert specialization: visualizing gate assignment distributions or per-expert accuracy on teacher-high-confidence subsets would confirm whether the partition-into-subtasks principle is realized.
- Sensitivity analysis on the number of experts (e.g., testing M > K or M < K) to clarify whether the alignment between experts and classes is essential or coincidental.
- A controlled comparison adding similar-capacity auxiliary modules (projector + prototype-like parameters) to standard KD, to further isolate the benefit of the MoE formulation beyond additional learned parameters.
- Gradient-direction diagnostics on samples where teacher and ground-truth disagree, to illustrate how MoE-KD resolves the claimed conflict.

## Removed Points

These points from the input reviews are flagged to be removed — treat them with caution:

- **From Harsh Critic: "overstates the novelty"** — This is a subjective judgment about framing rather than a specific verifiable weakness. The paper's observation about the teacher-ground-truth conflict is supported by references and the MoE resolution is original.
- **From Harsh Critic: "implicit assumption of feature space alignment"** — The projector 𝒢 is explicitly designed to address this alignment issue. The critic acknowledges the empirical validation, making this a speculative concern rather than a demonstrated flaw.
- **From Harsh Critic: "connection to label-noise learning is somewhat tangential"** — This is an observation about scope, not a weakness. The connection is presented as an interesting link, not a central claim.
- **From Harsh Critic: "conclusion claim is slightly misleading" about KL regularization** — The ELBO inherently contains a KL term by construction; noting this is a framing nitpick, not a substantive error.
- **From Strength Finder: none removed** — all six identified strengths are concrete, specifically cited, and verifiable from the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper that the authors themselves do not already articulate.

## Suggestions

1. Clarify the prototype aggregation procedure: specify whether **μ**ₖ is computed once at initialization, updated periodically, or estimated from mini-batches, and discuss the computational cost for large-scale datasets.
2. Add standard deviations (or confidence intervals) to the main results tables (Tables 1–3) to match the 5-run evaluation used in ablation.
3. Include at least one additional ablation on a heterogeneous teacher-student pair (e.g., WRN-40-2 → ShuffleNetV1) to demonstrate generalization of the ablation conclusions.
4. State explicitly whether baseline results were reproduced in the same codebase or taken from cited papers, and note any shared training settings.
5. Add a brief limitations paragraph discussing potential failure cases (e.g., poorly calibrated teachers, difficult feature alignment scenarios).
6. Acknowledge that the convergence proof applies to the full-dataset EM and note that the practical minibatch version inherits the standard stochastic EM convergence behavior (rather than the monotonic guarantee).
