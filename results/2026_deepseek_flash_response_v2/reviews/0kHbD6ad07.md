## Summary

This paper proves that decoder-only Transformer language models are almost surely injective: distinct prompts map to distinct last-token hidden states. The proof relies on real-analyticity of Transformer components to argue that collision sets have measure zero at initialization, and that gradient-based training preserves this property. The paper validates this via large-scale collision search (~5B pairwise comparisons across six model families finding zero collisions) and introduces SIPIT, an algorithm that leverages injectivity for exact input-text recovery from hidden states with linear-time guarantees.

## Strengths

1. **Proof that injectivity persists through training (Theorem 2.3).** The paper goes beyond prior work (Sutter et al. 2025) by arguing injectivity persists under gradient-based training, not just at initialization. The core approach—using real-analyticity of the update map and its non-singular Jacobian to argue that absolute continuity of the parameter distribution is preserved—is well-motivated and the main sketch for full-batch GD is sound in principle.

2. **Large-scale empirical collision search.** The paper conducts ~5 billion pairwise comparisons across six model families (Gemma-3 1B/4B/12B, GPT-2 Small/Medium/Large, Llama-3.1-8B, Mistral-7B-v0.1, Phi-4-mini-instruct, TinyStories-33M) and finds zero collisions. This includes models up to 70B parameters and quantized variants. This is genuinely supportive empirical evidence that the measure-zero collision set predicted by theory is never hit in practice.

3. **Quantization experiments showing robustness.** Tables 2-3 show that FP4 and INT8 quantization not only introduces no collisions but actually increases the minimum pairwise distance between representations across tested models. This supports the theory's predictions about boundary conditions and demonstrates practical robustness.

4. **Honest failure-case analysis.** The paper explicitly identifies when injectivity can break (tied embeddings, equal positional embeddings, non-analytic activations, quantization), clarifying the precise scope of the theory rather than overclaiming. This shows the authors understand where their assumptions are necessary.

5. **Clear theoretical framing and positioning.** The paper clearly distinguishes itself from prior inversion work (Thomas et al. 2025, Morris et al. 2023a;b, Nazir et al. 2025) and prior injectivity results (Sutter et al. 2025), making the contribution boundaries well-defined.

## Weaknesses

### Fatal

None.

### Major

1. **Proof sketch for mini-batch GD (Corollary 2.3.1) has a mathematical gap in the main text.** The proof sketch states that the batch Jacobian "coincides with the single-sample one by linearity of differentiation" at the witness point θ_* where the single-sample Jacobian determinant is nonzero. However, the batch update Jacobian is Dφ_B(θ) = I − η·(1/|B|)·∑D²L_i(θ), while a single-sample Jacobian is I − η·D²L_i(θ). These coincide at a given θ_* only if all per-example Hessians D²L_i(θ_*) are equal, which does not follow from "linearity of differentiation" (linearity gives that the Hessian of the average is the average of Hessians, not that each equals any individual Hessian). Moreover, even if the determinants are "sample-independent" (equal across samples), the determinant of the average Hessian is not generally equal to the determinant of any individual Hessian—the determinant is not linear. The sketch as presented in lines 113-115 does not adequately justify the extension from single-sample to mini-batch updates. Since the training-preservation claim is what distinguishes this work from Sutter et al. (2025), this gap is significant. **However**, this criticism targets the quality of the main-text sketch, not the proof itself (the full proof in Appendix C may resolve this), so it is Major rather than Fatal.

### Minor

2. **Inversion evaluation is narrow.** The main inversion experiment (Table 5) uses only 100 prompts of 20 tokens on a single model (GPT-2 Small). The quantized model experiments (Table 4) use 50 prompts of 10 tokens on two models. While the collision search is large-scale, the inversion experiments—which demonstrate the practical operationalization of the theory—are quite limited. Testing on longer prompts or larger models would strengthen confidence.

3. **HARDPROMPTS baseline comparison is not informative.** HARDPROMPTS is designed for prompt optimization rather than exact reconstruction from hidden states. Its 0.0 accuracy is expected and does not provide a meaningful comparison. The paper acknowledges this difference (line 311) but still features the comparison prominently.

4. **Algorithm naming inconsistency.** The paper uses SIFT (abstract, line 9; line 17), SIPIT (Section 3 header, line 45; line 137), SIpIT (Algorithm 1, line 167), and SiPT (Tables 4-5, lines 309-321) inconsistently. This appears to be a last-minute naming change that was not fully propagated and is confusing.

### Trivial

5. **No discussion of floating-point arithmetic limitations.** The theory is developed in ℝ but practical implementations use finite precision. The paper addresses quantization empirically but does not discuss whether standard FP32 rounding could affect the guarantee.

## Nice-to-Haves

