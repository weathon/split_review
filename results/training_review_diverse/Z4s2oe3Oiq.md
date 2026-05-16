Now I have thoroughly verified the claims against the paper. Let me produce the final review.

## Summary

This paper introduces normalized variants of EF21 and EF21-SGDM for distributed optimization under (L₀,L₁)-generalized smoothness. The authors prove that normalized EF21 achieves O(1/√K) convergence in gradient norm for deterministic nonconvex problems (matching EF21 under standard smoothness) and O(1/K^{1/4}) for the stochastic momentum variant, all without requiring data heterogeneity assumptions or knowledge of smoothness constants for the stepsize rule. Experiments on polynomial minimization, logistic regression, and ResNet-20/CIFAR-10 show normalized EF21 outperforming EF21 in convergence speed and accuracy.

## Strengths

- **First convergence analysis of normalized error feedback under generalized smoothness.** The paper provides the first theoretical treatment of normalized EF21 and EF21-SGDM under (L₀,L₁)-smoothness, extending error feedback theory to a practically relevant regime where standard L-smoothness fails. Prior analyses of EF21, EF21-SGDM, and EControl exclusively relied on traditional smoothness (Section 2; Theorem 1; Theorem 2).

- **O(1/√K) rate without data heterogeneity or smoothness-dependent stepsizes.** Theorem 1 establishes an O(1/√K) bound for normalized EF21 that holds for any data heterogeneity degree, and the stepsize rule γ_k = γ₀/√(K+1) does not require knowledge of L₀ or L₁. This contrasts with prior distributed generalized-smoothness works (Crawshaw et al., 2024; Liu et al., 2022) that require data heterogeneity conditions, and with original EF21 (Richtarik et al., 2021) whose stepsize depends on the unknown L (Section 1.1; Theorem 1; Section 4).

- **Stochastic extension matches EF21-SGDM rate.** Theorem 2 proves normalized EF21-SGDM achieves O(1/K^{1/4}) under generalized smoothness — the same rate as EF21-SGDM under traditional smoothness (Fatkhullin et al., 2024) — and also recovers single-node NSGD-M rates (Hubler et al., 2024) as a special case (Theorem 2; Section 5).

- **Theoretical comparison showing only a constant-factor slowdown under L-smoothness.** The paper derives that normalized EF21 is only a factor 2√2 slower than original EF21 when L₁=0 (standard smoothness), confirming that normalization does not significantly degrade rates while adding robustness to generalized smoothness (Section 4).

## Weaknesses

### Fatal
None.

### Major

- **The ResNet-20 experiment does not follow the paper's own theoretical prescription for normalized EF21, weakening the link between theory and empirical claims.** The paper claims normalized EF21 outperforms EF21 "due to its larger allowable stepsizes" (abstract, conclusion), but the ResNet-20 experiment (Section 6.2) uses a *constant* stepsize γ=5 for *both* algorithms. Normalized EF21's theory (Theorem 1) prescribes a *decreasing* schedule γ_k = γ₀/√(K+1), which would give much smaller stepsizes for most iterations. Meanwhile, EF21's theoretical stepsize under smoothness is ≈ 1/(L + L̃√(β/θ)) — orders of magnitude smaller than 5. Neither algorithm operates under its theoretical regime, so the 10% accuracy gap cannot be cleanly attributed to normalized EF21's theoretical advantage. The experiment is still informative as a heuristic robustness comparison, but it does not validate the paper's theoretical claims about larger allowable stepsizes. This is the paper's most significant weakness.

- **The polynomial function experiments (Figure 1) — central to the paper's motivation — lack any experimental setup description.** The abstract and introduction highlight these results, but Section 6 contains no subsection describing them. No function definition, dimension, initialization, compressor choice, or EF21 stepsize selection is reported. This makes the evidence in Figure 1 unreproducible and anecdotal.

### Minor

- **The convergence bound of Theorem 1 contains exponential factors that are not discussed.** The bound includes exp(8c₁L₁ exp(L₁γ₀)γ₀²), and the constants c₀, c₁ are not defined in the main text (they arise from the proof in the appendix). Even for modest parameters (e.g., γ₀=1, L₁=1), this exponential can be enormous. The paper does not discuss the practical magnitude of this constant or illustrate whether the bound is non-vacuous for realistic K. While this is common in generalized-smoothness analyses and does not invalidate the asymptotic rate, it weakens the practical implications of the claimed O(1/√K) convergence.

- **Logistic regression comparison is asymmetric in stepsize tuning.** For normalized EF21, K (and hence the stepsize schedule γ_k = γ₀/√(K+1)) is selected via grid search "as the smallest number of iterations required to achieve the desired accuracy" (Section 6.1). For EF21, a fixed theoretical stepsize is used without analogous tuning. Since K directly determines the stepsize magnitude, this conflates hyperparameter tuning with algorithm quality, making the comparison less clean than claimed.

- **No error bars or multiple runs for the ResNet-20 experiment.** The stochastic ResNet-20 training (mini-batch 128, 5 clients) reports only single-run results. Given mini-batch noise, the 10% accuracy gap lacks statistical reliability without variance reporting.

