Now I have everything I need. Let me produce the consolidated review.

---

## Summary

This paper proposes AutoCLIP, a method that improves zero-shot image classification with vision-language models by reweighting prompt templates per image at test time — entirely in embedding space, without additional encoder passes. The weights are tuned via a single gradient ascent step on a logsumexp objective, with step size automatically selected via bisection to control the entropy of the weight distribution. Experiments across 990 settings (7 datasets × 6 VLMs × 3 prompt strategies × varying K) show a consistent average improvement of 0.45 pp over the standard uniform-weight baseline, at negligible computational overhead.

## Strengths

- **Embedding-space adaptation with zero extra VLM forward/backward passes.** AutoCLIP operates entirely on precomputed embeddings, requiring only lightweight vector operations. This is a genuine practical advantage over prior test-time prompt-tuning methods (TPT, RLCF) that need multiple augmented image forward passes and gradients through the text encoder. (Lines 34, 88–90, Algorithm 2.)

- **Single-sample, source-free, and fully unsupervised.** Unlike ZPE (Allingham et al.), which needs a batch of target samples and source-domain statistics, AutoCLIP works on one image at a time with no source-domain information — a materially different and practically valuable setting. (Lines 53–54.)

- **Broad and consistent empirical validation.** The evaluation covers 990 distinct settings across 7 datasets, 6 VLMs, 3 prompt-generation strategies, and template counts from K=4 to K=500. AutoCLIP outperforms the uniform-weight baseline in 85% of cases, with average gains of 0.45 pp and up to 3 pp. (Figure 1, Table 1, Section 4.)

- **Mechanistic understanding via controlled experiments.** A simplified synthetic embedding analysis (Section 5) shows that AutoCLIP bridges mean and max aggregation, excelling under moderate class–prompt entanglement. This provides a principled explanation for why gains are larger on smaller VLMs and smaller on large well-disentangled ones, and why performance degrades slightly for ViT-L-14 on ImageNet-C. (Figure 7.)

- **Closed-form gradient and automatic step-size selection.** The gradient is derived analytically (Section 3.3), enabling deployment on edge devices without autodiff. The entropy-controlled step-size bisection (Section 3.4) replaces a dataset-dependent learning rate with an interpretable, globally-set entropy-reduction factor β. The ablation (Figure 4) shows Δ Accuracy is stable for β ∈ [0.7, 0.9], supporting the claim of robustness.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **No direct comparison to prior test-time prompt-tuning methods (TPT, RLCF).** The paper mentions TPT and RLCF in the Related Work and correctly identifies the computational differences (embedding-space vs. encoder-penetrating adaptation). However, a reader evaluating "should I use AutoCLIP or TPT?" has no accuracy comparison to go on. The paper's main baseline is the uniform-weight zero-shot classifier — which is appropriate for showing that reweighting helps, but insufficient for positioning among TTA methods. A head-to-head on the same datasets/backbones (even with the caveat that TPT is much more expensive) would clarify the accuracy–cost trade-off. This does not invalidate the paper's claims, but is a genuine gap.

- **The β choice is not truly hyperparameter-free in a strict zero-shot sense.** The paper claims AutoCLIP comes "essentially without free hyperparameters" and sets β=0.85 globally, but the ablation (Figure 4) shows β=0.7 performs better on average and the authors recommend β=0.7 for future work. This does not disqualify the method — the paper is transparent about the ablation and the stability over [0.7, 0.9] — but the framing as "hyperparameter-free" is slightly overstated. The appropriate characterization is "one global hyperparameter with low sensitivity in a broad range."

- **Missing timing measurements.** The paper repeatedly claims "minor additional computation overhead" but provides no runtime numbers. The bisection routine (Algorithm 2, Line 18) requires evaluating softmax entropy multiple times per image. While this is almost certainly negligible compared to VLM encoding (it operates on K-dimensional vectors, not on model parameters), actual wall-clock measurements would substantiate the claim.

- **No ablation on number of gradient iterations.** The paper states that one iteration suffices based on "preliminary experiments" (Line 96) but does not show this data. Given that multi-step updates could help (or hurt) in different regimes, a brief comparison (1 vs. 2 vs. 5 iterations) on a subset would strengthen the paper.

- **Statistical significance not reported.** The paper reports means over 7 runs but does not indicate whether improvements are statistically significant (e.g., via paired test). For small effect sizes (ImageNet: 0.17 pp), this matters. A simple bootstrap or signed-rank test across the 7 runs would suffice.

### Trivial
- The gradient formula in Section 3.3 (lines 139–140) is notationally dense and would benefit from a cleaner matrix-form expression for reproducibility.

## Nice-to-Haves
- Provide runtime measurements (in ms per image) for the full pipeline including bisection, especially compared to one VLM forward pass and to running TPT.
- Analyze per-image success rate: for what fraction of images does the gradient update increase the logsumexp objective, and what fraction see accuracy improve vs. degrade?
- Discuss failure cases more systematically (EuroSAT, large models on ImageNet-C) — e.g., by measuring class-descriptor similarity variance as a signal for when the method will be unreliable.
- Include a simple data-free heuristic for selecting β (e.g., based on gradient magnitude or the spread of similarities) rather than relying on a global default.

