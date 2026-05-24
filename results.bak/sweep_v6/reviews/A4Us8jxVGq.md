Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper studies how semantic associations emerge in attention-based transformers during training. The key technical contribution is a leading-term analysis of the gradients that yields closed-form expressions for each weight matrix (output, value, query-key, positional) as compositions of three corpus-derived statistics: bigram mapping (B̄), interchangeability mapping (Σ_B), and context mapping (Φ̄). Theorem 4.1 bounds the Frobenius-norm error between learned weights and these leading-term approximations for the first O(1/η) gradient steps. The paper validates these expressions on a 3-layer model trained on TinyStories (reporting cosine similarities >0.998) and demonstrates that covariance structures of Pythia-1.4B embeddings/attention correlate with the predicted statistics across training.

## Strengths

- **Closed-form leading-term expressions for all weight matrices are genuinely novel.** Theorem 4.1 (informal) provides explicit formulas (Eqs. 5–8) relating W_O, V^(l), W^(l), and P^(l) to corpus statistics B̄, Φ̄, Q̄, Δ with concrete Frobenius-norm error bounds. This goes beyond existing theoretical work that analyzes aggregated attention patterns or simplified architectures without deriving per-weight expressions.

- **The interpretation of weights as compositions of three linguistically grounded statistics is clean and insightful.** The decomposition into bigram mapping, interchangeability mapping (token similarity via shared previous-token distributions), and context mapping (prefix-suffix co-occurrence) provides a unified mechanistic account of what different weight matrices encode. This conceptual framework could prove useful for interpretability beyond the paper's own results.

- **The Pythia-1.4B experiments reveal non-trivial correlations with the theoretical predictions despite substantial architectural differences.** Figure 6 shows that embedding and attention covariance structures in a model with multi-head attention, MLP layers, and layer normalization correlate with the predicted leading-term features, especially at early training steps. The per-head analysis (Figure 7) further reveals layer-specific specialization patterns.

- **The empirical observation that the decomposition holds far beyond the theorem's formal guarantee (~5 steps) is genuinely interesting.** While this creates a scope mismatch (discussed below), the fact that cosine similarity to the leading-term expressions remains >0.7 even after 100 epochs is a notable finding that motivates future work on why these features are stable attractors of the dynamics.

## Weaknesses

### Fatal
None.

### Major

- **The theoretical guarantee does not cover the experimental regime used to "verify" it.** Theorem 4.1 guarantees the approximation holds for at most s ≤ η⁻¹·min(5/(8√T), 1/(12L)) gradient steps. For the TinyStories setup (η=0.005, T=200, L=3), this evaluates to s ≤ 5.56 gradient steps. Yet the experiments run for 100 epochs (~500–700+ gradient steps with batch size 2048) and the paper frames this as "verifying Theorem 4.1." The paper does acknowledge that the alignment persists "beyond" the theoretical regime, but the central narrative conflates what is rigorously proven with what is merely observed. This is not a trivial gap: the theory justifies the weight decomposition for the first handful of updates, while the empirical evidence for it comes almost entirely from a regime the theory does not cover. Either the theory needs to be extended to match the experiments, or the claims must be scoped much more carefully.

- **The connection between the simplified theoretical architecture and practical LLMs is correlational, and the generality claims go beyond what is supported.** The theory is derived for a single-head transformer with a shared QK matrix, no MLP, no layer norms, and value matrices in the vocabulary space. The Pythia experiments necessarily use an indirect methodology (comparing covariance matrices of embeddings/attention with covariance matrices of the theoretical leading terms). Even if these covariances agree, this does not demonstrate that the *mechanism* described by the theory (gradient leading terms driving early updates) is responsible — many other explanations could produce similar covariance structure. The claim that the theory "generalizes with the addition of multi-head attention or MLP" (p. 9, line 269) is stated as a conclusion without any argument for why the gradient leading-term analysis should survive these architectural changes.

### Minor

