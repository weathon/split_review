Now I have sufficient calibration data. Let me synthesize the final review.

**Round 1 Bracket:** The paper clearly falls below 3.5 (low bracket). The highest plausible score is around 3.0. The lowest plausible score is around 2.0.

**Round 2 Narrowing:** Comparing to the 2.00 anchor (AxYTFpdlvj), the paper under review is better structured and has more theoretical content. But compared to the 3.00 anchors (VyMW4YZfw7, oqdcThIQjA, ukmh3mWFf0), the paper under review has a *fatal* verification problem (regime mismatch) that those papers don't. The 3.00 papers' main issues were limited novelty or presentation, but their experiments were at least in the right regime. The paper under review has experiments that are fundamentally invalid for supporting its central claim. This pushes it below the 3.00 anchors.

**Final Score: 2.5**

Now let me write the review.

Let me carefully verify each of the harsh critic's claims against the paper text:

1. **Regime mismatch** (FATAL): Let me re-verify.
Line 17: "edges between vertices within the same block occur with probability a/n, while edges between vertices in different blocks occur with probability b/n, where a > b > 0"
Line 25-26: Theorem 1.2 from Coja-Oghlan: "if a, b > C_1" (a,b are constants)
Line 29-31: Theorem 1.3 from Chin et al.: "constants a > b > C_1"
Line 226: "n = 500, a = 0.06n, b = 0.04n"
Line 258: "edge probabilities a = 0.06n and b = 0.04n"

Wait, I need to be more careful about line 258. It says "edge probabilities a = 0.06n and b = 0.04n". But earlier it says edge probability is a/n. So if a = 0.06n, then the within-community edge probability is (0.06n)/n = 0.06. And a itself is 0.06n which scales with n.

But in the theory, a is a constant (like a = 15). So edge probability a/n = 15/n = O(1/n). Expected degree is O(1).

In the experiments, a = 0.06n, so edge probability = 0.06 = O(1). Expected degree = 0.06 × 2n = 0.12n = Θ(n).

This is a completely different regime. The sparse regime where the theoretical bounds apply has edge probabilities of order 1/n. The dense regime used in experiments has constant edge probabilities.

The information-theoretic lower bound (Zhang & Zhou, 2015) referenced by the paper is:
(2) (a-b)²/(a+b) ≤ c log(1/γ) means you CANNOT recover.

In the dense regime (a=0.06n, b=0.04n): (a-b)²/(a+b) = (0.02n)²/(0.1n) = 0.004n²/0.1n = 0.04n. So (a-b)²/(a+b) = Θ(n). Since (a-b)²/(a+b) grows with n, the condition becomes trivially satisfied for large n. The problem becomes fundamentally easier.

So the experiments are testing a completely different (much easier) regime than the theory. This is a fatal flaw. ✓ Verified.

2. **No proof of inverse-log rate**: Looking at the paper.
Line 270-276: "To these experimental results, we fit the empirical relationship: sin θ = C / ∛(log 2/γ) using OLS regression... The functional form in Equation 13, combined with the claims of Theorems 2.2 and 3.1, directly yields the final result stated in Theorem 1.3"

The paper admits this is an empirical fit (OLS regression). It does not derive the inverse-log relationship mathematically. It says this empirical fit "combined with" other theorems "directly yields" Theorem 1.3, but doesn't explain how. This is indeed not a proper proof. ✓ Verified.

3. **Deletion step not evaluated in sparse regime**: 
Line 62: Step 2 of Spectral Partition: "Zero out all the rows and columns of A corresponding to vertices whose degree is bigger than 20d, to obtain the matrix A'"
With a=0.06n, b=0.04n: d = a+b = 0.1n, 20d = 2n. Max possible degree is 2n-1 ≈ 2n. So the threshold is 2n, and since deg(v) ≤ 2n-1 < 2n, no vertices are deleted. The deletion step is indeed vacuous in the experiments. ✓ Verified.

4. **Constant C issue**: Let me look at this more carefully.
Line 192: "C = 1/2 (√(p_a p_b) + √(q_a q_b))^(2n) + 1/2 (√(q_a³p_b³/p_a q_b) + √(p_a³q_b³/q_a p_b) + q_a q_b + p_a p_b)^n"

For a=0.06n, b=0.04n: p_a=0.06, p_b=0.04, q_a=0.94, q_b=0.96.
√(p_a p_b) = √(0.0024) ≈ 0.049
√(q_a q_b) = √(0.9024) ≈ 0.950
Sum = 0.999
(0.999)^(2n) for n=500: (0.999)^1000 ≈ e^(-1.0) ≈ 0.368

