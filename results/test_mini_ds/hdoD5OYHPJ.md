Now I have a solid calibration. Let me finalize my review.

**Round 1 bracket**: I placed the paper between 4 and 7 based on initial calibration.

**Round 2 narrowing**: After reading CARPRT (5.75, Reject), DOTA (6.00, Reject), InCPL (5.00, Reject), RLCF (6.67, Accept), and Synergy & Diversity (6.25, Accept), the most directly comparable paper is CARPRT (5.75) — both address prompt reweighting for zero-shot CLIP classification, both show similar magnitude of gains (~0.5% average), and both share similar weaknesses (hyperparameter sensitivity, marginal gains on standard benchmarks, computational cost concerns). AutoCLIP is slightly cleaner than CARPRT (no pseudo-label dependency) and has more extensive evaluation (990 settings vs. CARPRT's), which puts it around the same level or slightly above. It is clearly stronger than InCPL (5.00) which had methodological problems. It is weaker than RLCF (6.67) which covers 3 tasks with a more novel framework.

Final score: **5.5**, Decision: **Reject** — solid paper with a clean method and extensive evaluation, but the modest gains, the β tension, and the absence of runtime characterization and ZPE comparison prevent a clear accept.

Now let me write the final review.

---

## Summary
AutoCLIP proposes a test-time method for per-image weighting of prompt templates in zero-shot classification with VLMs. Instead of averaging all prompt templates uniformly, AutoCLIP takes a single gradient step on a logsumexp objective in embedding space to assign higher weights to templates whose class descriptors are more similar to the image. The step size is automatically determined via bisection on a target entropy rate (β=0.85), so the method introduces only one hyperparameter. Experiments across 990 settings (8 datasets, 6 models, 3 prompt strategies) show an average gain of +0.45pp, with improvements on 85% of settings and up to +3pp.

## Strengths

- **Extremely thorough empirical evaluation**: The paper evaluates AutoCLIP across 990 combinations (8 datasets × 6 VLMs × 3 prompt strategies × multiple K values), which is genuinely impressive. This breadth directly supports the claim of broad applicability and gives confidence that the aggregate statistics (+0.45pp average, 85% improvement rate) are reliable.

- **Clean, well-motivated method**: AutoCLIP's intuition — that some prompt templates describe a given image better than others — is clearly illustrated (Figure 1), and the mathematical formulation (gradient ascent on logsumexp, entropy-controlled step size via bisection) is presented cleanly. The closed-form gradient (Section 3.3) enables deployment without autodiff, a practical nicety.

- **Mechanistic insight from controlled experiment**: Section 5 simulates synthetic embeddings with controlled "entanglement" and "instance noise" parameters, showing that AutoCLIP outperforms mean/max aggregation except at extreme low-entanglement + high-noise settings. This provides a testable explanation for the empirical pattern that weaker VLMs benefit more from AutoCLIP.

- **Semantic interpretability of learned weights**: Figure 4 shows that templates like "A drawing of…" receive lower weights on Food101 (a photo dataset) while "A photo of…" receives higher weights, confirming that the learned weights align with intuitive visual semantics.

## Weaknesses

### Fatal
None.

### Major
- **The "essentially no free hyperparameters" claim is overstated.** The paper sets β=0.85 as default (Section 3.4) but then in Section 4 recommends β=0.7 "for future work" because it "performs favorably" on average. This creates a direct tension: if the default needs changing after the fact, β is functionally a tunable hyperparameter. The paper attempts to finesse this by showing stability in [0.7, 0.9], which is reasonable, but the framing in the introduction ("comes essentially without free hyperparameters") is stronger than the evidence supports. This is the paper's most significant weakness because it undermines the central selling point of being a drop-in replacement.

- **No runtime or memory overhead characterization.** The paper repeatedly claims "minor additional computation overhead" and "few lines of code," but never measures wall-clock time, relative FLOPs, or memory usage. AutoCLIP requires: (a) computing a gradient (closed-form or autodiff) involving terms over all K templates and C classes, (b) softmax over K, and (c) a bisection loop to find α. For K=500 and C=1000, this is non-negligible compared to the baseline single forward pass. Without any measurements, the "minor overhead" claim is unsubstantiated, and the comparison to TPT methods (which the paper argues are more expensive) cannot be grounded.

### Minor
- **Gains on standard large-scale benchmarks are very small.** On ImageNet, ImageNetV2, and ImageNet-R with large models (ViT-L/14), improvements are +0.3%, +0.4%, +0.4% respectively (Table 1). On ImageNet-C, the average gain is +0.11% and negative for ViT-L/14 variants. The headline "up to 3 percent point" comes from Oxford Pets with a small model. The paper reports these numbers transparently, but the framing ("vast majority of settings," "up to 3%") obscures that on many practically relevant settings the gains are marginal. A practitioner deciding whether to adopt AutoCLIP needs a clearer cost-benefit characterization.

- **No quantitative comparison with ZPE (Allingham et al., 2023).** ZPE is identified as the most related prior work (also prompt weighting in embedding space), but the paper dismisses it as requiring a batch and source distribution without demonstrating that these requirements are actually necessary for a fair comparison. Even a brief experiment showing that ZPE fails without a batch — or a single-image adaptation — would clarify AutoCLIP's advantages. As it stands, the positioning against ZPE is asserted but not evidenced.

### Trivial
- The paper lacks a dedicated limitations section, which would be useful given the β sensitivity, EuroSAT degradation, and computational cost considerations.
- The line "models like CLIP scale e^(xd) by a learned temperature τ" (Section 3.2) is slightly unclear about whether AutoCLIP re-uses the same temperature from the VLM or estimates it separately.

## Nice-to-Haves
- A per-dataset breakdown of β sensitivity (beyond the aggregate in Figure 3) would help assess whether β=0.7 is universally preferable or dataset-dependent.
- Reporting standard deviations (not just standard errors) in main tables would help assess the significance of small gains.

## Removed Points
These points from the inputs were filtered as they are either factually incorrect, speculative, or nitpicks that do not affect the core assessment:

- **"The paper should include a single-image variant of ZPE"** — This is speculative; the critic suggests adapting ZPE to a setting its authors explicitly designed against (single-image, source-free). This is a "nice-to-have" comparison, not a necessary gap, since the paper clearly differentiates its setting from ZPE's.
- **"Missing appendix content / proofs"** — The parser strips appendix material; these exist in the original submission.
- **Claim that the objective "is not directly based on statistics"** — The paper defines its objective clearly (logsumexp of class-image similarities). This is a semantic quibble.
- **Formatting nitpicks** — Parser artifacts, not author errors.
- **Generic strength claims about "addressing an important problem"** — Too vague to retain as concrete strengths.
- **"Missing standard deviations in tables"** — Standard errors over 7 runs are reported; this matches the paper's stated protocol.
- **"No code release mentioned"** — Code release is not required for review and the paper is self-contained.

## Novel Insights
The harsh critic's point about the β=0.85 vs. β=0.7 tension is genuinely insightful: it reveals a credibility gap in the paper's "hyperparameter-free" framing. The paper's own ablation data show that the optimal β varies by dataset, yet the introduction claims the method has "essentially no free hyperparameters." The controlled experiment (Section 5) is another novel observation worth highlighting — by disentangling "class-prompt entanglement" from "instance noise," it provides a mechanistic hypothesis for why AutoCLIP helps smaller VLMs more than larger ones. This goes beyond the typical empirical sweep and offers a testable framework for understanding when per-prompt weighting will be beneficial.

## Suggestions
1. **Address the β tension head-on.** Either adopt β=0.7 as the default everywhere (and update the narrative accordingly), or remove the "no free hyperparameters" language. Show that one β works robustly across all datasets with no more than a small degradation on any single dataset.
2. **Add runtime measurements.** Report relative wall-clock time for at least two settings (K=80 CLIP templates, K=500 WaffleCLIP) — this is a 1-hour experiment that would substantially strengthen the paper.
3. **Include a ZPE adaptation comparison.** Run ZPE's weighting approach on single images (even if suboptimal) and report results. If it collapses to uniform, demonstrate this empirically.
4. **Add a limitations paragraph** explicitly discussing β sensitivity, EuroSAT degradation, and when AutoCLIP may not help.

## Score and Decision

**Round 1 bracket**: [4, 7]. Queried three bands: weak (high_score=3, returned papers at 2.0-3.0), middle (low_score=4, high_score=7, returned papers at 4.0-6.25), and strong (low_score=8, returned papers at 8.0). The paper clearly sits in the middle band.

**Round 2 narrowing**: Queried the [4.0, 6.0] and [5.5, 7.5] bands. Key anchors:
- CARPRT (5.75, Reject) — Most directly comparable (prompt reweighting for zero-shot CLIP). Similar magnitude of gains (~0.5%), similar hyperparameter sensitivity concerns. AutoCLIP has slightly cleaner methodology (no pseudo-labels) and broader evaluation, but same class of weaknesses. → AutoCLIP ≈ CARPRT or slightly better.
- InCPL (5.00, Reject) — Had methodological flaws (information leakage). AutoCLIP is clearly stronger. → AutoCLIP > 5.00.
- DOTA (6.00, Reject) — TTA method, comparable quality but more ambitious. AutoCLIP is slightly less ambitious → AutoCLIP ≈ 5.5–6.0.
- RLCF (6.67, Accept) — Broader coverage (3 tasks), more novel framework. AutoCLIP is weaker → AutoCLIP < 6.67.

**Final score**: 5.5. Positioned between CARPRT (5.75) and InCPL (5.00). The paper has a clean method and extensive evaluation but is held back by overstated claims about hyperparameter-freeness, absence of runtime measurements, and modest gains on standard benchmarks. This is a borderline paper; the core idea is sound and well-evaluated, but the presentation overreaches in ways that would need correction before acceptance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>