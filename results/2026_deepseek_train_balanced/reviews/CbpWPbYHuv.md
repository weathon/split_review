Here is my consolidated final review.

---

## Summary

This paper proposes PolyCom, a family of activation functions formed by composing polynomials with standard nonlinearities (ReLU, normalization, etc.), yielding two concrete instantiations: PolyReLU (Type I) and PolyNorm (Type II). The authors provide theoretical analysis showing approximation bounds relative to ReLU networks and claiming an optimal approximation rate in Sobolev spaces. They validate the method empirically on 1B-parameter dense LLMs and 1B/7B MoE models trained on hundreds of billions of tokens, reporting consistent improvements over ReLU, GELU, and SwiGLU.

## Strengths

- **Two-sided approximation bounds between PolyReLU and ReLU networks (Theorem 2, lines 132–147).** The paper provides both an upper bound and a matching-style lower bound for the size of a ReLU network needed to approximate a PolyReLU network. Two-sided analysis of this kind is more rigorous than the one-directional comparisons typical in activation-function papers, and the logarithmic gap formally quantifies a representational efficiency advantage.

- **Large-scale empirical validation on both dense and MoE architectures (Tables 1–4, lines 203–282).** Unlike most activation-function papers that test only on small models, this work trains 1B-parameter dense models on 250B tokens and 1B/7B MoE models on 200B tokens. PolyNorm consistently edges ahead of SwiGLU on average across downstream benchmarks (by ~1.2% on dense, ~0.6% on MoE), demonstrating practical viability at a scale that matters.

- **Systematic ablation of design choices (Section 4.3, lines 283–289).** The paper explores orders r ∈ {2,3,4}, compares four composition variants (PolyReLU, PolyPReLU, PolyNorm, PolyReLUNorm), and documents overflow risks for higher orders under low-precision arithmetic, leading to a principled default choice of r=3. This gives practitioners actionable guidance.

- **Mechanistic analysis via weight rank and layer-wise similarity (lines 291–292).** The analysis showing higher weight matrix ranks and lower layer-wise cosine similarity for PolyCom models provides interpretable diagnostics that go beyond reporting final accuracy.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Unsubstantiated equivalence claim between Type I and Type II PolyCom (line 49).** The paper states: "It can be theoretically shown that both approaches have equivalent expressivity, provided that ρ is a non-linear function. This is because polynomial terms are symmetric with respect to composition…" No proof, sketch, or even an intuitive argument is provided for this non-trivial claim. Since the paper's entire theory section (line 80) then says "As discussed in Section 2, PolyReLU and PolyNorm have equivalent expressivity. To streamline the analysis, we focus solely on the theoretical properties of PolyReLU," the theoretical analysis rests on an unverified assertion. At minimum, the authors should clarify the sense in which "equivalent expressivity" is meant and provide a proof sketch.

2. **Single-run experiments with no measures of variability.** Every result in Tables 1, 3, and 4 reports single numbers with no standard deviations, error bars, or significance tests. The reported improvements are modest (~1.2% for PolyNorm over SwiGLU on the dense model, ~0.6% on the MoE model). At this scale, training dynamics (data ordering, optimizer noise, initialization) can produce non-trivial variation, and the reader cannot assess whether these differences are reliable or within the noise floor. While multiple seeds at this scale are expensive, even 2–3 seeds for a subset of settings would substantially strengthen the evidence.

3. **Square ReLU listed as a baseline but excluded from the main comparison table.** Line 186 lists "square ReLU" alongside ReLU, GELU, and SwiGLU as a baseline. Square ReLU appears only in the ablation (Figure 3c) and is absent from Table 1's main comparison. Since PolyReLU (∑ a_i ReLUⁱ(x)) literally extends square ReLU (ReLU²(x)) by adding higher-order terms, excluding square ReLU from the main table makes it difficult to isolate whether PolyReLU's gains come from higher-order terms or simply from having a quadratic term. This omission makes the evaluation appear selectively favorable.

4. **Computational overhead of PolyNorm unmeasured.** PolyNorm (Equation 3) requires computing L2 norms of element-wise power vectors at every FFN forward pass — a non-trivial operation compared to the element-wise lookups of ReLU or GELU. The paper acknowledges overflow issues for higher orders (line 285) but provides no wall-clock timing, tokens/second throughput, or memory comparison against standard activations. For practitioners evaluating whether the modest accuracy gains justify the added complexity, this is a noticeable gap.

5. **Descriptive-only mechanistic analyses (Section 4.3).** The weight rank and layer-wise cosine similarity analyses (Figures 4–5) show that PolyCom models have higher weight ranks and lower layer similarity. However, these are purely correlational observations — no causal link is established between these properties and downstream performance. The paper's language ("this diversity likely enables the model…") appropriately hedges, but the analysis remains suggestive rather than explanatory.

### Trivial
None.

## Nice-to-Haves

- **Throughput and memory comparison.** A tokens/second and peak-memory comparison between PolyNorm and standard activations would directly answer the practical question of whether the method is deployable at scale.
- **Coefficient initialization ablation.** The coefficients are initialized as a_i = 1/3 (for r=3), but the sensitivity to this choice is not explored.
- **Clarify intermediate dimensions.** The paper adjusts intermediate size for SwiGLU to 2/3 of other activations but does not report the actual numerical dimensions used, making reproduction slightly harder.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Theorem 3 being "unsubstantiated" or "asserted without proof."** The proof resided in the appendix, which is stripped by the PDF parser. The comparison to Yarotsky (2017) and Boulle (2020) is factually correct as stated. The critic's claim that "subsequent work has shown ReLU networks can achieve the optimal rate without the log factor" depends on unverifiable external literature and is a missing-reference style argument, which is excluded per guidelines.
- **The comparison to Yarotsky being "unfair."** The paper correctly cites Yarotsky's published bound O(ε^{-d/n} log(1/ε)). Speculation about later improvements to that bound is not a valid criticism of the paper as written.
- **Lemma 1 being "trivial."** It is formally correct and provides the necessary foundation for Theorem 1. Its simplicity is not a weakness.
- **"Same size" framing (Theorem 1) being "misleading."** "Size" is standard terminology for neuron/weight count in approximation theory; the additional a_i coefficients per layer are negligible.
- **Theorem 2's logarithmic gap being "small."** A formal separation is meaningful regardless of the gap's magnitude.
- **Missing GSM8K/HumanEval tasks.** The paper lists 13 evaluation benchmarks; the selection is reasonable.
- **Related work not engaging with Hornik/Trefethen's central finding.** The paper explicitly discusses this limitation (line 41–42: "neural networks with polynomial activation are not dense within the space of continuous functions") and positions PolyCom as a solution to it.
- **Formatting/style/title nitpicks, typos, and grammar.** These are parser artifacts.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface an insight about the method or results that the paper itself does not already articulate.

## Suggestions

1. Provide a proof sketch for the equivalence claim between Type I and Type II PolyCom, or alternatively, drop the claim and explicitly characterize how the two variants differ.
2. Report results with at least 2–3 random seeds for the dense model (or a subset of settings) to give readers a sense of variability; include confidence intervals or error bars.
3. Include square ReLU in the main comparison table (Table 1) to allow a clean isolation of the effect of higher-order terms.
4. Add a throughput (tokens/second) and memory comparison for PolyNorm vs. standard activations.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>