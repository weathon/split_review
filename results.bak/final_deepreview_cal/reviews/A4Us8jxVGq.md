Now I have a thorough understanding of the paper and the calibration anchors. Let me produce the final consolidated review.

---

## Summary

This paper provides a theoretical analysis of how semantic associations emerge in attention-based transformers trained on natural language, via gradient leading-term expansions. The central contribution is a set of closed-form expressions for the output, value, and query-key weight matrices as compositions of three interpretable basis functions — bigram mapping (B̄), interchangeability mapping (Σ_B̄), and context mapping (Φ̄) — derived from corpus statistics. The theory is validated on a 3-layer attention-only model (TinyStories, cosine similarities >0.99 between theoretical and learned weights) and extended to Pythia-1.4B (covariance structure matches across layers and checkpoints).

## Strengths

- **First explicit closed-form weight characterizations for transformers on real text.** Theorem 4.1 provides concrete matrix expressions (Eqs. 5–8) for all weight types (output, value, query-key, positional) with explicit Frobenius-norm error bounds. This goes substantially beyond prior theoretical work that relied on synthetic data, simplified architectures, or non-standard training procedures. The derivation is grounded in a realistic setup with relative positional encodings, causal masking, residual streams, and natural language data.

- **Striking quantitative agreement on a controlled model.** Table 1 reports minimum cosine similarities of 0.9995 (attention), 0.9992 (value), and 0.9985 (output) between the predicted leading-term matrices and actual learned weights. Figure 4 shows these values remain above 0.9 for 30 epochs. This is unusually strong empirical support for a theoretical prediction of this complexity.

- **Generalization to a billion-parameter LLM is suggestive and ambitious.** Figure 6 shows that covariance matrices of Pythia-1.4B's attention weights and post-layer embeddings have strong cosine similarity with the corresponding leading-term features across layers and early training steps. The per-head analysis (Figure 7) further reveals layer-specific dynamics in how heads differentiate from the common starting point predicted by the theory, providing mechanistic insight beyond aggregate matching.

- **Interpretable linguistic structure in the basis functions.** Figure 5 demonstrates that the bigram mapping captures adjective-noun pairs (e.g., "red" → "truck"), the interchangeability mapping groups functionally similar tokens (e.g., "happy", "sad", "excited"), and the context mapping captures longer-range associations (e.g., "fish" → "pond", "lake"). These qualitative examples ground the abstract theory in recognizable linguistic patterns.

## Weaknesses

### Major

- **Mismatch between theoretical optimizer (full-batch GD) and experimental optimizer (SGD/Adam).** The theory in Section 3.3 assumes full-batch gradient descent (Eq. 4), but the TinyStories experiments use SGD with batch size 2048 (Section 5.1), and the Pythia experiments use Adam. The paper does not discuss this gap or provide an argument that the leading-term analysis is robust to stochastic gradients or adaptive optimizers. While the empirical agreement suggests robustness, the claim that "the experiments validate the theory" is weakened by this mismatch. To close this gap, the authors should either (a) run a full-batch GD control experiment, or (b) provide a theoretical argument (e.g., that the expected SGD gradient equals the full-batch gradient and the leading term is preserved in expectation).

- **The formal validity window is extremely narrow (≈5–9 steps) yet the theory is claimed to explain behavior at 100s–1000s of steps.** The bound in Theorem 4.1 requires s ≤ η⁻¹ min(5/(8√T), 1/(12L)). For the TinyStories parameters (T=200, L=3, η=0.005), this gives s ⪅ 5–9 steps, yet experiments run for 100 epochs (~thousands of steps). The paper acknowledges the results hold "well beyond" the formal window and treats this as a robustness finding (which is honest), but does not analyze why higher-order corrections do not accumulate as quickly as the bounds predict. The paper would be stronger with a discussion of why the constants in the bounds are loose and whether tighter analysis could extend the validity window.

### Minor

- **Pythia's absolute positional encodings vs. the theory's relative positional encodings.** The theoretical model (Definition 3.1) uses T5-style relative positional encodings, while Pythia uses learned absolute positional encodings. The paper mentions the MLP and multi-head attention architectural differences but not the positional encoding discrepancy. This should be acknowledged and discussed, as it could affect how well the theory transfers.

- **Covariance comparison methodology could be more explicit.** The description in Section 5.2 states that covariance matrices of E_{l,post} (|V|×d) are compared with Φ̄^T B̄^T (|V|×|V|), but it is not stated whether the comparison is between two |V|×|V| covariance matrices (E_{l,post} E_{l,post}^T) or some other object. Similarly, the description of how A_{l,tok} is compared to Q̄ needs clarification. These details matter for reproducibility.

- **The corpus mismatch for Pythia (OpenWebText vs. Pile) is partially addressed but under-discussed.** The paper computes leading-term matrices from OpenWebText but Pythia was trained on the Pile. A FineWeb sensitivity analysis is mentioned (Appendix B) but not discussed in the main text, and the potential effect of corpus mismatch on the (otherwise strong) correlations is not assessed.

- **The MLP ablation claim is speculative.** The paper states "one possible hypothesis is that the MLP at early stages functions similarly to the leading-term value mapping," but does not test this directly (e.g., by computing cosine similarity between the MLP output alone and Φ̄^T B̄^T). A simple additional computation would make this claim evidence-based.

### Trivial

