Now I have sufficient evidence to write the final review. Let me synthesize everything.

---

## Summary

This paper introduces Content-Aware Mamba (CMIC), a learned image compression model that augments Mamba-style state-space models with two mechanisms: (1) Content-Adaptive Token Permutation (CTP), which reorders latent tokens via codebook-based clustering so that semantically similar tokens are scanned contiguously rather than by rigid raster order; and (2) Global-Prior Prompting (GPP), which injects sample-specific prompts tied to those same cluster centroids into the SSM output projection to provide global context. CMIC achieves state-of-the-art BD-rate reductions over VTM-21.0 (15.91% on Kodak, 21.34% on Tecnick, 17.58% on CLIC) while using substantially fewer parameters, FLOPs, and memory than prior Mamba-based compression models.

## Strengths

1. **CTP and GPP are well-motivated and their contributions are clearly isolated.** The paper identifies two concrete, well-articulated limitations of vanilla Mamba for image compression (rigid raster scan failing to group correlated tokens; strict causality limiting global context). The ablation study in Table 2 cleanly isolates each component: CTP alone yields 1.8–2.4% BD-rate improvement over a single-scan Mamba baseline across datasets; GPP alone yields 0.5–1.4%; together they produce 2.7–3.6% total gain. Removing either from the full model causes clear performance drops.

2. **State-of-the-art rate–distortion performance with strong efficiency.** CMIC surpasses VTM-21.0 by 15.91–21.34% BD-rate across three standard benchmarks (Table 1), outperforming all listed transformer-based and Mamba-based LIC models. Compared to MambaIC (the prior best Mamba-based LIC model), CMIC reduces parameters by 56%, FLOPs by 57%, decoding latency by 39%, and peak GPU memory by 78%, while achieving better compression. This is a convincing efficiency–performance trade-off.

3. **Thorough experimental validation beyond main results.** The paper includes: (a) component ablations (Table 2); (b) comparison against attention/convolution alternatives for the CAM block (Table 4); (c) cluster count ablations (Table 6); (d) cluster activation statistics showing content-adaptive behavior (Table 5); (e) throughput and inference overhead measurements (Table 3); (f) qualitative cluster visualizations demonstrating semantic interpretability (Fig. 10); and (g) global ERF comparisons across model families (Fig. 7). The training stability analysis in Appendix A.8 with multi-seed loss curves is also a welcome addition.

4. **The codebook-based clustering mechanism is practically effective.** Using a shared, EMA-updated codebook per CAM block (inspired by VQ-VAE) avoids the instability of online K-Means while remaining efficient at inference time. The cluster visualizations in Fig. 10 and activation statistics in Table 5 convincingly show that the learned centroids capture semantically meaningful groupings (e.g., doors, clouds, feathers) and adapt their active count per image (mean ~23–26 of 64 centroids active).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **The "soft clustering" used for the ERF analysis in Figure 9 is undefined and unvalidated.** The paper states (line 733) that the ERF for the non-causality visualization is computed "with soft clustering" but never defines what this means, how it relates to the hard-assignment clustering used in the actual model, or why the gradients computed through it faithfully reflect the hard-assignment behavior. The appendix acknowledges (line 1612) that "K-means clustering and token sorting are non-differentiable, the resulting gradients are biased," which makes the omission of a soft-clustering definition particularly problematic. The qualitative conclusions drawn from Figure 9 (that GPP enables "seeing beyond" the causal scan; that CTP spreads activation over semantically related locations) cannot be fully trusted without this methodological detail. This weakens the mechanistic narrative but does not invalidate the quantitative results in Table 2.

2. **The gradient discontinuity introduced by hard clustering is acknowledged only briefly in the appendix and its implications are not analyzed.** The main text (Section 3.3) describes the hard argmax clustering and EMA-based centroid updates without mentioning that the layers preceding the clustering receive no gradient signal through the cluster assignments. Appendix A.8 mentions that "resulting gradients are biased" and shows training stability curves, but the paper never discusses whether this non-differentiability leaves performance on the table compared to a fully differentiable alternative (e.g., Gumbel-Softmax routing). This is a transparency issue rather than a soundness issue, since training is empirically stable.

### Trivial

1. **The phrase "non-causality" in the section heading (line 732) and occasional causal language are slightly overstated.** The hidden state recurrence **h**_i = **Āh**_{i-1} + **B̄x**_i remains strictly causal; only the output projection is conditioned on the global prompt. The paper mostly uses the appropriately tempered verbs "relaxes" and "mitigates," but "Visualization of Non-Causality" as a heading and phrasing like "breaks the fixed Euclidean-neighbor constraint" could be toned down for precision. This is a wording issue with no bearing on the empirical results.

## Nice-to-Haves

- A comparison between the hard-assignment clustering and a soft, differentiable variant (e.g., Gumbel-Softmax routing) would directly test whether the broken gradient chain matters. This is not essential for acceptance but would strengthen the paper.
- The comparison with Zhang et al. (2024b)'s clustering scheme, currently relegated to Appendix A.2, would be more useful to readers if a concise version appeared in the main text.
- A brief discussion of the limitations of the proposed approach (e.g., scenarios where the clustering may fail, or what happens with out-of-distribution images) would round out the paper.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "Overclaiming non-causality given still-causal state update (Methodological gap)"** — REMOVED as a standalone major weakness. The paper consistently uses "relaxes" and "mitigates" (lines 93, 503, 841–842) rather than claiming full non-causality. This is appropriately tempered language. The section heading "Visualization of Non-Causality" is slightly overconfident, captured as a trivial wording issue above.