- **The "three basis functions" framing inflates the count.** Σ_B = B̄^T B̄ is derived entirely from B̄; it is not an independent statistic. The paper presents Σ_B as a separate basis function (Eq. 10), but the real count is two primary statistics (B̄, Φ̄) plus one derived from B̄. This is a presentational issue — the contributions are not diminished — but it should be acknowledged or renamed.

- **The restrictive conditions of Theorem 4.1 are stated but not discussed as limitations.** The conditions η ≥ 1/T (constraining the learning rate) and L ≤ √T/4 (constraining depth, e.g., T=200 → L ≤ 3.5) are non-trivial. Real transformers are much deeper, and smaller learning rates are common. The paper should explicitly discuss how these constraints limit the theory's applicability.

- **The paper would benefit from explaining why the alignment persists so far beyond the theoretical guarantee.** The near-perfect cosine similarity (>0.998 in Table 1) across *all* epochs for the small-η setup, despite Frobenius-norm error bounds that should be large after O(10⁵) gradient steps, is an intriguing observation. The paper treats it as supportive evidence, but does not hypothesize why the leading-term *direction* (captured by cosine similarity) remains stable when the *magnitude* (captured by Frobenius norm) would have drifted according to the bounds. This is an explanatory gap.

- **The Pythia experiments lack statistical significance measures.** No confidence intervals, permutation tests, or baselines (e.g., random covariance comparison) are reported. Given that the comparison is between covariance matrices, which can share structure simply due to the data distribution, ruling out the null hypothesis that any model would show similar alignment would strengthen the claims.

### Trivial

- The shared QK matrix W^(l) (Def. 3.1) is non-standard and used by only a few prior works (Nichani et al., 2024). The paper does not discuss how this affects the generality of the results compared to separate Q/K parameterization.

## Nice-to-Haves

- A controlled experiment within the formal guarantee (s ≤ 5 steps) that directly measures Frobenius-norm error between learned weights and leading terms, then shows where the approximation breaks down. This would cleanly validate the theorem before exploring the longer regime.
- Replace learned weights with random weights and recompute cosine similarity to rule out the null hypothesis that any weight matrix aligns with corpus statistics through shared second-order structure.
- Linear probing on Pythia to test whether the predicted basis function features are actually used by the model for next-token prediction, rather than just covarying with the representations.
- A formal or heuristic argument for why the leading-term direction might be an approximate fixed point of the gradient dynamics, explaining the persistence beyond the theorem's regime.

## Removed Points

The following points from the reviews are removed per policy:

- **Harsh Critic Point 3** ("paper does not specify how Q and Δ are computed" / "appendix is missing"): The paper explicitly references Appendix A for the construction of Q̄ and Appendix C for experimental details. The appendix is stripped by the PDF parser; it exists in the original submission. Per instructions: "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references. The parser strips those sections from all papers."

- **Harsh Critic Point about TinyStories vocabulary of 3,000 words**: The paper explicitly acknowledges the vocabulary truncation as a choice "for clearer interpretability" and positions the TinyStories experiment as a controlled setting to match the theory, with the Pythia experiments addressing the full-vocabulary setting. This is not a weakness, it's a deliberate experimental design choice.

- Several **generic/nitpicky points** from the Harsh Critic: missing statistical significance (retained as Minor), formatting complaints (removed per instructions), and the suggestion that the shared QK "deviation from practice is not discussed or justified" — the paper explicitly cites Nichani et al. (2024) for this choice and notes that self-attention-only models can match MLP-equipped architectures (citing Wang et al., 2025).

## Novel Insights

The most interesting observation that emerges from the reviews — and from the paper itself — is that the leading-term weight decomposition aligns with learned weights *well beyond* the regime where the theory guarantees it. This creates a genuine puzzle: why does a first-order gradient expansion, formally valid for only ~5 steps, produce features that persist for hundreds or thousands of steps in both simplified and real transformers? Neither the paper nor the reviewers provide an explanation, but this gap suggests either (a) the leading-term direction is an approximate fixed point of the dynamics, or (b) the data distribution forces certain correlation structures regardless of optimization path. Distinguishing these would be a valuable direction for follow-up work. The paper's basis-function decomposition itself — regardless of whether the dynamics explanation is correct — provides a useful vocabulary for characterizing what transformers encode.

