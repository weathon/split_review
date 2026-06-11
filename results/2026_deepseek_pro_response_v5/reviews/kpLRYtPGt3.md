Now I have enough anchors across my bracket. Let me finalize the calibration:

**Comparison summary:**

| Anchor | Score | Comparison to Neon |
|--------|-------|-------------------|
| MAD (ShjMHfmPs0) | 6.67 | Neon is stronger — provides a working method with SOTA results, not just analysis |
| Stability (JORAfH2xFd) | 6.75 | Neon is stronger — goes beyond analysis to propose and validate a method |
| T-Stitch (2mqb8bPHeb) | 7.00 | Neon has more theoretical depth and broader architectural applicability; comparable practical impact |
| Consistency techniques (WNzy9bRDvG) | 7.00 | Neon has broader scope across architectures |
| RepG (gWgaypDBs8) | 7.33 | Similar theory+method structure; Neon is broader but RepG is cleaner |
| Lipschitz (WNkW0cOwiz) | 7.50 | Comparable theory+method; Neon has broader experiments |
| Shortcut Models (OlzB6LnXcS) | 8.00 | Shortcut Models is cleaner; Neon has the γ confound weakness |

Neon sits between 7.00 and 7.50. The γ co-optimization confound on the headline SOTA result is a real issue that prevents it from reaching the 8.00 level of Shortcut Models. But Neon's theoretical depth, architectural breadth, and practical simplicity put it above the 6.67-6.75 analysis-only papers.

**Final score: 7.0**

Now let me write the final review.Now let me write the final consolidated review.

---

## Summary

Neon is a post-hoc method that improves generative models by briefly fine-tuning them on their own synthetic outputs and then reversing the resulting weight update via a simple parameter extrapolation: θ_Neon = (1+w)θ_r − wθ_s. The key theoretical insight is that mode-seeking inference samplers (temperature < 1, top-k, CFG-guided diffusion/flow) create a predictable anti-alignment between synthetic-data and real-data population gradients, which negative extrapolation corrects. Demonstrated across four model families (diffusion, flow matching, autoregressive, few-step IMM) on three datasets, Neon achieves a new ImageNet-256 SOTA of 1.02 FID (xAR-L + Neon) with only 0.36% additional compute.

## Strengths

- **Elegantly simple method with broad applicability**: Neon reduces to a single post-hoc parameter merge requiring no new real data, no auxiliary models, no likelihood computation, and no inference modifications (Algorithm 1, Section 3). Despite this simplicity, it delivers substantial FID improvements across four model families (diffusion, flow matching, autoregressive, few-step) on three datasets (Sections 4.1–4.3).

- **Rigorous theoretical framework grounding the method**: Theorems 1 and 2 (Section 3.1) establish sufficient conditions for anti-alignment between synthetic and real-data gradients and prove that mode-seeking samplers guarantee this condition near good models. The theory also correctly predicts the complementary regime where diversity-seeking samplers would favor interpolation instead of extrapolation (line 171), adding theoretical completeness.

- **State-of-the-art empirical results with negligible cost**: Neon elevates xAR-L on ImageNet-256 from FID 1.28 to 1.02 using only 0.36% additional training compute (Section 4.2, Figure 5). Consistent improvements are shown across all configurations: EDM-VP CIFAR-10 (1.78 → 1.38), FFHQ-64 (2.39 → 1.12), VAR-d16 (3.30 → 2.01), and IMM 4-step (1.98 → 1.69, halving inference cost; Section 4.3).

- **Clear mechanistic explanation via precision-recall decomposition**: Figure 4 (Section 4.1) reveals that Neon's improvement operates through a precision-recall trade-off — precision monotonically decreases with w while recall follows an inverted-U peaking near the FID-optimal weight. This confirms the theoretical prediction that self-training concentrates mass on well-captured modes and reversing this redistributes mass to under-represented modes.

- **Well-designed ablations with practical insights**: Cross-architecture transfer (Figure 8) shows synthetic data from different architectures can improve a target model. The CIFAR-10C negative control (line 249) rules out generic OOD effects. Data-scarcity experiments (Figure 9) demonstrate Neon can compensate for a ~40% reduction in real training data. Robustness to synthetic data quality (Figure 10) shows insensitivity to CFG scale over a wide range.

- **Minimal data requirements**: With only 1k synthetic samples, xAR-L achieves 1.05 FID — within 0.03 of the 1.02 FID obtained with 750k samples (Section 4.2), demonstrating rapid stabilization of the degradation direction.

## Weaknesses

### Fatal
None.

### Major

- **Joint optimization of w and γ confounds attribution of the headline SOTA result**: For autoregressive and few-step models (Sections 4.2–4.3), the reported FID improvements come from jointly re-optimizing both the Neon extrapolation weight w and the classifier-free guidance scale γ. The base model FID was reported at a particular γ; the Neon-improved FID benefits from both the parameter extrapolation and the re-tuned γ. For VAR-d16, the paper helpfully reports that independent optimization (w only, γ fixed) yields FID 3.01 vs. joint 2.01 — meaning roughly half the gain comes from γ re-tuning. However, for xAR-L (the headline 1.02 SOTA result), this breakdown is not provided. The reader cannot assess how much of Neon's claimed contribution is from the core negative extrapolation mechanism versus CFG re-tuning. This weakens the central claim that the negative extrapolation mechanism is the primary driver of the improvement.

### Minor

