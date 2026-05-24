Now I have a solid calibration. Let me write the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None.

### Major
- weakness 1

### Minor
- weakness 2
- weakness 3

### Trivial
- weakness 4

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now think carefully about what goes where and finalize.

Here's my assessment:

**Summary**: PI-CCA proposes a replay-free continual learning framework for VLMs that preserves cross-modal alignment geometry (canonical correlations and subspaces) via a compact certificate, plus a prompt-invariance mechanism. It achieves SOTA on four VL-CL benchmarks.

**Strengths to keep**:
1. Conceptual shift: recasts forgetting as alignment-geometry drift rather than proxy matching (verified from §1, §3)
2. Constant-memory replay-free certificate via sketching (verified from Eq. 4, §3.2)
3. SOTA across all four benchmarks (Tables 1, 2)
4. Prompt-invariance mechanism with clear benefits (Figure 4)
5. Low task-order sensitivity (Figure 5)
6. Thorough component ablation (Table 3)

**Strength to remove**:
- Strength about Figure 3 correlations — conflicts with verified weakness about implausibly perfect correlations

**Weaknesses**:
1. **Major**: Figure 3 reports Pearson/Spearman correlations of 1.00 and 0.99 between geometry drift and performance drops. On experimental data with multiple varied hyperparameters (certificate size, EMAs, whitening, LoRA capacity, etc.), perfect correlations are suspicious. The paper mentions "realistic scatter" yet r=1.00 means zero scatter. The authors must clarify how these points were generated (number of unique configurations, whether deterministic, why scatter is absent) and, if needed, re-plot with appropriate variance or acknowledge the deterministic nature and caveat the interpretation.

2. **Minor**: Table 1 (MTIL, X-TAIL) reports only point estimates without standard deviations, while Table 2 includes error bars. The claimed improvements over strong baselines (e.g., +1.6 on MTIL Avg) may not be statistically significant without variance information.

3. **Minor**: The stop-gradient on Σ^{-1/2} in §3.4 means gradients do not propagate through the whitening transformation, even though whitening depends on the parameters via covariance estimates. This design choice is not justified or ablated. A simple comparison (with vs. without stop-gradient) would clarify whether this matters.

**Removed points**: Various complaints about missing appendix details (backbone, hyperparameters, anchor prompt set) are removed per policy — these exist in the appendix/ supplementary that was stripped. Strength finder's claim about Figure 3 correlations being a strength is removed as it conflicts with the verified weakness.

**Novel Insights**: One notable observation is that the subspace drift (D_ang) appears more predictive than spectral drift — this suggests directional alignment matters more than correlation magnitude, which is a non-obvious finding about CLIP's continual behavior.

**Score**: 6.0, borderline Accept.

Wait, actually, I need to think about the score more carefully using my calibration.

C-CLIP (anchor sb7qHFYwBc) scored 6.50 (6,8,6,6). It was accepted. Pi-CCA outperforms C-CLIP on all benchmarks and has a stronger conceptual framework. However, Pi-CCA has the Figure 3 issue that C-CLIP doesn't have. 

If we think of it: Pi-CCA's strengths are better than C-CLIP's, but its weaknesses (especially Figure 3) are also more concerning. So overall, Pi-CCA is roughly comparable to C-CLIP but with a different quality profile. I'd put it at 6.0 — slightly below C-CLIP's 6.50 due to the Figure 3 credibility issue, but above the rejected VLM papers at ~5.67.

Actually, let me reconsider. The Figure 3 issue is concerning but:
1. It doesn't affect the main SOTA results (Tables 1, 2)
2. The ablation study (Table 3) independently validates the components
3. The prompt invariance stress test (Figure 4) and task-order sensitivity (Figure 5) are clean

The Figure 3 is an *analysis* figure meant to support the intuition, not the core evidence. If the correlations are indeed near-1.00 due to deterministic computation and a small grid, the paper should clarify this. But it doesn't invalidate the main contribution.

I think 6.0 is fair. Let me proceed.Now I have all the information needed. Let me finalize the review.

**Calibration summary:**

**Round 1 Bracket**: Based on anchors, the plausible range is [5.5, 7.0]. The paper is clearly stronger than weak anchors (scores 2–3) and comparable to or slightly below C-CLIP (6.50).

**Round 2 Narrowing**: C-CLIP (6.50, accepted) is the most direct comparison — Pi-CCA outperforms it on all benchmarks with a more principled approach, but has the Figure 3 credibility issue. TiC-CLIP (6.25, accepted) and Spurious Forgetting (6.33, accepted) are in similar ranges but different domains. "Learning without Forgetting for VLMs" (5.67, rejected) and open-vocab CL (6.00, rejected) are weaker overall. Pi-CCA sits between the 6.0–6.5 range; the Figure 3 issue pulls it down from C-CLIP's 6.50.

