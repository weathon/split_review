Now I have all the evidence I need. Let me produce the final consolidated review.

---

## Summary

RotPruner introduces a training-based pruning framework that learns orthonormal rotation matrices to transform the weight and activation spaces of LLM linear layers before applying existing pruning methods (magnitude, Wanda, SparseGPT). The core insight is that the original parameter space is suboptimal for pruning and that a learned rotation—optimized via Cayley SGD without modifying pretrained weights—can produce a weight distribution with more salient outliers, enabling better pruning decisions. The method supports unstructured, 2:4 semi-structured, and structured sparsity and is evaluated on OPT, LLaMA-2, and LLaMA-3 families.

## Strengths

- **Novel and well-motivated core insight.** The paper demonstrates concretely (Section 3.1, Figure 2, Table 1) that the original weight space is not optimal for pruning, that random rotation hurts performance, but that a *learned* rotation produces more weight outliers and consistently improves perplexity over pruning in the original space. This is a clean conceptual contribution applicable across pruning methods.

- **Strong empirical results against one-shot baselines across models and sparsity patterns.** RotPruner achieves consistently lower WikiText-2 perplexity than SparseGPT, Wanda, and SliceGPT on OPT-125M through OPT-6.7B, LLaMA-2-7B, and LLaMA-3-8B at 50% unstructured, 2:4 semi-structured, and 30% structured sparsity (Table 2). Zero-shot accuracy improvements on OPT-6.7B and LLaMA-3-8B (Table 3) further validate that the approach transfers to actual task performance.

- **Flexible framework rather than a single algorithm.** RotPruner integrates with multiple base pruners (magnitude, Wanda, SparseGPT — Table 9) and supports three sparsity patterns. This makes it a general enhancement that can be layered on top of various one-shot methods, which the ablation study cleanly demonstrates.

- **Comprehensive ablation studies.** The paper ablates loss functions (Table 5), STE variants (Table 6), optimization methods (Table 7), calibration set size (Figure 5), number of rotation matrices (Table 8), and base pruning methods (Table 9). These provide clear evidence for the chosen design (cosine distillation loss + SR-STE + Cayley SGD) and show the method's robustness to design choices.

- **Efficient optimization that preserves pretrained knowledge.** Cayley SGD keeps matrices orthonormal at ~2× SGD cost (Section 3.3). The weights themselves are never updated, which distinguishes RotPruner from training-based methods that risk forgetting. The 8B model is pruned in 1.5 hours on a single L40S GPU — a practical cost.

## Weaknesses

### Fatal
None.

### Major

- **No comparison against other training-based pruning methods.** The paper positions RotPruner as a "training-based pruning framework" (Abstract, Section 2.2) and cites ADMM-Pruner, FISTAPruner, and AST as related training-based approaches. Yet all baselines in Tables 2–3 are one-shot methods (SparseGPT, Wanda, SliceGPT). The paper claims "state-of-the-art" performance, but without evidence that RotPruner also outperforms other training-based approaches (which also use calibration data and training), the SOTA claim is incomplete. Training-based methods typically outperform one-shot methods at higher computational cost, so showing improvement over one-shot baselines alone does not establish SOTA within the training-based class. The authors should include comparisons with at least the most comparable training-based methods that use similar calibration data scales.

### Minor

- **The "pruned model outperforms dense model" claim is stated without explanation or analysis.** Lines 163 and 165 report that OPT-6.7B at 50% sparsity and OPT-1.3B below 50% sparsity surpass the dense model's perplexity. This is a notable result that could arise from a regularization effect, under-trained dense baseline, or evaluation noise, but the paper offers no discussion. Adding a brief explanation (or contextualizing the magnitude of the improvement relative to the dense model's variance) would strengthen credibility. As presented, the claim risks appearing anomalous without support.

- **No variance or confidence intervals reported for main results.** Figure 5 shows that RotPruner is more sensitive to calibration set size than baselines (e.g., perplexity degrades noticeably when moving from 128 to 64 samples). The paper acknowledges this sensitivity but does not report standard errors or intervals for any main results (Tables 2, 3). Without this, the reader cannot assess whether improvements are statistically significant or artifacts of a specific calibration draw. This is a standard concern in LLM pruning papers (SparseGPT and Wanda also typically report single runs), but it carries extra weight here given the documented sensitivity.

