Now I have enough information to produce the final consolidated review. Let me synthesize everything.

---

## Summary

This paper introduces a weight-based method for classifying the read-write (RW) functionality of gated neurons in transformer MLPs, using cosine similarities between input, output, and gate weight vectors. The method yields a taxonomy of neuron types including *strengthening*, *weakening*, and *conditional strengthening* neurons. The authors discover a small class of weakening neurons (cos(w_in, w_out) ≈ −1) that activate frequently and have an outsize influence on model behavior. Across 12 LLMs, they find a universal layer-wise pattern: early-middle layers are dominated by conditional strengthening neurons, while late layers contain proportionally more weakening neurons. They also introduce *conditional ablation* to isolate the effect of specific activation-sign regimes, revealing that much of the weakening neurons' influence comes from cases with negative gate values — a previously unrecognized functional mechanism in Swish-activated transformers.

## Strengths

- **Novel taxonomy grounded in weight geometry.** The method of classifying neurons by cosine similarities between their weight vectors (w_in, w_out, w_gate) is simple, principled, and yields a clean, reproducible classification scheme (Table 1, Figure 2). It fills a gap in the literature, where most neuron analysis has focused on either input contexts or output weights in isolation, not the relationship between them.

- **Discovery of weakening neurons with validated outsize influence.** Zero-ablating all 243 weakening neurons in OLMo-7B substantially affects attribute rate and next-token entropy, while ablating an equal number of random neurons from the same layers has negligible effect (Figure 3). The mean ablation results (Section F.4) provide convergent evidence. This is a genuinely surprising and well-demonstrated finding.

- **Conditional ablation technique and negative-gate mechanism.** The conditional ablation method (Section 6.2) is an elegant technical contribution that isolates the effect of specific activation-sign patterns. The finding that negative gate values drive much of the sharpening effect of weakening neurons (Figure 3b, bottom-left subplot) is novel and challenges the common assumption that negative gate values are merely useful for training dynamics. The case study of neuron 31.9634 (Section 8) corroborates this finding at the individual neuron level.

- **Cross-model universality of layer-wise patterns.** Figure 1(a) convincingly demonstrates that the median cos(w_in, w_out) transitions from positive to negative across layers in nine different LLMs of varying architectures and scales. This is a robust empirical regularity that any theory of MLP computation must account for.

- **Strong negative correlation between cos(w_in, w_out) and activation frequency.** Section 7 shows near-linear negative correlations (e.g., r = −0.97 at layer 15) between a neuron's weight geometry and how often it activates, extending prior findings from GELU models to gated activation functions. This provides an elegant link between static weight structure and dynamic behavior.

## Weaknesses

### Fatal

None.

### Major

- **Ablation experiments do not fully control for activation frequency as a confound.** Table 5 shows that weakening neurons activate much more frequently (mean 0.691) than random neurons (0.384) or conditional strengthening neurons (0.132). Any frequently activating neuron will have a larger effect when zero-ablated, so the observed difference in attribute rate and entropy could be partially attributable to frequency rather than the weakening class *per se*. The paper acknowledges this in Section 7 ("activation frequencies do not fully explain their effect") and the conditional ablation results (showing effects from rare negative-gate activations) partially mitigate the concern, but a direct control — e.g., ablating a set of high-frequency non-weakening neurons — would substantially strengthen the claim. This does not invalidate the core contribution but leaves an alternative explanation partially open.

### Minor

- **The mapping from weight cosine similarity to functional "read-write" behavior has an interpretive gap.** The paper classifies neurons based on static weight geometry and then uses functional-sounding labels (strengthening, weakening). The authors are appropriately careful: they explicitly state that the semantic interpretation is "not a necessary assumption" and is "helpful for building intuition" (Section 4.1). The ablation experiments provide causal evidence that the weakening *class* matters, but they do not directly demonstrate that individual strengthening neurons actually strengthen their detected directions during inference, nor that weakening neurons weaken them. This gap between geometric classification and operational function is acknowledged but not fully bridged. The case studies (Section 8) are helpful but qualitative and limited to two neurons.

