- Decision: Reject
- Avg Score: 4.60
- Scores: 6, 6, 3, 5, 3
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper makes two contributions to multi-modal variational autoencoders. First, it proposes a new variational objective (Eq. 7) that avoids the irreducible conditional-entropy gap of mixture-based bounds by introducing a second latent variable — one encoding a modality subset and the other encoding all modalities — with a KL term that aligns them. Second, it introduces learnable permutation-invariant aggregation schemes (SumPooling via DeepSets, Self-Attention via Set Transformers) that are more flexible than the standard fixed Product-of-Experts (PoE) and Mixture-of-Experts (MoE) aggregators. The paper provides theoretical analysis (distribution matching, information-theoretic interpretation, identifiability) and experiments on linear toy models, non-linear identifiable models, and the MNIST-SVHN-Text benchmark showing consistent log-likelihood improvements.

## Strengths

1. **Novel variational objective that addresses a known limitation of mixture-based bounds.** The paper correctly identifies the irreducible gap of mixture-based bounds due to conditional entropies (Daunhawer et al., 2022) and proposes a principled alternative. Corollary 1 and Remark 3.5 show that, unlike the mixture bound, the proposed objective can become tight in the infinite-capacity encoder limit. The bound is explicitly an "approximation of a lower bound" (line 97), and the paper is transparent about the indefinite term in Corollary 1 (line 205: "is not necessarily negative").

2. **Learnable aggregation schemes that consistently outperform fixed PoE/MoE.** Across all experimental settings — linear Gaussian (Tables 1–2), non-linear identifiable models (Tables 3–4), and MNIST-SVHN-Text (Table 5) — SumPooling and Self-Attention achieve higher test log-likelihoods than PoE or MoE for the same variational objective. For example, on the bi-modal linear toy (Table 1), the relative LLH gap drops from 1.29 (PoE) to ≈3.6×10⁻⁵ (SumPooling); on MNIST-SVHN-Text (Table 5), the joint LLH rises from 6775 (PoE) to 7056 (SumPooling) under the proposed objective.

3. **Information-theoretic interpretation providing a principled rate-distortion analysis.** Lemma 4.2 and Corollary 4.3 show that the proposed objective can be viewed as a Lagrangian relaxation of bounds on marginal and conditional mutual information, enabling a multi-modal rate-distortion trade-off analysis (Figure 4). This goes beyond the standard mixture-based analysis and gives practitioners a principled lens for understanding trade-offs.

4. **Reasonably thorough experimental design.** The experiments span linear toy models with analytical ground truth, non-linear identifiable models with controlled generative factors, and a real-world tri-modal benchmark (MNIST-SVHN-Text). Multiple evaluation metrics are used (LLH, MCC, rate-distortion, conditional coherence), and the paper compares its proposed objective against mixture-based bounds with the same aggregation schemes, providing a clean ablation of the two contributions.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **The bound status could create reader confusion despite transparent discussion.** The paper's title ("tighter variational bounds") and abstract ("tightly approximate") may lead readers to expect a guaranteed lower bound, whereas the conditional term ℒ_{\𝒮} is an *approximation* of a lower bound — it can exceed the true log-likelihood if q_φ(z|x_𝒮) is far from p_θ(z|x_𝒮). The paper *does* transparently discuss this (Remark 4.2, Corollary 1, contribution statement line 97), so the criticism is about framing rather than omission. Nevertheless, a reader who skims the title and abstract without reading the fine print could walk away with a mistaken impression. A small clarification in the abstract (e.g., "a variational objective that can tightly approximate the data log-likelihood while avoiding the irreducible gap of mixture-based bounds, at the cost of being an approximate rather than strict lower bound") would eliminate this risk. The paper otherwise handles this honestly.