## Removed Points

- *"The method's objective is not directly aligned with classification accuracy"* — This is a known property of surrogates (logsumexp approximates max, which for correct classification is what matters). The paper's ablation (Figure 5) compares alternative objectives (mean, max, entropy) and logsumexp performs best. The criticism is valid in principle but is equally applicable to almost all loss functions used in practice (e.g., cross-entropy is also a surrogate for accuracy). The empirical evidence justifies the choice.

- *"Bisection could add seconds per image for large K and C"* — Bisection operates on a K-dimensional softmax entropy computation (K ≤ 500). This is vector operations on a single small array, negligible compared to VLM encoding (seconds per image for ViT-L-14). The concern is factually overblown; the correct response is to provide actual timings, not to flag it as a computational bottleneck.

- *"Controlled setting is too simplified to be conclusive"* — The paper explicitly states this is a "strongly simplified" setting intended to "gain some insights" and "provide possible explanations." The critic acknowledges this. This is not a weakness; it is appropriately scoped.

- *Controlled setting missing "oracle" baseline* — This is a nice-to-have, not a weakness. The comparison to mean and max aggregation is the natural and sufficient baseline for the controlled analysis.

- *Generic formatting/presentation nitpicks* (error bars too small to see, figures confusing, missing appendix content) — Removed per formatting-artifact rules.

## Novel Insights

The most interesting observation emerging from this review is the tension between AutoCLIP's framing as "hyperparameter-free" and the honest admission that β=0.7 performs better than the default 0.85. Rather than undermining the paper, this transparency actually reveals a deeper truth: the method's success does not hinge on a carefully tuned hyperparameter at all. The critical insight is that the entropy-controlled step size mechanism (Section 3.4) is the true contribution, not any specific β value. The bisection procedure converts an otherwise dataset-dependent learning rate into a interpretable knob whose broad range [0.7, 0.9] yields stable gains. Future work could replace the global β with a per-image adaptive scheme or eliminate it entirely — the core idea (one gradient step on logsumexp in embedding space) would survive either way.

## Suggestions
1. Add a comparison to TPT and RLCF on a representative subset (e.g., ImageNet, ImageNet-R, Food101 with ViT-B/16 and K=80 CLIP templates) with the caveat about differing computational budgets clearly stated.
2. Report wall-clock time per image (including bisection) for one or two representative settings. Even 2–3 lines in the ablation section would substantiate the "minor overhead" claim.
3. Either adopt β=0.7 as the default (since the data favor it) or shift the framing from "hyperparameter-free" to "one robust global hyperparameter." These are both honest and improve the paper.
4. Add a brief table or sentence showing accuracy improvement fraction broken down per-image (e.g., % of images where accuracy improves / stays same / degrades on one dataset).
5. Include a simple paired significance test for the main results table.

## Score and Decision

**Calibration anchors** (all retrieved from the calibration corpus):

| Anchor | Avg Human Score | How it compares to AutoCLIP |
|--------|----------------|-----------------------------|
| kIP0duasBb.md (RLCF) — *Test-Time Adaptation with CLIP Reward* | 6.67 (Accept) | RLCF tackles more tasks (classification + retrieval + captioning) but requires an extra CLIP model for reward computation and multiple augmented forward passes. AutoCLIP is narrower (classification only) but simpler and cheaper. Similar overall quality. |
| NeVbEYW4tp.md (Self-TPT) — *Efficient Test-Time Prompt Tuning* | 5.00 (Reject) | Also addresses efficiency in TTA. AutoCLIP is cleaner (no source training phase, no gradient matching loss), has more comprehensive evaluation (990 vs 3 settings), and avoids concerns about novelty dilution. Clearly stronger. |
| Rc3RP9OoEJ.md (InCPL) — *In-context Prompt Learning* | 5.00 (Reject) | Uses labeled in-context examples at test time, raising fairness concerns. AutoCLIP is fully unsupervised, which is a substantially harder and more applicable setting. Stronger paper. |
| A78MiKnGrL.md (Search4Prompt) — *Test-time Zero-shot Recognition with Good Attributes* | 4.50 (Reject) | Attribute-retrieval + prompt tuning. AutoCLIP is simpler, has broader evaluation, and avoids dependence on LLM attribute quality. |
| pdzHpQbGrn.md (Active TPT) — *Active Test Time Prompt Learning* | 2.50 (Reject) | Weakly motivated, marginal gains, trivial modifications to existing methods. AutoCLIP is in a completely different tier — principled method, strong evaluation, clean story. |

AutoCLIP is a solid paper: a simple, well-motivated idea, executed cleanly, evaluated comprehensively, and presented transparently. The gains are modest (0.45 pp average) but come at essentially zero cost. The weaknesses are fixable and do not threaten the core contribution. It compares favorably to the median calibration anchor and sits below the strongest (RLCF at 6.67) only because its scope is narrower and the improvement magnitude is smaller.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>