Now I have a thorough understanding of the paper and all the verified claims. Let me produce the final consolidated review.

## Summary

The paper proposes Duet, a training method that aims to preserve clean accuracy during certified robustness training. The key idea is to use SVD to decompose weight matrices into rotation matrices (claimed to affect clean accuracy) and singular values (claimed to affect certified robustness), then align the rotation matrices between a pre-trained vanilla model and the certification model via a similarity loss. The method also uses low-rank approximation for efficiency.

## Strengths

- **Novel identification of the source of the clean-accuracy degradation.** The paper argues, through an SVD decomposition lens, that certified robustness training over-regularizes singular values (via spectral norm scaling) while neglecting rotation matrices, which harms clean accuracy. This provides a more specific diagnosis than prior general observations about over-regularization. (Section 4.2, lines 109-111)

- **The proposed fix — rotation matrix alignment — targets the diagnosed cause directly.** Rather than using generic distillation or multi-objective training, Duet explicitly preserves the unit-vector structure (U, V^T) of the weight matrices, which the paper argues is responsible for clean accuracy. This is a more principled intervention than ad-hoc regularization. (Section 4.4, Eq. 150)

- **Low-rank approximation for practicality.** Section 4.3 describes using a truncated set of orthogonal unit vectors to approximate the rotation matrices, which selects important directions and reduces storage/computation. This addresses a real scalability concern. (Lines 126-134)

- **High rotation matrix similarity is reported (95.6% vs 77.8% for standard certified training).** This provides a direct measurement that the mechanism is operating as intended, even if the metric itself is not fully defined. (Section 5, line 180)

- **The method is designed as a plug-in to existing certified training frameworks.** The similarity loss is added to the existing training objective, making it compatible with BCP-style training without requiring a fundamentally new training paradigm. (Section 4.1, Algorithm 1 reference)

## Weaknesses

### Fatal
None.

### Major

- **The central quantitative claims are not backed by a visible results table.** The introduction states a +3.76% clean accuracy improvement and −0.93% certified accuracy decrease over a global-Lipschitz baseline, but the experiment section contains no numerical table showing these values. Results are presented only via figure references (Figures 2 and 3, which are image placeholders in the text). The baseline numbers for BCP (Lee et al., 2020) and Local Lipschitz (Huang et al., 2021) are never given in the text. Without a table reporting clean accuracy, certified accuracy, and standard deviations for all methods, the reader cannot verify the claimed improvement. This is the single most critical weakness — the paper's headline quantitative contribution is not evidenced in a verifiable form.

- **The method is underspecified to the point of irreproducibility.** (a) The total training objective is never stated — how Loss_sim (Eq. 150) is combined with the certified robustness loss (e.g., the BCP worst-logit loss) is not specified, and the weighting hyperparameter λ is absent. (b) All training hyperparameters (learning rate, batch size, number of epochs, optimizer, weight decay, warm-up schedule) are omitted. (c) The paper says it uses "either ReLU or MaxMin as the activation function" (line 167) without specifying which was used for which experiment. (d) The low-rank approximation is described conceptually but it is unclear whether the certification model's rotation matrices are also approximated during training or only the vanilla model's are. These gaps mean the method cannot be reproduced from the paper as written.

- **No standard deviations, error bars, or multiple trials.** Every reported number appears to come from a single run. In a setting with well-known training variance (certified robustness training is notoriously sensitive to initialization and hyperparameters), single-run results are not credible evidence.

### Minor

- **Factual inaccuracy in the explanation.** Line 119 states: "the maximum singular value σ1 is the same as the other singular values, which results in equal variations in the weight matrix across all directions." This is not generally true — singular values of certification model weight matrices are not identical. The intended intuition (that spectral norm regularization makes singular values *more similar* to each other than in a vanilla model) may be correct, but the statement as written is false and could mislead readers.

- **The rotation matrix similarity metric is never defined.** The paper reports "average similarity" of 77.8% vs. 95.6% but never specifies whether this is cosine similarity, angular distance, Frobenius-norm based, or something else. Without a definition, these numbers are uninterpretable.

- **No computational cost comparison.** The paper criticizes local Lipschitz methods (Huang et al., 2021) for being expensive but does not report training time, per-iteration cost, or peak GPU memory for Duet. Since the method adds SVD computation plus an extra forward pass through the vanilla model, its own cost should be quantified.

