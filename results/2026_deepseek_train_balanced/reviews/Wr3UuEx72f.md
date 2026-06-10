## Summary

This paper introduces LARP, a video tokenizer for autoregressive generative models that replaces standard patchwise tokenization with a learned query-based holistic scheme. By decoupling token count from patch count and co-training a lightweight 21.7M-parameter AR transformer as a prior during training (discarded at inference), LARP shapes the discrete latent space for generation rather than reconstruction. On UCF-101, LARP achieves 57 FVD, outperforming all published methods including MAGVIT-v2-MLM (58 FVD), and its ablation study cleanly demonstrates that the AR prior is responsible for a 190→107 gFVD improvement while reconstruction quality degrades — directly supporting the paper's central thesis.

## Strengths

1. **State-of-the-art FVD of 57 on UCF-101 class-conditional generation (Table 1).** LARP outperforms all published methods including the closed-source MAGVIT-v2-MLM (58 FVD) and MAGVIT-v2-AR (109 FVD). Within the AR model family, LARP roughly halves the best prior result, and this holds with a generator size (632M) that is *smaller* than MAGVIT-v2-AR's (840M).

2. **Ablation cleanly isolates the AR prior model's effect (Table 2, lines 354–358).** Removing the AR prior model degrades gFVD from 107 to 190 (a 78% increase) while *improving* rFVD from 31 to 23. This divergence is the exact signature of the claimed mechanism — the prior optimizes the latent space for generation, not reconstruction — and is the paper's most compelling evidence.

3. **Holistic query-based tokenization decouples token count from patch count (Section 3.2, Eq. 3).** The learned query design means the number of discrete tokens (256/512/1024) is independent of the number of patches (1024), eliminating the flattening-order problem that plagues patchwise tokenizers. Figure 2(b) empirically demonstrates this flexibility.

4. **Continuous AR transformer design solves a real technical challenge (Section 3.3, lines 193–202).** Replacing the AR model's embedding look-up with a linear projection and using SVQ-style cosine-similarity outputs enables gradient flow from the AR loss into the evolving discrete codebook during training — a nontrivial engineering contribution.

5. **Scheduled sampling for the evolving codebook (Section 3.3, lines 204–210).** The two-round token mixing strategy addresses the mismatch caused by the codebook shifting during training. Ablation confirms its importance (107→142 gFVD without it).

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are supported by the evidence.

### Minor

- **The "optimal token order" claim is asserted without evidence (line 379).** The conclusion states LARP "defines an optimal token order," but the paper provides no analysis of what ordering emerges, whether it has any spatial or semantic structure, or how it compares to alternatives (raster scan, random, etc.). The improvement from the AR prior could plausibly come entirely from latent space shaping independent of any ordering effect. This is an overclaim: the paper should either provide evidence (e.g., visualization of learned query positions) or soften the language (e.g., "a learned order suited for AR generation").

- **The headline UCF101 result (57 FVD) uses a 632M AR generator vs. MAGVIT-v2-MLM's 307M (Table 1).** A controlled comparison at equal generator size is missing. LARP-L-Long with the 343M generator achieves only 102 FVD on UCF101 — substantially worse than MAGVIT-v2-MLM's 58 — suggesting that some of the headline gains come from generator scale rather than the tokenizer alone. The paper acknowledges this in passing (line 290: "Our best results are obtained with a larger AR generator") but does not provide the cleaner experiment.

- **LARP's reconstruction FVD (20–24) lags significantly behind MAGVIT-v2 (8.6) (Table 1).** The paper notes this as a design feature (line 372), but it also means the tokenizer is substantially less faithful for any downstream use that prioritizes reconstruction fidelity. This tradeoff is not discussed as a limitation.

- **On K600 frame prediction, LARP (5.1 FVD) trails MAGVIT-v2-MLM (4.3 FVD) (Table 1).** The paper does not discuss this gap. While LARP outperforms all AR methods on K600 (which the paper correctly claims), the comparison with the leading MLM method is relevant context that is absent from the discussion.

