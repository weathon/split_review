Now I have all the information I need to write the final consolidated review. Let me produce it.

---

## Summary

This paper provides the first theoretical analysis of the training dynamics, ICL generalization, and robustness to outliers of a one-layer Mamba model, and compares it with a one-layer linear Transformer under the same data setup. The authors prove quantitative convergence guarantees (Theorem 1), generalization bounds under distribution-shifted test outliers (Theorem 2), and show that Mamba tolerates outlier fractions α arbitrarily close to 1 while the linear Transformer breaks at α ≥ 1/2 (Theorems 3, 4). Corollaries 1–2 characterize the mechanism: linear attention selects examples sharing the query's relevant pattern, while nonlinear gating suppresses outliers and applies exponential decay by distance from the query. Synthetic experiments validate the theoretical threshold predictions and the mechanistic interpretation.

## Strengths

- **First theoretical analysis of Mamba training dynamics for ICL.** The paper provides explicit sufficient conditions on batch size, prompt length, outlier magnitude, and training iterations (Theorem 1) for a one-layer Mamba to achieve low hinge loss on all tasks in the distribution. This fills a gap in the literature, where prior work analyzed Transformers but not Mamba/SSM architectures.

- **Clear theoretical comparison with linear Transformers yielding a crisp robustness threshold.** Theorem 2 shows Mamba tolerates test outlier fractions α < min(1, p_a l_tr/l_ts), which can approach 1 with appropriate prompt length. Theorem 4 shows the linear Transformer requires α < 1/2. This α = 1/2 vs. α → 1 distinction is a clean, memorable takeaway, and Figure 2 directly validates it across three outlier labeling schemes.

- **Mechanistic analysis that explains *how* the architecture achieves robustness.** Corollary 1 shows linear attention concentrates on context examples sharing the query's relevant pattern (verified in Figure 3). Corollary 2 shows the nonlinear gating nearly zeroes out outlier examples and decays exponentially with distance from the query for clean examples (verified in Figure 4). Together these explain *why* Mamba outperforms the linear Transformer: the gating layer actively suppresses corrupted examples.

- **Experiments designed to test specific theoretical predictions.** The three types of outlier labeling functions (label flipping, targeted, random) in Section 4.1 directly test the robustness claims under varied corruption models. The multi-layer experiments in Section 4.2 probe the mechanistic predictions (attention concentration, gating suppression, exponential decay) and find them preserved beyond the one-layer theoretical setting. Table 1 further tests an important boundary condition (outlier placement) and the results align with the exponential decay prediction.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The analyzed model is a significant simplification of Mamba (A = −I).** Setting A = −I eliminates the learned diagonal parameterization and the full selective-scan mechanism that distinguishes Mamba from a simple gated RNN. The paper is transparent about this — it states the assumption upfront (line 59, citing Gu & Dao 2023) and notes extensions in Appendix E.6 — and the derived model in (3) cleanly isolates the effect of nonlinear gating versus linear attention. However, the paper consistently refers to this as a "one-layer Mamba," which may overstate the connection to practical Mamba architectures. The theoretical results are more accurately about "gated linear attention with product-of-sigmoids gating." This is a framing issue rather than a technical flaw, but it matters for how the community will interpret the results.

- **The outlier robustness guarantee in Theorem 2 requires test outliers to lie in the positive linear span of training outliers.** Condition (a) requires each test outlier pattern v to be a linear combination ∑ᵢ λᵢ vᵢ* of the V training outlier patterns with ∑ᵢ λᵢ ≥ L > 0, plus orthogonal noise. This is a convex cone condition that excludes, for example, test outliers that are negations or substantially rotated versions of training outliers. The paper states this condition clearly, but the practical implications — which real-world prompt corruption scenarios do or do not satisfy it — are not discussed.

- **The comparison with linear Transformers is based on sufficient conditions, not proven necessity.** The α < 1/2 bound for Transformers in Theorem 4 is a sufficient condition derived under the same training regime, not a lower bound proving that linear Transformers cannot handle α ≥ 1/2 under any training. The paper acknowledges this explicitly (line 191: "The comparison is made between sufficient conditions") and Remark 6 adds appropriate caveats. The experiments in Figure 2 provide empirical support for the threshold, but the theoretical claim should be read as "under these training conditions, our analysis guarantees success only for α < 1/2" rather than "linear Transformers are fundamentally incapable beyond α = 1/2."

- **The required context length for α close to 1 grows large, which is not explicitly flagged as a limitation.** Condition (c) of Theorem 2 requires α < p_a l_tr/l_ts for robustness when α approaches 1. This implies l_tr must exceed l_ts/p_a, which can be substantial. The paper notes the condition but does not discuss the scaling cost.

### Trivial

- Equation reference "(200)" on line 65 should be "(2)."

## Nice-to-Haves

- Interpreting the batch-size lower bound in Theorem 1 (in particular the dependence on V² and β⁻⁴) in practical terms would help bridge the theory-practice gap.
- The main-text experiments use a single parameter configuration (d=30, M₁=6, V=3, l_tr=l_ts=20, p_a=0.6). Varying these parameters to illustrate sensitivity to the theoretical conditions would strengthen the empirical case.
- The decay base of 1/2 in Corollary 2's gating bound (Eq. 18) appears as a specific constant; a brief comment on how it depends on model parameters (initialization, training) would add insight.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic claim that the paper does not discuss that the Transformer comparison is based on sufficient/upper bounds:** REMOVED. The paper explicitly states this at line 191: "The comparison is made between sufficient conditions for the desired generalization. This is a common practice used in existing works." The paper also adds Remark 6 clarifying the scope. This criticism is factually incorrect — the paper directly addresses the concern the reviewer claims is missing.

