Now I have a thorough understanding of the paper and have verified each criticism against the actual text. Let me produce the final consolidated review.

## Summary

This paper proposes a unified view of delta-parameter editing operations (pruning, quantization, low-rank approximation, extrapolation) in post-trained models through a Riemann sum approximation of the loss function. It categorizes editing methods into three classes — competitive (DARE), decreased (BitDelta, Twin-Merging, TIES-Merging), and improved (EXPO) — and derives expressions showing how each affects the loss. The framework is validated across LLaMA-3, Mistral, and ViT models on 16 tasks, and extensions are proposed for DARE and BitDelta.

## Strengths

- **Riemann sum framework unifies methodologically diverse editing operations under a single tractable loss-change expression.** The paper derives a single approximation (Eq. 1) that simultaneously expresses why DARE preserves performance (the term vanishes to zero via randomness + Law of Large Numbers), why BitDelta/Twin-Merging/TIES-Merging degrade it (the term is positive), and why EXPO can improve it (the term can be negative when gradient aligns with delta direction). Prior work gave each method separate, ad-hoc explanations (embedding approximation for DARE, SVD for Twin-Merging, etc.); this is the first framework treating them as instances of the same mathematical object.

- **Identifies a sharper condition for DARE-like performance preservation.** The paper isolates that randomness in the *element-wise product of delta parameters and the loss gradient* (not randomness in delta parameters alone) is the operative condition for a zero approximation term (Sec. 4.3), with controlled experiments confirming this distinction. This is a more precise characterization than DARE's original "random drop preserves embeddings" claim.

- **Shows that sign-flipping delta parameters (k<0) preserves performance**, challenging prior assumptions (TIES-Merging, BitDelta) that individual delta-parameter signs are critical. This supports the paper's broader point that collective behavior of the entire delta parameter distribution matters more than individual directional adjustments (line 151).

- **Shows that EXPO's extrapolation vs. interpolation choice is data-dependent, not a fixed property of the method.** The paper demonstrates (Sec. 6.2) that for LLaMA3-8B-Instruct, *interpolation* (negative α) outperforms extrapolation on most benchmarks, directly contradicting EXPO's framing that extrapolation is the mechanism for improvement.

- **Multi-bit extension of BitDelta** with magnitude-aware blocking surpasses the original post-trained model at 4 bits, revealing redundancy beyond what prior quantization work suggested.

## Weaknesses

### Major

1. **The framework is only partially predictive; for two of three categories it provides a post-hoc mathematical description rather than a prediction.** For DARE (competitive performance), the theory derives Δℒ≈0 deterministically from randomness + the Law of Large Numbers (Eq. 122–124) — this is genuinely predictive. However, for the decreased-performance methods (BitDelta, Twin-Merging, TIES-Merging), the paper derives expressions for Δℒ but cannot determine the sign theoretically — line 218 explicitly states "We exploit the value of the approximation term through experiments." For EXPO (improved performance), the sign depends on whether the gradient aligns with the delta direction, which is checked experimentally (line 270). This asymmetry between categories means the framework provides a unified *expression* for all methods but a predictive explanation only for the competitive-performance category. The paper's abstract claim of "elucidating" and "explaining" all categories is partially accurate but the limitations in predictive power should be more clearly acknowledged.

2. **The TIES-Merging analysis captures only the magnitude-based pruning component, not the full multi-task merging algorithm.** Equation (198) models TIES-Merging as simple magnitude-based pruning on a single delta matrix (M ⊙ ΔW). The actual TIES-Merging involves sign-conflict resolution across *multiple* task vectors from different fine-tuned models — its core mechanism is multi-task merging, not single-delta pruning. The paper should explicitly clarify that it analyzes the pruning aspect of TIES in isolation. This is not fatal (the pruning operation itself is of interest), but the current framing is misleading.

### Minor

3. **The EXPO formulation simplifies away the checkpoint-to-checkpoint delta.** The paper (line 250) correctly notes that EXPO computes deltas between an aligned model and its *initial fine-tuning checkpoints*, but Equations (253–258) treat ΔW as the standard pre-trained-to-post-trained difference. While the essential extrapolation behavior is preserved, this simplification could affect the gradient landscape assumptions and should be acknowledged as an approximation rather than presented as equivalent.

4. **No discussion of when the first-order Riemann sum approximation breaks down.** The paper uses C=1 (midpoint rule with one interval), which is a coarse approximation. For large edits (large α in EXPO, extreme k in the DARE extension), higher-order Hessian terms could dominate, but the paper never discusses this limitation or bounds the approximation error. The EXPO section's observation about an optimal α (line 270) is precisely where higher-order terms start to matter, but the theory has no way to predict this optimum.

## Nice-to-Haves

- The DARE analysis would be strengthened by testing additional non-random interventions beyond the sign-based one, to more convincingly establish the generality of the claimed condition.
- Engaging with alternative theoretical frameworks (e.g., the "nearly orthogonal" view of task vectors from the model merging literature, e.g., Ilharco et al. 2023) would help position the Riemann sum lens relative to existing explanations.

## Removed Points

These points were evaluated and removed with justifications:

- **Criticism about missing figures/tables**: The paper uses `\input{}` commands for figures and tables. Per instructions, parser-rendering artifacts (unresolved `\input` paths from PDF extraction) are not author errors — the visual results exist in the original submission.
- **Criticism about DARE being "tautological" or "circular"**: The DARE derivation (Eq. 108–124) starts from first principles (random Bernoulli mask + Law of Large Numbers) and derives Δℒ≈0. This is a genuine prediction, not circular reasoning. Calling a random dropout operation "random" is not circular; the derivation shows *why* randomness produces Δℒ≈0.
- **Criticism about "necessary and sufficient" being unsupported**: The paper tests two specific interventions — (1) disrupting delta-parameter randomness → performance intact, (2) disrupting product randomness → performance degrades. This provides empirical evidence supporting the claim; demanding that "any deviation" be tested is an unreasonable standard for empirical work.
- **Criticism about EXPO being fundamentally mischaracterized**: The paper acknowledges EXPO's checkpoint-to-checkpoint delta (line 250) and uses a simplified formulation. The core extrapolation insight is preserved. The claim about a "different gradient landscape" is speculative — the paper does not show the simplification invalidates the analysis.
- **All typo and formatting nitpicks**: Per instructions, these are not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Acknowledge more explicitly in the paper that the framework provides a unified *expression* for all methods but is predictive primarily for the competitive-performance category. For decreased and improved categories, the theory provides a post-hoc mathematical characterization that is still unifying but does not predict outcomes without empirical input. This honest characterization would strengthen rather than weaken the paper.
2. Clarify in the TIES-Merging and EXPO sections that the analysis uses simplified formulations, with a brief note on what is lost and why the simplification is still informative.
3. Add a discussion of the first-order approximation error and when higher-order Hessian terms may become significant, to strengthen the theoretical foundation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>