Now let me run the calibration search to bracket the score.Let me read the most topically similar middle-range anchors in detail.Now let me do Round 2 narrowing within the 4-6 bracket.Now I have enough information to write the final review. Let me compose it.

---

## Summary

This paper proposes correcting the well-known complexity bias of normalizing flow (NF)-based OOD detection by generating low-complexity synthetic outliers from in-distribution data and training the model with an adversarial softplus objective that penalizes high likelihoods on those outliers. The method is applied to image benchmarks (CIFAR-10/100, iSUN vs. SVHN/LSUN/CelebA), high-dimensional real-world image datasets (Chest X-ray, RealBlur, KonIQ-10k), and a small text experiment on IMDb. The core argument is that synthetic low-complexity samples can substitute for real labeled outlier data and correct the NF bias diagnosed by Osada et al. (2024) and Serra et al. (2020).

---

## Strengths

- **Empirical bias correction is visibly demonstrated (Figure 3):** Scatter plots of image complexity C(x) vs. latent likelihood p_Z(z) show that before training, lower-complexity OOD samples (SVHN) cluster at higher likelihoods than ID samples (CIFAR-10). After synthetic outlier training, this inversion is visibly reduced and ID/OOD separation improves. This directly supports the paper's central claim.

- **Softplus loss removes manual threshold (Section 2.3):** The paper shows analytically that the softplus-penalized OOD loss yields a gradient factor p/(1+p) that saturates smoothly as p → 0, avoiding the explicit threshold clamping required by Schmier et al. (2022). This is a concrete and principled improvement over the only prior NF-specific OOD training objective.

- **Synthetic outliers match or exceed real outliers in multiple settings (Tables 2 and 3):** On CIFAR-10 vs. SVHN, synthetic outliers (Gaussian blur + CCM) yield 96.99% AUROC versus 93.27% for real outliers. The result holds across multiple ID/OOD pairings in both tables, making this one of the paper's most concrete findings—even if the real outlier source is underspecified (see weakness).

- **Plug-and-play improvement on established NF architectures (Table 5):** CS-Flow AUROC increases from 87.7% to 92.3% and FastFlow from 90.3% to 93.4% on the Chest X-ray dataset. This demonstrates the method does not require re-architecting existing flows and is deployable on top of current best-of-breed NF models for industrial/medical imaging.

- **Lipschitz constant increase corroborated empirically (Table 4):** Training with synthetic outliers raises the estimated Lipschitz constant by roughly an order of magnitude (e.g., 0.99 → 34.26 on CIFAR-10), consistent with the hypothesis from Osada et al. (2024) that higher Lipschitz constants improve OOD discrimination for low-complexity inputs.

---

## Weaknesses

### Fatal

None.

### Major

- **No comparison to non-NF baselines** — The paper frames its contribution as a broadly useful fix for OOD detection, but exclusively compares within the NF family (MLE baseline and real outlier variant). The broader OOD detection literature includes energy-based scoring, Mahalanobis distance on pretrained features, and virtual outlier synthesis in feature space (VOS, Du et al., 2022, which is cited in the introduction). Without at least one representative comparison from outside the NF family on the core benchmark pairs (CIFAR-10 vs. SVHN, CIFAR-10 vs. LSUN), the reader cannot assess whether the repaired NF closes or merely narrows the gap with what already works. This gap makes it impossible to evaluate the practical significance of the contribution.

- **Real outlier baseline is underspecified** — Section 3.1 identifies the key comparison as MLE vs. real outliers (RO) vs. synthetic outliers: "dual likelihood training with a few real outliers (RO) (specifically comprising [10]% of the ID data samples)." The paper never states which dataset these real outliers are drawn from. If they are sampled from the evaluation OOD datasets (e.g., SVHN, LSUN), the comparison is an oracle upper bound; if they come from a disjoint OOD pool, the comparison means something different. The headline claim that "synthetic outliers match real ones" rests on this unspecified comparison. This is not a formatting artifact — it is a methodological omission that directly affects how the result should be interpreted.

