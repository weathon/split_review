I have a thorough understanding of the paper and both reviews. Let me write the consolidated review.

## Summary

This paper revisits FedExProx, a distributed proximal method with extrapolation, and identifies a surprising gap in its prior theoretical analysis: the known guarantees for quadratic objectives were no better than vanilla GD. The paper develops a refined analytical framework that avoids an $L_{\max}$-dependent lemma used in prior work, proving a tighter linear convergence rate for non-strongly convex quadratics. Using a computation+communication time model, the paper shows FedExProx can provably outperform GD when communication dominates. The analysis is extended to partial participation, adaptive extrapolation strategies (GraDS, StoPS), and functions satisfying the Polyak–Łojasiewicz condition. Small-scale experiments validate the predicted U-shaped time-complexity curves.

## Strengths

1. **Identifies a concrete limitation in the prior FedExProx theory**: Theorem 1 (and Remark 1) cleanly shows that under the original analysis by Li et al. (2024), FedExProx's time complexity on quadratics is no better than vanilla GD, even when local computation cost is independent of $\gamma$. This motivates the entire paper.

2. **Derives a genuinely tighter convergence rate for quadratics, enabling provable improvement over GD**: Theorem 2 establishes a linear rate $O(L_\gamma / \mu^+_\gamma \log 1/\varepsilon)$ for non-strongly convex quadratics. Theorem 3 then shows that with this rate, the optimal $\gamma$ yields total time complexity never worse than GD, and strictly better when $\mu/\tau \ge 2$. The diagonal example (lines 211–228) demonstrates an explicit setting where FedExProx achieves $\tilde O(\mu)$ vs. GD's $\tilde\Omega(\mu \times (\max\Sigma a_{ij})/(\min\Sigma a_{ij}))$.

3. **Extends the analysis to the PL condition under weaker assumptions than prior work**: Theorem 5 (labeled Theorem 6 in the paper) achieves linear convergence for FedExProx under the PL condition on $M^\gamma$, whereas Li et al. (2024) required strong convexity of $f$. The paper correctly notes this allows for multiple solutions.

4. **Provides adaptive extrapolation strategies (GraDS and StoPS) that match the optimal constant-extrapolation rate**: Theorem 5 shows that both adaptive strategies achieve $O(L_\gamma/\mu^+_\gamma \log 1/\varepsilon)$ convergence for quadratics, with StoPS working for any $\gamma > 0$ without prior knowledge of the optimal $\alpha$.

5. **Gives an instructive explanation for why the new analysis is tighter**: Section 7 (lines 354–360) clearly explains that prior work relied on Lemma 4 ($M^\gamma(x)-M^\gamma(x_*) \ge (f(x)-f(x_*))/(1+\gamma L_{\max})$) which introduced $L_{\max}$, while the new analysis avoids this by directly bounding $\|x-x_*\|$ and using $L$-smoothness of $f$.

6. **Includes partial participation analysis**: Theorems 3 (stochastic) and 4 (stochastic PL) extend the tighter rates to the realistic setting where only a random subset of clients participates each round, with the same optimal $\gamma$ interval as the deterministic case.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The PL "outperforming" claim relative to the prior strongly convex analysis lacks direct comparison.** The paper states (Contributions, item 5) that the PL analysis "demonstrates improved dependence on problem-specific constants." While the analysis is certainly more general (PL is weaker than strong convexity), the paper does not provide a concrete comparison of the rates. The lower bound $\mu^+_\gamma \ge \mu^+ / (4(1+\gamma L_{\max}))$ (line 322) is noted to be loose, but no example or bound is given showing that the actual rate $O(L_\gamma/\mu^+_\gamma)$ is strictly better than what would follow from strong convexity. A side-by-side comparison (even a single synthetic example where the new constant is clearly better) would substantiate the claim. This does not undermine the correctness of the PL extension or its generality, but the rhetorical claim of "outperforming" currently rests on an implicit comparison the reader cannot verify.

2. **No proof sketch of Theorem 3 (the central time-complexity result) is provided in the main text.** Theorem 3 is the paper's most striking result — it states the exact $\gamma$-interval where FedExProx's time complexity is no worse than GD. The main text gives only a diagonal-matrix example and the general interval statement, but no algebraic sketch of how $T_\mu(\gamma) \le T_{\text{GD}}$ is derived from the condition $\mu/\tau \ge 2$. While the full proof is in the appendix (stripped by the parser), a short derivation in the main text would significantly improve reader confidence in this central claim.

3. **The adaptive results claim "significantly improving upon the previous result" without showing the prior bounds.** The paper states that the GraDS and StoPS bounds refine Li et al. (2024)'s analysis for quadratics, but does not reproduce or even qualitatively describe the prior bounds. The GraDS bound (11) still involves $L_{\max}$ via $\frac{2+\gamma L_{\max}}{1+\gamma L_{\max}}$, making it unclear what exactly has been improved without the previous bound for comparison. A short side-by-side statement would resolve this.