- **No discussion of limitations.** The paper tests only one dataset (CIFAR-10), one architecture (6 conv + 2 FC), and one perturbation radius (36/255 l2). The conclusion does not acknowledge these scope restrictions or discuss when the method might fail.

- **Section 4.2 is repetitive and lacks a clear logical bridge to the loss function.** The intuitive argument about rotation matrices vs. singular values is stated several times in similar language, but the derivation from this intuition to the specific form of Loss_sim (Eq. 150) — particularly the scaling factors ‖σ_cer‖/‖σ_van‖ and ‖σ_van‖/‖σ_cer‖ — is not explained. The reader is left wondering why those specific scaling terms appear.

### Trivial

- The paper contains several minor typos and grammatical errors ("offilne" → offline, "matirx" → matrix, "confilct" → conflict, repeated phrases). These do not affect the technical content.

## Nice-to-Haves

- An ablation isolating the rotation-matrix similarity loss from the certified robustness loss would directly show that the improvement is due to the proposed knowledge transfer rather than other incidental factors.
- Testing on an additional dataset (e.g., SVHN, Tiny ImageNet) and at least one more perturbation radius would strengthen the generality claims.
- A discussion of how the method relates to knowledge distillation (since it uses a teacher model) would help position the contribution.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Criticism about garbled matrix equations / broken formatting.** These are parser artifacts, not author errors, per hard rules.
2. **"Algorithm 1 is referenced but its content is not visible."** The algorithm exists as an image in the original submission; the parser stripped it. Not an author error.
3. **"The definitions themselves are correct but do not connect to the method."** This is a generic scope complaint about a preliminaries section — preliminaries are supposed to be background, not connected to the method in detail.
4. **"The paper does not clearly state how its method differs from existing knowledge-distillation approaches."** The paper frames its contribution around SVD-based rotation matrix alignment, which is a different mechanism from standard logit-level or feature-level distillation. The difference is implicit in the formulation.
5. **Strength Finder's claim that the paper "demonstrates" a +3.76% improvement.** This conflicts with the verified weakness that the experimental evidence is insufficiently presented. The paper *claims* this improvement, but the evidence does not meet the bar for "demonstrated."

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any interpretation of the method's implications that the authors themselves did not identify.

## Suggestions

1. **Add a complete results table** showing clean accuracy and certified accuracy (with standard deviations over ≥3 seeds) for: (a) the vanilla model (upper bound), (b) global-Lipschitz certified training (BCP), (c) local-Lipschitz certified training, and (d) Duet. This is the single most important improvement.
2. **State the full training objective explicitly:** L_total = L_cert + λ · L_sim, specify λ, and describe how L_cert is computed (presumably via BCP's worst-logit formulation).
3. **Report all training hyperparameters** (optimizer, learning rate and schedule, batch size, epochs, warm-up schedule, weight decay) and specify whether ReLU or MaxMin was used.
4. **Define the rotation matrix similarity metric** — what mathematical operation produces the 77.8% and 95.6% numbers?
5. **Correct the factual imprecision** about "all singular values being equal" on line 119; replace with a softer statement about singular values becoming more similar.
6. **Add a computational cost table** comparing training time and GPU memory for all methods.
7. **Include a limitations paragraph** acknowledging the single-dataset, single-architecture, single-radius scope.

## Score and Decision

**Originality:** Moderate — the SVD-based decomposition of the problem and the rotation-matrix alignment loss are genuinely novel angles within certified robustness.

**Importance of research question:** High — the clean accuracy vs. certified robustness trade-off is a well-known bottleneck for deploying certified models.

**Support for claims:** Low — the central quantitative claim is stated but not backed by a proper results table; the method is not reproducible.

**Soundness of experiments:** Low — single dataset, single architecture, single seed, no standard deviations, no numerical table.

**Clarity of writing:** Low to moderate — the method is conveyed but with significant gaps and repetitive prose.

**Value to the research community:** Potentially moderate if the method is real and properly validated, but negligible in the current form because the evidence cannot be assessed.

The paper identifies a real problem and sketches an interesting SVD-based approach. However, the experimental evaluation is thin to the point where the central quantitative claim is unverifiable from the text, and the method description is too incomplete to reproduce. These are not minor presentation issues — they are structural gaps that prevent the paper from making a believable contribution. A major revision that adds rigorous experiments, a proper results table, and a complete method specification could make this a viable paper.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>