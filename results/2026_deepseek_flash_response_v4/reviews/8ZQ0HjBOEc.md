Now let me compile the final review with calibrated score.

**Round 1 bracket:** I initially determined the paper falls between 3.5 and 7.5, with stronger evidence pushing it toward the lower-middle portion (4.0–5.5).

**Round 2 narrowing anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/bWz8aOPwsJ.md` | 3.75 | R2 | Empirical paper with flawed theory (Theorem 4.1 had errors). P has more substantive theory and is clearly stronger. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/YN4uWzcbtt.md` | 4.25 | R2 | Clean proof of NTK positive definiteness; incremental but rigorous. P has a more interesting question but less rigorous central proof. Comparable. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/kOtFuzoA93.md` | 4.00 | R2 | Dense theory with notation issues, no experiments. Similar profile to P. P is slightly stronger due to cleaner non-central results. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/WH9NhxOeu9.md` | 5.00 | R1/R2 | Solid theory with overstatement issues, rejected. P has similar overstatement but less rigorous central proof. P is weaker. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/VEJzjAvaIy.md` | 5.75 | R1/R2 | Clear proof, accepted despite some reviewers finding it unsurprising. P has a more novel question but far less rigorous central proof. P is weaker. |

**Final score: 4.5.** This places P above papers with flawed theory (3.75) and comparable to clean-but-incremental theory papers (4.25), but below papers with solid, verifiable central results (5.00, 5.75). The interesting question and solid Theorem 2 prevent a lower score, but the unverifiable Theorem 3 proof and overstated claims prevent a higher one.

---

## Summary

This paper studies how the deterministic limiting NTK of infinitely wide fully-connected ReLU networks behaves as depth L → ∞ (with L ∈ o(width)). It proves two main results: (1) Theorem 2 shows the normalized kernel Θ̄_∞^{(L)} converges entrywise to the matrix of ones, becoming singular. (2) Theorem 3 argues via rough differential equations that despite this singularity, the NTK predictor κ_x κ^{-1} converges to a well-defined limit. The paper also distills three sufficient conditions for generalizing to other kernel sequences and provides limited empirical illustrations.

## Strengths

1. **Clean characterization of normalized NTK convergence (Theorem 2, Proposition 4).** The paper derives a closed-form recursive update for the normalized kernel (Proposition 4, lines 147-151) and proves monotonic entrywise convergence to 1 (Theorem 2, line 153). This follows cleanly from known ReLU NTK recursions and is a solid, well-motivated result.

2. **Identifies a genuinely interesting and non-trivial question.** The observation that the kernel becomes singular while the predictor may still converge is worth studying. The paper correctly identifies that prior work (Xiao et al. 2020) requires an invertibility assumption that fails in this regime (line 227), and frames a real technical gap in the literature.

3. **Distills sufficient conditions for potential generalization (Section 6).** The three extracted properties (positive definiteness for large L, diagonal dominance, vanishing determinant, lines 237-241) provide a useful template for researchers wanting to apply similar reasoning to other kernel families.

## Weaknesses

### Major

1. **Theorem 3's proof sketch is incomplete and the central claim cannot be verified from the main text.** This is the paper's key contribution, but the proof (lines 193-225) has critical gaps:
   - **Undefined notation** (\(\tilde{\Theta}\)): The symbol \(\tilde{\Theta}_\infty^{(L)}\) appears throughout Theorem 3 and its proof (lines 183-227) but is never defined. The Notation section defines \(\Theta\) (unnormalized) and \(\bar{\Theta}\) (normalized, Definition 4, line 137-139). Context suggests \(\tilde{\Theta}\) is meant to be \(\bar{\Theta}\), but this is never stated. The proof then says "Theorem 2 guarantees that \(\tilde{\Theta}_\infty^{(L)}(XX^\top)\) converges to 1" — but Theorem 2 is stated for \(\bar{\Theta}\).
   - **The interpolation construction does not obviously yield a limit as L→∞.** The proof constructs a pairwise interpolation between matrices at depths L and L+1 (line 195), but how this collection of pairwise constructions yields a limit as L→∞ is not explained.
   - **Inequality chain (lines 219-223) lacks justification.** The steps rewriting the denominator as powers of determinants and replacing those powers with 1 are asserted without derivation.
   - **Application of Lyons' Universal Limit Theorem is asserted, not verified.** The proof claims the driving signals converge in 1-variation and that the RDE setup satisfies the theorem's conditions, but provides no verification. Rough path theory requires establishing convergence in specific p-variation topologies and verifying that the vector fields satisfy the theorem's conditions — none of this is done.
   - The proof relies heavily on the missing appendix (Appendix D on RDE background), making it impossible to assess completeness from the main text alone.

   Since the paper's central claim cannot be properly evaluated from the main text, this is a serious weakness that prevents acceptance.

2. **The result is existence without characterization, which limits its contribution relative to the paper's framing.** Theorem 3 asserts that κ_x κ^{-1} converges to *some* bounded limit that yields e_i at training points, but does not characterize what this limit is for test points. The paper repeatedly contrasts itself with Xiao et al. (2020) (lines 31, 225-227, 262), who give a concrete characterization: the mean predictor collapses to a data-independent constant in the ordered phase. The paper's claim to "generalize" Xiao et al.'s result (line 262) is overstated — it handles a case Xiao et al. cannot, but with a substantially weaker type of result (existence without interpretable characterization). This gap between the paper's ambitious framing and what is actually proved is significant.

### Minor

3. **Experiments do not directly validate Theorem 3's central claim.** The experiments (Figure 1, Appendix F on MNIST) show convergence of kernel entries ρ^{(L)}, η^{(L)}, and the product \(\bar{\kappa}^{(l)}(x^\top X^\top)(\bar{\kappa}^{(l)}(XX^\top))^{-1}\) as L increases. However: (a) computed values are not compared to any known or predicted limit; (b) there is no verification that stabilization has actually been reached (only that values appear to level off); (c) no error bars or multiple-seed statistics are provided. The paper states that "this depth limit is sufficient to show convergence" (line 245) for the kernel entries, yet acknowledges convergence is logarithmic — values at L=30 could still be far from 1. The experiments do not test the specific claim of Theorem 3 (that the predictor converges to a well-defined limit), only that some related quantities appear to stabilize.

4. **Inconsistent notation between \(\tilde{\Theta}\) and \(\bar{\Theta}\).** The paper defines \(\bar{\Theta}\) (normalized) in Definition 4 and uses it in Theorem 2, then switches to \(\tilde{\Theta}\) in Theorem 3 (line 183) without definition or explanation. In the discussion (line 227) it states "Theorem 2 guarantees that \(\tilde{\Theta}_\infty^{(L)}(XX^\top)\) converges to 1" — but Theorem 2 concerns \(\bar{\Theta}\). This notational inconsistency makes the proof difficult to follow.

5. **The "generalization to other kernels" criteria (Section 6) are presented as a contribution but no theorem is proved.** Three sufficient conditions are listed (lines 237-241) and one example (η^{(L)}) is mentioned, but no theorem is stated or proved showing these conditions suffice. The η example is introduced without analysis. This reads as a suggestion for future work rather than an established result.

6. **Limited scope.** While acknowledged, the cumulative restrictions (data on the sphere, no biases, ReLU only, L ∈ o(width)) mean the results apply to a fairly narrow setting. The claimed extension to non-compact domains is gestured at (stereographic projection) but not worked out.

### Trivial

7. Slight inconsistency between Figure 1 caption (x-axis 0 to 20) and text claiming experiments go to L=30 (line 245).

## Nice-to-Haves
- Characterizing the limiting predictor beyond existence (e.g., determining whether it is a data-independent constant, as in Xiao et al.'s ordered phase) would substantially raise the value of Theorem 3.
- A simpler proof that avoids the heavy RDE machinery would make the argument more transparent and easier to verify.
- Connecting the theory to finite-width networks through even a small experiment would strengthen claims of practical relevance.

## Removed Points
Points from reviewers that were filtered out with brief justification:

- **"The RDE framework appears disproportionate to the result obtained"** (Harsh Critic) — Subjective methodological preference, not a verifiable weakness. Without the full proof in the appendix, one cannot assess whether the machinery is disproportionate or necessary. Removed.
- **Section-by-section "Missing Parts" (no rate of convergence for predictor, no connection to finite-width networks)** (Harsh Critic) — These are nice-to-haves or scope-extension requests, not core weaknesses. Some preserved as Nice-to-Haves.
- **"Proposition 3's reliance on invertibility of κ creates a tension"** (Harsh Critic) — The paper explicitly acknowledges this tension at line 155 ("The result above can be taken to be a major obstacle..."). Strawman; the paper addresses this directly. Removed.
- **"RDE-based proof that the NTK predictor converges despite kernel singularity (Theorem 3)"** (Strength Finder) — This conflicts with the verified weakness that the proof is incomplete. Cannot be assessed from the main text. Removed.
- **"Empirical demonstration that the predictor converges at modest depths"** (Strength Finder) — Overstated relative to what the experiments actually show. Preserved in weakened form as Minor weakness #3.
- **Generic strengths** (Strength Finder) — Removed as non-specific (e.g., "this paper addressed an important problem").

## Novel Insights
The harsh critic identifies a genuinely insightful tension at the heart of the paper: Theorem 3 provides existence of a limit without characterization, yet the paper frames this as an advantage over Xiao et al. (2020), who give a concrete characterization (data-independent constant in the ordered phase) under a different assumption regime. The paper's claim to "generalize" Xiao et al.'s result is imprecise — it handles a singular case Xiao et al. cannot, but with a qualitatively weaker type of result (existence only, no characterization). A more honest framing would acknowledge that the paper offers a *different kind* of contribution (handling the singular limit via RDE machinery) rather than claiming to improve upon or generalize Xiao et al.'s concrete characterization.

## Suggestions
1. Define \(\tilde{\Theta}\) explicitly in the main text and clarify its relationship to \(\bar{\Theta}\) and \(\Theta\).
2. Expand the proof sketch of Theorem 3 substantially, addressing the logical gaps identified above, even if the full proof remains in the appendix.
3. Either characterize the limiting predictor (even partially) or adjust the paper's claims to match what is actually proved — an existence result for a specific singular regime, not a generalization of Xiao et al.'s characterization.
4. Strengthen experiments by either (a) comparing the computed predictor to an identifiable quantity, or (b) at minimum providing error bars and demonstrating that the predictor values have converged within statistical uncertainty rather than merely appearing to stabilize.

## Score and Decision

**Round 1 bracket:** The paper's central proof issues place it below clearly accepted theory papers (5.75 anchor) but above papers with fundamentally flawed or trivial contributions (~3.75). Initial bracket: 4.0–5.5.

**Round 2 narrowing:** Compared against anchors at 4.25 (clean but incremental, rejected), 4.00 (dense theory with notation issues), and 5.00 (solid but overclaimed, rejected), the paper sits between 4.0 and 5.0. The interesting question and solid Theorem 2 prevent a score below 4.0, but the unverifiable Theorem 3 proof, overstated claims relative to Xiao et al., and thin experiments prevent a score above 5.0. The paper is weaker than the 5.00 anchor (which had a clear, though limited, central result) and comparable to the 4.25 anchor (which had clean proofs but was incremental).

**Final score: 4.5.** The paper identifies an interesting question and has a solid supporting result (Theorem 2), but the central contribution (Theorem 3) is not convincingly established from the main text. The proof sketch has gaps that cannot be resolved without the appendix, and the result itself (existence without characterization) is weaker than the paper's framing suggests. The contribution is not ready for publication in its current form.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>