## Suggestions

1. **Re-scope the paper's claims to match what is actually proved.** The theoretical contribution should be presented as: "closed-form expressions for weights at the earliest stages of training (first ~5–6 gradient updates) under a simplified architecture." The empirical persistence beyond this regime should be presented as a separate, interesting observation — not as "verification" of the theorem. For example, rephrase "To verify Theorem 4.1" to "To test whether the leading-term features extend beyond the theorem's formal guarantee."

2. **Provide an explicit hypothesis or mechanism for why cosine similarity persists beyond the Frobenius-norm bound.** Since cosine similarity measures direction (not magnitude), one concrete possibility is that the leading-term matrix is an approximate eigenvector of the gradient flow, so later updates preserve its direction. Even a heuristic argument would substantially strengthen the paper.

3. **Add statistical significance or null-hypothesis controls to the Pythia experiments.** Report the distribution of cosine similarities under random embeddings or random weight matrices to calibrate what values count as meaningful agreement. This is standard for covariance comparison studies.

4. **Acknowledge the dependence of Σ_B on B̄ directly.** Rename "three basis functions" to "two primary statistics (bigram and context mappings) plus a derived interchangeability statistic" to avoid inflating the count.

## Score and Decision

**Calibration anchors** (retrieved from the DeepReview 13k corpus):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/97rOQDPmk2.md` | 7.33 | Stronger theory-experiment alignment — proof covers full training trajectory, not just first 5 steps. More carefully scoped claims. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/STUGfUz8ob.md` | 7.60 | Strong theory-practice bridge with proposed architectural improvements validated empirically. Better-scoped contributions. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0uI5415ry7.md` | 6.50 | Similar simplified-model as proxy approach, but more honest about limitations and better matched experiments to theory. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/MO5PiKHELW.md` | 5.50 | Rich empirical methodology with causal interventions; less theory but stronger evidence. Comparable overall quality. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/YKzGrt3m2g.md` | 4.25 | Interesting theoretical connection but limited empirical scope. Weaker on validation than the reviewed paper. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hNkXTqDrfb.md` | 3.75 | Similar overclaiming issue — claims about syntax/semantics go beyond what theory supports. Weaker empirical validation than reviewed paper. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4fVuBf5HE9.md` | 4.33 | Very simplified setup with limited task relevance. Less ambitious and less interesting than reviewed paper. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hFQZmKFtlT.md` | 3.50 | Different topic; limited empirical backing for claims about memorization vs. understanding. |

The paper under review is stronger than the 3.5–4.3 band papers (hNkXTqDrfb, 4fVuBf5HE9, hFQZmKFtlT) — it provides genuine closed-form expressions, not just qualitative claims, and validates on a real LLM (Pythia-1.4B). It is weaker than the 6.5+ band papers (97rOQDPmk2, STUGfUz8ob, 0uI5415ry7) because the theory-experiment scope mismatch is a structural issue that undermines the central narrative. It is comparable to the 5.5–6.0 band papers (MO5PiKHELW) — real contributions with notable limitations.

**Score: 5.5**

**Decision: Reject**

The paper has genuine contributions — the closed-form weight expressions and the clean basis-function decomposition are novel and potentially valuable. The Pythia experiments, even if correlational, reveal interesting structure. However, the fundamental mismatch between the theoretical guarantee (~5 gradient steps) and the experimental validation (hundreds to thousands of steps) is not a minor presentation issue; it breaks the paper's central argument that the theory *explains* the observed weight structure. The paper would be substantially improved by re-scoping the claims to honestly separate what is proven from what is observed, adding mechanistic explanations for the persistence beyond the formal regime, and providing stronger null-hypothesis controls for the Pythia experiments. As it stands, I cannot recommend acceptance at ICLR.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>