- Expand the inversion experiments to longer prompts (100-200 tokens) and larger models (e.g., Llama-3.1-8B) to match the scale of the collision search.
- Include the gradient-guided policy details (Algorithms 2 and 3) in the main text rather than only in the appendix, since the efficiency claims depend on it.
- Discuss the floating-point arithmetic issue more explicitly.

## Removed Points

These points were raised by reviewers but are removed after cross-checking against the paper:

- **Criticism about the separating parameter construction in Theorem 2.2 being "hand-wavy"**: The full proof is in Appendix C; the main-text sketch is intentionally concise. There is no evidence the full proof is insufficient, and the construction described (setting one attention head to attend to the mismatch position) is a standard constructive argument.
- **Criticism about the threat model being too limited (requires hidden states)**: The paper explicitly acknowledges this limitation (line 141: "designing an efficient algorithm for that setting is nontrivial and left to future work"). This is appropriate scope management.
- **Criticism about missing error bars for collision distances**: The collision-search reports minima across large prompt sets; error bars are not standard for this kind of deterministic verification check.
- **Strength about "comparative positioning against closest prior inversion work"**: This is generic and standard practice rather than a distinctive strength.
- **Criticism about the algorithm being "straightforward given the theorem"**: While the algorithm is a direct operationalization, the paper's contribution is the combination of theorem + algorithm + experiments; the algorithm's simplicity follows from the strength of the theoretical result.

## Novel Insights

The harsh critic's observation about the batch Jacobian argument in Corollary 2.3.1 is the only genuinely novel insight that goes beyond the paper's own analysis. Specifically, the claim that the batch Jacobian determinant is nonzero because it "coincides" with the single-sample one at the witness point conflates linearity of the Hessian operator (averaging Hessians) with equality of determinants (which is nonlinear). Even if all individual Hessians share the same determinant at that point, the determinant of their average is not equal to that common determinant. This is a real mathematical subtlety that the paper's sketch glosses over. Beyond this, no other reviewer observation adds genuinely new insight beyond the paper's own contributions.

## Suggestions

- Provide a corrected sketch for Corollary 2.3.1 that either (a) gives a separate witness-point construction for the batch Jacobian, or (b) justifies why the single-sample witness point suffices despite the nonlinearity of the determinant.
- Expand the inversion experiments to at least 200+ prompts of varying lengths and include at least one larger model (e.g., Llama-3.1-8B).
- Resolve the SIFT/SIPIT/SIpIT/SiPT naming inconsistency throughout the paper.
- Consider adding a brief discussion of floating-point arithmetic and its relation to the theoretical guarantees.

**Calibration Anchors Consulted:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| NSBP7HzA5Z (Inductive Transformers) | 3.00 | R1 | Much weaker; vague proposal, no rigorous theory |
| 5dDYhvt6dY (Efficient Transformer) | 3.00 | R1 | Much weaker; narrow translation task, no theory |
| mlPTNEIsgb (Blind Inverse Audio) | 3.25 | R1 | Much weaker; unrelated domain |
| t9dWHpGkPj (Language Model Inversion) | 5.50 | R1, R2 | Comparable; lacks theory but has broader empirical scope |
| YzxMu1asQi (Adversarial Attacks Activations) | 6.50 | R1 | Slightly stronger; clean scaling law finding with broader experiments |
| KSBx6FBZpE (Uncovering Latent Memories) | 6.25 | R1 | Slightly stronger; thorough empirical study |
| STUGfUz8ob (When can transformers reason) | 7.60 | R1 | Stronger; more rigorous proofs, clearer writing |
| Xo0Q1N7CGk (Conformal Isometry) | 8.00 | R1 | Clearly stronger; well-executed theoretical + empirical |
| Vz5HgVwcdu (Injectivity ReLU Networks) | 5.00 | R2 | Weaker; purely theoretical with limited experiments |
| 1lFZusYFHq (Induction Heads) | 6.20 | R2 | Comparable; similar theoretical rigor but weaker experiments |
| 6S4WQD1LZR (Universal In-context Learners) | 6.67 | R2 | Slightly stronger; more polished theoretical presentation |
| jwsPS8yRe4 (Trained Transformer Classifiers) | 6.00 | R2 | Comparable; both theory papers with simplifying assumptions |

**Round 1 bracket:** 4.5–7.0

**Round 2 narrowing:** Compared against anchors at 5.00 (weaker), 5.50 (comparable), 6.00 (comparable), 6.20 (comparable), the paper lands near the upper end of the bracket but the main-text sketch gap prevents it from reaching 6.5+. 

**Final calibrated score: 6.0** — The paper has genuine contributions (injectivity proof approach, large collision search, SIPIT algorithm) but the mini-batch GD proof sketch gap and narrow inversion experiments hold it back from being a clear accept. The gap is fixable and likely resolved in the appendix, making this a solid borderline accept.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>