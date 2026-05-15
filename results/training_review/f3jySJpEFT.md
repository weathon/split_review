Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

The paper studies stochastic sparse linear bandits and demonstrates that the compatibility condition *only on the optimal arm* (Assumption 3) is sufficient to achieve \(\mathcal{O}(\mathrm{poly}\log dT)\) regret under the margin condition, without needing additional diversity assumptions (anti-concentration, relaxed symmetry, balanced covariance) that prior Lasso bandit literature required. The authors propose FS-WLasso, a forced-sampling then weighted-loss algorithm, and prove its regret bound using a novel induction-based analysis. They also provide a systematic comparison of assumption strengths across the literature.

## Strengths

- **Strictly weaker sufficient condition for poly-logarithmic regret.** The paper shows that compatibility on the optimal arm alone suffices for \(\mathcal{O}(\mathrm{poly}\log dT)\) regret, whereas all prior single-parameter Lasso bandit work required additional diversity assumptions (anti-concentration, relaxed symmetry & balanced covariance). The assumption relationships are systematically compared in Table 1 and Figure 1, with the paper proving that prior conditions imply theirs but the converse does not hold (Section 2.3, Discussion of Assumptions). A concrete counterexample (fixed suboptimal arms) is provided.

- **Regret bound established under minimal assumptions.** Theorem 1 establishes regret scaling as \(\mathcal{O}(s_0^2 \log T (\log d + \log\log T))\) for \(\alpha=1\), and analogous poly-log rates for other \(\alpha\), relying only on boundedness, margin condition, and compatibility on the optimal arm. The bound also nearly matches the lower bound of Li et al. (2021) up to a \(\log T\) factor, as noted in the discussion of Theorem 1 (lines 349–351).

- **Novel induction-based proof technique.** The paper introduces a high-probability induction argument (Section 3.4) to handle the cyclic dependency between optimal-arm selection and estimation error — when estimation error is small, optimal arms are chosen more often, which further reduces estimation error. This technique is claimed to be of independent interest and addresses a structural difficulty not resolved by prior approaches that rely on automatic exploration from diversity conditions.

- **Unified view via Theorem 2.** The paper shows that when additional diversity assumptions *are* satisfied, the forced-sampling stage can be eliminated (\(M_0 = 0\)) while still achieving poly-log regret. This unifies the exploration-intensive and exploration-free approaches and highlights the role of forced sampling as compensating for the weaker baseline assumption.

## Weaknesses

### Fatal
None.

### Major

- **Experimental evaluation is far too thin to support the claimed "superior performance."** The experiments section (Section 4, lines 442–474) is minimal: it tests only two synthetic settings, provides no hyperparameter specifications for any baseline algorithm, gives almost no description of the data generation process (only one sentence about "correlated Gaussian" and "fixed suboptimal arms"), includes no sensitivity analysis for \(M_0\) (despite claiming insensitivity in the remark), and reports no statistical tests. While the paper's primary contribution is theoretical, the abstract and introduction explicitly claim "superior performance" and "consistent superiority," which the current experiments do not convincingly demonstrate. The experiments need substantial expansion — at minimum, hyperparameter details, a sensitivity study for \(M_0\), and ideally real-data or benchmark experiments — before this claim can be accepted.

### Minor

- **The constant \(\tau\) in Theorem 1 is not given an explicit form.** The theorem states that \(\tau\) "depends on \(x_{\max}, s_0, \phi_*, \sigma, \alpha, \Delta_*, \log d, \log \delta\)" (line 317) but does not specify how. Since \(\tau\) appears in the algorithm's weight parameter \(w = \sqrt{\tau/M_0}\) and in the regret decomposition \(I_\tau\) and \(I_T\), the theorem statement as presented in the main text is incomplete. This is common practice when full details are deferred to the appendix, and it does not affect the asymptotic poly-logarithmic claim (since \(\tau\) is a constant w.r.t. \(T\)). However, a reader of the main paper alone cannot verify the exact bound. The paper would benefit from at least a sketch of how \(\tau\) is constructed.

- **The forced-sampling length \(M_0\) depends on unknown problem parameters.** Theorem 1 prescribes \(M_0\) in terms of \(s_0, \rho, \phi_*, \sigma, \Delta_*\), etc. — quantities unknown to a practitioner. The paper acknowledges this (Remark, lines 362–369) and notes \(M_0\) is tuned as a whole hyperparameter, which is standard practice in the bandit literature. However, there is a gap between the theoretical guarantee (which requires a specific \(M_0\) value) and the practical tuning procedure (which may set it differently). A data-dependent or adaptive choice of \(M_0\) would strengthen the contribution.

