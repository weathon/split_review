Now I have enough calibration information. Let me write the consolidated review.

## Summary

This paper derives closed-form expressions for attention-based transformer weights trained on natural language under next-token prediction, using a gradient leading-term approximation that is accurate during early training. The weights are characterized as compositions of three interpretable basis functions — bigram mapping (B̄), interchangeability mapping (Σ_B̄), and context mapping (Φ̄) — which capture statistical and semantic associations between tokens. The theory is validated on a 3-layer transformer trained on TinyStories (cosine similarity >0.99) and, via a covariance-based adaptation, on Pythia-1.4B trained on OpenWebText.

## Strengths

1. **First closed-form characterization of transformer weights trained on natural language data.** Theorem 4.1 gives explicit expressions for the output, value, query-key, and positional matrices (Eqs. 5–8) in terms of corpus statistics (B̄, Φ̄, Q̄, Δ) with explicit Frobenius norm error bounds. Table 1 reports minimum cosine similarities >0.998 between theoretical and learned weights across all layers in the matching architecture. This goes substantially beyond prior theoretical work that relies on synthetic languages or simplified architectures.

2. **Interpretation of learned features as compositions of three linguistically meaningful basis functions.** Section 4.2 defines (1) bigram mapping (Eq. 9), (2) interchangeability mapping (Eq. 10), and (3) context mapping (Eq. 11). Figure 5 shows that the most-correlated tokens under each basis function capture genuine semantic relations (e.g., "red"↔"balloon", "fish"↔"pond"). The end-to-end decomposition in Eq. (12) provides a mechanistic account of how the residual stream, attention, and output matrix cooperate: the output matrix provides a bigram baseline while the attention mechanism refines predictions via contextually predictive tokens (Section 4.2.3).

3. **Validation on a realistic large-scale LLM (Pythia-1.4B).** Section 5.2 presents a methodology to bridge the architectural gap (multi-head attention, MLP) by comparing covariance structures of token embeddings with theoretical leading-term matrices. Figure 6 shows high cosine similarity (>0.9) at early training steps across most layers for both attention and embedding mappings, with an MLP ablation and per-head analysis (Figure 7) providing finer-grained insight. The attempt to validate the theory on a billion-parameter model goes well beyond the toy settings common in this literature.

4. **Rigorous handling of realistic architectural components.** The model (Definition 3.1) includes causal masking, relative positional encodings, residual streams, and multi-layer attention — all present in practical transformers. The error bounds in Theorem 4.1 are uniform across layers and do not require sequential or frozen-weight training, contrasting with assumptions in prior work (Bietti et al., 2023; Huang et al., 2025).

## Weaknesses

### Fatal

None.

### Major

1. **The empirical validation does not directly test what the theorem guarantees.** Theorem 4.1 provides **Frobenius norm bounds** (e.g., ‖W_O − sηB̄‖_F ≤ 3s²η²), but the paper validates using **cosine similarity** between the learned weights and their leading terms. These are different metrics: cosine similarity can be high even when the Frobenius norm difference is large (if the learned weight is a scaled version of the leading term plus a large orthogonal component). The paper states "To verify Theorem 4.1, we measure the cosine similarity" (Section 5.1), but the proof bounds Frobenius error, not cosine similarity. The reported cosine similarities >0.99 are encouraging circumstantial evidence, but they do not constitute a direct test of the proven bounds. Reporting relative Frobenius error ‖W_learned − sηB̄‖_F / ‖W_learned‖_F for the matching-architecture TinyStories experiment would directly connect the empirical validation to the theoretical claim.

2. **The theoretical regime (s ≤ ~5–6 gradient steps) and the experimental regime (100 epochs, likely >10⁵ steps) are dramatically mismatched.** For the TinyStories experiment (T=200, L=3, η=0.005), the bound requires s ≤ η⁻¹ min(5/(8√T), 1/(12L)) ≈ 5.6 gradient steps. The paper trains for 100 epochs with batch SGD. While the paper acknowledges that "features remain informative well beyond" the theoretical regime, it does not provide any analysis — theoretical or experimental — of why the approximation persists orders of magnitude past its proven validity bound. This gap means the central claim of empirical verification is supported for a regime far smaller than what is actually tested. A focused study of the first ~5–10 steps (where the theorem applies) to measure Frobenius error directly would be the minimum remedy.

