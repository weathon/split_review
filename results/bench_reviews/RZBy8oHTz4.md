Now I have verified the paper content thoroughly. Let me produce the final consolidated review.

## Summary

This paper proposes adding a scalar factor $\tau$ to the negative-pair term of the spectral contrastive loss (SpeCL), which is algebraically equivalent to regularizing the mean of representations toward zero ("zero-mean regularization"). The authors show this uniformly reduces positive-pair graph weights, which can mitigate the effect of "wrong connections" (false positive pairs). They provide theoretical analyses for two settings: (i) unsupervised domain adaptation, where they prove the target error bound is tightened by a $(1-\tau)^2$ factor, and (ii) supervised learning with label noise, where they show the modification implicitly reduces mislabeled weights in the noise transition matrix. They further connect the supervised SpeCL minimizer to Neural Collapse (simplex ETF). Experiments on digit UDA datasets, CIFAR-10/100, and SVHN with symmetric label noise show consistent but small improvements over the $\tau=0$ baseline.

## Strengths

- **Clean theoretical connection between a simple loss modification and zero-mean regularization.** Adding a scalar $\tau$ to the negative term of SpeCL is shown (Eq. 3.2) to be exactly equivalent to adding $\|\mathbb{E}[f(x)]\|^2_2$ regularization. This is an elegant algebraic insight that cleanly links a one-line change to a known regularization effect with interpretable consequences.

- **Provable UDA error bound tightening.** Proposition 3.2 demonstrates that introducing $\tau$ multiplies the target-domain error bound by $(1-\tau)^2$, providing a theoretical guarantee of improved domain generalization under the stochastic block model graph. This is a non-trivial extension of the analysis in Shen et al. (2022).

- **Neural collapse connection for supervised SpeCL.** Theorem 3.3 shows that the global minimizer of the supervised SpeCL satisfies $\hat{H}^\top\hat{H}=rI-\tau\mathbf{1}\mathbf{1}^\top$, which for $\tau=1$ recovers the simplex ETF from Neural Collapse (Papyan et al., 2020). This theoretical characterization is neat and insightful.

- **Label-noise mitigation theory.** Proposition 3.5 provides a clean result: for symmetric label noise with rate $\omega$, setting $\tau \geq r\omega$ makes the noisy-label minimizer equivalent to the clean-label minimizer up to rescaling. The intuition (Figure 3) that uniform weight reduction re-normalizes to reduce noise rate is compelling.

- **Consistent, if modest, empirical gains.** Across self-supervised learning, supervised learning, UDA (four digit transfer tasks), and noisy-label learning (CIFAR-10/100, SVHN), $\tau > 0$ consistently outperforms $\tau = 0$, with the effect most pronounced at high label noise (Table 3). This consistency lends credibility to the theoretical predictions.

## Weaknesses

### Fatal

None.

### Major

- **Insufficient experimental scope relative to the claims.** The UDA experiments are limited to four digit datasets (SVHN, MNIST, USPS, MNIST-M) — all small-scale, low-resolution. No results are reported on standard UDA benchmarks such as Office-Home or VisDA, and no comparisons are made to established UDA methods (DANN, CDAN, etc.). The paper claims zero-mean regularization "can tighten the error bound" for UDA, but the experiments never validate this on a challenging domain shift. Similarly, the label-noise experiments test only symmetric noise (despite Proposition 3.5 being limited to symmetric noise) and compare only to CE, Focal loss, and GCE — not to modern contrastive-based label-noise methods (e.g., DivideMix, SCAN, SelCL).

- **Theoretical bounds are not connected to experiments.** The UDA bound (Proposition 3.2) depends on eigenvalue gaps $\tilde{\lambda}_d(0)-\tilde{\lambda}_{d+1}(0)$ and the condition $\tau < (\tilde{\lambda}_1(0)-\tilde{\lambda}_d(0))/\tilde{\lambda}_1(0)$, but these quantities are never estimated or discussed empirically. The paper does not verify whether the observed (small) error reductions match the predicted multiplicative form, nor whether the required conditions on $\tau$ actually hold in practice. The theory thus provides plausible intuition but remains untestable from the presented experiments.

