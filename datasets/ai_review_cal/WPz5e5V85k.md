- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper presents a convergence analysis of the Wasserstein proximal algorithm (JKO scheme) under a Wasserstein Polyak–Łojasiewicz (PL) inequality, without assuming geodesic convexity. Theorem 3.4 provides an explicit linear convergence rate \(F(\rho_n)-F^* \le (1+\xi\mu)^{-2n}(F(\rho_0)-F^*)\). The paper also claims to analyze an inexact variant and presents an application to mean-field neural network training, but these portions are not present in the submitted manuscript.

## Strengths

- **Theorem 3.4 — Linear convergence under Wasserstein PL without geodesic convexity.** The paper's central result is clearly stated: an explicit unbiased linear contraction rate \((1+\xi\mu)^{-2n}\) under only a PL-type inequality (Definition 3.2) and Assumption 2. This is a genuine theoretical contribution, as prior proximal algorithm analyses required geodesic convexity or strong convexity. The rate is clean and directly interpretable.

- **Lemma 3.1 (derivative of the Hopf-Lax semigroup).** The paper proves the key relation \(\partial_\xi u(\rho,\xi) = -\frac{1}{2\xi^2}\mathcal{W}_2^2(\rho_\xi,\rho)\), linking the time-derivative of the Moreau-Yoshida approximation to the squared Wasserstein distance. This is foundational for the convergence analysis and is handled with appropriate technical care.

- **Self-contained framing of Assumption 2 and its compact-domain justification.** Remark 3.3 correctly notes that if \(\Theta\) is compact, Assumption 2 holds automatically because \(\nabla\frac{\delta F}{\delta\rho}(\rho_\xi) = (T_{\rho_\xi}^\rho - \mathrm{id})/\xi\) follows from the existence of the first variation of \(\mathcal{W}_2(\cdot,\rho)\). This provides a concrete sufficient condition for the main theorem.

## Weaknesses

### Fatal

- **Section 4 (experiments and MFLD application) is entirely absent from the manuscript.** The abstract, introduction (line 71: "In Section 4, we discuss how to apply the proximal algorithm for MFLD of a two-layer neural network and provide numerical experiments"), contributions (line 52: "Our numeric experiments show a faster training phase..."), and conclusion (line 205) all refer to numerical experiments and an application section that does not exist in the submitted text. The paper transitions directly from Section 3 (Theorem 3.4) to Section 5 (Conclusion) with no Section 4 present. The paper's practical claims — that the proximal algorithm is faster than noisy gradient descent for mean-field neural networks — are therefore unverifiable from the submission. This goes beyond a missing appendix: a main body section promised by the paper itself is absent, making the manuscript substantively incomplete.

### Major

- **The claimed improvement over existing rates under geodesic convexity is not substantiated.** The paper states (line 52): "When restricted to \(\mu\)-convex objective functional, our result yields a sharper linear convergence rate … than the existing literature (Yao & Yang, 2023; Cheng et al., 2024)." No explicit prior rates are provided, and no comparison of constants is given. The reader cannot determine whether the factor of 2 in the exponent \((1+\xi\mu)^{-2n}\) is a genuinely sharper rate or an artefact of different definitions (PL constant vs. strong convexity constant). This is a methodological gap in an otherwise theoretical paper.

- **The inexact proximal algorithm is listed as a contribution but developed nowhere in the main text.** The abstract, the contributions list (line 52: "We also analyze the inexact proximal algorithm for geodesically semiconvex objectives under PL-type inequality"), Section 3 (line 137: "we shall extend our analysis to the inexact proximal algorithm setting"), and the conclusion (line 205: "We also analyzed the inexact gradient variant under an extra geodesic semiconvexity condition") all claim or promise this analysis, yet no theorem, definition, or analysis of the inexact algorithm appears in the main body. The paper moves directly from Theorem 3.4 to Section 5. While this may be deferred to the appendix, the paper advertises it as a main contribution without any statement of the result in the main text.

### Minor

