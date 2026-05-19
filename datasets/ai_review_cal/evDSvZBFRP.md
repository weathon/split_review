- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5
Now I have a thorough understanding of the paper and the reviews. Let me produce the final consolidated review.

---

## Summary

This paper proposes a method for formally verifying transformers using polynomial zonotopes—a non-convex set representation that preserves nonlinear dependencies through attention layers. The key technical contribution is exact matrix-set multiplication for the attention mechanism (avoiding the outer-approximations that convex relaxations require), combined with a tunable parameter ρ_lim that controls precision vs. computation time. The method generalizes prior zonotope-based transformer verification (Bonaert et al., 2021). Experiments on four small binary classifier models show larger verified embedding volumes than the zonotope baseline, and the paper provides formal complexity bounds.

---

## Strengths

1. **Exact matrix-set multiplication through attention preserves nonlinear dependencies.** Proposition 2 and Section 3.3 show that the paper computes the product of two polynomial zonotopes exactly (Eq. 11), avoiding the outer-approximations that convex relaxations require. This is the core technical advance, clearly contrasted with prior work, and Figure 3b visualizes the tighter enclosure this yields for a single attention head.

2. **Single-parameter precision trade-off generalizing prior convex methods.** Section 3.5 explains that setting ρ_lim = 1 recovers zonotope-level precision (Bonaert et al., 2021, Sec. 5.1), making the proposed method a strict generalization. Table 2 demonstrates that increasing ρ_lim yields progressively larger verified embedding volumes (e.g., normalized volume 3.73 on Yelp at ρ_lim = 4 vs. 1.0 for the zonotope baseline), confirming the tunable precision in practice.

3. **Empirical demonstration of scaling beyond brute-force synonym enumeration.** Figure 3a quantitatively compares enumeration (exponential in number of synonym words) against the proposed set-based verification, which completes in seconds. Table 1 further shows a verified sentence with 96 synonym words corresponding to 2+ billion sentences handled in a single query.

4. **Formal complexity analysis with bounded runtime.** Theorem 1 proves the overall verification complexity is O(t·h·d_V·d_model·g_max·κ), which is linear in all parameters after applying order reduction. Lemma 3 analyzes the uncontrolled generator growth, and the paper explicitly introduces mechanisms (ρ_lim, g_max) to contain it. This provides clear theoretical grounding for the method's tractability.

---

## Weaknesses

### Fatal
None.

### Major

1. **Model architecture specifications are entirely missing.** The paper evaluates on "four large language models M_i, i ∈ [4], trained from scratch for binary classification" (Section 4) but provides no information about their architecture: embedding dimension (d_model), number of transformer blocks (κ), number of attention heads (h), dimension of Q/K/V projections (d_{QK}, d_V), or any other structural parameter. Without these details, readers cannot assess what scale of model was actually tested, whether the models are truly "transformer-based" or simplified variants, or how this compares to the architectures these experiments should inform. This omission undermines the experimental section's interpretability and should be fixed in the main paper.

### Minor

1. **No ablation of the precision/computation trade-off.** The paper introduces ρ_lim and g_max as critical parameters controlling how much precision is sacrificed through order reduction, but provides no analysis of this trade-off. An ablation study—e.g., showing verified volume as a function of ρ_lim (beyond the four values in Table 2) or g_max for a fixed model—would give readers concrete insight into how the method behaves. The absence is particularly notable because the paper's central claim is that precision is "tunable at the cost of additional computation time," yet the relationship between these parameters and precision loss is not explored.

2. **No variance reporting.** Table 2 reports "averaged results of 20 sentences" but provides no standard deviations, confidence intervals, or per-sentence breakdowns. Since verification results can vary substantially by input, the stability of the reported improvements is unclear.

### Trivial

1. **"Normalized verified volume"** in Table 2 is not formally defined in the text. The paper states volume is normalized to the zonotope baseline, but the reader is left to infer how volume is computed (product of per-dimension ε?).

2. **Softmax enclosure details are deferred entirely.** The reformulation in Eq. 12 and the enclosure via exponential/inverse functions in Lemma 2 reference prior work for implementation details. While acceptable for a conference paper, a brief note on how positivity of the inverse argument is ensured would improve self-containedness.

---

## Nice-to-Haves

- Testing on a moderately larger architecture (e.g., a 2–3 layer transformer with d_model = 128–256) would substantially strengthen the claim that the method is progressing toward LLM-scale verification.
- A clearer upfront statement of the verification problem (the two-stage classifier-as-safety-shield setup) would improve exposition; the current presentation requires inference from the running example.

---

## Removed Points

The following points from the reviews are removed with justification:

1. **"Evaluation mismatch — paper does not verify LLMs"** (Harsh Critic, Critical Issue 1): Removed. The paper's title includes "Towards," the abstract uses "towards formally verifying LLMs," and Section 6 explicitly states "all methods are not yet applicable to modern-size large language models." The paper is a methods paper demonstrating feasibility on smaller models, which is appropriate for this stage of research. The critic's framing as a fatal mismatch overstates what the paper claims.

2. **"Baseline comparison is suspect"** (Harsh Critic, Critical Issue 2): Removed. The paper's claim that ρ_lim = 1 recovers zonotope-level precision is mathematically sound—polynomial zonotopes reduce to zonotopes when higher-order terms are interval-hulled. The paper also has a *separate* zonotope baseline (labeled "Z, Bonaert et al. (2021)") in Table 2, so the comparison is not circular. The harsh critic's concern about interval hull vs. zonotope misunderstands that Bonaert et al., Sec. 5.1 explicitly discusses interval-hulling higher-order terms as an order-reduction technique for zonotopes.

3. **"Scalability not demonstrated (exponential growth)"** (Harsh Critic, Critical Issue 3, partial): Removed as stated. The Lemma 3 exponential bound is *without* order reduction; Theorem 1 gives the *with*-reduction bound (linear in all parameters). The paper transparently shows both. The valid sub-concern about lacking an ablation of precision loss from order reduction is preserved as Minor weakness #1 above.

4. **Various section-by-section nitpicks** about the running example being "convoluted," modified layer normalization not being "flagged as a limitation," softmax enclosure being "too vague," and order reduction being "insufficiently described": All removed. The running example is clear, the normalization is described as following prior work, the softmax enclosure appropriately defers to well-known techniques (Singh et al., 2018; Bonaert et al., 2021; Wei et al., 2023), and the order reduction method cites (Kochdumper & Althoff, 2020, Sec. II-E). These are standard practices.

5. **"IBP baseline is trivially weak"**: Removed. IBP is a standard baseline in neural network verification; its inclusion does not harm the paper.

6. **"Comparison with Wei et al. (2023) and Zhang et al. (2024)"**: Removed. The paper cites these works in the related work section and contrasts its non-convex approach with their convex relaxations. Explicitly requiring experimental comparison with every related method is beyond what is expected.

7. **All Strengths-Finder points about "scaling beyond brute-force enumeration" and "formal complexity analysis"**: These are retained as Strengths 3 and 4 above since they are well-grounded in the paper.

---

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective on the work that the authors themselves do not already articulate.

---

## Suggestions

1. **Add a table with full model specifications** (d_model, κ, h, d_{QK}, d_V, number of parameters) for each of the four models evaluated. This is the single most important improvement to the experimental section.
2. **Include an ablation study** showing verified volume as a function of ρ_lim (more granular values) and g_max.
3. **Report per-sentence results** (e.g., in a scatter plot or table with individual values) or at minimum include standard deviations across the 20 sentences.
4. **Define "normalized verified volume" explicitly** in the text or a footnote.

---