2. **MoPoE is not directly compared in the main LLH experiments.** The paper acknowledges MoPoE as a permutation-invariant aggregation scheme (Remark 4.1) and includes results cited from prior work in the conditional coherence table (Table 5), but MoPoE is absent from the primary LLH comparisons in Tables 1–4. While MoPoE is a *fixed* scheme (like PoE/MoE), not a learned aggregation function like the paper's main aggregation contribution, a direct comparison under identical conditions would strengthen the claim that the proposed schemes are generally beneficial. The omission is notable but not critical, because the paper's aggregation contribution focuses on *learnable* PI functions — a different design dimension.

3. **Some results show high variance without discussion of statistical reliability.** In Table 3, the PoE LLH under the mixture bound is −318±361.2 — the standard deviation far exceeds the mean. While most other entries have more moderate variance, the paper does not comment on which differences are statistically robust. This does not invalidate the overall trends (which are consistent across many experiments) but makes it harder to assess individual comparisons.

4. **The identifiability evidence is less compelling than claimed.** Proposition 2 is a direct translation of prior work (Lu et al., 2022) from the iVAE setting. The experimental evidence (Tables 2–4) shows that MCC values are uniformly high across methods (often 0.98–1.00), so the incremental benefit of the proposed innovations for identifiability is small. The paper does acknowledge this in its weaker claim ("can become beneficial"), but the identifiability section feels somewhat disconnected from the main narrative.

### Trivial

- The large number of remarks in Section 2 (seven remarks) interrupts the flow; some could be streamlined or moved to the appendix.

## Nice-to-Haves

- A direct comparison against MoPoE under the same experimental conditions (same architectures, latent dimensions, β) for at least one key experiment, to clarify where the learnable aggregation schemes sit relative to this existing PI alternative.
- A brief discussion in the limitations of scenarios where the indefinite term in Corollary 1 could cause the objective to overestimate the log-likelihood, and whether this can be mitigated in practice.
- Expanded experiments on the private latent variable setting (Section 5.4), which currently receives only a single table row and a few qualitative figures.

## Removed Points

The following points from the inputs were removed with justification:

- **"No code or reproducibility details"** (Harsh Critic): The instruction requires removal of criticisms about missing appendix content and reproducibility details such as hyperparameters and architecture specifics, as these were likely in the appendix (stripped by the parser). Also falls under the rule against nitpicks about "trivial implementation details, or large artifacts impractical to include."
- **"Missing related works"** (Harsh Critic): The instruction prohibits mentioning missing related works as the reviewer cannot confirm their existence.
- **"Axis labels too small to read" on rate-distortion plots** (Harsh Critic): Parser/formatting artifact, not a paper flaw.
- **"Pure formatting/style nitpicks"** and typographical complaints: Removed per the instruction that parser issues are not author errors.
- **Strengths from Strength Finder that were generic or conflicted with verified weaknesses**: Several generic strengths about "importance of the problem" and "timely topic" were removed as they lacked specific evidence or constituted scope-creep sycophancy. Only concrete, evidenced strengths are retained.
- **The claim that the bound "is not guaranteed to be a lower bound" as a fatal flaw**: While factually correct, the paper explicitly and repeatedly acknowledges this (line 97: "approximation of a lower bound"; line 138: "only approximates a lower bound"; Remark 4.2; Corollary 1). The paper's title/comparative framing is also appropriate — "tighter" is a comparative claim relative to the mixture bound, which is true in the infinite-capacity limit. Demoted from "fatal" to minor framing concern.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. In the abstract, add a brief qualification that the proposed objective is an approximate lower bound (not guaranteed) — e.g., "a variational objective that can tightly approximate the data log-likelihood while avoiding the irreducible gap of mixture-based bounds."
2. Add a direct MoPoE comparison in at least one of the main LLH tables (Tables 1–4) to benchmark against this existing permutation-invariant alternative.
3. Comment on the high variance in Table 3 (PoE under mixture bound) and clarify which comparisons are likely robust.
4. Reduce the number of remarks in Section 2 by moving tangential ones to the appendix or collapsing them into in-text sentences.