- The TinyStories dataset size is not reported in the main text, making it hard to compute actual gradient steps per epoch from the stated batch size.
- The paper uses a closed vocabulary (3,000 most frequent words) and word-level tokenization; the BPE experiment is relegated to the appendix. The implications of this choice for generalizability should be noted in the main text.

## Nice-to-Haves

- A concrete numerical example of B̄, Σ_B̄, Φ̄, and Q̄ for a tiny vocabulary (e.g., 10 words on a mini-corpus) would make the three-step construction of Q̄ significantly more accessible.
- Confidence intervals or bootstrap-based significance tests for the Pythia cosine similarity values would strengthen the claim that observed similarities are above chance.

## Removed Points

These points from the reviewers were evaluated and removed or downgraded:

- *"The paper does not state the training dataset size for TinyStories"* — This belongs in the appendix section of experimental details (Appendix C), which was stripped by the PDF parser. Downgraded to trivial.
- *"No confidence intervals or error bars for Pythia experiments"* — Nice-to-have; not standard for large-scale LLM analysis. Moved to nice-to-haves.
- *"The paper could cite more recent work"* — Generic; removed.
- *"The theory assumes η ≥ 1/T which is unusual"* — This is explicitly stated and the bound is part of the theorem; the paper is transparent about its conditions. Demoted to minor note.
- *"The paper doesn't address whether the corpus mismatch could affect results"* — This is partially inaccurate; the paper mentions a FineWeb sensitivity analysis in Appendix B. Downgraded to minor.
- *Strength: "More realistic setup than prior work"* — Kept as it's specific and evidence-backed.
- *Strength: "Interpretable semantic structure"* — Kept with concrete examples from Figure 5.
- *Strength: "Fine-grained per-head analysis"* — Kept with specific reference to Figure 7 observations.

## Novel Insights

The contrasts between the two reviewer perspectives reveal a paper whose core contribution is genuinely novel (first closed-form weight characterizations for transformers on real text) but whose experimental validation has a structural gap that is acknowledged in the theory section but not addressed in the experiments. The harsh critic's most valuable observation is that the optimizer mismatch (full-batch GD → SGD/Adam) is not just a "this could be better" issue but a disconnect between the formal conditions of Theorem 4.1 and the experimental setup used to validate it. Conversely, the strength finder correctly highlights that the cosine similarities >0.99 on the small model are unusually strong for a theoretical prediction of this complexity — this level of empirical corroboration is rare in neural network training dynamics work and deserves emphasis. The tension between these two views suggests the paper would benefit most not from more experiments but from explicitly addressing why the leading-term analysis is robust to the GD/SGD gap (e.g., noting that the expected gradient is identical and the noise is zero-mean), and from reframing the claims to acknowledge the gap honestly rather than tacitly switching optimizers between theory and experiments.

## Suggestions

1. Add a brief remark in Section 3.3 or 5.1 acknowledging the GD/SGD gap and providing an informal argument that the expected gradient under SGD equals the full-batch gradient, so the leading-term prediction is unchanged in expectation. This one paragraph would substantially strengthen the paper's internal coherence.
2. Add a short paragraph in Section 5.1 discussing why the formal bounds are conservative and why the empirical agreement persists far beyond the formal validity window — even a few sentences hypothesizing about loose constants or the structure of higher-order corrections would help.
3. Clarify the covariance comparison methodology for Pythia (which specific covariance matrix, which dimensions) and add a sentence about the FineWeb sensitivity analysis in the main text rather than relegating it entirely to the appendix.
4. Include a small synthetic example (5–10 word vocabulary) showing the actual values of B̄, Σ_B̄, Φ̄, and Q̄ to illustrate the three-step construction of the attention matrix.

## Score and Decision

**Round 1 bracketing:** The paper was compared against anchors in three bands. The weak band (avg scores 2.33–3.40) consisted of papers on linearization of gradient-based learning and NTK analyses — clearly weaker due to more limited scope. The middle band (avg scores 4.25–6.33) included papers on transformer mechanistic interpretability and training dynamics — this paper sits solidly in this range. The strong band (avg scores 7.33–8.0) included papers with very tight theory-experiment alignment (e.g., SignGD analysis) — this paper is weaker than those due to the optimizer mismatch and narrow validity window.

**Round 2 narrowing:** Anchors at 5.75 (JoMA), 6.0 (one-step GD ICL), 6.20 (induction heads), and 7.33 (SignGD) were read in full. The paper under review is:
- Stronger than the 5.75 JoMA anchor (which relies on stronger assumptions like token orthogonality and had less direct weight-level validation).
- Comparable to the 6.20 induction heads anchor (similar level of theoretical contribution to a topical problem, similar gaps between theory and realistic settings) but with stronger empirical validation.
- Weaker than the 7.33 SignGD anchor (which has complete end-to-end theoretical characterization of dynamics with tight alignment to experiments, though on a simpler problem).

**Final score:** 6.0

The paper makes a genuinely novel theoretical contribution with unusually strong empirical support (cosine >0.99) on the controlled model, and ambitious extension to Pythia-1.4B. However, the optimizer mismatch between theory and experiments and the narrow formal validity window compared to the actual training duration are real gaps that prevent a higher score. These are addressable (the former with a paragraph of justification, the latter with a discussion of bound tightness), making the paper suitable for acceptance with revisions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>