- **Text experiments are too thin to support "broad applicability" claim** — Section 3.3 uses only 1,000 IMDb training samples, tests against four OOD text corpora, includes no contemporary text OOD detection baseline (only the MLE NF trained on the same data), and reports no variance. Critically, the text outlier synthesis (sentence length filtering + WordNet synonym replacement) is never verified to actually produce lower-complexity text in the operationalized sense used throughout the paper (compression ratio). Without measuring whether the synthetic text has lower C(X') than the ID text, the text method is not connected to the hypothesis that motivates the entire approach. The conclusion's claim of "broad applicability across tasks" is not supportable by these experiments alone.

### Minor

- **Lipschitz analysis is post-hoc correlation, not causal derivation** — Section 2.1 states: "we *hypothesize* that the introduction of synthetic outliers has an influence on the local Lipschitz constant L_A, increasing its value." The hypothesis that a higher L_A leads to more dispersed latent representations for low-complexity inputs comes from Osada et al. (2024); the paper then shows L_A increases empirically. This is a correlation check that runs in the right direction, not a derivation of why the proposed training procedure causes this change. The Lipschitz analysis would be more convincing if it showed the gradient norm increase is concentrated on low-complexity inputs specifically (where the hypothesis predicts the effect), not uniformly across the input distribution — a test achievable within the existing experimental setup.

- **MVTecAD experiments referenced but absent** — Section 3.2 ends mid-sentence: "We also conducted experiments on the MVTecAD dataset (Bergmann et al." — no results are presented, and Table 5 covers only Chest X-ray, RealBlur, and KonIQ-10k. This appears to be an incomplete section. The reference should either be completed with results or removed.

- **No variance reporting** — All evaluations use 1,000 randomly sampled ID and 1,000 OOD test samples. For AUROC and FPR95 at this evaluation set size, sampling variance can be non-trivial. No standard deviations or multiple-run statistics are reported anywhere in Tables 2–6. This makes it impossible to assess whether differences between ablation variants (e.g., Gaussian blur alone vs. CCM alone vs. combined) are reliable or incidental.

### Trivial

- **Softplus gradient saturation not investigated in practice** — Mathematically, the gradient factor p/(1+p) vanishes for synthetic outliers that the model has already pushed to very low likelihood early in training. Whether this is practically consequential (or whether early-training synthetic outliers are already at moderate likelihood) is not examined. A brief remark would close this question.

---

## Nice-to-Haves

- A direct ablation comparing Serra et al.'s complexity-adjusted scoring (same MLE-trained NF, only the inference score changing) against the proposed training procedure with plain NLL scoring would isolate how much of the improvement comes from training correction versus post-hoc complexity normalization. Currently, the best-performing variants combine both, conflating the two contributions.
- For the augmentation-then-blur pipeline (Section 2.2.1), an ablation showing blur-only versus augmentation-only versus combined would clarify whether the CCM augmentation step contributes meaningfully or whether the complexity reduction from blur alone is sufficient. The current Table 2 shows both separately but does not control for the ordering.
- Showing the Lipschitz gradient norm increase is specifically concentrated on low-complexity inputs (rather than uniformly across the distribution) would considerably tighten the mechanistic story in Section 2.1.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Enriching semantic diversity through augmentation before blurring is not rigorously justified"** (Harsh Critic) — The paper provides a qualitative rationale ("enriches semantic diversity and broadens the range of outliers"). While a rigorous justification is absent, this concern is presentational and does not threaten the method's core claim.

- **"Comparison against non-NF methods is unfair if asymmetry favors baseline"** — Removed per hard rules; any asymmetry in comparisons here (if it existed) would favor the *alternative methods*, which would actually strengthen, not weaken, the paper's claim.

- **"Broad applicability is a strength"** (Strength Finder) — Removed because it directly conflicts with the verified Major weakness that the text experiments are thin and the text synthesis is unverified. A strength that conflicts with a verified weakness is removed per rules.

- **"Softplus ablation request vs. Schmier's clamping"** (Harsh Critic) — Retained only as Trivial/Nice-to-Have; the reviewer framed it as a major gap but it is not — the paper already analytically establishes the smoothness property and contrasts it qualitatively with Schmier et al.

- **Requests for missing appendix proofs, hyperparameter details, or complete training logs** — Removed per hard rules (parser strips appendices; these exist in the original submission).

---

## Novel Insights

The most substantive insight emerging from this review — beyond the paper's own contributions — is the observation that the softplus objective's gradient vanishing for outliers already at low likelihood is a structural trade-off that may not have been adequately considered: the same property that ensures numerical stability during late training may cause the training signal from well-separated synthetic outliers to decay prematurely, concentrating all learning pressure on the marginal cases. This is not demonstrated to be a problem empirically, but it is a non-obvious consequence of the design choice that is worth tracking in follow-up work.

---

## Suggestions

1. **Specify the real outlier dataset** in the camera-ready: state explicitly which dataset RO samples are drawn from, whether any samples overlap with OOD test sets, and how they were selected. This is a single sentence that would substantially change how Tables 2 and 3 are read.
2. **Measure synthetic text complexity**: for at least one text OOD pair, compute C(X') (using gzip, as defined in Definition 1 for text) on the synthetic text outliers and verify it is lower than C(X) for the ID IMDb data. Without this measurement, the text method is not connected to the paper's own complexity definition.
3. **Add one non-NF baseline** on the core CIFAR-10 vs. SVHN pair to contextualize where the repaired NF sits relative to alternatives that do not suffer from the bias in the first place.
4. **Complete or remove the MVTecAD sentence** in Section 3.2.
5. **Report standard deviation** across at least 3 random draws of the 1,000-sample evaluation subsets, or report results on the full test set, so readers can assess reliability of differences between ablation variants.

---

## Score and Decision

**Round 1 — Bracket:** Topically similar papers retrieved:
- rcmhydaEJp (Flow-based imputation, avg 3.0): Weak submission on NF+OOD — not a clean fit but establishes a low floor.
- jQ596tXT3k ("Likelihood Peaks," avg 5.67): Proposes principled OOD detection via probability mass and LID estimation; more theoretically grounded than the paper under review.
- Go8hf9wKJx (DOG, avg 4.25): Synthetic outlier generation via diffusion models; more sophisticated approach, comparable experimental scope issues.
- gRXLa6LS3J (FoMo-OD, avg 5.75): Zero-shot OD via synthetic pretraining; different paradigm.
- 3a505tMjGE (AVOID, avg 6.0): Theoretically rigorous correction of DGM overestimation in OOD detection; stronger theoretical grounding.
- am7BPV3Cwo (ImOOD, avg 5.75): Statistical framework for imbalanced OOD; broader experimental evaluation.

**Initial bracket: 4.0–5.5.**

**Round 2 — Narrowing:**
- AVOID (6.0): Provides a full theoretical derivation of the root cause of overestimation, proposes a post-hoc and training-time fix, includes ablation studies. More theoretically rigorous, more comprehensive experimental comparison. The paper under review is less theoretically grounded and lacks comparisons outside the NF family — clearly *below* AVOID.
- am7BPV3Cwo/ImOOD (5.75): Has statistical derivation of a bias term, unified plug-in framework evaluated against several SOTA OOD methods on three benchmarks. Broader comparison scope than the paper under review. Paper under review is below this level.
- jQ596tXT3k (5.67): More principled explanation, SOTA results relative to comparable flow-based benchmarks. Paper under review is comparable or slightly below this on theory; on practical application it covers more dataset types.
- Go8hf9wKJx/DOG (4.25): Uses diffusion models for sophisticated outlier generation but has presentation issues and only small-scale results. The paper under review is cleaner and addresses a specific verified failure mode more directly; it sits at or slightly above DOG.

**Conclusion:** The paper under review is similar in overall quality to DOG (4.25) — addresses a real problem, shows consistent gains, but lacks critical comparisons and has an incompletely validated multi-modal claim. The one distinguishing factor in the paper's favor is that the method is more theoretically grounded in the Osada et al. hypothesis than DOG's approach, and the image experiments are more systematic. Slightly above DOG, I place the paper at **4.5**.

**Axis evaluation:**
- *Originality*: Moderate. The method (bias correction via low-complexity synthetic outliers + softplus loss) is a meaningful but incremental extension of prior work (Serra et al., Osada et al., Schmier et al.). The synthesis strategy (Gaussian blur + standard augmentation) is straightforward.
- *Importance*: Moderate. The complexity bias in NFs is a documented and real problem; fixing it has practical value for anomaly detection in imaging pipelines.
- *Claims vs. evidence*: Weak in two places. The "broad applicability" claim is unsupported by the text experiments. The "comparable to real outliers" claim rests on an unspecified comparison.
- *Experimental soundness*: Acceptable within the NF family, poor with respect to the broader OOD landscape.
- *Writing clarity*: Adequate. The MVTecAD incomplete sentence and unspecified RO source are notable gaps.
- *Value to the community*: Limited without non-NF comparisons; the community needs to know whether fixed NFs compete with energy-based or feature-space methods on the same benchmarks.

| Anchor | Avg Human Score | Round | Comparison |
|---|---|---|---|
| rcmhydaEJp (Flow imputation) | 3.0 | R1 | Clearly weaker submission; paper is above this |
| Go8hf9wKJx (DOG) | 4.25 | R1/R2 | Closest peer; paper is slightly stronger in focus and motivation |
| SabhfFUfA1 (LPath VAE) | 4.67 | R2 | Paper is comparable or slightly below |
| LjygLD0AkT (LPath NF) | 5.00 | R2 | Stronger theoretically; paper is below |
| jQ596tXT3k (Likelihood Peaks) | 5.67 | R1/R2 | More principled analysis; paper is below |
| am7BPV3Cwo (ImOOD) | 5.75 | R2 | Broader comparison scope; paper is below |
| gRXLa6LS3J (FoMo-OD) | 5.75 | R1 | Different paradigm; paper is below |
| 3a505tMjGE (AVOID) | 6.00 | R2 | Stronger theory and ablation; paper is clearly below |
| SctfBCLmWo (Dataset Bias) | 8.0 | R1 | Strong analysis paper; paper is well below |

**Round 1 bracket: 4.0–5.5. Round 2 narrowing: 4.25–5.0. Final score: 4.5.**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>