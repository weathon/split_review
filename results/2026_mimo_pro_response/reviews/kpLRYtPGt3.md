Now I have enough calibration data. Let me synthesize the final review.

## Summary
This paper introduces Neon (Negative Extrapolation frOm self-traiNing), a post-hoc parameter merge technique that improves generative models by reversing the degradation direction caused by fine-tuning on self-generated synthetic data. The authors prove that mode-seeking inference samplers create a predictable anti-alignment between synthetic and real-data population gradients, enabling negative extrapolation to reduce true data risk. Neon achieves state-of-the-art FID of 1.02 on ImageNet-256 with xAR-L using only 0.36% additional compute, and is demonstrated across diffusion, flow matching, autoregressive, and few-step generator architectures.

## Strengths
- **Rigorous theoretical grounding with concrete, falsifiable predictions**: The paper provides Theorems 1 and 2 (Section 3.1, Eq. 4–6) connecting inference sampler properties to gradient anti-alignment. The Taylor expansion (Eq. 4) predicts a U-shaped FID vs. w curve and optimal w* ≈ −s/(αz) decreasing with fine-tuning steps, both empirically confirmed in Figure 4. The 2D Gaussian toy (Figure 2, Eq. 3) provides clear geometric intuition.

- **Demonstrated universality across four fundamentally different model families**: Neon is evaluated on diffusion (EDM-VP, Section 4.1), flow matching (Section 4.1), autoregressive (xAR-B/L, VAR-d16/d30, Section 4.2), and few-step generators (IMM, Section 4.3) across CIFAR-10, FFHQ-64, ImageNet-256, and ImageNet-512. This architecture-agnostic nature is a direct advantage over DDO (requires likelihood computation, cannot apply to flow matching or IMM) and Discriminator Guidance/SIMS (diffusion-specific).

- **State-of-the-art results with negligible compute overhead**: Neon elevates xAR-L from FID 1.28 to 1.02 on ImageNet-256 (0.36% additional compute, 750k samples), surpassing UCGM's 1.06 (Section 4.2). On FFHQ-64, EDM-VP improves from 2.39 to 1.12 (0.85% extra compute). For IMM, 4-step Neon (FID 1.69) nearly matches 8-step base quality (1.98), effectively halving inference cost with <0.005% of IMM's training compute (Section 4.3). Even with just 1k samples, xAR-L achieves FID 1.05.

- **Quantified mechanism via precision-recall decomposition**: Figure 4 dissects Neon's effect showing precision monotonically decreases with w while recall follows an inverted-U peaking near the FID-optimal weight, matching the quadratic prediction from Eq. 4. This provides mechanistic evidence that Neon redistributes probability mass from over- to under-represented modes.

- **Cross-architecture transfer with null-result control**: Figure 8 shows synthetic data from a flow matching model improves EDM-VP (FID 1.59 from 1.97) and IMM data similarly helps (FID 1.80), with theoretical justification via spectral closeness of Hessians (Appendix B.8). Crucially, CIFAR-10C corrupted images produce no improvement (Section 4.4), confirming the signal requires model-generated data specifically.

## Weaknesses

### Fatal
None

### Major
- **Entanglement of Neon contribution with CFG re-optimization for autoregressive models**: For autoregressive models, the paper jointly optimizes merge weight w and CFG scale γ at evaluation time (line 207: "At evaluation, we jointly optimize both the merge weight w and CFG scale γ"). Figure 6 shows γ-only optimization yields FID 3.01 vs. joint optimum 2.01 for VAR-d16. While Figure 6 demonstrates w=0 across all γ never reaches the joint optimum (confirming Neon is a necessary component), and the diffusion/flow experiments validate Neon independently without CFG co-optimization (Section 4.1), the headline ImageNet-256 results do not cleanly decompose the individual contributions. A straightforward ablation — holding γ fixed at its base-model optimal while varying only w — would directly quantify Neon's isolated contribution on ImageNet and make the headline results more interpretable.

### Minor
- **A-MONO assumption for diffusion/flow models is stated but not empirically verified**: Theorem 2 guarantees anti-alignment for mode-seeking samplers unconditionally for autoregressive models, but for diffusion and flow models (Footnote 2, line 161), the guarantee requires an additional "curvature-density coupling" assumption (A-MONO). This is stated as an assumption rather than verified empirically. The empirical results validate Neon works for diffusion/flow, but a simple empirical check would strengthen the theoretical contribution for this model family.

- **No comparison against naïve weight-averaging baselines**: The paper does not compare Neon against simple model merging methods (e.g., averaging θ_r with an independently trained checkpoint). While the theoretical analysis explains why the specific anti-aligned direction is valuable, an empirical comparison against generic parameter interpolation would sharpen the contribution.

### Trivial
None

## Nice-to-Haves
- Exploring multiple rounds of Neon (applying it iteratively to the already-improved model) would be informative.
- Including generation cost in the compute accounting — for xAR-L, generating 750k high-quality ImageNet samples has non-trivial cost beyond fine-tuning compute.
- Testing base model quality robustness across a wider FID range (Figure 9 only tests ~1.85–1.87 range on CIFAR-10).