- **No experimental comparison against existing synthetic-data improvement methods**: The paper devotes space in related work (Section 2, line 60) to distinguishing Neon from DDO, SIMS, Discriminator Guidance, and Self-Play Fine-Tuning, arguing that Neon is simpler and more universal. However, no head-to-head comparison is provided. While the universality claim is well-supported by the cross-architecture results, a comparison on at least one shared benchmark (e.g., EDM-VP CIFAR-10 vs. DDO) would allow readers to assess whether simplicity comes at a performance cost.

- **Anti-alignment mechanism not directly measured on real models**: The theoretical analysis (Theorems 1–2) claims that mode-seeking samplers produce synthetic gradients anti-aligned with population gradients. The empirical validation is entirely indirect — the precision-recall trade-off (Figure 4) is consistent with the theory but does not constitute a direct test. The key quantity s = ⟨r_d, P r_s⟩ is never computed or estimated for any real model. A direct measurement on even one model would strengthen the theory-empirics connection.

### Trivial

- **Figure 4 caption error** (line 193): The caption states "w = −1 corresponds to the model directly trained on synthetic data, i.e., θ_Neon = θ_r." By equation (2), w = −1 gives θ_Neon = (1+(−1))θ_r − (−1)θ_s = θ_s, not θ_r. The w = 0 case is correctly identified as the base model. This appears to be a copy-paste error.

## Nice-to-Haves

- Report the Neon-only improvement for xAR-L with γ fixed at the base model's optimal value, to isolate the core method's contribution from CFG re-tuning.
- Report variance estimates (e.g., ±std across multiple seeds or sample splits) for the main FID results, particularly given the use of 10k-sample FID for hyperparameter selection.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "Taylor expansion argument requires small fine-tuning, but experiments use B ≈ 1-3Mi"** — REMOVED. This confuses total training budget B with per-step size α. The theory uses α (learning rate per step), which is small (reduced learning rate, as stated in Section 4); total budget B can be large while α remains small through many steps. The experimental results (optimal w* decreasing with more training) are consistent with the theory.

- **Harsh Critic: "A-MONO assumption deferred to Appendix B.7, which is stripped"** — REMOVED. Per hard rules, we cannot penalize the paper for the parser stripping the appendix. The assumption is flagged in the main text (footnote 2, line 161) with a reference to the appendix for details.

- **Strength Finder: generic strengths about "important problem" or "interesting question"** — REMOVED. These are superficial and not grounded in specific evidence from the paper.

- **Harsh Critic: "Abstract overstates what the theory actually establishes"** — REMOVED. The abstract says "We prove that Neon works because typical inference samplers... create a predictable anti-alignment," which accurately describes Theorems 1–2. The theory does prove anti-alignment under mode-seeking samplers, which is what makes Neon reduce risk.

## Novel Insights

The paper's strongest novel contribution is the theoretical connection between mode-seeking inference samplers and gradient anti-alignment (Theorems 1–2), which provides a principled explanation for why reversing self-training degradation works. This insight is non-obvious: the conventional view is that self-training on synthetic data is harmful (model collapse), but the paper reframes the degradation as a structured, harnessable signal. The complementary prediction — that diversity-seeking samplers would instead favor interpolation (w < 0) — adds theoretical completeness and could guide future work.

## Suggestions

- Add a direct measurement of gradient anti-alignment for at least one model (e.g., compute the inner product between empirical gradients on held-out real vs. synthetic batches at θ_r for EDM-VP CIFAR-10). This single experiment would substantially close the theory-empirics gap.
- For the xAR-L headline result, report FID when varying w alone with γ fixed at the base model's optimal value, to let readers assess how much of the 1.28 → 1.02 improvement is attributable to Neon's core mechanism.
- Fix the Figure 4 caption to correctly state that w = −1 corresponds to θ_Neon = θ_s (the degraded model), not θ_r.

## Score and Decision

**Calibration anchors referenced across rounds:**

| Round | Anchor | Avg Score | Comparison |
|-------|--------|-----------|------------|
| 1 | TCIG (RFJGFrMvYj) | 1.50 | Neon far stronger |
| 1 | KD Model Collapse (8TbqoP3Rjg) | 2.00 | Neon far stronger |
| 1 | Augmented Conditioning (9aIlDR7hjq) | 4.00 | Neon clearly exceeds |
| 1 | Real-Fake (svIdLLZpsA) | 6.00 | Neon stronger — more theory, broader scope |
| 1 | Model Collapse Chain (P5UETqZXqT) | 5.75 | Neon stronger — provides method, not just analysis |
| 1 | MAD (ShjMHfmPs0) | 6.67 | Neon stronger — method + analysis, not just analysis |
| 1 | Stability (JORAfH2xFd) | 6.75 | Neon stronger — goes beyond analysis to method |
| 1 | LeFusion (3b9SKkRAKw) | 8.00 | Comparable quality; Neon has more weaknesses |
| 2 | T-Stitch (2mqb8bPHeb) | 7.00 | Comparable; Neon has more theory, T-Stitch is cleaner |
| 2 | Consistency techniques (WNzy9bRDvG) | 7.00 | Neon has broader architectural scope |
| 2 | RepG (gWgaypDBs8) | 7.33 | Similar theory+method structure; Neon broader |
| 2 | Lipschitz Singularities (WNkW0cOwiz) | 7.50 | Comparable theory+method; Neon has broader experiments |
| 2 | Shortcut Models (OlzB6LnXcS) | 8.00 | Shortcut Models cleaner; Neon has γ confound issue |

**Round 1 bracket:** 6.5–8.0  
**Round 2 narrowed:** Neon sits between 7.00 (T-Stitch) and 7.33 (RepG). Neon has stronger theory and broader applicability than T-Stitch, but the γ co-optimization confound on the headline SOTA result prevents it from reaching the 7.5+ level. Score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>