- **Strength Finder: Generic strengths** — REMOVED claims like "the paper identifies clear limitations" (this is restating the introduction, not a strength) and "the paper is generally well-written" (too generic). These are merged into the summary.

- **Harsh Critic: "Comparison with Zhang et al. (2024b) appears only in appendix"** — REMOVED. This is a presentation preference, not a weakness, and is listed as a nice-to-have above.

- **Harsh Critic: "Prompt dictionary design is directly derived from MambaIRv2... the difference is minor"** — REMOVED. The paper openly cites MambaIRv2 for the attentive state-space equation (line 495–497) and the novelty claim is explicitly about tying the prompt to clustering centroids, not about inventing the prompting mechanism. This is transparent attribution, not a weakness.

## Novel Insights

Beyond the paper's own contributions, the review process surfaces an interesting tension in SSM-based vision models: adding global context via output-projection modulation (GPP) is a lightweight alternative to multi-directional scanning that avoids quadrupling computation, yet it cannot fully substitute for bidirectional state updates. The paper demonstrates that this partial solution is sufficient for image compression, suggesting that for tasks where global context is primarily needed for output quality rather than state dynamics, prompt-based conditioning may be a broadly applicable design pattern. The cluster-activation analysis (Table 5: only ~36–41% of centroids active per image with high variance) also provides concrete evidence that codebook-based clustering naturally yields content-adaptive sparsity without explicit sparsity losses.

## Suggestions

- Define "soft clustering" precisely for Figure 9. If it is simply the use of cosine similarity scores as soft assignment weights during the backward pass (a straight-through estimator variant), state this explicitly and justify why it produces faithful ERF estimates. If it cannot be properly justified, consider replacing Figure 9's analysis with an alternative that does not rely on gradients through the clustering step (e.g., analyzing attention-equivalent patterns in the SSM output matrix **C**).
- Add a short paragraph in the main text (Section 3.3) acknowledging the gradient discontinuity and referencing Appendix A.8 for the stability evidence. Even a sentence like "The hard clustering breaks the gradient chain through the assignments; the centroids are updated via EMA, and the layers preceding the clustering learn through the reconstruction loss. We verify training stability in Appendix A.8" would substantially improve transparency.
- Tone down "Visualization of Non-Causality" to something like "Visualization of Global Context Injection" or "Effect of GPP on ERF."

## Score and Decision

### Anchor comparison:

- **MambaSIC** (`/home/wg25r/review_agent/human_reviews_2026/0dHrYUd17W.md`, avg 4.00): A Mamba-based stereo image compression paper with straightforward architecture adaptation, limited novelty, decent results. CMIC is substantially stronger in both novelty (two non-trivial mechanisms vs. one straightforward adaptation) and empirical validation (more thorough ablations, stronger relative gains over baselines).

- **SF-Mamba** (`/home/wg25r/review_agent/human_reviews_2026/X4KsowemNB.md`, avg 4.50): A vision Mamba paper addressing non-causal interactions with patch-swapping and batch folding. Novelty was questioned due to overlap with prior work and marginal downstream performance. CMIC has stronger empirical results, more clearly isolated component contributions, and a more compelling application-domain fit.

- **S³Mamba** (`/home/wg25r/review_agent/human_reviews_2026/42gPoLZLQB.md`, avg 4.50): Arbitrary-scale SR with SSMs. Similar mid-tier quality but with weaker empirical validation. CMIC is clearly stronger.

- **TS-Mamba** (`/home/wg25r/review_agent/human_reviews_2026/RygnSGcV49.md`, avg 5.50): Online video SR with SSMs, accepted as poster. Decent novelty and empirical results. CMIC has comparable or stronger empirical thoroughness and more clearly impactful domain results.

- **Mamba-3** (`/home/wg25r/review_agent/human_reviews_2026/HwCvaJOiCj.md`, avg 7.00, Oral): Major SSM architecture contribution with theoretical depth, three methodological innovations, rigorous proofs. CMIC lacks this theoretical depth but compensates with stronger domain-specific empirical validation and clear practical impact. CMIC scores below Mamba-3.

- **InfoTok** (`/home/wg25r/review_agent/human_reviews_2026/JEYWpFGzvn.md`, avg 7.33, Oral): Adaptive tokenization with strong information-theoretic grounding. CMIC has less theoretical depth but similarly strong empirical validation within its domain. CMIC scores below InfoTok.

- **Log-Normal SSM** (`/home/wg25r/review_agent/human_reviews_2026/XSsI8KXOed.md`, avg 2.67): Weak methodology, limited baselines, limited scale. CMIC is far stronger.

- **Generative Image Compression** (`/home/wg25r/review_agent/human_reviews_2026/YPOKlcOP1o.md`, avg 4.00): All 4s, limited novelty. CMIC is clearly stronger.

CMIC sits above the ~4.0–4.5 tier (MambaSIC, SF-Mamba, S³Mamba) and below the ~7.0+ Oral tier (Mamba-3, InfoTok). It is comparable to or slightly stronger than TS-Mamba (5.50, poster accept). Given the paper's clear motivation, well-isolated component contributions, thorough empirical validation, and SOTA results with efficiency gains — tempered by the unvalidated ERF analysis and unacknowledged gradient discontinuity — the paper merits acceptance as a poster.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>