Now I have all the evidence I need. Let me construct the consolidated review.

## Summary

This paper addresses the stability-plasticity dilemma in incremental semantic segmentation. Rather than freezing old knowledge (as most prior methods do), the authors propose a dynamic feature-space adjustment framework guided by two principles: *compression* (shrinking and dimensionally reducing feature representations) and *sparsity* (maximizing inter-class separation in a Gaussian mixture feature space). Experiments on VOC and ADE20K across five incremental settings show substantial plasticity gains — up to 11.7% MIoU improvement on the challenging 10-1 VOC setting over prior state-of-the-art.

## Strengths

- **Novel dynamic-adjustment paradigm for incremental segmentation**: Unlike prior methods that freeze old knowledge or apply fixed regularization, this paper proposes to *dynamically* reconstruct the feature distributions of both old and new classes via compression and sparsity constraints. This is a meaningful conceptual departure from the field's dominant stability-first approach, where old knowledge is treated as inviolable.

- **Large and consistent empirical gains**: The method achieves notable improvements across five incremental configurations on VOC (plasticity improvements of 6.2%–11.7%) and on ADE20K (100-5 setting). The gains are consistent across datasets and difficulty levels, and the paper shows benefits in both old-class retention and new-class learning.

- **Ablation studies isolate the contribution of compression and sparsity**: The paper separately evaluates the effect of removing compression or sparsity, and shows that both components contribute to the overall performance. The comparison of weighted vs. attention-based feature fusion provides practical guidance for implementation.

- **Qualitative validation complements quantitative results**: Visualizations of feature distributions (Figure 6) and segmentation outputs (Figure 7) support the claimed mechanism of compact intra-class / sparse inter-class representations, and the authors re-ran comparative visual results using publicly available code.

## Weaknesses

### Major