### Minor

3. **The Pythia-1.4B validation is necessarily indirect.** As the paper acknowledges, multi-head attention and MLP modules make it "impossible to directly read off average token correlations from the weights." The workaround — comparing covariance matrices of token embeddings with those of the theoretical leading-term matrices — is reasonable but provides weaker evidence than a direct weight comparison. Covariance structure is a high-level summary; different matrices can produce similar covariances. The paper would benefit from additional finer-grained checks (e.g., per-head attention pattern comparisons where possible).

4. **No variance or uncertainty reporting.** The TinyStories experiment (Table 1, Figure 4) appears to come from a single run without error bars. The Pythia heatmaps (Figure 6) similarly lack quantification of variance. The strong claims would be more robust with multiple random seeds and standard deviations reported.

5. **The training setup has a subtle mismatch with the theory.** The theory assumes full-batch gradient descent (Eq. 4), but the TinyStories experiment uses mini-batch SGD with batch size 2048 (Section 5.1). While this is a reasonable practical choice, the theoretical bounds do not directly cover mini-batch noise.

### Trivial

6. The paper uses "epochs" as the unit of training time in experiments (Section 5.1) but the theory is stated in terms of gradient steps (s). The corresponding number of gradient steps per epoch is not stated, making it difficult to directly compare the experimental duration (~100 epochs) against the theoretical regime (s ≤ ~5.6 steps).

## Nice-to-Haves

- **Direct Frobenius norm comparison** for the TinyStories setting, as this would directly test Theorem 4.1 rather than using cosine similarity as a proxy.
- **Null model baseline** showing what cosine similarity looks like for random embeddings or initial weights, to demonstrate that the high observed similarity is non-trivial.
- **A study focused on the first ~10 gradient steps** where the theoretical bound provably holds, to establish whether the approximation is tight within its proven regime before examining longer training.
- Additional ablations on how the approximation quality depends on vocabulary size and sequence length.

## Removed Points

These points are flagged as removed; treat them with caution.

1. **"Theoretical analysis presented with insufficient precision"** — Removed because the paper explicitly references Appendix A for formal definitions and Appendix D for proofs. The parser removes appendix content from all papers; the formal definitions exist in the original submission. The main text provides Eq. (9), (10), (11) with clear descriptions and the three-step construction of Q̄ with a pointer to Appendix A.

2. **"Missing related works" / "Insufficient differentiation from prior work"** — Removed per hard rules (cannot verify existence of related works without external sources). The paper does clearly distinguish its contribution in the Introduction (lines 33–35) and Related Works (Section 2), explicitly noting how it differs from Bietti et al., Nichani et al., Huang et al., Tian et al., and others.

3. **"First explicit characterization claim overstated"** — Removed. While the Pythia validation is indirect, the claim refers to providing closed-form weight expressions for a transformer trained on real-world text, which is indeed a first relative to prior work that uses synthetic languages or simplified architectures. The paper's Introduction transparently describes what is and is not achieved.

4. **"Reproducibility / undisclosed hyperparameters"** — Removed per hard rules. The paper provides the key hyperparameters (learning rate 0.005, batch size 2048, sequence length 200, vocabulary 3000) and references the appendix for further experimental details.

5. **Typo/formatting/style nitpicks** — Removed per hard rules (parser artifacts, not author errors).

## Novel Insights

Looking across the two reviewers, neither identifies a genuinely novel observation that the paper itself does not already articulate. The harsh critic's most penetrating point — that the Frobenius-norm theorem is tested with cosine similarity, not Frobenius error — is an important methodological critique of the paper's empirical strategy, but it is a weakness in the paper's execution, not a novel insight about the science. Similarly, the Strength Finder's observations about the three basis functions and the Pythia validation reflect the paper's own framing. No genuinely novel insight emerges beyond the paper's contributions.

## Suggestions