**Final score**: **6.0** — strong contributions with one significant analysis concern.

Here is the final consolidated review:

---

## Summary

PI-CCA proposes a replay-free continual learning framework for vision-language models that preserves cross-modal alignment by directly constraining the geometry (canonical correlations and subspaces) of the whitened image-text cross-covariance via a compact, constant-memory certificate, plus a prompt-invariance mechanism via projector averaging. Across MTIL, X-TAIL, VLCL, and ConStruct-VL, the method achieves state-of-the-art results among replay-free methods, including surpassing a synthetic-replay baseline (GIFT) without storing any past data. The core conceptual insight — that preserving alignment invariants rather than optimizing proxy signals better retains zero-shot generalization — is well-motivated and supported by multiple lines of evidence.

## Strengths

- **Principled conceptual reframing.** The paper recasts forgetting in VL-CL as alignment-geometry drift and targets the canonical correlation spectrum and subspace directly (§3.2–3.3), rather than distilling logits, similarities, or weights as prior work does. This is a clean departure from the proxy-regularization paradigm.

- **Constant-memory replay-free certificate.** The certificate stores only top-*k* canonical correlations and sketched subspaces (Eq. 4) with sketch dimension *h* ≪ *d_v*, *d_t*, ensuring memory does not grow with the number of tasks. This is genuinely replay- and generator-free.

- **State-of-the-art results across all benchmarks.** Tables 1 and 2 show consistent first-place results on MTIL (Avg 76.8, Last 75.5), X-TAIL (Avg 68.1), VLCL (I2T R@1 48.6), and ConStruct-VL (FA 75.2, AF 2.7), outperforming every replay-free baseline and even the synthetic-replay GIFT method.

- **Thorough component ablation confirming necessity of each term.** Table 3 systematically ablates spectral preservation (λ₁=0 → −2.5 on MTIL Avg), subspace preservation (λ₂=0 → −2.2), prompt invariance (λ₃=0 → −1.5), and covariance EMA (β=0 → −2.7), cleanly attributing gains to each certificate component.

- **Prompt-invariance mechanism validated under stress.** Figure 4 shows that the L_pi term flattens performance degradation across increasing prompt perturbation strength, with +2.44 p.p. R@1 improvement at s=1.0 on ID templates and similar gains OOD. This addresses a genuine robustness gap in prior VL-CL work.

- **Low task-order sensitivity.** Figure 5 demonstrates narrow IQRs across 20 random task permutations, confirming that PI-CCA's performance is not an artifact of a favorable ordering.

## Weaknesses

### Fatal
None.

### Major

1. **Implausibly perfect correlations in Figure 3.** The four panels report Pearson r = 1.00 and Spearman ρ = 1.00/0.99 between geometry drift (D_ang, D_ρ) and performance drops (ΔAvg, ΔR@1). On experimental data generated by sweeping multiple hyperparameter dimensions (certificate size, EMAs, invariance strength, whitening, pairing, LoRA capacity/LR, sketch type), perfect correlations strain credulity — measurement noise, mini-batch stochasticity, or non-linearities would typically produce scatter. The figure caption itself mentions "realistic scatter" yet r = 1.00 implies zero scatter. This inconsistency undermines the analysis that directly links geometry preservation to downstream retention. **The authors must clarify** how the data points were generated (number of unique configurations, whether deterministic), why correlations are exactly/near 1.00, and ideally report variance or re-plot with appropriate scatter. Without clarification, this evidence cannot be taken at face value. Importantly, this does **not** invalidate the paper's main results (Tables 1–2, ablation in Table 3, prompt invariance in Figure 4), which stand independently.

### Minor

2. **Missing variance information in Table 1.** Table 1 (MTIL, X-TAIL) reports only point estimates without standard deviations, while Table 2 includes error bars. The claimed improvements (e.g., +1.6 on MTIL Avg, +0.7 on X-TAIL Last) are modest enough that statistical significance is unclear. The field standard is to report variance across seeds, which the reproducibility statement suggests exists; this should be reflected in the main table.

3. **Stop-gradient on whitening matrices is not justified or ablated.** Section 3.4 states that Σ^{-1/2} is computed with a stop-gradient "if needed." This means gradients for the spectral and subspace losses do not propagate through the whitening transformation, even though the whitening matrices depend on the parameters via covariance estimates. The paper neither justifies this choice nor compares against a version that backpropagates through whitening (e.g., via implicit differentiation or full eigen-decomposition gradients). A simple ablation — does removing the stop-gradient change results? — would clarify whether this matters in practice.

### Trivial
None.

## Nice-to-Haves