## Removed Points
These points are flagged to be removed, treat them with caution:
- Criticisms about missing appendix content, proofs, or supplementary materials are removed per rules (appendix stripped by parser).
- Formatting or style nitpicks are removed (parser artifacts, not author issues).
- Questions about existence/availability of cited models or datasets are removed per hard rules.

## Novel Insights
The paper's most genuinely novel conceptual contribution is reframing self-training degradation not as noise or failure, but as a structured, exploitable anti-aligned gradient signal that can be mathematically characterized. The formal proof that mode-seeking samplers (temperature < 1, top-k, top-p, CFG) guarantee this anti-alignment (Theorem 2) is a genuine theoretical insight that explains both why naïve self-training fails and why reversing it succeeds — this connects previously disparate observations about model collapse and synthetic data training under one framework. The cross-architecture transfer result (degradation signal is portable because models with similar representations share similar overconfidence patterns) is a practically important secondary insight.

## Suggestions
- Add an ablation holding γ fixed at base-model optimal while varying only w for xAR-L/VAR-d16 on ImageNet-256 to decompose the individual contributions.
- Include a brief empirical verification of the A-MONO assumption for at least one diffusion model (e.g., plot E[‖∇_x f‖² | x_0] vs. log p(x_0)).
- Consider adding a comparison against naïve weight averaging as a baseline.

## Calibration Report

**Round 1 anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| u1cQYxRI1H | 0.50 | R1 | Not relevant (diffusion for illumination editing, misretrieved) |
| Uj0h13lVrR | 1.00 | R1 | Much weaker paper (GFlowNet optimization, low scores) |
| 5lUdTogEL3 | 1.00 | R1 | Much weaker (person re-ID, unrelated) |
| 5kMwiMnUip | 1.40 | R1 | Much weaker (jailbreaking LLMs, unrelated) |
| 2o58Mbqkd2 | 3.25 | R1 | Weaker (combining diffusion models, less practical impact) |
| lNtio1tdbL | 3.00 | R1 | Weaker (model merging via task vectors, narrower scope) |
| f7Zq9CqQEM | 3.40 | R1 | Weaker (text-to-3D, narrower scope) |
| LyJi5ugyJx | 2.38 | R1 | Anchored as 9.2 actual (consistency models - much stronger fundamental contribution) |
| b9dBNNeDd3 | 4.60 | R1 | Weaker (set autoregressive modeling, rejected) |
| zfIxlvKq4u | 4.00 | R1 | Weaker (AR design space exploration, rejected) |
| BYoN2c0o6M | 4.00 | R1 | Weaker (M-VAR, rejected) |
| DLBlR0rea5 | 4.50 | R1 | Weaker (diffusion on abstract rules, rejected) |
| svIdLLZpsA | 6.00 | R1 | Comparable but NEON is stronger (Real-Fake, synthetic data for classification) |
| S5EqslEHnz | 5.60 | R1 | Weaker (generated data for contrastive learning) |
| CjPt1AC6w0 | 6.25 | R1 | Comparable but NEON has stronger results (synthetic data for transfer learning) |
| FKksTayvGo | 7.00 | R1 | Comparable (DDBM, novel formulation, good theory) |
| RuP17cJtZo | 8.00 | R1 | Comparable in quality (Generator Matching, strong theoretical framework) |
| 25kAzqzTrz | 8.00 | R1 | Comparable (FixMatch generalization theory, strong theory) |
| et5l9qPUhm | 8.00 | R1 | Most topically relevant (Strong Model Collapse, rejected with all 8s) |
| g7ohDlTITL | 8.00 | R1 | Slightly stronger (Riemannian Flow Matching, fundamental framework) |
| WNzy9bRDvG | 7.00 | R2 | Comparable (Improved Techniques for CMs, practical improvement) |
| tLFWU6izoA | 6.60 | R2 | Weaker (Diffusion Feedback for CLIP) |
| 5BSlakturs | 7.33 | R2 | Weaker (compositional T2I, narrower scope) |
| ff2g30cZxj | 7.33 | R2 | Weaker (posterior sampling for image restoration) |
| oI5tZaWkF9 | 7.50 | R2 | NEON is stronger (LLM data weighting for text classification) |
| 07yvxWDSla | 8.00 | R2 | Comparable (synthetic continued pretraining, strong practical impact) |

**Round 1 bracket:** Between 7.0 and 8.5. NEON is clearly above the 6.0-7.0 range papers (Real-Fake, DDBM, Improved CMs) due to stronger theory, broader experiments, and SOTA results. NEON is comparable to the 8.0 papers (Generator Matching, FixMatch generalization) but with a more focused, practically impactful contribution. NEON falls below 9.0+ (sCM at 9.2) which has more fundamental theoretical contribution.

**Final score:** 7.5 — NEON has strong theory, broad empirical validation, new SOTA results, and remarkable simplicity. The CFG co-optimization entanglement for autoregressive models is the main substantive weakness preventing a higher score, but it is partially mitigated by the independent diffusion/flow validation. The paper clearly outperforms the 7.0 anchors and is close to but slightly below the 8.0 anchors due to the CFG issue and the unverified A-MONO assumption.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>