- **Structured pruning initialization conflates the learned rotation with fine-tuning.** For structured pruning, Q is initialized to SliceGPT's PCA-based rotation matrices, then fine-tuned (Section 3.4). The paper reports RotPruner outperforming SliceGPT, but this improvement could come primarily from the additional training steps rather than the rotation being *learned* per se. An ablation initializing Q to identity (analogous to the unstructured/semi-structured setting) would separate these factors. No such ablation is provided for structured pruning.

### Trivial

- **The calibration split of WikiText-2 should be specified explicitly.** The paper states "Perplexity is measured on test set of WikiText-2" (line 151) and "We use WikiText2 as the calibration set" (line 155) without clarifying which split (train or validation) the calibration samples are drawn from. While standard practice is to use the training split, stating this explicitly would remove any ambiguity.

## Nice-to-Haves

- An ablation for structured pruning where Q is initialized to identity (rather than SliceGPT's solution) to isolate the benefit of learning the rotation from the benefit of additional fine-tuning.
- Reporting perplexity across multiple calibration draws (e.g., 3–5 random seeds with std dev) to quantify stability, especially given the documented sensitivity to calibration set size.
- An end-to-end wall-clock speed benchmark for full-model inference (not just single layers) with and without the residual rotations, to give practitioners a complete picture of the inference cost.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Section 3.1 motivation is weak / link to algorithm is weak** — This is an overly pedantic reading of a motivation section. The paper provides a clear narrative arc: toy example → minimize ||AW||₀ → hard → approximate with ||AW||₁ → activation matters too → end-to-end loss optimization. Perfectly adequate for a motivation section.

- **Section 3.2 inconsistency between fusion claim and residual rotations** — The paper is clear: fusion *can* be done theoretically (via SliceGPT's computational invariant), but the practical implementation adds residual rotations, whose overhead is explicitly measured in Section 4.2 (Table 4). There is no inconsistency.

- **Data leakage / calibration-evaluation overlap concern** — The paper explicitly distinguishes calibration ("WikiText2") from evaluation ("test set of WikiText-2"). Standard practice in the field is to use the training split for calibration and the test split for evaluation, making leakage unlikely. The criticism is based on an assumption not supported by the text.

- **Zero-shot tasks are minimal** — Seven tasks (WinoGrande, Piqa, RTE, ARC Easy, ARC Challenge, WNLI, QNLI) is a standard evaluation suite for LLM pruning papers. This criticism does not reflect a genuine weakness.

- **Missing related works from 2024–2025** — No specific papers are named by the reviewer, so this cannot be verified. The paper already cites works from 2024 (Ashkboos et al., Liu et al., Huang et al., Dubey et al.).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add at least one training-based pruning baseline** (e.g., ADMM-Pruner or FISTAPruner) to the main comparison tables. If these methods use different settings (weight updates vs. frozen weights), clearly explain the differences and how the comparisons should be interpreted. If full comparison is impractical, explicitly qualify the "state-of-the-art" claim to refer to the class of one-shot-pruner-enhancement methods.

2. **Explain or contextualize the "pruned outperforms dense" result** in one sentence — whether it reflects a regularization effect, noise relative to the dense baseline, or an artifact of evaluation.

3. **Report variance** (at least 3 random calibration draws) for the main perplexity tables, or at minimum for one representative model (e.g., OPT-1.3B) to establish the stability of the claimed improvements.

4. **For structured pruning, include an ablation** initializing Q to identity and comparing against the SliceGPT-initialized variant.

## Score and Decision

The paper introduces a genuinely novel idea (learned rotation before pruning) that is well-motivated, supported by reasonable evidence, and practically efficient. The main empirical gap is the absence of training-based baselines, which makes the "state-of-the-art" claim incompletely supported. However, the core contribution does not depend on being SOTA among *all* training-based methods — the demonstration that learned rotation consistently improves over one-shot methods is itself a solid contribution. The remaining issues (unexplained out-performance of dense model, no variance reporting, structured pruning ablation gap) are addressable in revision.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>