1. Report **relative Frobenius error** (‖W_learned − sηB̄‖_F / ‖W_learned‖_F) alongside cosine similarity for the TinyStories experiment. This directly tests the bound in Theorem 4.1 and eliminates the metric mismatch.

2. Run a **short-time experiment** focused on the first 5–10 gradient steps (where the theorem provably holds) to establish that the approximation is tight within its proven regime. Show both Frobenius error and cosine similarity over these steps.

3. Report results from **multiple random seeds** (e.g., 3 seeds) with standard deviations in Table 1 and Figure 4.

4. Clarify how many gradient steps each epoch corresponds to in the TinyStories experiment, and state the total number of gradient steps reached at each checkpoint.

5. For the Pythia experiment, consider adding a **per-head attention pattern comparison** where feasible (e.g., comparing top-k attended tokens between the theoretical Q̄ projection and actual attention heads), going beyond covariance-level comparisons.

## Score and Decision

**Round 1 (Bracketing):** Queries targeting three bands returned anchors at avg 3.00 (weak, reject-range papers on transformer training dynamics), avg 4.0–6.5 (mid-range), and avg 8.00 (strong-accept papers on unrelated topics). The paper clearly exceeds the 3.0 band (different class of work — these are reject-range papers with simpler scope or flawed execution) and falls well short of the 8.0 band (oral-level work on different topics). Initial bracket: **4.5–6.5**.

**Round 2 (Narrowing):** Queries targeting (4.5, 7.5) and (5.0, 7.5) returned anchors at 5.0 (Reject — simplified setting, theory-experiment misalignment), 5.2 (Accept Poster — elegant but limited scope), 5.5 (Accept Poster — interesting theory, imperfect causal evidence), 6.0 (Accept Poster — solid theoretical analysis), and 6.5 (Accept Poster — clear theory, good validation). The paper under review is stronger than the 5.0 anchor (which had a more limited contribution and worse theory-experiment alignment) and comparable to the 5.2 and 5.5 anchors in terms of ambition–evidence balance. However, it has a more significant validation gap (Frobenius vs. cosine, 5 steps vs. 100 epochs) than the 6.0 and 6.5 anchors, which had cleaner empirical support for their theoretical claims. The paper's theoretical contribution (realistic architecture, natural language, closed-form expressions) is genuinely novel, but the empirical verification has structural gaps.

**Selected anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| l8eWnNH7qN (Ill-Conditioning) | 3.00 | R1 | Much weaker — different focus, simpler analysis |
| S0IIgb33fO (Fan-in Asymmetry) | 2.67 | R1 | Much weaker — gradient analysis for redundancy, not weight characterization |
| 27fc8hXB5N (Grokking Dynamics) | 3.33 | R1 | Much weaker — different phenomenon, limited theory |
| CfFj68C9Cn (Learning to Recall) | 6.50 | R1/R2 | Stronger in empirical rigor; simpler setting (single-layer, synthetic task) |
| 1pTzWVvwEd (Incremental Learning) | 4.50 | R2 | Weaker — very simplified architecture, limited empirical support |
| 7CAvzaRUkH (Interpreting Multi-Layer) | 4.50 | R2 | Comparable — probing methodology but less novel theory |
| sY14iAFGIH (How Transformers Learn ICL) | 4.00 | R2 | Weaker — on-convergence analysis only, restricted setting |
| utSqpxQHXq (Two failure modes) | 6.00 | R2 | Stronger — cleaner empirical validation of theory |
| z8xjWmyQSZ (Strong Correlations) | 5.20 | R2 | Comparable — interesting theory, limited experimental scope |
| 2g8vgmyXgQ (Provable ICL Nonlinear) | 5.00 | R2 | Weaker — theory-experiment alignment concerns, simpler setting |
| J4GYMiE3JT (Structural Inference) | 6.50 | R2 | Stronger — cleaner interpretability methodology |
| TLSUIyBIfs (Quantitative Bounds) | 7.00 | R2 | Stronger — rigorous theory with clean experiments |
| c5TFhCJ6fs (Attention Sinks) | 5.50 | R2 | Comparable — interesting theory, imperfect causal evidence |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>