- **The supervised SpeCL design choice (including same-class pairs in the negative term) is non-standard and potentially problematic.** Equation 3.8 sums over all $c,k$ pairs, meaning same-class pairs contribute to both the positive and negative and positive terms, creating a contradictory objective (pushing same-class representations to be both similar and opposite). The paper's justification (loss would go to infinity otherwise) is informal and would not satisfy standard analyses of supervised contrastive losses (Khosla et al., 2020), where this issue does not arise. While this design is essential for the spectral decomposition proof of Theorem 3.3, it limits the practical relevance and compatibility with widely used contrastive formulations.

### Minor

- **Gains are small across all settings.** The improvements over $\tau=0$ are typically 1–2 absolute percentage points (Tables 1–3). While consistent, the practical significance is modest, and without comparisons to stronger baselines, it is unclear whether the proposed modification would be preferred over other approaches (e.g., simply using a larger margin, temperature tuning, or standard InfoNCE with supervised positives).

- **No hyperparameter sensitivity analysis for $\tau$.** The paper never plots accuracy as a function of $\tau$ or discusses how to select it. Since the theory requires $\tau$ to satisfy certain eigenvalue conditions (for UDA) or $\tau \geq r\omega$ (for label noise), a sensitivity study would help understand whether performance degrades quickly when $\tau$ is misspecified.

- **The label-noise theory is limited to symmetric noise and class-balanced data.** The paper acknowledges Proposition 3.5 covers only symmetric noise but does not discuss asymmetric or instance-dependent noise, which are more realistic. No experiments test asymmetric noise.

### Trivial

- Figure labels and some inline notation are difficult to parse in the extracted text (e.g., the condition in Theorem 3.1), though these appear to be extraction artifacts rather than author errors.

## Nice-to-Haves

- A sensitivity study plotting accuracy vs. $\tau$ for one or two representative tasks, to demonstrate the range in which the method is effective and how to choose $\tau$ in practice.
- Empirical verification of the uniform-reduction mechanism: e.g., measuring class-mean similarities as $\tau$ increases to confirm the relative gap between correct and incorrect connections grows as claimed.
- Estimation of the eigenvalue gaps from the empirical adjacency matrix on at least one small dataset to test whether the theoretical conditions for Proposition 3.2 are satisfied.

## Removed Points

- *"No comparison to margin-based InfoNCE"* — The paper's claims are about SpeCL, not about InfoNCE. The modification is motivated by a specific spectral decomposition view that applies to SpeCL. Requesting a comparison to margin-based InfoNCE assumes transferability that the paper does not claim and is scope creep.

- *"Table partially garbled"* and *"Theorem 3.1 notation is unreadable"* — These are PDF extraction artifacts, not author errors. The original submission is assumed to have clear tables and notation.

- *"Evaluate on ImageNet"* — The paper's experiments are on moderate-scale datasets; demanding ImageNet experiments for a method that makes modest claims is disproportionate, though larger-scale UDA benchmarks (Office-Home, VisDA) would be reasonable.

- *"The framing that zero-mean regularization implicitly mitigates wrong connections exaggerates what the method does"* — The paper provides formal theory (Theorems 3.1–4, Propositions 3.2, 3.5) backing this claim. The claim is appropriate.

## Novel Insights