- **The cosine-similarity threshold τ = 0.5 is arbitrary and its robustness is not explored.** The classification into prototypical categories depends on a hard cutoff at ±0.5. No sensitivity analysis is provided to show whether the main findings (late-layer weakening dominance, class distribution) are stable under different thresholds, or whether a continuous treatment would be more appropriate. Given that the paper also presents continuous analyses (Figures 1a, 2, 4), this is not a fatal issue, but the claimed class sizes and distributions should be interpreted with appropriate caution.

- **Functional ablation is limited to a single model (OLMo-7B).** The universality claims are geometric (cross-model consistency of weight cosine patterns), and these are well-supported by Figure 1. The functional claims about weakening neuron influence are demonstrated only on OLMo-7B. Extending ablation experiments to one or two additional models would strengthen the generality of the functional findings, though the paper's main contribution does not rest on cross-model functional claims.

### Trivial

- The paper could benefit from reporting statistical tests or confidence intervals for the ablation results, though single-run evaluation is standard in this subfield and the effects shown are substantial enough to be convincing without formal tests.

## Nice-to-Haves

- An ablation control matching on activation frequency (e.g., selecting the top-N most frequently activating neurons that are *not* weakening neurons, and ablating those) would elegantly rule out the frequency confound.

- Sensitivity analysis varying τ from, say, 0.3 to 0.7 to assess the stability of the weakening-neuron count and layer distribution.

- Extending the conditional ablation analysis to other neuron classes (e.g., conditional strengthening) to see whether negative-gate effects are unique to weakening neurons or a more general phenomenon.

- A systematic rather than case-study-based check of whether weight-based classifications correspond to activation-level behavior across a larger sample of neurons.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

**1. Preprocessing sign-flip concerns (from Harsh Critic):** The critic claimed the preprocessing step (multiplying w_in and w_out by sign of cos(w_gate, w_in)) disrupts classification because it can flip cos(w_gate, w_out). This is directly addressed in Section C of the paper. The preprocessing is a symmetry property that does not change model behavior (the two sign flips cancel in the product). The paper explicitly shows (Figure 5 vs. Figure 2) that without preprocessing, weakening neurons split into two equivalent clusters. The preprocessing unifies functionally equivalent representations. The classification is performed on preprocessed weights by design, and the justification is clearly provided. **Removed because the paper already addresses this concern thoroughly.**

**2. Case study "cherry-picking" and contradiction criticism (from Harsh Critic):** The critic claimed that the weakening neuron case study is cherry-picked and that the neuron's activations "contradict the simple weakening hypothesis." In fact, the paper itself states that the weakening neuron "is much harder to interpret" and that the most interpretable activations occur specifically in the negative-gate regime. The paper is honestly reporting complexity, not hiding it. The case study corroborates the conditional ablation findings rather than undermining them. **Removed because the critic's characterization misrepresents what the paper actually says.**

**3. Demand for functional validation of the semantic interpretation:** The critic demanded that the paper demonstrate that strengthening neurons actually "increase the targeted direction in the residual stream during inference." The paper explicitly states in Section 4.1 that the semantic/concept interpretation "is not a necessary assumption for our neuron classification" — the classification describes mathematical RW functionality (what direction gets added/subtracted), which follows directly from the weight geometry. The ablation experiments validate that the classification captures functionally meaningful groupings. **Removed because the paper is appropriately scoped and does not overclaim semantic interpretability.**

**4. "Universality claims without functional validation" (Harsh Critic):** The critic claimed the paper asserts functional universality without evidence. The paper's universality claim is about the geometric pattern (cosine similarity distributions), which is demonstrated across 9 models in Figure 1(a). The paper does not claim functional universality across all models — functional claims are tied to OLMo-7B ablation experiments. **Removed because the criticism conflates geometric and functional claims.**

**5. Strength Finder - "publicly available models and data" as a strength:** While true, this is a generic characteristic of most modern ML papers and does not constitute a distinctive strength. **Dropped as superficial.**