- **External computational cost anchor.** The Pareto plots (Figure 2) map PI-CCA's own capacity trade-offs, but an external comparison point (e.g., where C-CLIP or ZSCL lies in memory-time-performance space) would strengthen the efficiency claim.
- **Sensitivity plots for λ₁, λ₂.** The ablation sets each λ to zero, but a brief continuous sweep showing how performance varies between 0 and the chosen default would confirm the operating point is not brittle.
- **Backbone architecture identified in main text.** The paper states that LoRA adapters are used but never explicitly names the backbone (presumably CLIP ViT-B/32) in the main text; adding this early in §4.1 would help.

## Removed Points

These points are flagged to be removed per policy; treat them with caution.

- **Strength about Figure 3 correlations as mechanistic evidence.** The Strength Finder presented the ≈1.00 correlations as core evidence linking geometry stability to performance. This directly conflicts with the verified Major weakness above (implausibly perfect correlations undermine credibility). Per policy, the weakness wins; this strength is removed.
- **Weaknesses about missing appendix/hyperparameter details.** Multiple reviewer complaints about the anchor prompt set not being specified, default λ values not in main text, and backbone architecture not stated are removed. These details exist in the appendix (which is stripped by the parser) and/or are standard to defer to supplementary material.
- **Weakness about "no comparison of computational cost against baselines on same axes" (Figure 2).** This is a nice-to-have enhancement, not a genuine weakness — the paper provides Pareto analysis of its own method, which is already informative.
- **Weakness about "Hungarian vs. sorted surrogate pairing" being incompletely analyzed.** The paper already reports that they yield nearly identical results (76.8 vs. 76.7 on MTIL Avg), which is sufficient.
- **Weakness about α sensitivity in certificate EMA.** The ablation already tests α=0 (drop of 1.2), providing a boundary condition. Additional α sweeps are nice-to-have, not required.
- **Strength Finder's generic/conflicting strengths.** Strengths framed as "this paper addressed an important problem" or other generic claims that lack specific evidence are removed. All remaining strengths are concrete and evidence-grounded.

## Novel Insights

One interesting observation that emerges from the paper beyond its own claims is that **subspace drift (D_ang) appears more predictive of performance degradation than spectral drift (D_ρ)** across multiple hyperparameter configurations (Figure 3 and §4.3). This suggests that *directional* alignment — i.e., which canonical directions the embeddings use — matters more for zero-shot retention than the magnitude of the correlations themselves. If confirmed, this has implications beyond continual learning: it implies that VLM fine-tuning protocols (even in non-continual settings) should prioritize maintaining the orientation of the cross-modal embedding subspace rather than just the alignment strength. Theoretically, this could connect to the observation that CLIP's canonical directions correspond to interpretable semantic concepts, and drifting away from them degrades generalization even if correlation magnitudes are preserved.

## Suggestions

1. **Clarify the Figure 3 data generation process.** Provide the exact number of unique (k, h, λ, EMA, etc.) configurations plotted, report whether the data is deterministic or averaged over seeds, and either show confidence ellipses or acknowledge that the near-perfect fit results from deterministic computation over a grid. If the correlations remain high (e.g., r > 0.95) with realistic variance added, the qualitative conclusion is unchanged and the figure becomes credible.

2. **Add standard deviations to Table 1.** The variance data appears to exist (Table 2 has it, and the reproducibility statement mentions seeds); include it in the main classification results to match field conventions.

3. **Ablate the stop-gradient on whitening.** Report one additional row in the ablation (or a brief note) comparing PI-CCA with vs. without stop-gradient on Σ^{-1/2}. If results are similar, state that; if worse, discuss the implications.

## Score and Decision

**Calibration (anchors retrieved across rounds):**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| C-CLIP | sb7qHFYwBc | 6.50 | 1–2 | Direct baseline; Pi-CCA outperforms it but has the Figure 3 credibility issue |
| TiC-CLIP | TLADT8Wrhn | 6.25 | 2 | Benchmark paper on continual CLIP training; different focus, similar quality tier |
| Spurious Forgetting (LLMs) | ScI7IlKGdI | 6.33 | 2 | Different domain (LLMs); comparable rigor |
| LwF for VLMs | k9NYnsC4Mq | 5.67 | 1–2 | Rejected; weaker empirical evidence and methodological concerns |
| Open-vocab CL | wE1I9IGqeH | 6.00 | 2 | Rejected; modest improvements, novelty concerns |
| Vision+Language Synergy | 9aZ2ixiYGd | 5.00 | 1 | Accepted but relies on external LLM knowledge, less clean setting |
| Weak anchors (various) | JIlIYIHMuv et al. | 2.00–2.50 | 1 | Clearly inferior; flawed or preliminary work |

**Round 1 bracket**: [5.5, 7.0]. **Round 2 narrowing**: Pi-CCA is comparable to C-CLIP (6.50) in overall quality but is pulled down by the Figure 3 issue. It is clearly stronger than the rejected VLM-CL papers (5.67–6.00). The final score reflects a paper with a strong conceptual contribution and convincing empirical results across benchmarks, but with a significant analysis concern that needs resolution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>