## Summary

Neon (Negative Extrapolation from Self-Training) proposes a post-hoc method that improves generative models by: (1) briefly fine-tuning on the model's own synthetic outputs, then (2) extrapolating away from the resulting degraded weights via a simple parameter merge: θ_Neon = (1+w)θ_r - wθ_s. The paper provides theoretical grounding (Theorems 1–2) showing that mode-seeking inference samplers induce anti-alignment between synthetic and population gradients. Experiments span diffusion, flow matching, autoregressive, and few-step architectures on ImageNet, CIFAR-10, and FFHQ, with the headline result of xAR-L reaching FID 1.02 on ImageNet-256 using 0.36% additional compute.

## Strengths

1. **Theoretically grounded mechanism with formal guarantees.** Theorems 1 and 2 provide a rigorous sufficient condition under which mode-seeking samplers (temperature<1, top-k, CFG, finite-step ODE solvers) guarantee gradient anti-alignment (cos φ < 0), which negative extrapolation exploits to reduce true data risk. The theory also correctly identifies the complementary interpolation regime for diversity-seeking samplers, demonstrating understanding of boundary conditions.

2. **Consistent quantifiable improvements across four distinct architecture families.** Diffusion (EDM-VP CIFAR-10: 1.78→1.38), flow matching (CIFAR-10: 3.5→2.32), autoregressive (xAR-L ImageNet-256: 1.28→1.02; VAR-d30 ImageNet-512 →1.69), and few-step generators (IMM T=8 ImageNet-256: →1.46). This breadth distinguishes Neon from architecture-specific methods.

3. **Minimal compute overhead precisely reported throughout.** Every experimental result includes additional compute as a fraction of base training budget (e.g., 0.36% for xAR-L, 0.85% for FFHQ-64, <0.005% for IMM). The method uses as few as 1k synthetic samples and requires no real data, no auxiliary models, and no inference modifications.

4. **Comprehensive ablations addressing the natural skeptical questions.** (a) Base-model quality (Fig 9): Neon works even on models trained with only 30k real samples. (b) Synthetic data quality (Fig 10): varying CFG scale γ ∈ [1,3] yields near-identical final FID (1.30–1.31). (c) Cross-architecture transfer (Fig 8): flow matching and IMM data improve EDM-VP. (d) CIFAR-10C null result cleanly isolates the effect as specific to model-generated data.

5. **Careful characterization of the (w, γ) interaction for autoregressive models.** Figure 6 shows joint optimization is crucial: independent γ-tuning yields FID 3.01 vs. joint (w, γ) yields 2.01 for VAR-d16 — a nearly 1 FID-point difference — providing practical deployment guidance.

## Weaknesses

### Major

