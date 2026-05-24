## Summary

This paper claims that decoder-only Transformer language models are almost-surely injective: different prompts produce distinct last-token hidden states. The authors prove this at initialization using real-analyticity arguments, argue it persists under gradient-based training, and introduce SIPIT, an algorithm that reconstructs the exact input text from hidden states with linear-time worst-case guarantees. Large-scale empirical tests (100k prompts, 5B comparisons) across six model families find zero collisions, and SIPIT achieves 100% exact recovery on 100 test prompts while exploring less than 0.22% of the vocabulary on average.

## Strengths

1. **Novel theoretical framing and proof of injectivity at initialization.** The paper establishes a rigorous connection between real-analyticity of Transformers and the almost-sure injectivity of the prompt-to-last-token-state map (Theorems 2.1, 2.2). The argument that the collision set has Lebesgue measure zero for any pair of distinct prompts is clear and correct, and relies only on standard architectural assumptions (analytic activations, LayerNorm with ε>0). This is a genuinely different result from Sutter et al. (2025) who prove injectivity only at initialization and with respect to the full hidden-state matrix rather than the task-relevant last-token state.

2. **Full-batch GD training preservation is well-motivated.** Theorem 2.3's argument — that a GD step with a.e. non-singular Jacobian pushes forward absolutely continuous measures to absolutely continuous measures, so the parameter distribution never concentrates on the measure-zero collision set — is mathematically standard (area formula for C¹ maps). The sketch in the main text is brief but the underlying reasoning is sound.

3. **Constructive inversion algorithm with provable correctness.** SIPIT (Algorithm 1) and Theorem 3.1 turn the theoretical injectivity property into an operational tool with a clear worst-case guarantee (T|V| steps). The algorithm exploits the causal structure of Transformers in a clean way.

4. **Large-scale, multi-model empirical validation.** The collision search over 100k prompts (~5B pairwise comparisons) across GPT-2, Gemma-3, Llama-3.1, Mistral, Phi-4, and TinyStories, finding zero collisions with minimum distances consistently above 10⁻⁶, is thorough and directly supports the central claim. The experiments with quantized models (FP4, INT8) on models up to 70B parameters further strengthen the evidence.

5. **Empirically efficient exact recovery.** SIPIT reconstructs all test prompts exactly while exploring a tiny fraction of the vocabulary (0.19–0.22%), and runs in orders of magnitude less time than the brute-force baseline. This demonstrates that the theoretical guarantee translates into practical utility.

## Weaknesses

### Major

1. **The justification for extending injectivity to SGD and mini-batch GD has a mathematical gap.** Corollary 2.3.1 argues that the batch update map φ_ℬ has a Jacobian determinant that is not identically zero because "at the point θ_* from the single-sample proof (where the Jacobian determinant is sample-independent and nonzero) the batch Jacobian coincides with the single-sample one by linearity of differentiation." This conflates determinant equality with matrix equality. Knowing that det(I−η·Hessian_i(θ_*)) is sample-independent and nonzero for each i does **not** imply that the average Hessian's Jacobian determinant is nonzero — the determinant of a matrix average is not determined by the determinants of the individual matrices. Establishing that the batch Jacobian determinant is not identically zero requires a different argument or a stronger construction, which the paper does not provide. Since SGD/Adam is how all large models are actually trained, this gap weakens the paper's central claim that injectivity holds "under standard training procedures." The full proof in the appendix (not available for inspection) may address this, but as presented in the main text the reasoning is incomplete.

### Minor

2. **The HARDPROMPTS baseline comparison in Table 5 is inappropriate.** HARDPROMPTS (Wen et al., 2023) is designed for approximate prompt optimization from logits, not exact recovery from hidden states. The paper even acknowledges that such methods are "complementary but not directly comparable" yet still reports 0.00 accuracy for HARDPROMPTS, creating a misleading contrast. The paper would be better served by omitting this baseline or including it with a clear disclaimer that it solves a different problem. The BRUTEFORCE ablation already provides a valid efficiency comparison.

3. **The inversion experiments use only 100 prompts.** While the results are clean (100% accuracy), this is a small sample. Confidence intervals or tests on more data would strengthen the claim that the gradient-guided policy reliably avoids collisions in practice. The paper's own theoretical results suggest the algorithm should work for any prompt, but the empirical demonstration is narrow.

4. **No discussion of floating-point/numerical precision collisions.** The theoretical argument shows that distinct prompts map to distinct real-valued representations, but in practice, floating-point arithmetic could cause two mathematically distinct values to collide at the same binary representation. A brief discussion of whether the observed minimum distances (~10⁻³ to 10¹) provide sufficient margin against FP32 rounding would strengthen the practical relevance.

5. **The proof sketch for injectivity at initialization (Theorem 2.2) is vague about the constructive step.** The sketch says "freeze the network so that the last state reduces to embedding plus position" and "set one attention head so that the last position attends almost entirely to i\*." How this is achieved in the presence of LayerNorm (which rescales per-example statistics and couples positions) is not addressed. This is a sketch, so some vagueness is expected, but the construction's feasibility with practical architectural components is less obvious than the sketch suggests.

### Trivial

6. The paper states step sizes must be in (0,1) without discussion. This restriction is reasonable for standard gradient descent analysis but the bound is stated as a fact without justification.

## Nice-to-Haves

