Now I have a clear picture. Let me write the final consolidated review.

## Summary

This paper introduces PI-CCA, a replay-free continual learning framework for vision-language models that preserves cross-modal alignment geometry via compact "CCA certificates" — sketched summaries of the top-k canonical correlations and subspaces. During adaptation on new tasks, the method enforces spectral and subspace-angle consistency with the certificate using only mini-batch statistics, while prompt invariance is induced by averaging the certificate over prompt perturbations. The method is evaluated across four benchmark tracks (MTIL, X-TAIL, VLCL, ConStruct-VL) and achieves state-of-the-art results among replay-free methods, with ablations confirming both the spectral and subspace terms are necessary for the reported gains.

## Strengths

- **Novel, principled approach to replay-free VL-CL.** The core idea — directly preserving the CCA geometry (canonical correlations and subspaces) of the whitened cross-modal covariance — is a clean departure from prior work that regularizes proxy signals (logits, similarities, parameters). The paper correctly identifies that these proxies "regularize outcomes rather than directly controlling the alignment object." The use of random orthonormal sketches (R_v, R_t) to keep the certificate memory constant in the feature dimension (h×k with h ≪ d_v, d_t) is well-motivated, and the Pareto analysis in Fig. 2 shows a broad efficient ridge (k∈[48,96], h∈[192,320]) where both memory and step time are practically acceptable.

- **Consistent state-of-the-art across four diverse benchmarks.** Tables 1 and 2 show PI-CCA outperforming all replay-free baselines on MTIL (76.8 Avg, +1.6 over C-CLIP), X-TAIL (68.1 Avg, +1.8 over C-CLIP), VLCL retrieval (48.6 I2T R@1, +2.5 over C-CLIP), and ConStruct-VL (75.2 FA / 2.7 AF). Notably, it surpasses the synthetic-replay method GIFT on VLCL without storing or generating any data. The evaluation covers classification, task-agnostic, retrieval, and structured-concept tracks, providing strong evidence that the method generalizes across VL-CL settings.

- **Ablation confirms both spectral and subspace terms are necessary.** Table 3 shows that removing the spectral term (λ₁=0) drops MTIL Avg by 2.5 points and VLCL R@1 by 2.3; removing the subspace term (λ₂=0) drops MTIL Avg by 2.2 and VLCL R@1 by 2.7. These are the largest single-factor drops, supporting the claim that directly constraining both canonical correlations and subspaces is the driver of retention, not a coincidental regularizer. The ablation also covers the prompt-invariance term, EMA updates, spectral moments, and sketch type.

- **Prompt invariance mechanism is validated.** Fig. 4 shows that the L_pi term (Eq. 11) flattens the degradation slope under increasing perturbation strength s: at s=1.0, PI-CCA improves R@1 by +2.44 p.p. (ID) and reduces Average Forgetting by ≈1.10 over the no-L_pi variant. This validates the projector-averaging design as an effective way to reduce prompt sensitivity.

- **Task-order robustness is demonstrated.** Fig. 5 shows narrow interquartile ranges across 20 random task orders on MTIL, confirming that the method's retention is not an artifact of a particular sequence.

## Weaknesses

### Fatal
None.

### Major

- **Fig. 3 geometry→performance correlation reports Pearson/Spearman values of 0.99–1.00, which is suspiciously perfect.** The paper says "We sweep realistic perturbations (certificate size, EMAs, invariance strength, whitening, pairing, LoRA capacity/LR, sketch type)" but does not report how many configurations were sampled or whether the drift and performance metrics are computed on independent splits. A correlation of exactly 1.00 (or 0.99) across multiple panels is implausible under realistic noise unless (a) the number of configurations is very small and the trend is deterministic, or (b) the drift and performance measurements are not independent. The paper's central claim that "stability of the canonical subspace/spectrum reliably predicts downstream performance" is presented as a key takeaway, but this specific evidence is not credible as shown. The authors must clarify: (i) how many configurations were sampled, (ii) whether drift and performance drop are computed on disjoint data, (iii) why the correlations are near-perfect. If the analysis is valid, the mechanism should be explained. If not, the correlation should be recomputed with proper randomization. This does *not* invalidate the core method results (Tables 1–3 stand on their own), but it weakens the paper's interpretability narrative.

### Minor

- **Missing error bars on Table 1 and Table 3.** Table 2 (VLCL, ConStruct-VL) reports ± ranges, but Table 1 (MTIL, X-TAIL) and Table 3 (ablations) report only point estimates. Since there is randomness from batch order, LoRA initialization, and task order (even within a fixed sequence), readers cannot assess whether PI-CCA's advantage over C-CLIP on MTIL Avg (76.8 vs. 75.2) is statistically significant. The paper should run multiple seeds and report mean ± std for all main results, or at minimum justify why the metrics are deterministic.

- **Baseline tuning configurations are not fully specified.** The paper lists baselines but does not state whether all use the same backbone (CLIP ViT-B/16), the same parameter-efficient adaptation (LoRA), or full fine-tuning. If some baselines use full fine-tuning while PI-CCA uses LoRA, the comparison could be unfair in either direction. This should be clarified.