- **Harsh Critic claim that the sensitivity to outlier placement (CQ vs FQ) is not discussed in relation to theoretical bounds:** REMOVED. Section 4.2 explicitly discusses this finding (lines 281–287) and connects it to Corollary 2's exponential decay result: "when outliers are placed close to the query, the clean examples that share the same pattern as the query are pushed farther away, and the gating values on these examples decay exponentially according to (18), thereby degrading ICL performance."

- **Harsh Critic claim that the paper should discuss the divergence of required context length for α close to 1 as a limitation not acknowledged:** PARTIALLY REMOVED — the paper explicitly states the condition α < p_a l_tr/l_ts and notes it "can be close to 1 if the prompt length is selected in a way such that p_a l_tr/l_ts ≥ 1." The scaling cost is implicit. Moved to Minor rather than treated as a major omission.

- **Strength Finder claim about this being the "first theoretical analysis of Mamba ICL":** KEPT — this is accurate and the paper explicitly positions itself as such, with appropriate comparison to prior work.

- **Strength Finder generic phrasing about the paper addressing an important problem:** REMOVED as generic/superficial.

- **Harsh Critic claim about "missing parts" — discussion of batch-size lower bound scaling, sensitivity to parameters, etc.:** MOVED to Nice-to-Haves. These are reasonable suggestions but not weaknesses per se.

## Novel Insights

The paper's theoretical framework reveals a clean architectural story: the nonlinear gating layer in Mamba serves as a learned outlier filter that can suppress corrupted context examples almost entirely (gating values close to 0), while simultaneously implementing a recency bias (exponential decay with index distance) on clean examples. This dual function of the gating — simultaneous suppression and localization — is not obvious from the Mamba architecture description and represents a genuinely novel mechanistic insight. The finding that this gating can be trained to generalize to unseen outlier patterns (provided they lie in the positive span of training outliers) suggests that the model learns a representation of "outlier-ness" in the gating feature space, which is an interesting direction for future work.

## Suggestions

- Clarify the model class in the title/abstract: the paper analyzes a "gated linear attention model (a simplified one-layer Mamba with A = −I)" rather than full Mamba. This would preempt the most common objection readers will have.
- Add a paragraph in the limitations section discussing what types of real-world prompt corruptions would or would not satisfy the positive-linear-span condition in Theorem 2(a), with concrete examples.
- In Section 3.4, add one sentence explicitly distinguishing sufficient conditions from necessary ones to avoid any reader misinterpretation: "We emphasize that α < 1/2 is a sufficient condition for our training setup; it does not preclude the possibility that alternative training methods or architectures could enable linear Transformers to handle higher outlier fractions."

Now, regarding score calibration. Let me report on all anchors retrieved:

## Score and Decision

**Round 1 — Bracketing:**
- `fzZfju8y0g` (avg 3.40): In-context neural PDE — applied work, not theory. Much weaker than current paper.
- `EVg9lwHFJs` (avg 3.00): Emotion recognition with ICL — empirical, weak. Much weaker.
- `4y3GDTFv70` (avg 3.25): Latent space theory for emergent abilities — weak theory. Much weaker.
- `kkVTeMvC9D` (avg 3.40): Training Jacobian — different topic. Weaker.
- `aKJr5NnN8U` (avg 6.50): In-context vs in-weight learning theory. Similar quality, slightly stronger framing and broader validation.
- `aN4Jf6Cx69` (avg 4.50): Mechanistic basis of ICL — polarized scores. Current paper is stronger.
- `gK1rl98VRp` (avg 6.00): AR-NTP ICL theory — current paper has clearer theoretical takeaway and better-connected experiments.
- `ikwEDva1JZ` (avg 6.50): ICL with representations — strong mechanistic analysis. Similar quality.
- `SPS6HzVzyt` (avg 8.00): Context-parametric inversion — different topic, very strong. Current paper is weaker.
- `STUGfUz8ob` (avg 7.60): Relational reasoning theory — stronger contribution with broader implications.

**Initial bracket:** 5.5–7.0.

**Round 2 — Narrowing:**
- `n7n8McETXw` (avg 6.50): Training Nonlinear Transformers for CoT — the closest structural match. First theoretical analysis of training dynamics for a specific architecture, similar data modeling, similar experiments. The current paper has comparable theoretical depth but weaker framing (A=−I simplification is more severe than the one-layer simplification). Current paper is slightly below this anchor.
- `EGjvMcKrrl` (avg 6.00): SSM generalization analysis — rejected despite all 6s due to experimental gaps. Current paper has better theory-experiment connection.
- `v9Pguuamfp` (avg 5.60): ICL as kernel regression — weaker theoretical contribution, less connected experiments. Current paper is stronger.
- `kIZ3S3tel6` (avg 5.50): Outliers in optimization — different topic. Current paper is stronger.
- `rLX7Vyyzus` (avg 6.00): Systematic outliers in LLMs — empirical paper, different style.

**Comparison summary:** The current paper sits between `gK1rl98VRp` (6.00, decent theory but weak experiments) and `n7n8McETXw` (6.50, similar structure but slightly better executed). The paper has clear, crisp theoretical results (especially the α threshold comparison), well-connected experiments, and a compelling mechanistic story. The main limitations — A=−I simplification making it "gated linear attention" rather than full Mamba, restrictive outlier span condition — are real but acknowledged.

The paper is a solid theoretical contribution with clear value to the community. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>