The reviewers collectively surface a tension in this paper that is worth highlighting: the theoretical contributions are genuinely clean and insightful (the zero-mean regularization equivalence, the UDA bound tightening, the Neural Collapse connection, the noise-transition-matrix reduction), but the experimental validation is mismatched in ambition. The theory makes predictions about eigenvalue gaps, noise rates, and error bounds that could, in principle, be tested concretely, yet the experiments never attempt to verify any of these predicted mechanisms — they simply report aggregate accuracy numbers on small-scale datasets. This gap between "what the theory says should happen" and "what the experiments actually measure" is the paper's most significant limitation. A stronger version of this work would either (a) empirically validate the mechanism (e.g., by measuring how class-mean angular separation changes with $\tau$, or estimating eigenvalue gaps), or (b) scale up to standard benchmarks (Office-Home, VisDA for UDA; CIFAR-N or Clothing1M for label noise) to demonstrate that the theoretical predictions translate to practically relevant improvements.

## Suggestions

1. **Expand UDA experiments to Office-Home or VisDA** — without this, the claim that zero-mean regularization helps domain adaptation is unsubstantiated at a practically meaningful scale.
2. **Empirically verify the eigenvalue condition** — estimate $\tilde{\lambda}_1(0)-\tilde{\lambda}_d(0)$ for a small dataset and check whether the theoretical $\tau$ condition is satisfied.
3. **Include a $\tau$ sensitivity plot** — show accuracy vs. $\tau$ on at least one task per setting (UDA, noisy labels) to guide practice.
4. **Add asymmetric label-noise experiments** (or at least class-dependent) **label noise experiments** to match real-world conditions.
5. **Acknowledge the non-standard design of supervised SpeCL** more prominently as a limitation — the same-class-in-negative design should be explicitly compared to standard supervised contrastive loss.

## Score and Decision

**Calibration anchors** (all from the human-review corpus):

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NU9AYHJvYe.md` (Optimal Sample Complexity of Contrastive Learning) | 7.50 | Much stronger theoretical contribution with tight bounds and stronger empirical validation (ResNet18 on CIFAR with verification of theoretical predictions). |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibrationNCnZwcH5Z.md` (Non-negative Contrastive Learning) | 5.75 | Similar type of contribution (modification to contrastive learning with theory), but stronger experiments (ImageNet-100) and baselines. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibrationFfu7fTgw.md` (Spectral Contrastive Regression) | 5.00 | Similar spectral/contrastive theme; rejected due to novelty concerns despite decent experiments. Current paper has cleaner theory but weaker experiments. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibrationLZQTFGToA.md` (Contrastive Learning is Spectral Clustering on Similarity Graph) | 4.50 | Accepted but with wide score variance (1–6); had mathematical issues with mathematical rigor. Current paper is theoretically sounder. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration76lvHZqeS.md` (A Unified Framework of Theoretically Robust Contrastive Loss against Label Noise) | 4.40 | Rejected; similar topic (label noise + contrastive), similar weakness of limited experiments and strong assumptions. Current paper has comparably limited experimental validation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibrationwMoE1y0Nb.md` (Understanding Distribution Alignment Through Category Separability) | 3.50 | Weak experiments, narrow setting, limited practical irrelevance. Current paper is clearly stronger in theory and experiment. |

**Relative assessment:** The paper sits around the 4.5–5.5 range. It has cleaner theory and more systematic theoretical analysis than the 4.4 and 3.5 anchors, but its experimental validation is markedly weaker than the 5.75 and 7.5 anchors. The theoretical contributions are real but the experiments are too narrow — small-scale datasets, no SOTA comparisons, no mechanism verification — for the claims to be fully supported. The core idea is interesting and could be a useful contribution with stronger validation, but in its current form the empirical evidence does not match the ambition of the theoretical claims.

**Score: 5.0** — The paper has genuine theoretical value and a clean central insight, but the experimental evaluation is insufficient in scope and depth.

**Decision: Reject** — The paper would need substantially stronger experiments (larger-scale benchmarks, SOTA comparisons, mechanism verification) to warrant acceptance. The theoretical contributions are interesting but not strong enough to compensate for the weak empirical validation; the contribution level is more appropriate for a workshop or a journal extension with additional experiments.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>