### Trivial

- **The whitening differentiation (Eq. 2 / §3.4) uses "stop-gradient on the inverse square root if needed," which is ambiguous.** The paper should clarify under what conditions stop-gradient is applied and whether the losses actually constrain the whitened space as intended through the backward pass.

## Nice-to-Haves

- **Hyperparameter sensitivity curves.** The paper claims robustness but only shows component-level ablations (setting λ=0) rather than varying λ₁, λ₂, λ₃, η, α, β over a range. Sensitivity curves (even in the appendix) would strengthen the robustness claim.
- **Operational definition of prompt perturbation strength s.** The paper says "token-level synonym swap/back-translation/template jitter ratio" but does not specify how s∈[0,1] is mapped to the perturbation procedure. Providing this in the main text would improve reproducibility.
- **Comparison with a replay-based method using a small memory budget** (e.g., ER with 1% memory) to contextualize the replay-free advantage.
- **A deliberate certificate corruption experiment** (e.g., using wrong k or wrong sketches) to provide a stronger causal test of the drift→performance link.

## Removed Points

- **Criticism about sketch guarantees / error bounds not being in the main text.** The paper states theoretical explanation is in the appendix (§A.4). The appendix was stripped by the parser; this is not a valid criticism of the submission.
- **Criticism about gradient propagation through Σ^{-1/2} being underspecified.** The paper explicitly discusses eigendecomposition and Newton–Schulz approaches with "stop-gradient if needed." This is reasonable for a conference paper.
- **Criticism about missing related works.** The reviewer did not specify which works are missing, and I cannot verify this without external knowledge.
- **"Strength" about Fig. 3 correlation being strong evidence.** This conflicts with the verified weakness above; per the filtering rules, the weakness wins and this strength is removed.
- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem") — removed as lacking specific content.
- **Criticism about "code not released" or reproducibility from missing code.** The paper states code will be released upon acceptance, which is acceptable.
- **Criticism about "not yet released" baselines.** All cited baselines and models are assumed to exist as of the current date.

## Novel Insights

None beyond the paper's own contributions. The synthesis of the reviews does not surface a genuinely new observation about the paper that its own analysis does not already contain.

## Suggestions

1. **Clarify Fig. 3 immediately.** This is the single most impactful thing the authors can do. Report the number of configurations, state whether drift and performance are computed on disjoint data, and if the correlations are genuinely 0.99–1.00, explain the mechanism. If the analysis is flawed, re-run it transparently.
2. **Add error bars to Table 1 and Table 3** from at least 3 random seeds. This is standard practice and will strengthen the statistical claims.
3. **Specify the tuning configuration** (LoRA vs. full fine-tuning, backbone) for each baseline in the main text or a clear table footnote.
4. **Provide the mapping from s to perturbation procedure** in the main text, or at minimum give a concrete example for s=0.5 and s=1.0.

## Score and Decision

Now let me calibrate against the anchors.

**Round 1 bracket**: I placed the paper in the 5.0–7.0 range.

**Anchor comparisons**:

1. **vs KeepLoRA (5.5, Accept Poster)**: KeepLoRA is a simpler LoRA-based approach evaluated only on MTIL classification. PI-CCA is more novel (CCA certificates), more thoroughly evaluated (4 benchmarks), and has a more principled theoretical foundation. PI-CCA is clearly stronger. → PI-CCA > 5.5

2. **vs Compo-ReAlign (6.0, Accept Poster)**: Very similar in spirit — both are geometry-aware, principled approaches for VL CL. Both have strong theoretical grounding, thorough evaluation, and ablation studies. The key difference is that PI-CCA has the Fig. 3 correlation concern, which is a real but non-fatal weakness. Compo-ReAlign has no equivalent issue. PI-CCA ≈ Compo-ReAlign or slightly weaker due to this concern. → PI-CCA ≈ 6.0

3. **vs RLAP-CLIP (6.0, Accept Poster)**: RLAP-CLIP is limited to classification and uses a heuristic combination of components (RL + MoE). PI-CCA is more principled, evaluates on more diverse tasks, and has a cleaner architecture. PI-CCA is stronger. → PI-CCA > 6.0

4. **vs CoMem (5.0, Accept Poster)**: CoMem is more complex (concept-graph, multiple objectives), has more hyperparameters, and relies on a fixed relation schema. PI-CCA is cleaner and has stronger results. → PI-CCA > 5.0

5. **vs "Heads collapse" (7.33, Accept Poster)**: This is a theoretical CL paper with a different scope, not directly comparable.

**Final score**: The paper is clearly stronger than the 5.5 anchors (KeepLoRA) and the 5.0 anchor (CoMem). It is comparable to the 6.0 anchors (Compo-ReAlign, RLAP-CLIP). The Fig. 3 correlation issue is a real concern but does not undermine the core method contribution. The paper's strengths — novelty, thorough evaluation, principled design, consistent SOTA results — outweigh the weaknesses. I assign a score of **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>