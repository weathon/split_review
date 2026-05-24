Now I have a clear picture of the calibration landscape. Let me write the final consolidated review.

---

## Summary

This paper proposes TAK (Task Arithmetic with KFAC regularization), a method that links representation-drift regularization in task arithmetic to the generalized Gauss-Newton (GGN) curvature matrix, then approximates it via Kronecker-factored approximate curvature (KFAC). The key idea is that, under model linearization, the per-task representation drift penalty reduces to a quadratic form of the Jacobian Gramian, which is exactly a GGN matrix. By pre-computing KFAC factors for each task, the method avoids needing other tasks' data during training. An aggregation heuristic (Eq. 8) merges per-task Kronecker factors into a single surrogate, achieving O(1) complexity in the number of tasks. The paper evaluates TAK on vision (8 Vision benchmark with CLIP ViT-B/32, B/16, L/14) and language (T5-base on 6 NLU tasks), covering task addition, negation (unlearning), and localization, with extensive ablations on sample size, Monte Carlo variants, memory compression, and training overhead.

## Strengths

- **Dataless regularization matches or exceeds data-dependent state-of-the-art.** Table 1 shows TAK achieving 86.0% absolute accuracy on ViT-B/32 (best α) versus 85.6% for τJp (Yoshida et al., 2025), which requires full external task data. TAK accomplishes this without accessing other tasks' data, directly supporting the core claim of a practical dataless regularizer. The advantage holds across ViT-B/16 and ViT-L/14 as well.

- **O(1) storage and runtime via Kronecker accumulation.** Table 3 demonstrates that the accumulated regularizer (Eq. (8), complexity O(1)) performs within 0.5–0.8 absolute points of the naïve O(T) multi-task objective on ViT-B/16 and T5-base. This is a concrete algorithmic advantage: storing one set of Kronecker factors rather than T sets.

- **Robustness to task-vector rescaling eliminates validation-data dependence.** Figure 4a shows that TAK with α=1 achieves 85.8% absolute accuracy on ViT-B/32, virtually tied with its tuned best (86.0%). In contrast, unregularized Linear FT varies by ~2 points across the same α sweep. This means TAK removes the need for held-out tuning of the scaling coefficient — a practical advantage in federated or privacy-sensitive settings.

- **Compelling task localization across all eight tasks.** Figure 5 plots the distribution of ‖J_θ f(x,θ₀) τ_t‖₂² for inlier vs. outlier examples. Under TAK, outlier scores concentrate near zero for every task, whereas Linear FT shows wide, overlapping distributions. This directly visualizes the disentanglement property claimed in Sec. 1 and suggests downstream utility for out-of-distribution detection.

- **Efficient KFAC estimation with minimal data and computation.** Figure 7a shows that 128–256 examples and a single Monte Carlo sample saturate downstream accuracy. Figure 6b reports total pre-computation time as 3.9 minutes for all eight vision tasks (MC=1), orders of magnitude faster than the exact Botev approach (198.7 min). Memory compression (Fig. 7b) reduces storage from ~550 MB to ~70 MB with only ~1-point accuracy drop, making the method practical at scale.

- **State-of-the-art in task negation (unlearning).** Table 2 reports that TAK drives target-task accuracy to 3.4% (strongest forgetting) while preserving control-task accuracy at 62.4% on ViT-B/32, outperforming τJp (6.7% target, 60.8% control) without requiring access to the control dataset (ImageNet). This is particularly striking because τJp's regularization requires the full control dataset.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The "dataless" framing is slightly overclaimed.** The method requires 128–256 examples per task to pre-compute the KFAC factors (acknowledged in Fig. 7a: "using 128–256 examples is already sufficient"). The title, abstract, and body repeatedly use "dataless" and "without requiring access to external data." The method is more accurately described as *data-efficient* or *privacy-preserving with a small one-time sample overhead* — it is not dataless in the literal sense that no data is ever needed. While the paper is transparent about the small sample requirement, the terminological mismatch could mislead practitioners who expect zero data dependence. The method's value remains high — reducing data needs from full datasets to a few hundred examples — but the framing should be calibrated.