- **Mathematical motivation (Section 3) is sloppy and overclaimed**: The paper presents Equations (1)–(7) as a "mathematical structural analysis" that "demonstrates the benefit of compression-sparsity." In reality, the derivation from Equation (1) to Equation (2) requires assumptions not stated or justified (the claimed decomposition $\log P(\theta|X) = \log P(X_2|\theta) + \log P(\theta|X_1) - \log P(X_2)$ does not follow from Bayes' rule without additional independence assumptions). The Fisher information relation (Equation 6) is invoked from prior work but never connected to the compression-sparsity design choices. The concluding claim that "compression and sparsity for feature space distribution among different classes can maximize the probability distribution" is asserted, not derived. This does *not* invalidate the method or its empirical results — many papers in this area lack any theoretical motivation at all — but the paper oversells the math as a foundation when it is at best suggestive intuition. The authors should either tighten the derivation or re-frame this section as motivation rather than analysis.

- **Critical implementation detail for constraint enforcement is missing**: Equations (9)–(10) impose hard inequality constraints ($\mathrm{Diam}(F_t^r) < \min \mathrm{D}(\ldots)$ and $\mathrm{D}(\ldots) > \max \mathrm{D}(\ldots)$) but the paper never specifies *how* these constraints are enforced during training. Are $\gamma$ and $\tau$ learned via projected gradient descent? Via soft penalty terms in the loss? Via architectural guarantees? The paper states they "are learnable parameters that satisfy the constraint conditions" without any mechanism. This is a genuine reproducibility gap — a reader cannot reimplement the core method from the description. The supplementary material (mentioned as containing source code) may resolve this, but the description in the main paper is insufficient.

- **Main experimental comparisons lack statistical rigor**: No confidence intervals, standard deviations, or multi-seed results are reported for any method in Table 1 or Table 2. Given that incremental segmentation results are known to be sensitive to random seeds, data ordering, and memory sampling, single-run comparisons are insufficient to establish reliable superiority — especially for large claimed margins. The paper also does not explicitly confirm that *all* baseline results (MIB, SSUL, LGKD, Coinseg, etc.) were obtained under identical conditions (same backbone, optimizer, memory budget, and data ordering). Only Coinseg is explicitly said to be retrained "using the same backbone and memory sampling strategy," and MIB/LGKD visual results used "publicly available codes and training strategies." It is unclear whether the quantitative results cited for baselines are re-run or taken from original papers, which may use different experimental configurations.

### Minor

- **Hyperparameter choice for $\alpha$ and $\beta$ across settings is confusing**: The paper states that $\alpha{=}0.2/\beta{=}0.8$ gives the best results on VOC (including the headline 11.7% gain in 10-1), but then uses $\alpha{=}0.8/\beta{=}0.2$ for the main results "for fair comparisons in a consistent manner." This requires clarification: the 11.7% headline gain specifically uses the *different* hyperparameter setting, meaning the consistent-setting number for 10-1 is actually 9.8%. While the paper is transparent about both values and the choice is not inherently wrong, the presentation can mislead a casual reader into thinking the 11.7% figure reflects the consistent configuration. The paper should explicitly show results for both settings on all configurations.

- **Loss function notation is messy**: Equation (15) contains unclear index ranges (summing $j\neq i$ over $2||C||$ while $i$ runs over $||C||$), and the use of $\widetilde{P}_t^i$ and $P_{t-1}^j$ in a contrastive-style ratio is not clearly explained. The notation appears to be a contrastive formulation but the intent is hard to parse.

- **Feature distribution visualization limitations**: Figure 6 is described as showing more concentrated intra-class and sparser inter-class distributions, but it is not clear whether this is an actual t-SNE/embedding visualization of the model's representations or a schematic diagram. The paper would benefit from empirical feature-space visualizations on real data.

### Trivial

- The term "Gaussian mixture distribution" is used somewhat imprecisely — the method seems to model per-class features as unimodal Gaussians and then compute distances between their peaks, but the "mixture" terminology suggests multiple components per class, which is not consistently operationalized.
- Equation numbering jumps (Equations 9–10 refer to the two constraints, but the text later refers to "Equation (9)" for the fusion weight — this is actually Equation (11)/the weighted combination).

## Nice-to-Haves

- **Per-class breakdown and failure analysis**: The large plasticity gains are impressive, but it would be helpful to see if these gains concentrate in certain classes (e.g., those appearing only in the last step) or are distributed evenly. Reporting per-class IoU for incremental classes would strengthen the analysis.
- **Multi-seed results**: Even 2–3 seeds with standard deviation would substantially increase confidence in the reported margins.

## Removed Points

These points are flagged to be removed; treat them with caution.
- Critic's claim that Equation (5) is "a Taylor expansion of a Gaussian mixture" that "is not standard." **Reason for removal**: Factually wrong. The equation performs a second-order Taylor expansion of $\log P(\theta|X_1)$ around the posterior mode $\theta^*$, which is a standard Laplace approximation. The Gaussian mixture representation (Eq. 3) is of the *log-posterior*, and a Taylor expansion of the log-posterior is standard.
- Critic's claim that the loss function involves "division of a scalar by a vector norm, exponentiation of a vector." **Reason for removal**: The expression $\frac{\widetilde{P_t^i}}{||\widetilde{P_t^i}||}$ is a unit vector, and its dot product with another unit vector is a scalar; $\exp(\text{scalar})$ is standard. The notation is messy but mathematically valid.
- Critic's claim of "mismatched distributions" in the contrastive loss denominator. **Reason for removal**: Contrastive losses by design contrast different representations (here $\widetilde{P}_t^i$ against $P_{t-1}^j$). This is the intended behavior, not an error.
- Critic's claim about "two peaks per class" being inconsistent. **Reason for removal**: The paper models each class's feature distribution as a Gaussian Mixture Distribution which can naturally have multiple modes; $P_1^{C_i}$ and $P_2^{C_i}$ refer to the farthest-separated peak points within a class's GMD.
- Critic's phrasing about "not yet released" or "cannot be independently verified" regarding cited entities. **Reason for removal**: Per the review rules, all cited references are assumed to exist as stated.
- All pure formatting/style nitpicks about table readability, garbled text, line breaks, etc. **Reason for removal**: These are parser artifacts, not author errors.

## Novel Insights

The harsh critic's observation that the mathematical section (Section 3) is a sequence of identity-like equations that are *asserted* to support the method rather than *derived* to do so is genuinely insightful. This is not merely a presentation weakness — it reveals a pattern in which the paper overclaims the rigor of its motivation. The critic's detailed breakdown of why Equation (2) does not actually follow from Equation (1) without hidden independence assumptions identifies a real mathematical error that the paper should correct (or at minimum, explicitly state its assumptions). However, the critic's conclusion that this "invalidates a core pillar" overreaches: the paper's primary contribution is the empirical demonstration of dynamic feature adjustment, not a formal theorem. The most valuable cross-cutting insight from reconciling the reviews is that the paper sits uncomfortably between two modes — it tries to be a theoretically-motivated paper (Section 3) while being an empirically-driven systems/methods paper (Sections 4–5) — and it would be stronger if it committed fully to one framing.

## Suggestions

1. **Re-frame Section 3 explicitly as intuition/motivation, not rigorous analysis.** Clarify the assumptions needed for Equation (2) or remove it entirely. Drop the claim of "mathematical analysis demonstrating the benefit" and replace with "the following probabilistic perspective provides intuition for why compression and sparsity may help."
2. **Specify how the constraints in Equations (9)–(10) are enforced.** State whether $\gamma$ and $\tau$ are learned with projected gradient descent, Lagrangian relaxation, soft penalties, or another mechanism. This is critical for reproducibility.
3. **Add multi-seed results** (at least 3 seeds with mean and std) for the main tables, or at minimum for a representative subset of settings.
4. **Clarify which baselines were re-run and under what conditions.** A table footnote or experimental section stating "All baseline results are re-run using our backbone and data pipeline" or "Baseline results are cited from original papers; see Appendix for configuration details" would resolve this concern.
5. **Show results for both $\alpha/\beta$ settings on all configurations**, and be explicit about which setting produces each reported number.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>