1. **No direct empirical comparison to related methods on shared base-model checkpoints.** The paper compares Neon against published numbers (UCGM's 1.06) and positions it against DDO, SIMS, Discriminator Guidance, and Self-Play FT on qualitative grounds (architecture-specific, requires auxiliary models, inference-time modifications). It does not re-implement or run any of these methods on the same base checkpoints. The SOTA claim (xAR-L + Neon = 1.02 vs. UCGM = 1.06) is a cross-architecture comparison; for all we know, DDO applied to xAR-L could achieve FID < 1.02. Without apples-to-apples evidence, the paper's comparative claims are weaker than its methodological claims. This gap is significant because the paper's narrative explicitly contrasts Neon's simplicity against these methods' overhead.

### Minor

2. **Gap between theoretical assumptions and empirical verification.** The sufficient conditions in Theorems 1 and 2 involve spectral constants m, M, error norms, sampler bias terms η0, η1, and cos φ that are never estimated for any of the models evaluated. The "small error" condition (‖ε‖ small) is violated by many models in Figure 9 that still benefit from Neon. The A-MONO assumption for diffusion/flow models (footnote 2) is a non-trivial caveat deferred to an appendix. The theory provides intuition but is not directly verified to hold in the experimental setting.

3. **No variance or uncertainty reporting for FID.** FID has known sampling variability (0.05–0.10 across evaluation runs or different synthetic draws); single-run results without confidence intervals or multiple seeds make it hard to assess the statistical significance of improvements, especially for smaller deltas (e.g., 1.28→1.02 vs. 1.78→1.38).

4. **Transferability experiment scope is limited.** Cross-architecture transfer (Figure 8) tests only one target model (EDM-VP) with three source models. Reversing the direction or testing other model families as targets would strengthen the claim.

### Trivial

5. Compute overhead reported only as a percentage of base training budget; providing absolute wall-clock time would help practitioners whose training costs vary enormously across architectures.

## Nice-to-Haves
- Estimate anti-alignment s empirically for one small model to directly verify cos φ < 0.
- Test transferability in the reverse direction (e.g., improving an autoregressive model with diffusion-generated data).
- Report FID with confidence intervals over multiple evaluation runs or synthetic dataset draws.

## Removed Points

These points were removed after cross-checking against the paper; they are not valid weaknesses:

- **"SOTA claim presented as settled fact"**: The paper explicitly names UCGM's 1.06 as the comparison point (Section 4.2, Fig. 5 caption). The claim is specific and transparent. The substantive concern about comparison scope is retained in Major weakness #1.
- **"Paper does not independently verify that DDO cannot apply to likelihood-free architectures"**: This is a statement about DDO's own claimed limitations, reported accurately. Not a weakness of Neon.
- **"Theory is overstated"**: The paper states "we prove rigorously that mode-seeking inference samplers create a predictable anti-alignment" — this is true as a mathematical statement under the stated assumptions (Theorems 1–2). The gap between assumptions and practical verification is captured in Minor weakness #2.
- **Strength Finder generic statements** (e.g., "important problem"): Removed; only evidence-grounded strengths retained.
- **Harsh Critic speculations about missing appendix content**: The appendix is removed by the parser; these criticisms cannot be verified and are excluded per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions
- Add a direct comparison to at least one related method (DDO or SIMS) on a shared public checkpoint (e.g., EDM-VP on CIFAR-10). This single experiment would substantially strengthen the comparative claims.
- Empirically compute cos φ or the alignment s for a small model to bridge the theory-experiment gap.
- Report FID with standard deviations over multiple evaluation runs.

## Calibration Anchors

**Round 1 (bracketing):**
| Path | Avg Score | Comparison |
|------|-----------|------------|
| JJH7m9v4tv.md (Post-hoc Discriminator Guidance) | 3.00 | Much weaker; limited evaluation, less novel |
| oOa3ZCtMjJ.md (GAN + CLIP) | 3.00 | Much weaker; incremental combination |
| GXXQfSpJNI.md (Fair Image Generation) | 2.33 | Much weaker; limited experiments |
| W4djmqKZC6.md (Pixel-Aware Diffusion) | 3.00 | Much weaker; incremental tweak |
| Xr5iINA3zU.md (Collapse or Thrive?) | 5.75 | Weaker; analytical only, no improvement method |
| P5UETqZXqT.md (Model Collapse Chain) | 5.75 | Weaker; analytical study of collapse |
| ShjMHfmPs0.md (Self-Consuming MAD) | 6.67 | Weaker; studies collapse but proposes no improvement method |
| JORAfH2xFd.md (Stability Iterative Retraining) | 6.75 | Weaker; analytical framework |
| I5lcjmFmlc.md (Robust Classification via Diffusion) | 8.00 | Different topic (classification) |
| OlzB6LnXcS.md (Shortcut Models) | 8.00 | Stronger; cleaner comparisons, uniformly high scores |
| CxXGvKRDnL.md (Progressive Compression) | 8.00 | Different topic |
| 6O3Q6AFUTu.md (NoiseDiffusion) | 8.00 | Different topic |

**Round 2 (narrowing, bracket 6.0–7.5):**
| Path | Avg Score | Comparison |
|------|-----------|------------|
| 6p74UyAdLa.md (Dynamic Negative Guidance) | 6.25 | Weaker; limited to MNIST/CIFAR-10, missing ImageNet |
| gWgaypDBs8.md (Representative Guidance) | 7.33 | Comparable; diffusion-only, similar comparison gap |
| KZgo2YQbhc.md (PaRa) | 7.50 | Comparable; similar missing-SOTA-comparison weakness but accepted |
| FoMZ4ljhVw.md (PnP Inversion) | 6.50 | Different topic |
| 1v7SRWsYve.md (MAP Model Merging) | 6.33 | Different topic |
| 88JJjsLtqr.md (Less is More) | 6.50 | Different topic |

**Round 1 bracket:** Clearly above 3.0–6.0 range, comparable to 6.0–7.5 range.  
**Round 2 narrowing:** Neon is stronger than DNG (6.25) due to broader evaluation (ImageNet-256 vs. MNIST/CIFAR-10). It is comparable to RepG (7.33) and PaRa (7.50) in overall quality; like those papers it has a known comparison gap, but its gap is more central to the narrative (direct competitors DDO/SIMS not compared on same checkpoints). The uniformly strong Shortcut Models (8.00) has no such gap and cleaner evaluation — Neon falls below that tier. Final score: **7.0**.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>