- **The non-linear regime extension lacks theoretical grounding.** The paper states "although our regularization is not theoretically exact in the non-linear regime" and relies on attention-only fine-tuning (Jin et al., 2025) to induce "approximately linear behavior." However, no bound on the linearization error is provided, no analysis of how the regularizer's effectiveness correlates with non-linearity, and no discussion of conditions under which the approximation would break down. The empirical results (Fig. 2, right) show it works, but the claim of "extending to non-linear regimes" is only partially supported by the evidence.

- **No discussion of failure modes or limitations.** The paper does not address when the linearization assumption (Jacobian at θ₀) might degrade — e.g., for tasks requiring large parameter updates, low-resource domains, or large distribution shifts relative to pre-training. Adding a brief limitations paragraph would strengthen the paper.

- **The aggregation heuristic (Eq. 8) lacks theoretical motivation.** Approximating a sum of Kronecker products with a Kronecker product of sums is not generally correct. The paper calls it a "heuristic" and provides empirical validation (Table 3, showing marginal gaps), which is sufficient to support the claim. However, a brief discussion of when this approximation might break down (e.g., when task factors are highly dissimilar) would strengthen the presentation. The current text introduces the heuristic without commentary until the empirical section.

### Trivial
- The paper mentions Exact and MC variants of KFAC but could more clearly state upfront that the main results use MC with M=1 (this is inferable from Fig. 6b but not stated in the experiment setup).

## Nice-to-Haves

- **Quantitative task localization metric:** The histograms in Fig. 5 are compelling but would be strengthened by a quantitative detection metric (e.g., AUROC for inlier-vs-outlier discrimination) to connect more directly to the OOD detection literature.
- **Ablation on task weighting:** The paper weights tasks by dataset size (λ_t ∝ |D_t|). An ablation on uniform vs. size-based weighting would help assess sensitivity to this choice, particularly for imbalanced dataset sizes.
- **Comparison with a simpler baseline:** Regularizing with the unweighted sum of squared Jacobian norms (a degenerate KFAC with identity factors) would help isolate the benefit of KFAC's structured approximation over a uniform L2 penalty on gradients.

## Removed Points

- *"Fig. 4a comparison is not apples-to-apples"* — The paper also provides Fig. 4b where all methods use linearized checkpoints, making the comparison fair. The authors acknowledge both figures. The criticism is addressed by the paper itself. **Removed** because the paper already provides the more honest comparison.
- *"Missing confidence intervals"* — Single-run evaluation on large-scale benchmarks is standard in this literature. **Removed** as a methodologically inappropriate demand.
- *"Missing related work"* — Rule: do not mention missing related works. **Removed.**
- *"Squared loss choice should be more explicitly stated"* — The paper states this clearly in the main text (Sec. 3.2, p. 3): "If we choose squared error... the GGN becomes the Jacobian Gram matrix exactly." **Removed** because it is already in the main text.
- *"Unclear which KFAC variant is used"* — This is partially inferable from the paper (MC with M=1 from Fig. 6b). Moved to Trivial.
- *"Formatting, typos, grammar"* — Parser artifacts, not author errors. **Removed.**
- *Generic strengths from Strength Finder* — None of the listed strengths were generic; all were concrete and paper-specific. **All kept.**

## Novel Insights

The key insight that emerges from reading the paper alongside the τJp (Yoshida et al., 2025) anchor is that representation-drift regularization in task arithmetic is *not fundamentally about data* — it is about curvature. Both methods regularize via the Jacobian Gramian, but τJp materializes this through data-dependent computation, while TAK recognizes the Gramian as a GGN matrix and exploits decades of curvature approximation research (KFAC) to make it dataless. This reframing is principled and productive: it immediately supplies compressed representations, O(1) aggregation, and the ability to share curvature *instead of* data. The paper thus transforms an engineering problem (how to regularize without data) into a well-studied approximation problem (how to compress the GGN), opening the door for future work to plug in more sophisticated curvature approximations as they become available.

## Suggestions

1. **Calibrate the "dataless" terminology** in title/abstract to "data-efficient" or "privacy-preserving (requires a small one-time sample)," and explicitly state the maximum sample size (currently 128–256 examples per task) in the contribution list.

2. **Add a brief limitations paragraph** discussing when the linearization assumption at θ₀ may break down (large distribution shift, low-resource domains, large parameter changes) and how this would affect TAK's effectiveness.

