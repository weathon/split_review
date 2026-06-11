## Summary
Neon is a post-hoc parameter-merging method that improves pre-trained generative models by first fine-tuning on self-synthesized data (which degrades quality) and then reversing that update via negative extrapolation: θ_Neon = (1+w)θ_r − wθ_s. The paper provides theoretical analysis (Theorems 1–2) proving that mode-seeking samplers induce anti-alignment between synthetic and real-data gradients, making this reversal effective. Empirically, Neon is evaluated across four model families (diffusion, flow matching, autoregressive, few-step) on three datasets, achieving consistent FID improvements with negligible compute overhead — including a state-of-the-art FID of 1.02 on ImageNet-256 with xAR-L.

## Strengths
- **Formal theoretical framework for why the method works**: Theorems 1 and 2 derive sufficient conditions (mode-seeking samplers → cos φ < 0 → s < 0 → Neon reduces risk), going well beyond heuristic motivation. The theory also correctly identifies the complementary regime (diversity-seeking samplers) where interpolation rather than extrapolation is appropriate (lines 171–172).
- **State-of-the-art result with negligible overhead**: xAR-L on ImageNet-256 improves from FID 1.28→1.02 (surpassing UCGM's 1.06) using only 0.36% additional training compute (line 209). The compute overhead is consistently <3% across all experiments.
- **Demonstrated universality across four model families**: Evaluations on diffusion (EDM-VP), flow matching, autoregressive (xAR, VAR), and few-step (IMM) models on ImageNet, CIFAR-10, and FFHQ show consistent FID improvements with specific numbers reported for each (EDM CIFAR-10: 1.78→1.38, flow matching CIFAR-10: 3.5→2.32, VAR-d16: 3.30→2.01, etc.).
- **Informative ablations that support the causal mechanism**: The CIFAR-10C null result (line 249) confirms the improvement is specific to anti-alignment with the model's own modes, not generic out-of-distribution data. Figure 9 shows Neon compensates for a 40% reduction in real training data. Cross-architecture transfer (Figure 8) is a novel property not established by prior methods.
- **Transparent identification of failure regimes**: The paper explicitly discusses when Neon would not work (diversity-seeking samplers, lines 171–172) and characterizes the precision-recall trade-off mechanism (Figure 4).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Joint (w, γ) optimization for autoregressive models makes it hard to isolate Neon's standalone contribution**: For xAR-L, the headline FID improvement from 1.28→1.02 involves jointly optimizing both the merge weight w and CFG scale γ. The paper does not report what FID would be with Neon at the baseline-optimal γ, making it impossible to fully attribute the gain to Neon vs. expanded CFG tuning range. While the paper provides this breakdown for VAR-d16 (independent γ gives 3.01, joint gives 2.01, lines 227–228), the analogous ablation is missing for the flagship xAR-L result. This does not invalidate the method — joint tuning is presented as a feature — but it tempers the headline claim.
- **No controlled comparison against the most closely related methods**: The related work discusses DDO, SIMS, and Discriminator Guidance (line 60), and the paper distinguishes Neon from them on simplicity/universality grounds, but provides no quantitative comparison on shared architectures/benchmarks. At least one controlled comparison (e.g., Neon vs. DDO on xAR or VAR) would help substantiate the significance claim.
- **No confidence intervals or variance estimates for any FID numbers**: While FID with 50k reference samples has low variance, reporting results from multiple runs or multiple synthetic dataset seeds would strengthen confidence, especially for small-|S| settings where the paper's own analysis (line 173) notes variance is a limiting factor.
- **No dedicated limitations section**: The paper does not discuss limitations such as the precision-recall trade-off (precision decreases with w, as shown in Figure 4), the need for joint (w, γ) tuning for autoregressive models, and the theoretical small-‖ε‖ requirement, though the empirical results suggest robustness to this condition.

### Trivial
None.

## Nice-to-Haves
- Direct empirical measurement of the theoretical quantities s (alignment) and cos φ on real-scale models to further confirm the anti-alignment mechanism at scale, beyond the 2D Gaussian toy example.
- An explicit test of the mode-seeking dependency: generating synthetic data with a diversity-seeking sampler (τ > 1 for autoregressive models, or no CFG for diffusion) and verifying that interpolation (w < 0) rather than extrapolation (w > 0) then helps.

## Removed Points
These points are flagged to be removed; treat them with caution:
- **"No access to original training data" as overstatement**: The paper accurately states Neon requires no access to original training data. Neon only needs the base model checkpoint and does not access the original dataset during its procedure. The harsh critic's framing of this as an overstatement is incorrect.
- **Proofs deferred to appendix**: The reviewer notes that Theorem 2's proof is in Appendices B.6–B.7 and conditions like A-MONO cannot be evaluated. The appendix exists in the original submission — it was stripped by the PDF parser (line 283: "Rest of paper (reference and Appendix) is removed"). This is a parser artifact, not a paper issue.
- **Theory not empirically validated at scale / results could be explained by simpler regularization story**: The paper provides multiple indirect validations specifically predicted by the theoretical framework (CIFAR-10C null result, precision-recall analysis, Figure 9 on base model quality, U-shaped |S| relationship). Direct measurement of s and cos φ is a reasonable extension but not a flaw in the current work — many theory papers in ML provide explanatory mechanisms consistent with but not uniquely proven by experiments. Moving this to "Nice-to-Haves."
- **Strength Finder's strength about formal proof**: Verified and retained.
- **Strength Finder's strength about cross-architecture transferability**: Verified and retained.
- **Generic/superficial strengths from Strength Finder**: Removed any that conflict with verified weaknesses.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- For the xAR-L SOTA claim, report Neon's FID at the baseline-optimal γ alongside the jointly-optimized result, so readers can attribute the gain to Neon vs. expanded γ tuning.
- Add at least one controlled comparison against DDO (or another applicable method) on a shared architecture (e.g., VAR or xAR on ImageNet-256).
- Report FID variance across multiple runs or synthetic dataset seeds for key results.
- Add a brief limitations paragraph covering the precision-recall trade-off, the need for joint tuning with autoregressive models, and the small-‖ε‖ theoretical condition.

---

## Calibration Report

### Round 1 — Bracketing

**Low band (<3.5)**: Queried "parameter merging for generative models image generation" with high_score=3.5. Retrieved papers avg 2.50–3.40 — e.g., Conditional LoRA Parameter Generation (3.40), ATM: Alternating Tuning and Merging (3.00). These are clearly weaker than Neon in both contribution and execution.

**Middle band (3.5–7.5)**: Queried "improving diffusion models with post-hoc methods self-training synthetic data" with low_score=3.5, high_score=7.5. Retrieved papers avg 4.00–6.60 — e.g., Real-Fake (6.00), Diffusion Feedback Helps CLIP (6.60), Diff-2-in-1 (5.80).

**High band (>7.5)**: Queried "state-of-the-art image generation on ImageNet FID improvement theoretical analysis" with low_score=7.5. Retrieved papers avg 8.00 — e.g., One Step Diffusion via Shortcut Models (8.00), SDXL (8.00), Strong Model Collapse (8.00), NoiseDiffusion (8.00). These are landmark-scale works.

**Initial bracket**: [5.5, 7.5]

### Round 2 — Narrowing

Queried "parameter merging post-hoc improvement generative models image synthesis" (low=3.5, high=6.5) and "theory of synthetic data model collapse self-training reversal" (low=5.0, high=7.5). Retrieved anchors:

| Anchor | Avg Score | Round | Comparison to Neon |
|--------|-----------|-------|-------------------|
| Real-Fake: Effective Training Data Synthesis (svIdLLZpsA) | 6.00 | R1 | Weaker: similar theoretical framing but narrower evaluation scope; concerns about limited novelty |
| Diffusion Feedback Helps CLIP (tLFWU6izoA) | 6.60 | R1 | Weaker: similar post-hoc improvement approach but more heuristic design choices, weaker theory |
| LCSC: Checkpoint Averaging (QowsEic1sc) | 6.00 | R2 | Weaker: simpler contribution, less surprising, narrower model coverage |
| Diffusion-NPO (iJi7nz5Cxc) | 7.00 | R2 | Comparable: similar simple+effective method, but Neon has stronger theoretical foundations (formal theorems) and broader architecture coverage |
| Stability of Iterative Retraining (JORAfH2xFd) | 6.75 | R2 | Weaker: similar theory+empirical, but Neon has more convincing experiments and fewer concerns about assumptions |
| Self-Consuming Models Go MAD (ShjMHfmPs0) | 6.67 | R1 | Weaker: analysis-only (no improvement method), empirical breadth less than Neon |
| STL Theory Perspective (WttfQGwpES) | 6.67 | R2 | Comparable theory depth, but weaker on empirical validation |
| Model Collapse Chain of Diffusion (P5UETqZXqT) | 5.75 | R2 | Weaker: describes collapse but proposes no reversal method |

### Final Score Determination

Neon is stronger than all mid-band anchors except Diffusion-NPO (7.00), to which it is comparable or slightly superior due to its formal theoretical framework (Theorems 1–2) and coverage of four model families vs. diffusion-only. It is weaker than the high-band anchors (Shortcut Models, SDXL), which are landmark-scale works with broader impact. The weaknesses are all minor and addressable. Therefore the final score is **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>