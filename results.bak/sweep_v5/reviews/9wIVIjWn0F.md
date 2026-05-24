## Summary

This paper proposes Regression-based Test-Time Adaptation (RTA), a method for view selection in CLIP-based test-time adaptation. The authors first demonstrate that selecting augmented views using ground-truth cross-entropy loss (LCE) dramatically outperforms entropy-based selection ("Ceiling TTA," Tables 1–2). They then learn a lightweight regression decision tree (LightGBM) that maps CLIP logits to **pseudo-label** cross-entropy loss using 1,000 pseudo-labeled samples from ImageNet validation. At test time, the pre-trained regression model predicts loss for each augmented view, and the top-k lowest-loss views are ensembled. RTA requires no online parameter updates, just a single offline training session.

---

## Strengths

1. **The Ceiling TTA oracle experiment (Tables 1–2) is genuinely striking and well-motivated.** Using true-label cross-entropy loss for view selection yields massive gains over entropy (e.g., ViT-B/16 with 64 views: 89.0% vs. 70.6% on IN-1k, 90.2% vs. 64.3% on IN-A). This observation convincingly motivates the search for alternatives to entropy-based selection and is the paper's most compelling finding.

2. **RTA achieves consistent improvements across a broad evaluation suite.** The method is tested on single-label (ImageNet + 4 variants + 10 cross-domain), and multi-label (MSCOCO, VOC2007, NUSWIDE) benchmarks with two backbones (RN50, ViT-B/16). Gains over strong baselines like Zero and BCA are small but directionally consistent (e.g., OOD avg for ViT-B/16: RTA 65.84% vs. Zero 65.03%; multi-label MSCOCO: RTA 58.95% vs. ML-TTA 57.52%).

3. **The method is computationally lightweight and practically appealing.** RTA uses a small LightGBM tree (depth 5, leaves 16) trained once on 1,000 samples, requiring no per-instance backward passes, prompt tuning, or online adaptation. This efficiency is a genuine practical advantage over methods like TPT/DiffTPT that update prompts per instance.

4. **Ablation studies on view count and training sample size (Figures 4–5) provide useful practical guidance.** Both saturate beyond ~128 views and ~5,000 samples, giving concrete deployment recommendations.

---

## Weaknesses

### Fatal
None.

### Major

1. **The paper never addresses the gap between the motivating oracle (true labels) and the actual method (pseudo-labels).** The Ceiling TTA in Section 4.1 uses ground-truth labels and achieves 89.0% on IN-1k (ViT-B/16, 64 views). The actual RTA replaces true labels with CLIP's own pseudo-labels — the same model being tested. This replaces the target from true cross-entropy loss to *CLIP's own pseudo*-cross-entropy loss, which is fundamentally different (RTA achieves 71.13% on the same setting — a ~18 point gap). The paper's framing throughout — "directly establish a regression mapping between augmented views and their corresponding cross-entropy loss" (abstract), "exploits such view-loss relationships" — implies the relationship with **true** label loss, but the regression is trained to predict pseudo-loss. The paper never acknowledges or discusses this discrepancy, and a head-to-head comparison of RTA vs. the oracle is absent. This framing mismatch materially overstates the contribution.