3. **Provide quantitative detection metrics** (e.g., AUROC) for the task localization analysis in Fig. 5 to make the OOD-detection potential more concrete.

## Score and Decision

### Calibration Protocol

**Round 1 — Bracketing:**
- Weak band (< 3.5): Continual-learning papers at 1.5–3.0 — clearly lower quality and relevance.
- Middle band (3.5–7.5): *Mastering Task Arithmetic: τJp* (6.0, accepted), *Leveraging Submodule Linearity* (6.0, accepted), *Fine-Tuning Attention Modules Only* (6.25, accepted), *SUPERMERGE* (4.33, rejected), *Task Arithmetic in Trust Region* (5.75, rejected).
- Strong band (> 7.5): *Second-Order Perspective on Model Compositionality* (7.5, accepted), *Unlocking the Power of Function Vectors* (9.0, accepted) — broader or more theoretical contributions.

**Round 1 bracket:** Based on the strong empirical evaluation and clear contribution, the plausible range is 6.0–7.5.

**Round 2 — Narrowing (within the bracket):**
- *τJp* (6.0, accepted): Direct competitor. TAK improves on τJp by eliminating its core weakness (data dependence) while maintaining or exceeding accuracy, adds O(1) complexity, and provides more extensive ablations. TAK is clearly stronger.
- *Fine-Tuning Attention Modules Only* (6.25, accepted): Similar domain. TAK has more comprehensive evaluation (vision + language, addition + negation, extensive ablations) and a more principled contribution (curvature framing vs. empirical observation about attention modules). TAK is stronger.
- *Second-Order Perspective* (7.5, accepted): More theoretical paper about model compositionality. TAK has stronger empirical evaluation but lighter theory. Comparable in overall quality but slightly different type of contribution. TAK is slightly below this anchor.

**Final position:** The paper sits between the 6.0–6.25 task-arithmetic anchors (which it clearly surpasses) and the 7.5 theoretical anchor (which it approaches but does not exceed). The weaknesses are genuine but minor — they do not threaten the core contributions. The paper's novelty (linking representation drift to curvature approximation), thoroughness, and practical impact warrant a score above the 6.0–6.25 band but below the 7.5 theoretical paper.

**Score: 7.0 / Decision: Accept**

### Calibration Table

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| WM5G2NWSYC (Projected Subnetworks) | 2.00 | 1 | Much weaker; tangential topic |
| ZyMXxpBfct (Forward Explanation) | 1.50 | 1 | Much weaker; not relevant |
| HCCkCjClO0 (Online Weight Approximation) | 3.00 | 1 | Much weaker; continual learning focus |
| 1VwWi6zbxs (τJp) | 6.00 | 1, 2 | Direct competitor; TAK improves by being dataless, more efficient, more thoroughly evaluated |
| 4mni4W1ZXy (Regularity explains emergence) | 4.00 | 1 | Different topic; lower quality |
| lIdc5DUplq (SUPERMERGE) | 4.33 | 1 | Different merging approach; less thorough |
| irPcM6X5FV (Submodule Linearity) | 6.00 | 1, 2 | Similar domain; TAK has stronger empirical scope |
| dj0TktJcVI (Attention-Only FT) | 6.25 | 2 | Directly related; TAK has more comprehensive evaluation and more principled contribution |
| q3ztjJRQuJ (Task Arithmetic in Trust Region) | 5.75 | 2 | Rejected; less thorough evaluation |
| g8sGBSQjYk (Second-Order Optimization Param.) | 7.33 | 2 | Different topic (optimization); not directly comparable |
| Q0TEVKV2cp (Debiasing Mini-Batch Quadratics) | 6.75 | 2 | Different topic (optimization theory) |
| kxebDHZ7b7 (TRAM) | 6.75 | 2 | Different topic (sharpness-aware minimization) |
| OZVTqoli2N (Second-Order Perspective on Compositionality) | 7.50 | 2 | Theoretically richer; TAK has stronger empirical validation but lighter theory |
| gc8QAQfXv6 (Unlocking Function Vectors) | 9.00 | 1 | Different domain (LLM continual learning); higher-scoring outlier |

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>