- **Weaker theoretical claims would be more honest.** If the SGD proof gap cannot be cleanly closed (e.g., if the missing construction requires assumptions that do not hold for commonly used optimizers), the authors should soften the claim from "injectivity persists under practical training" to "injectivity at initialization, with strong empirical evidence that it persists after training." The empirical work is strong enough to support a weaker theoretical claim.
- **Include Algorithms 2 and 3 (gradient-guided policy) in the main text** rather than only referencing them. The current Algorithm 1 is a shell without the policy subroutines.
- **Test SIPIT on recovery from only the final-layer last-token state**, which the paper identifies as an open direction. This would address a natural expectation raised by the abstract's framing.

## Removed Points

- The harsh critic's claim that the "probability one" framing is ambiguous about covering training randomness — the paper clearly states "with probability one over the random initialization" (lines 51–55).
- The criticism that the legal implications section is speculative — this is a discussion/conclusions section, where forward-looking implications are appropriate.
- The criticism about missing appendix content (the full proofs) — the parser strips appendices; they exist in the original.
- The claim that the full-batch GD argument is "heuristic" and insufficient — the area formula for C¹ maps with a.e. non-singular Jacobian is a standard, rigorous result; the Inverse Function Theorem sketch in the main text is a common presentation choice.
- The claim that the abstract misleads about recovery from the final representation — Section 3 explicitly states this is left to future work.
- The claim that step size restriction (0,1) is arbitrary — this is standard in GD analysis and not meaningfully restrictive for practice.
- The claim that "linear-time guarantees" should be qualified — the paper already says "worst case bound" (line 31).

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the SGD proof conflates determinant sample-independence with matrix equality is the only novel diagnostic insight that is not already present in the paper's own limitations.

## Suggestions

1. **Fix the SGD/mini-batch GD proof.** Provide a correct argument for why the batch update map's Jacobian determinant is not identically zero. One plausible approach: construct a specific parameter setting (e.g., all weights zero) where the Hessian of each sample's loss vanishes, so Dφ_ℬ = I regardless of batch composition. If this is already in the appendix, state it clearly in the main text.
2. **Remove the HARDPROMPTS comparison** from Table 5, or add an explicit caveat that it solves a fundamentally different problem and is included only to illustrate the contrast in problem formulation.
3. **Increase the inversion experiment sample size** and report per-token success rates with confidence intervals.
4. **Add a brief discussion of numerical precision.** The minimum observed L2 distances (10⁻³ to 10¹) appear to provide ample margin against FP32 rounding (machine epsilon ~10⁻⁷), but making this explicit would preempt a natural reader concern.
5. **Clarify the constructive step in Theorem 2.2** by noting how LayerNorm can be controlled (e.g., by setting its gain to zero or making the residual dominate the normalization statistics).

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| TW5DEgtacg (Rank collapse) | 2.00 | 1 | Much weaker; purely negative theoretical result |
| 8cDoHzqDXP (Recall scaling) | 3.33 | 1 | Narrower focus, less empirical scope |
| UhercDq1QK (Non-linearity in attention) | 3.00 | 1 | Largely unrelated to injectivity/inversion |
| xm5MELPxTv (Support-preserving maps) | 3.33 | 1 | Different framing, less direct empirical support |
| CtwyBsbvOA (Multi-task learners) | 4.00 | 1 | Less ambitious claim, smaller scope |
| m4ESoE5wnZ (Induction heads) | 4.50 | 1 | Construction-based, no guarantees about practical models |
| wqwtDpPeEf (InverseScope) | 5.50 | 1 | Related inversion topic but no theoretical guarantees, incremental methodology |
| dqGWQdFdTC (Internal planning) | 5.00 | 1 | Information-theoretic analysis, no constructive algorithm |
| rl2dPJEk8b (Bi-Lipschitz AE) | 5.00 | 2 | Injectivity in autoencoders (different domain), less rigorous theory |
| utSqpxQHXq (Two failure modes) | 6.00 | 2 | Comparable theoretical+empirical depth; current paper has more surprising claim |
| n5bPL58uMC (Trapped by simplicity) | 6.00 | 2 | Narrower focus on noise robustness; less general |
| IAFwK6NyrP (Counting Power) | 6.40 | 2 | Cleaner theory but limited experiments; current paper has stronger empirical validation |
| CfFj68C9Cn (Learning to Recall) | 6.50 | 2 | Clean theory on toy setting; current paper has broader practical relevance |
| RJXwuAMUiI (Attention Head Count) | 7.00 | 2 | Strong theory+experiments; current paper's central claim is more novel but theory is less polished |
| TLSUIyBIfs (Length Generalization) | 7.00 | 2 | Strong quantitative theory; different topic |
| gdZ6J5hZzF (Sequences of Logits) | 7.33 | 2 | Strong empirical+theoretical; cleaner theory, different topic |

**Round 1 bracket:** The paper plausibly sits between the weak anchors (avg ~3) and strong anchors (avg ~8), i.e., in the (3.5, 7.5) range.

**Round 2 narrowing:** Anchors at 6.0–7.0 on similar topics (transformer theory + empirical validation) suggest the paper is comparable to the upper end of the middle band. The theoretical novelty is genuine and the empirical validation is large-scale, but the SGD proof gap and the questionable HARDPROMPTS baseline prevent it from rising to the 7.0 level (where papers like "Attention Head Count" sit with cleaner theory). It is clearly stronger than InverseScope (5.50), which addresses a related problem without theoretical guarantees.

**Final score:** 6.0 — a solid paper with a novel and interesting result, strong empirical support, and a constructive algorithm, held back from a higher score by the incomplete SGD proof justification and a minor evaluation blemish.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>