2. **Missing baseline: Maximum Softmax Probability (MSP) view selection.** Since the regression model predicts pseudo-loss = −log(softmax of the pseudo-label's class), the most natural simple baseline is selecting views with the highest softmax confidence (MSP). Entropy (which the paper compares against) is related but not identical — MSP is simpler and directly corresponds to what the regression is approximating. If MSP achieves similar results to RTA, the regression mapping adds little. This baseline must be included to substantiate the claim that the learned mapping provides value beyond what CLIP's own confidence signal already captures. The paper compares against entropy-based methods (Zero, TPT, etc.) but never MSP, which is the direct ablation.

### Minor

3. **Gains over strong baselines are small, and no variance/confidence intervals are reported.** For ViT-B/16, the OOD average improvement over Zero is 0.81 percentage points. On the 10 cross-domain datasets, RTA (68.70%) barely edges past BCA (68.59%). Without multiple seeds, error bars, or statistical significance tests, it is unclear whether these differences are stable or noise. The paper uses "significantly outperforms" (abstract, conclusion) without any significance testing.

4. **The claim of adapting to "arbitrary test distributions" is overblown.** The regression model is trained on 1,000 filtered samples from ImageNet validation, and tested on ImageNet variants (A, V2, R, K) and standard fine-grained benchmarks (Cars, Aircraft, Pets, etc.). While these cover a reasonable range, they are all natural-image benchmarks well-represented in CLIP's pretraining distribution. No evaluation on truly out-of-distribution targets (e.g., medical, satellite, or stylized imagery) supports the claim of "arbitrary" distributions.

5. **No ablation separating the effect of pseudo-label noise.** Training the regression on true labels (when available) vs. pseudo-labels would directly quantify how much performance degrades due to pseudo-label approximation. This would bridge the gap between Section 4.1's oracle and Section 4.2's actual method. Without it, the reader cannot tell whether the ~18 point gap on IN-1k stems from pseudo-label noise or from the regression model's capacity.

### Trivial

6. Figures 4 and 5 use dual y-axes with different ranges (IN-1k Acc: 69.0–71.5; Invariant Acc: 63.5–66.0), which visually exaggerates the gap between the two curves. A single-axis or normalized presentation would be clearer.

---

## Nice-to-Haves

- **Per-view ranking analysis:** A comparison of how well RTA's predicted loss vs. entropy correlates with true LCE on individual augmented views (e.g., Spearman correlation or view-ranking AUC) would directly test whether the regression mapping captures information qualitatively different from entropy.
- **Train on a non-ImageNet dataset:** Training the regression on a completely unrelated dataset (e.g., random web images) and testing on the same benchmarks would meaningfully support the generalization claim.
- **Qualitative view-selection examples:** Showing which views are selected by entropy, RTA, and the oracle for a few test images would help the reader understand the practical differences.

---

## Removed Points

- *"The regression mapping does not approximate the oracle"* — downgraded from Fatal to Major #1 (reframed). The paper *does* use pseudo-labels transparently (Section 4.2, line 184). The issue is not that the method fails to approximate the oracle — it's that the paper's framing conflates true-label and pseudo-label loss.
- *"Causal versus correlational claim"* — removed. The paper does not claim causality; it claims a correlational mapping, which is supported by the t-SNE and Spearman analysis.
- *"No adaptation at all"* — removed. This is a design choice, not a weakness; the paper frames it as a feature (no per-instance updates).
- *"Missing appendix/proofs"* — the parser strips these from all papers; they are present in the original submission.
- *"Training on original images only, testing on augmented views"* — the paper explicitly addresses this: "the original image itself can actually be regarded as a view" (line 184), and the t-SNE analysis in Section 4.1 already uses augmented views.
- *Various generic formatting/style nitpicks* — removed per instructions.
- Strength Finder strengths about "important problem" and "well-structured paper" — generic, moved here. The concrete strengths are retained above.

---

## Novel Insights

The calibration search surfaced a paper structurally similar but with complementary weaknesses: "BAT-CLIP" (avg 5.50) proposed bimodal adaptation for CLIP under corruptions but had a fatal flaw of using test-set ground-truth labels in a way that violated the TTA setting. The present paper avoids that specific pitfall but introduces a subtler version of the same problem: the Ceiling TTA oracle uses true labels to motivate the approach, while the actual method substitutes CLIP's own pseudo-labels without acknowledging the gap. The parallel is that both papers' strongest results come from using information (true labels) that the method itself does not have access to. The calibration also surfaced "ML-TTA" (avg 6.25), a multi-label TTA paper that, like the present work, achieves consistent gains through a clean, principled modification to the loss function — but that paper's contribution is directly supported by its theory, whereas RTA's oracle-method disconnect weakens the narrative.

---

## Suggestions

1. **Explicitly acknowledge and analyze the oracle-method gap.** Add a paragraph discussing why pseudo-label noise causes the drop from the Ceiling TTA (~89%) to RTA (~71%) and include an ablation training the regression on true labels to quantify this.
2. **Add MSP view selection as a baseline.** This is the simplest confidence-based method and the most direct competitor to the regression approach. If MSP matches RTA, the contribution collapses; if RTA outperforms MSP, that genuinely demonstrates value.
3. **Report variance across multiple seeds for the main results.** Given the small margins (often <1–2%), confidence intervals are necessary to establish robustness.
4. **Tone down "arbitrary test distributions" to what is actually demonstrated.** Replace with "a wide range of natural-image distributions" or similar.
5. **Consider training the regression on a more diverse or unrelated dataset** to support the generalization claim more convincingly.

---

## Score and Decision

### Calibration Anchors (all from deepreview_13k_calibration)

| Path | Avg Score | Comparison to RTA |
|------|-----------|-------------------|
| `kIP0duasBb.md` (RLCF) | 6.67 | Stronger: evaluated on 3 tasks (classify, retrieve, caption), clearer novelty. RTA is more narrow. |
| `75PhjtbBdr.md` (ML-TTA) | 6.25 | Stronger: clean theory-to-contribution link, no oracle-method disconnect. RTA broader but narratively weaker. |
| `yD2JMeKumt.md` (DOTA) | 6.00 | Comparable: both have practical efficiency and broad eval, but DOTA had concerns about human-feedback efficiency. |
| `z7PhIgVmZU.md` (BAT-CLIP) | 5.50 | Comparable: both have a core framing disconnect. BAT-CLIP had fatal flaws (using test labels), RTA's is subtler. |
| `Rc3RP9OoEJ.md` (InCPL) | 5.00 | Similar: marginal gains, overclaiming. InCPL had info-leakage concerns; RTA has oracle-method disconnect. |
| `PxL35zAxvT.md` (TTA+aux) | 4.67 | Similar core problem: method doesn't match framing. That paper re-invented UDA; this paper's oracle gap is analogous. |
| `pdzHpQbGrn.md` (Active TTA) | 2.50 | RTA is clearly stronger: cleaner method, broader evaluation, no trivial engineering. |

RTA has a genuinely interesting finding (the Ceiling TTA oracle) and a clean, practical method. However, the central framing conflates true-label loss (oracle) with pseudo-label loss (method), the gains over strong baselines like Zero are small and unreplicated, and a critical baseline (MSP) is missing. Relative to the anchors, this paper sits between InCPL (5.00) and BAT-CLIP (5.50) — a solid empirical system with a significant narrative weakness.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>