**6. Strength Finder - "methodological contribution of conditional ablation beyond this paper":** While the conditional ablation method is nice and useful, calling it a standalone methodological contribution is somewhat generous — it is a straightforward conditioning on activation signs. **Weakened and folded into the associated strength about the negative-gate finding.**

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: weight-geometric regularities that are clearly non-random (Figures 1, 2) and correlate with functional importance (Figure 3) but whose precise mapping to neuron-level operational semantics remains partially opaque. This mirrors a broader challenge in mechanistic interpretability — the gap between structure (weights/geometry) and function (causal role) — and the paper's honest treatment of this gap (acknowledging complexity in the weakening neuron case study, not overclaiming semantic content) is a methodological strength. The finding that negative gate values carry functional signal in trained models also independently corroborates and extends concurrent work (Kong et al., 2025; the "Negative Pre-activations Differentiate Syntax" paper from the anchors), suggesting that smooth activation functions are not merely training-dynamics conveniences but are actively exploited for computation.

## Suggestions

- The most impactful single addition would be an activation-frequency-matched baseline for the ablation experiments. This would definitively rule out frequency as the primary driver of the weakening-neuron effect and would fit naturally into the existing experimental framework.

- Varying τ and reporting the stability of key findings (e.g., number of weakening neurons, layer distribution) would address concerns about the arbitrary threshold without requiring new experiments — it is a simple re-analysis of existing data.

- Consider reframing some of the functional language to more precisely reflect what is demonstrated: the classification captures the *direction of residual stream updates* (which is mathematically established) rather than *concept manipulation* (which requires additional semantic validation).

---

**Anchor calibration:**

- `/home/wg25r/review_agent/human_reviews_2026/RzcCrU0tXP.md` (avg 5.50, "Negative Pre-activations Differentiate Syntax"): Most directly comparable — also finds functional roles for negative activation regions in smooth-activation LLMs. Current paper has broader scope (full taxonomy, cross-model analysis, conditional ablation technique) and comparably strong evidence. Current paper rates slightly higher.

- `/home/wg25r/review_agent/human_reviews_2026/v6HPsCu2R8.md` (avg 5.33, "Hedonic Neurons"): Novel MLP interpretability method with ablation validation. Current paper is similarly innovative in methodology, with stronger cross-model evidence. Comparable quality.

- `/home/wg25r/review_agent/human_reviews_2026/pJoSE7Cvj0.md` (avg 5.00, "Achilles Heel of LLMs"): Finds sparse critical neurons via perturbation. Current paper provides more mechanistic depth (taxonomy, conditional ablation, negative-gate mechanism) and is more novel methodologically.

- `/home/wg25r/review_agent/human_reviews_2026/mRLnS8jQWt.md` (avg 4.50, "Rethinking Layer Relevance"): Critiques cosine similarity as an interpretability metric. Current paper uses cosine similarity productively to discover new structure; substantially more novel contribution.

- `/home/wg25r/review_agent/human_reviews_2026/lnTX3GoeTY.md` (avg 4.50, "Feature segregation by signed weights"): Related method using signed weights. Current paper is broader in scope and model coverage, with stronger causal evidence.

- `/home/wg25r/review_agent/human_reviews_2026/Z1m2tXaH2G.md` (avg 2.50, "Revisiting LLM Pruning using NSA"): Rejected for heuristic methodology and weak validation. Current paper is substantially stronger in both methodology and validation.

- `/home/wg25r/review_agent/human_reviews_2026/QCB0HN61TU.md` (avg 7.00, "Map the Flow"): Higher-scoring mechanistic interpretability work on VideoLLMs. Current paper is narrower in task scope (no downstream task evaluation) but comparably rigorous in methodology.

- `/home/wg25r/review_agent/human_reviews_2026/UJ2UUjT2ko.md` (avg 8.00, "Mixing Mechanisms"): Top-tier mechanistic interpretability with clean experimental design and definitive findings. Current paper is less polished and has more open questions, but makes comparably novel discoveries.

The current paper has genuine, well-supported contributions (novel taxonomy, discovery of weakening neurons, conditional ablation, universal geometric patterns, negative-gate mechanism). The main limitations — activation frequency control, threshold sensitivity, single-model ablation — are addressable and do not undermine the core claims. This places the paper solidly above the 4.0-5.0 range and comparable to the stronger 5.0-6.0 anchors. It does not reach the polish and definitiveness of the 7.0-8.0 anchors due to the remaining methodological gaps.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>