So the first term of C is 0.5 × 0.368 = 0.184. The second term will be even smaller (since it involves terms like √(q_a³p_b³/p_a q_b) = √(0.94³×0.04³/(0.06×0.96)) = √(0.83×6.4e-5/0.058) = √(9.2e-4) ≈ 0.03, so the whole expression raised to the nth power is (something < 1)^500 ≈ tiny.

C ≈ 0.184. ln C ≈ -1.69. This is negative but not a big deal for the expression in Equation 11. The reviewer's claim that C is "vanishingly small" is somewhat overstated but the broader point about the derivation being opaque is valid. However, this is more of a minor technical point rather than a major issue. Let me keep it as a minor point if at all.

Now, let me think about what to keep in the strengths.

Strength Finder's strengths:
1. "Spectral partition alone achieves inverse-log error rates" — This is THE CLAIM, not evidence for it. The experiments are in the wrong regime. This is not actually a strength. REMOVE.
2. "Tighter error bounds than the quadratic relationship" — The Chernoff analysis does produce tighter bounds than the quadratic relationship from Theorem 3.2. However, this analysis is done in the dense regime and the paper doesn't clarify whether the same holds in the sparse regime. Still, it's a genuine technical contribution showing that the Chernoff analysis framework can yield tighter bounds. KEEP with caveat.
3. "Elimination of the degree-based deletion step preserves statistical independence" — Claimed but proof is in appendix. KEEP as a mild strength.

Let me also verify if the paper actually shows the Chernoff bounds are tighter. Looking at Figure 4a description (lines 226-228): "The results demonstrate that our Chernoff-based analysis yields significantly tighter bounds than the original theorem. For any given value of sin θ, our approach provides a substantially lower upper bound on the achievable error rate γ."

This is within the dense-regime experiments. But the tightness claim is about the bounds relative to each other, not about the regime. So the mathematical relationship could hold in either regime. The issue is that the experiments are in the wrong regime to validate the theory.

OK, I'm ready to write the final review.## Summary

This paper proposes a simplified spectral algorithm for two-community stochastic block model (SBM) community detection by removing the degree-based deletion step and the Correction stage from prior work. The authors claim that Spectral Partition alone achieves the inverse-logarithmic error rates previously thought to require the additional Correction step. The paper provides Chernoff-based and normal-approximation analyses, and presents experimental results using the simplified algorithm.

## Strengths

- **Chernoff-based analysis framework yields tighter bounds than the quadratic bound of Theorem 3.2.** The paper derives constraints from Chernoff concentration inequalities (Section 3.4) and shows numerically that these produce a tighter relationship between error rate γ and eigenvector alignment sin θ than the previous γ ∝ sin² θ bound. This represents a genuine technical exercise in tightening the analysis, even if limited to the specific parameter regime studied.

- **Clear framing of the research question.** The paper identifies a well-motivated question: whether the Correction step in Chin et al. (2015) is actually necessary, or whether Spectral Partition already achieves near-optimal rates. The "simplify to amplify" narrative is coherent and the modified algorithm (removing the degree-deletion step) is cleanly described.

## Weaknesses

### Fatal

- **The experimental regime does not match the theoretical regime, invalidating the empirical validation.** The paper's theoretical framing and all referenced results (Coja-Oghlan 2009, Chin et al. 2015) are for the *sparse* SBM where `a, b > 0` are *constants independent of n*, giving edge probabilities a/n and b/n of order O(1/n) and expected degree O(1). The key Theorems 1.2 and 1.3 explicitly require `a, b > C₁` as constants. However, all experiments use `a = 0.06n, b = 0.04n` (lines 226, 258), yielding *constant* edge probabilities of 0.06 and 0.04, expected degree Θ(n), and a fundamentally easier dense-regime problem where many methods achieve near-perfect recovery. The experiments therefore provide **zero evidence** that the simplified algorithm works in the sparse regime where the claimed contribution would matter. This is a structural flaw that undermines the paper's central empirical contribution.

### Major

- **No rigorous proof that the simplified algorithm achieves the inverse-log bound.** The paper claims (line 276) that the empirically fitted curve sin θ = C/∛(log 2/γ) (Equation 13) "combined with the claims of Theorems 2.2 and 3.1, directly yields the final result stated in Theorem 1.3." However:
  - Equation 13 is a purely empirical curve fit (OLS regression on experimental data, not a derivation).
  - The paper does not explain *how* this combination of an empirical fit and the generic bounds of Theorems 2.2 and 3.1 yields the specific information-theoretic condition (a-b)²/(a+b) ≥ C₂ log(2/γ).
  - No theorem is provided proving that the simplified algorithm achieves the inverse-log rate. The claimed central result is therefore unsupported.

- **The removal of the degree-based deletion step is not validated in the regime where it matters.** Step 2 of Spectral Partition zeros out rows/columns of vertices with degree > 20d. In the paper's experiments with a=0.06n, b=0.04n, we have d=0.1n and 20d=2n, meaning the threshold equals the maximum possible degree (2n-1). No vertices are ever removed — the deletion step is *vacuous*. There is no experimental or theoretical verification that the algorithm works without this step in the sparse regime where it would actually make a difference.

### Minor

- **The Chernoff-derived "prediction" (Equation 11) is fitted to optimization data via OLS rather than derived as a closed-form bound.** The paper admits (line 226) that Equation 11 is "fitted to the optimization data using ordinary least squares (OLS) regression." This weakens the claim that it is a theoretical prediction rather than a post-hoc fit. The normal approximation (Equation 12) is similarly fitted to Monte Carlo data.

- **The empirical relationship Equation 13 uses a cube-root-inverse-log form without theoretical justification.** The functional form sin θ = C/∛(log 2/γ) is presented as a finding but no derivation is given for why the exponent is 1/3, or how this connects to the information-theoretic bound in Theorem 1.3.

### Trivial

- The figure descriptions are repetitive (e.g., the caption text for Figure 4 appears twice in the paper body, lines 202-203 and 218-219).

## Nice-to-Haves

- The paper would be strengthened by running experiments in the sparse regime (e.g., a=15, b=5, with varying n) to actually validate the theoretical claims.
- An explicit theorem statement with a proof sketch (not deferred entirely to the appendix) showing that the simplified algorithm achieves the inverse-log error rate would substantially improve the contribution.
- Reporting confidence intervals or variance estimates for the experimental curves would help assess reliability, especially given only 10 repetitions for scaling experiments.

## Removed Points

- *"The constant C in Section 3.4 is problematic... ln C becomes negative"* — For the experimental parameters, ln C ≈ -1.69, which is a modest negative value and not inherently problematic for the expressions in Equation 11. This point is an overstatement.
- *"The abstract overstates what is demonstrated"* — While somewhat true, this is a generic observation that applies to many papers and is not a specific, actionable weakness.
- *"Section 2.1 motivation is not used later"* — The independence property is invoked in Section 3 analysis; this criticism is factually inaccurate.
- *"Suboptimal figure choices (opacity encoding)"* — A presentation nitpick that does not affect the paper's validity.
- *"10 repetitions is too small"* — While noted, this is a minor methodological concern rather than a structural weakness; it is subsumed by the fatal regime-mismatch issue.
- *"Missing appendix/proofs"* — The parser strips these; they exist in the original submission.
- *Various pure formatting/style nitpicks* — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions — the core observation (that Chernoff-based constraints can tighten the sinθ-γ relationship) is the main technical content, but the absence of a proof in the target regime and the fatal experimental mismatch prevent any validated insight.

## Suggestions

1. **Run all experiments in the sparse SBM regime** where a and b are constants (e.g., a=15, b=5, n ranging from 500–5000) to actually validate the algorithm in the setting where the claimed theoretical improvement applies.
2. **Provide a rigorous theorem and proof** showing that the simplified Spectral Partition achieves the inverse-log relationship (a-b)²/(a+b) ≥ C₂ log(2/γ), rather than relying on an empirical curve fit.
3. **Validate the removal of the degree-deletion step** by demonstrating that the spectral norm bound of Theorem 2.2 holds without deletion in the sparse regime, either via theorem or direct simulation.
4. **Clarify the connection** between the empirical fit (Equation 13), Theorems 2.2 and 3.1, and Theorem 1.3 — show the derivation explicitly rather than asserting it.

## Score and Decision

**Calibration procedure:**

*Round 1 — Bracketing:* Searched for SBM/community detection papers in three bands. Low-band anchors (scores 2.00–3.40) relevant to this paper included papers on graph decoding (avg 2.00), simplifying GNNs (avg 3.00), fast graph clustering (avg 3.00), and attributed graph clustering (avg 3.40). High-band anchors (scores 4.75–5.75) included papers on exact community recovery with side information (5.75) and finding number of clusters (4.75). The paper clearly falls in the low band (below 3.5).

*Round 2 — Narrowing:* Examined anchors in detail. The 2.00 anchor (AxYTFpdlvj) was poorly structured with missing details — the paper under review is better structured. The 3.00 anchors (VyMW4YZfw7, oqdcThIQjA, F8l0llkMk0, ukmh3mWFf0) had issues of limited novelty or presentation quality but did not have a fatal experimental flaw. The paper under review has a fatal regime mismatch that these 3.00 papers lack, making its experimental validation irrelevant to its theoretical claims. Among low-band anchors, only the 2.00 paper had a comparably fundamental problem (missing methodological details). The paper under review falls between these: better written and structured than the 2.00 paper, but with a fatal flaw that the 3.00 papers do not have.

*Final score:* 2.5 — The paper is coherently written and identifies an interesting question, but the regime mismatch between theory and experiments is a fatal structural flaw, and the central claim is asserted without proof. These issues preclude acceptance.

MY FINAL SCORE: <score>2.5</score>
MY FINAL DECISION: <decision>Reject</decision>