- **No limitations section.** The paper should discuss: (a) the reconstruction-quality gap vs. MAGVIT-v2, (b) reliance on CFG (the "No CFG" ablation sees gFVD degrade from 107 to 121), (c) the computational cost of two-round scheduled sampling per iteration, and (d) whether the method scales to higher resolutions (only 128×128 is tested).

- **The relative weighting of reconstruction loss components (L1, LPIPS, GAN, SVQ) is not specified (line 183).** These weights are important for reproducibility. Only the AR prior loss weight (α=0.06) is reported.

- **The generator size used in ablation/scaling experiments (LARP-B, LARP-S) is not reported.** The ablation table (Table 2) and scaling experiments use LARP-B with "the default AR model" (line 301), but the size of this generator is never stated. This makes it impossible to compare the ablation baselines against Table 1 results.

### Trivial

- **CFG guidance scale not reported.** The ablation shows CFG matters (107→121 without it), but the scale used is never specified.
- **Only point estimates of FVD are reported.** Given known FVD variance, confidence intervals or multiple-seed results would strengthen comparisons.
- **Generator architecture details for baselines are listed only by parameter count** (depth, width, other design choices not reported).

## Nice-to-Haves

- An experiment freezing the learned queries at their positions but randomizing their indices before AR training. If gFVD degrades, the ordering matters; if not, the improvement comes purely from latent space shaping (as suggested by the critic).
- A controlled comparison with MAGVIT-v2-MLM using the same generator size and architecture on UCF101.
- An ablation comparing the holistic query-based tokenizer against a patchwise variant with the same ViT backbone and parameter count, both with and without the AR prior, to separate the contributions of the holistic architecture from the AR prior.
- Discussion of statistical significance / confidence intervals.

## Removed Points

These points were flagged by reviewers but are removed after verification against the paper:

- **"Global vs. local distinction is overstated"** — The critic argued that ViT-based patchwise tokenizers already produce global representations via self-attention. However, the paper's claim is about the *tokens* being tied to specific patch locations (each token corresponds to a spatial position), not about the encoder's representational capacity. The paper clarifies this in Section 3.1 (lines 119–121): "the latent vector at each position is typically the direct output of its spatialtemporally corresponding input video patch." This is a genuine architectural difference, not a framing error.

- **"SOTA claim is selectively emphasized / misleading"** — The paper carefully scopes its SOTA claim to UCF101 in every mention (abstract line 11, introduction line 51, contributions line 57). On K600, it only claims outperforming *AR methods* (line 57: "outperforming all AR methods on the K600 frame prediction benchmark"), which is true. The critic's reading that the overall impression is "misleading" does not hold up against the paper's precise language.

- **"Visualization comparison only against weak baseline"** — The critic criticizes visual comparisons for showing only OmniTokenizer. OmniTokenizer is the most recent video tokenization baseline in the table and the only one with comparable rFVD to LARP. The comparison is reasonable.

- **"Missing related works"** — Removed per hard rule.

- **"Formatting/typo/style nitpicks"** — Removed per hard rule.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's central thesis — that the AR prior shapes the latent space for generation, not reconstruction — but do not surface an independent novel observation.

## Suggestions

1. Provide a controlled comparison at equal generator size (e.g., LARP tokenizer + 307M generator vs. MAGVIT-v2-MLM, 307M) to cleanly attribute the UCF101 gains.
2. Either provide evidence for the "optimal order" claim (e.g., visualize the learned query positions' structure) or soften the language throughout the paper.
3. Add a limitations section that honestly discusses the reconstruction-quality tradeoff, CFG reliance, and K600 gap vs. MAGVIT-v2-MLM.
4. Report the reconstruction loss component weights and the CFG guidance scale.
5. Specify the generator size used in the ablation and scaling experiments.

## Score and Decision

The paper makes a genuine contribution: the holistic query-based tokenizer with co-trained AR prior is novel, clearly motivated, and convincingly supported by the ablation study. The UCF101 result (57 FVD) is a meaningful advance, and the ablation showing 190→107 gFVD improvement from the AR prior is compelling evidence for the mechanism. The weaknesses are in framing (the "optimal order" overclaim), missing controlled comparisons (unequal generator size for headline result), and omitted details (loss weights, CFG scale, generator sizes in ablations) — none of which are fatal. These are addressable in a revision.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>