- **The proof sketch (Section 3.4) is quite high-level.** While it identifies three key difficulties (initial condition, propagation, and probability bounding), the description of the "domino-like phenomenon" and the induction argument lacks enough technical specificity for a reader to assess the argument's novelty or correctness without consulting the deferred appendix. Given that the induction technique is claimed as a contribution of independent interest, a somewhat more detailed sketch in the main body would be helpful.

### Trivial

- The paper mentions "A formal version of the theorem and proof are deferred" at line 315 but the sentence cuts off, suggesting a missing reference to the appendix section.

## Nice-to-Haves

- A concrete, worked-out example of a context distribution that satisfies the paper's assumption but violates every prior diversity assumption (beyond the fixed-suboptimal-arms case mentioned), with explicit verification.
- A sensitivity analysis for \(M_0\) in experiments to support the claim that performance is "not sensitive" to this choice.
- A discussion comparing the paper's upper bound to the known lower bound from Li et al. (2021) across different \(\alpha\) regimes.

## Removed Points

These points from the reviewers were removed as they do not constitute valid weaknesses of the paper:

1. **"Theorem 2 partially undermines the paper's novelty"** (Harsh Critic). Showing that forced sampling is unnecessary under stronger conditions does *not* undermine the paper's main contribution — it provides a unified framework bridging exploration-intensive and exploration-free approaches. This is a strength, not a weakness.

2. **"Comparison to fixed-suboptimal-arms is favorable by construction"** (Harsh Critic). Testing on a setting where prior assumptions fail is precisely the right evaluation for a paper claiming weaker assumptions. This is not "favorable by construction" — it tests the claimed advantage.

3. **"Verifying Assumption 3 is difficult in practice"** (Harsh Critic). This applies equally to prior work's assumptions (which are even stronger). The paper is a theoretical contribution, and the practical verifiability of assumptions is a shared issue across the literature, not specific to this work.

4. **"Abstract claim depends on appendix proofs"** (Harsh Critic). The claim that the assumption is "strictly weaker" is supported by the reasoning in the main text (Section 2.3, Discussion of Assumptions, and Figure 1); formal proofs deferred to appendix is standard practice.

5. **Strength Finder's "numerical validation" strength overclaimed.** The experiments are too limited to be a genuine strength; this was downgraded to a weakness above.

## Novel Insights

The reviewers' criticisms and cross-checking against the paper reveal an interesting tension: the paper's theoretical contribution (weaker sufficient conditions for poly-log regret) is structurally sound and well-motivated, yet the connection between theory and practice remains somewhat loose. The constant \(\tau\) and the parameter-dependent \(M_0\) create a gap between the theorem's guarantees and what a practitioner can actually set. This gap is common in bandit theory but is worth noting as a direction for future work. The induction-based proof technique, if it holds up in the full appendix, represents a genuinely new way to handle the selection–estimation cycle in bandits, and its applicability beyond this specific setting is worth watching.

## Suggestions

1. **Expand the experimental section substantially.** At minimum: report all hyperparameter settings for every baseline, describe the data generation process completely, add a sensitivity study for \(M_0\), and include statistical comparisons (e.g., confidence intervals beyond the standard deviation bars). Ideally, add at least one real-data or semi-synthetic benchmark experiment.

2. **Provide at least a sketch of how \(\tau\) is constructed** in the main text or state a concrete value/range. Even an informal description like "\(\tau\) is of order \(\mathrm{poly}(x_{\max}, s_0, \phi_*^{-1}, \sigma, \Delta_*^{-1}, \log d, \log(1/\delta))\)" would help readers assess the bound.

3. **Add a brief remark on how a practitioner could set \(M_0\)** in a way that approximately preserves the theoretical guarantee (e.g., using a doubling trick, or tuning on a small grid and citing the theory as motivation for why modest values work).

4. **Provide a more detailed proof sketch** in Section 3.4, perhaps including the key inequality that shows how estimation error implies bounded suboptimal selections and vice versa, and how the induction overcomes the accumulation of failure probabilities.

## Score and Decision

The paper makes a meaningful theoretical contribution by identifying compatibility on the optimal arm as the essential sufficient condition for poly-log regret in sparse linear bandits — strictly weaker than prior assumptions. The main weaknesses are (1) thin experiments that don't adequately support the claimed "superior performance," and (2) the unspecified constant \(\tau\) in the main-text theorem statement. Neither issue is fatal to the paper's core theoretical contribution, but both need attention. The paper would benefit from substantial experimental improvements and a more complete statement of the main theorem.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>