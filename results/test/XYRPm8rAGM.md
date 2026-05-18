Now I have all the verification I need. Let me compose the final review.

## Summary

This paper identifies a fundamental flaw in the existing Jensen-gap explanation for deep ensembles (the average loss has no practical meaning; what matters is outperforming every individual member) and proposes a new theory based on **distributional equivalence**: although ensemble members make point-wise different predictions, these predictions follow identical distributions over the data. Under this property combined with neural collapse, the paper proves that ensembles are guaranteed to outperform every individual member (Theorem 4.1), derives a closed-form expression for how performance scales with ensemble size (Theorem 5.1), and shows that asymptotic ensemble performance can be estimated using only two models (Theorem 4.4). The theoretical results are validated on 3000 trained models across multiple architectures and datasets.

## Strengths

1. **Identifies a genuine flaw in the Jensen-gap explanation.** The paper proves (Proposition 3.1, §3.3–3.4) that the Jensen gap compares the ensemble to the *average* loss, which carries no practical meaning — the relevant quantity is outperforming every *individual* member. This reframes the problem and motivates the search for a better explanation.

2. **Discovers and validates distributional equivalence.** Using KS tests and Wasserstein distances on 4950 model pairs from 100 models (Figs. 2–3, §4.1), the paper shows that the conditional prediction distributions \(P(\ell \mid F=f^{(i)})\) are nearly identical across ensemble members, despite point-wise disagreement. This is the cornerstone of the theoretical analysis.

3. **First rigorous proof that deep ensembles outperform every single member (not just the average).** Theorem 4.1 (§4.3) proves \(\mathbb{E}_X[\phi(\mathbb{E}_F[F(X)])] \le \min_f \mathbb{E}_X[\phi(f(X))]\) under the neural-collapse approximation, directly addressing the gap left by Jensen-based explanations.

4. **Closed-form expression for ensemble performance as a function of size \(M\).** Theorem 5.1 (§5) decomposes the Brier score and NLL into the asymptotic ensemble loss plus a \(1/M\) decay term, matching empirical results across 100 models (Fig. 7).

5. **Practical estimation scheme requiring only two models.** Theorem 4.4 and Fig. 4 (§4.3) show that the infinite-ensemble Brier score can be accurately estimated from the cross-model agreement of two independently trained models — a genuinely useful tool for practitioners.

6. **Unusually large-scale empirical study.** Training 3000 models (100 members × 10 architecture/dataset combinations) on CIFAR-10/100 and TinyImageNet (§3.1) provides strong statistical support for the theoretical claims.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Notation error in Theorem 4.2.** The theorem states \(\Delta_B = \rho - \rho^2 - \operatorname{Var}_{p_X}[\hat{f}(X)]\) (line 173), but for a binary model \(\hat{f}\) under neural collapse, \(\operatorname{Var}_{p_X}[\hat{f}(X)] = \rho - \rho^2\), which would give \(\Delta_B = 0\) always — contradicting the theorem's own claim that \(\Delta_B = 0\) iff point-wise equivalence holds. The surrounding discussion (line 179) correctly uses \(\operatorname{Var}_{p_X}[\bar{\hat{f}}(X)]\) (the variance of the *ensemble* predictions), and the intended quantity is clear from context. This is a missing bar in the notation (\(\hat{f}\) should be \(\bar{\hat{f}}\)), but it makes the formula as written mathematically inconsistent. The authors should correct this.

2. **Theoretical results are proven only for the binary-collapse case, without error bounds for soft predictions.** Theorems 4.1–4.4 and 5.1 are derived for \(\hat{\mathcal{F}}\) (binarized predictions under complete neural collapse). The paper asserts transferability to soft predictions via empirical demonstration (Figs. 4, 7), which is reasonable but not rigorous. No theoretical bound on the approximation error from binarization is provided, and the claim that neural collapse is "already existing" (line 235) is not quantified. This limits the theoretical generality.

3. **Distributional equivalence directly validated for only one configuration.** The main visual and statistical validation of distributional equivalence (Figs. 2–3) is shown for CNN with \(k=40\) on CIFAR-10. While the subsequent experiments (Figs. 4, 5, 7) indirectly support generalizability by showing good theory-experiment match across many architectures and datasets, direct re-validation of the property in those settings would strengthen the paper.

### Trivial
None.

## Nice-to-Haves

- A brief discussion of failure modes or boundary conditions under which distributional equivalence might break (e.g., insufficient training, non-convergence, or very small datasets).
- For the NLL Taylor expansion in Theorem 5.1, reporting the proportion of samples where the clipping term (upper bound of 5) is active would help assess approximation quality, especially on harder datasets.
- Explicitly noting that Theorem 4.1 combines Jensen's inequality with distributional equivalence (which the paper already demonstrates) to turn an average-over-models bound into a per-model bound would help readers situate the contribution relative to prior work.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Circularity" criticism** (Harsh Critic's Claim 1): The critic argues the paper is circular because distributional equivalence is unexplained. This misreads the paper's contribution: observing an empirical property and deriving its consequences is how science works. The paper transparently admits distributional equivalence is observational (line 244) and does not claim to explain its origin. There is no circularity.

- **Missing related works on bias-variance decomposition (Geman et al., 1992; Breiman, 1996)**: By instruction, I cannot evaluate missing related works as weaknesses.

- **Selective prior work framing**: The critic notes Theorem 4.1 uses Jensen's inequality + distributional equivalence, which the paper never denies. The difference (per-model bound vs. average bound) is real and acknowledged by the critic. This is a tone critique, not a substantive weakness.

## Novel Insights

The most interesting observation from the reviews is that the paper's core contribution is simultaneously its most impressive and most fragile feature: distributional equivalence is a beautifully simple empirical discovery that cleanly explains ensemble behavior, yet the paper offers no hypothesis for *why* it holds. This is not a flaw — many important scientific discoveries are descriptive — but it means the paper's "demystification" is partial (mechanism, not origin). The practical estimation scheme (Theorem 4.4) is arguably underappreciated by both the critic and the strength finder: the ability to predict infinite-ensemble performance from *two* models is a genuinely actionable tool that may prove more impactful than the theoretical framing around it. The bias-variance trade-off analysis (Fig. 5) connecting global diversity over data to non-monotonic ensemble performance is another under-highlighted insight.

## Suggestions

1. **Fix the notation in Theorem 4.2**: Change \(\operatorname{Var}_{p_X}[\hat{f}(X)]\) to \(\operatorname{Var}_{p_X}[\bar{\hat{f}}(X)]\) to match the surrounding discussion.
2. **Soften the framing**: Replace "demystify" / "true mechanism" with language that more accurately reflects the conditional nature of the contribution (e.g., "identify distributional equivalence as the enabling property and derive its consequences"), especially given the admitted observational status of the key property.
3. **Add error bounds or a tighter empirical bridge**: Even a simple bound showing that the binarization error is controlled under mild calibration assumptions would significantly strengthen the theory-to-practice link.

## Score and Decision

The paper identifies a genuinely interesting empirical property (distributional equivalence), correctly diagnoses the insufficiency of prior Jensen-based explanations, and provides a clean theoretical framework that explains multiple observed behaviors of deep ensembles while also yielding a practical estimation scheme. The weaknesses are minor — a notation fix in one theorem, a missing theoretical bound for the binary approximation, and limited direct validation of the key property across settings — none of which undermine the core contribution. The empirical study is unusually thorough (3000 models). This is a solid paper with real contributions.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>