4. **Inexact proximal computations are mentioned only in a remark (line 334–336).** The paper claims a result for inexact proximal operators (Theorem 6, reffered to in Contributions item 5) but only remarks on it in the main text with a reference to the appendix. A short statement of the inexact rate in the main text would strengthen the practical relevance.

5. **Minor notation inconsistency.** The time complexity $T_\mu(\gamma)$ is defined with $\widetilde O$ in (6) (line 199), but Theorem 3's inequality $T_\mu(\gamma) \le T_{\text{GD}}$ does not carry the tilde. This is a small consistency issue.

### Trivial
- The paper uses $\mu^+_\gamma$ for the smallest non-zero eigenvalue in the quadratic case and for the PL constant in the PL case. The paper itself acknowledges this analogy (line 352), so it is not confusing, but a brief note in the PL section clarifying the dual usage would help careful readers.

## Nice-to-Haves
- **Larger-scale experiments.** The current experiments (max dimension $d=7$, $n=14$ clients for quadratics; $d=3$, $n=4$ for hinge loss) are sufficient for qualitative validation of the theory. Adding a moderate-scale experiment (e.g., $d=100$, $n=50$) would rule out the concern that the U-shaped phenomenon is an artifact of tiny problem sizes. However, as a theory paper, this is not a requirement.
- **Discussion of the very-small-$S$ regime** (e.g., $S=1$) in partial participation, where $L_{\gamma,S}$ is dominated by $L_{\max}/(1+\gamma L_{\max})$. The theorems cover all $S$, but an explicit remark about when the advantage over GD may diminish would be helpful.

## Removed Points

These points were raised in the reviews but are removed or downgraded for the reasons stated:

- **"π(γ) derivation introduced later"** — Pure structure/organization nitpick, not a substantive weakness.
- **"No results for general convex functions beyond quadratics and PL"** — The paper acknowledges this limitation and explicitly scopes it to future work. Not a weakness.
- **"Missing comparison/discussion with FedExP"** — The paper cites FedExP and briefly discusses it in context (lines 57–58, 76). A detailed comparison would be a nice addition but is not a gap given the paper's focus on FedExProx's own theory.
- **"Experiments are too small; this is a methodological gap"** — This is a theory paper with illustrative experiments. The scale is appropriate for validating theoretical predictions. Demanding large-scale experiments evaluates the paper against the wrong class of expectations.
- **"Notation inconsistency between μ^+_γ in quadratic vs PL cases"** — The paper explicitly addresses this in line 352. The dual usage is natural and the paper notes the analogy.

## Novel Insights

The key insight — that prior FedExProx analysis was pessimistic because it relied on Lemma 4 linking $M^\gamma$ to $f$ via $(1+\gamma L_{\max})^{-1}$, and that bypassing this lemma by establishing convergence in distance then using $L$-smoothness yields tighter rates — is a genuinely useful observation for the community. It suggests that similar bottlenecks may exist in other proximal-method analyses and that distance-based arguments could unlock tighter guarantees. The finding that FedExProx's time complexity can be strictly better than GD under a realistic cost model (when communication dominates) overturns the prior understanding and gives a principled reason to use proximal oracles in communication-heavy FL settings.

## Suggestions

1. Add a short proof sketch for Theorem 3 in the main text (3–5 lines of algebra showing how the interval condition arises).
2. Either drop the "improved dependence on problem-specific constants" language for the PL case, or support it with a direct comparison of rates (even a qualitative one).
3. Reproduce the prior adaptive bounds (from Li et al. 2024) alongside the new ones for a clear side-by-side comparison.
4. Add a brief statement of the inexact proximal convergence rate in the main text (a single line with the rate).
5. Fix the $\widetilde O$ consistency between equation (6) and Theorem 3.
6. Consider adding one moderately larger experiment (d=100, n=50) to illustrate robustness, though this is optional for a theory paper.

## Score and Decision

**Originality**: 7/10 — The key insight (avoiding the $L_{\max}$-dependent lemma via distance-based analysis) is clever and leads to clearly improved results. The contributions are incremental but substantial relative to Li et al. (2024).

**Importance of research question**: 8/10 — Understanding whether FedExProx can actually outperform GD is an important question that prior analysis left unresolved. The paper addresses this decisively for quadratics and PL functions.

**Claims well-supported**: 7/10 — The quadratic results are well-supported. The PL and adaptive claims would benefit from more explicit comparisons. The experiments validate the theory.

**Soundness**: 8/10 — The theoretical framework appears sound. The main results are clearly stated and the analysis path (avoid Lemma 4, work in distance) is principled.

**Clarity**: 8/10 — The paper is well-structured and clearly written. The "why we get a tighter analysis" section is particularly effective.

**Value to community**: 7/10 — Useful theoretical contribution that clarifies the capabilities of FedExProx and provides a framework for tighter analysis of proximal methods.

**Overall score**: 7.5/10 — A solid theory paper with genuine contributions. The weaknesses are all minor and addressable. The core quadratic analysis is the main contribution and is well-supported.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>