- **The nonconvexity condition λ > λ_min(A^T A)/(2n) is stated but not verified for the real LIBSVM datasets (Breast Cancer, ala).** The paper asserts this ensures nonconvexity but provides no evidence that the condition actually holds for these datasets.

- **Mini-batch size requirement B_init = √(K+1) for the stochastic algorithm (Theorem 2) is non-standard.** It requires the first iteration to use a batch size determined by the total iteration count K, which may not be known in advance. The paper acknowledges this in the conclusion as future work, but the limitation is significant for practitioners.

### Trivial

- **Inconsistency in the top‑k sparsifier parameter:** The ResNet-20 text (line 223) states k = 0.01d, while the Figure 3 caption states k = 0.1d. These differ by a factor of 10 and need correction.

- **The abstract's claim of "first proof of convergence for normalized error feedback algorithms across a wide range of machine learning problems"** is somewhat vague. The contribution is better scoped to "first proof for normalized EF21 under generalized smoothness."

## Nice-to-Haves

- Include clipped SGD and normalized SGD as additional baselines in the experiments, since these are established methods for generalized smoothness and would strengthen the positioning relative to prior work.
- Show a direct comparison where EF21 diverges under generalized smoothness (with a small constant stepsize) to dramatize the necessity of normalization.
- Provide a numerical illustration of the Theorem 1 bound for a concrete problem (e.g., the polynomial from Figure 1), showing whether it gives a non-vacuous gradient norm guarantee for realistic K.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Criticism about c₀, c₁ not being defined in the main text.** The definitions appear in the proof appendix, which was stripped by the parser. The original submission contains these definitions.
- **Criticism about the algorithm description being missing ("10: end for" appears).** This is a parser artifact — the full algorithm pseudocode exists in the original submission.
- **Criticism that the Section 4 comparison with EF21 under L-smoothness is "tangential."** This comparison is informative: it quantifies the cost of normalization (only 2√2 slowdown) and shows that normalized EF21 gracefully reduces to the known case, which is standard practice in optimization theory papers.
- **Criticism that the stepsize-independence claim is "misleading" for the deterministic case.** The paper correctly states that the stepsize *rule* γ_k = γ₀/√(K+1) does not require L₀ or L₁ (Theorem 1 holds for any γ₀ > 0). The clean-bound special case γ₀ = 1/(8cL₁) is presented as an illustrative choice, not as a requirement. The paper also transparently acknowledges that the stochastic (EF21-SGDM) case does require L₁ (line 181). No dishonesty here.
- **Complaint that the experiments lack comparison with "EF14, EControl" and other error feedback methods.** The paper scopes its empirical comparison to EF21 vs. normalized EF21, which is naturally the most direct baseline. Demanding a broader survey of error feedback methods under generalized smoothness is scope creep.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations largely corroborate the paper's stated strengths (first analysis under generalized smoothness, rate matching, no data heterogeneity requirement) and surface real but fixable experimental issues.

## Suggestions

1. **Fix the ResNet-20 experiment.** Either (a) run normalized EF21 with its theoretically prescribed decreasing stepsize γ_k = γ₀/√(K+1) and compare against EF21 with a similarly tuned constant stepsize, or (b) acknowledge that the constant-stepsize setting is a heuristic robustness test rather than a validation of the theory. In either case, clarify what the experiment is designed to show.

2. **Add the polynomial function experiment setup to Section 6** (function form, dimension, initialization, compressor, EF21 stepsize selection) so that Figure 1 is reproducible.

3. **Add error bars / multiple seeds** to the stochastic ResNet-20 experiment.

4. **Discuss the exponential factor** in Theorem 1 — provide a concrete numerical illustration showing whether the bound is non-vacuous for realistic K, or acknowledge that the practical bound quality is limited.

5. **Verify the nonconvexity condition** λ > λ_min(A^T A)/(2n) for the real datasets, or note if it was assumed without verification.

6. **Resolve the k=0.01d vs. k=0.1d inconsistency** in the ResNet-20 description.

## Score and Decision

The paper makes a solid theoretical contribution by providing the first convergence analysis of normalized error feedback algorithms under generalized smoothness, with rates matching those of their unnormalized counterparts under standard smoothness and without restrictive data heterogeneity assumptions. The main weaknesses are in the experimental validation, where the link between theory and practice is not as clean as claimed. The theoretical results are novel and significant enough to warrant publication, but the experimental section needs substantial revision to properly support the empirical claims.

**Originality:** High (first analysis of normalized error feedback under generalized smoothness).  
**Importance of research question:** High (communication-efficient distributed optimization under realistic non-smoothness assumptions).  
**Claims support:** Moderate (theory well-supported; experiments only partially).  
**Soundness of experiments:** Weak (protocol issues, missing details, no error bars).  
**Clarity:** Moderate (theorem statements somewhat opaque without appendix constants).  
**Value to community:** Good (theory is useful; experiments need improvement).

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>