- **Assumption 2 is not explicitly verified for the neural network setting where \(\Theta = \mathbb{R}^d\).** The paper states in the Notations section that \(\Theta = \mathbb{R}^d\) by default. The compact-domain justification in Remark 3.3 therefore does not apply to the neural network case. The paper appeals to Corollaries 3.5 and 3.6 (which are absent from the main text) to cover the non-compact case via the minimal-strong-subdifferential argument. While the minimal-norm argument is logically sound, the main text alone does not establish why it applies specifically to the MFLD objective \(F_\tau(\rho) = R(\rho) + \tau\int\rho\log\rho\) with \(\Theta=\mathbb{R}^d\).

- **The connection from uniform LSI to the Wasserstein PL inequality (Definition 3.2) is asserted rather than explained.** The paper states (line 46) that the neural network architecture "satisfies the uniform LSI which in turn implies a Wasserstein PL inequality (cf. Definition 3.2)," but the mapping between these two inequalities is not developed in the main text. The reasoning relies on definitions and results in the appendix.

- **Table 1's rates are presented without sources or derivations.** The table (embedded as an image) compares convergence behaviors but does not cite specific prior results with their stated rates, making it difficult to verify the claimed contrasts.

### Trivial

- The "unbiased" terminology in the abstract merits clarification: the paper uses "unbiased" to mean discretization-error-free convergence, which is a non-standard usage relative to the optimization literature where "unbiased" typically describes gradient estimators.

## Nice-to-Haves

- Provide explicit prior rates (with constants) from Yao & Yang (2023) and Cheng et al. (2024) to substantiate the claimed "sharper" convergence.
- Include a brief explanation in the main text of why the minimal-subdifferential argument implies Assumption 2 for the MFLD objective with \(\Theta = \mathbb{R}^d\), without requiring the reader to reconstruct it from appendix references.

## Removed Points

These points were raised by reviewers but are removed from the main assessment for the reasons given:

- **Corollaries 3.5 and 3.6 are referenced but not present in the main text.** → These likely reside in the appendix, which the parser strips from all papers. The rule states: "REMOVE criticisms about missing appendix, missing proofs in appendix, or absent references. The parser strips those sections from all papers; they exist in the original submission."
- **Point about Langevin comparison not being directly about the proposed algorithm.** → The paper explicitly positions the comparison in Table 1 as illustrating the distinction between proximal and Langevin approaches for KL divergence, which is a valid contextualization.
- **Criticism that \(\Theta\) not being compact is a fatal gap for Assumption 2.** → The paper addresses non-compact cases via the minimal-subdifferential argument (citing Corollaries 3.5/3.6). Whether the reasoning is fully established depends on the appendix. The main-text treatment is thin but not fatal.
- **Strength about "extension to the inexact proximal algorithm."** → This strength is removed because no inexact analysis appears in the main text; it is a claimed contribution that does not deliver in the submission.
- **Strength about "empirical evidence for faster training."** → Removed because the experiments are in the missing Section 4 and cannot be evaluated.
- **Various formatting and stylistic nitpicks.** → Removed per the hard rule against formatting/parser artifact criticisms.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the incompleteness of the submission but do not generate insight beyond what the paper itself states.

## Suggestions

1. **Complete the manuscript** by including Section 4 with the promised experiments (setup, architectures, datasets, hyperparameters, error bars, and comparison with noisy gradient descent). Without this section, the practical claims are unverifiable.
2. **Provide an explicit comparison with prior rates** (Yao & Yang 2023, Cheng et al. 2024) — state their convergence rates explicitly in the main text so the claimed improvement can be evaluated.
3. **Include a statement of the inexact proximal analysis in the main text** — at minimum, state the theorem and its assumptions, even if the proof is deferred to the appendix. Currently this contribution exists only as a promise.
4. **Add a brief main-text justification** for why Assumption 2 holds for the MFLD objective over \(\Theta = \mathbb{R}^d\), rather than relying solely on the compact case and cross-references to the appendix.
