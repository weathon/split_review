Now I have all the information I need. Let me compile the final review.

## Calibration Analysis

**Round 1 bracket**: After reading the paper and the harsh critic's analysis, I formed a preliminary bracket of 3.5–5.5. The paper has a clear theoretical error (Lemma 1 proof) but strong empirical evaluation.

**Round 2 narrowing**: I examined anchors in the 4.0–6.5 range. The closest comparable papers are:
- **F7XPZnIUHh (4.20, Reject)**: "Adversarial Learning of Decomposed Representations" — shares the same failure mode: a theoretical error in a core proof. That paper was scored 3,5,5,5,3, with Reviewer 1 specifically noting "Error in derivations."
- **Oc4ji1iCjQ (6.75, Reject)**: "Catch the Shadow" — methodologically similar (learns representations for causal inference), but that paper had sound theory. Its score is significantly higher.
- **qDhq1icpO8 (6.75, Accept)**: "CBRL.CIV" — representation learning for IVs, accepted with solid theory and experiments.
- **0gqCIaBRQ9 (5.25, Reject)**: "Regularized DeepIV" — solid theory but incremental, rejected.

The paper under review is closer to F7XPZnIUHh (4.20) in terms of the severity of the theoretical error, but has stronger and more comprehensive experiments. It is clearly below the ShadowCatcher (6.75) and CBRL.CIV (6.75) papers in theoretical soundness.

The low-band anchors (3.0–3.4) are papers with fundamental flaws and poor writing — the current paper is above those.

**Final score**: 4.0 — acknowledges the empirical contribution while reflecting the unsound theoretical lemma that is central to the paper's claimed contribution.

Let me now write the review.

---

Actually, let me carefully reconsider whether the Lemma 1 error is truly as bad as I think. Let me re-examine the proof once more.

The paper's proof:
```
0 = Cov(Z, e_Y - E[e_Y|X, T])
= E[Z·(e_Y - E[e_Y|X, T])] - E[Z]·E[(e_Y - E[e_Y|X, T])]
= E[Z·(e_Y - E[e_Y|X, T])]
= E[Z·e_Y] - E[Z]·E[e_Y|X, T]
= Cov(Z, e_Y)
```

The critical step: going from line 3 to line 4.

E[Z·(e_Y - E[e_Y|X,T])] = E[Z·e_Y - Z·E[e_Y|X,T]] = E[Z·e_Y] - E[Z·E[e_Y|X,T]]

The paper writes E[Z·e_Y] - E[Z]·E[e_Y|X,T]

So they incorrectly replaced E[Z·E[e_Y|X,T]] with E[Z]·E[e_Y|X,T].

Now, E[Z]·E[e_Y|X,T] is a random variable (since E[e_Y|X,T] is a random variable), while E[Z·E[e_Y|X,T]] is a number. So the equality is mixing apples and oranges.

Moreover, continuing from line 4 to line 5:
E[Z·e_Y] - E[Z]·E[e_Y|X,T] = Cov(Z, e_Y)

Cov(Z, e_Y) = E[Z·e_Y] - E[Z]·E[e_Y]. 
For this to equal E[Z·e_Y] - E[Z]·E[e_Y|X,T], we'd need E[e_Y] = E[e_Y|X,T] which means e_Y ⟂ (X,T), which is the condition we're trying to ensure!

So the proof has TWO errors:
1. Mistaking E[Z·E[e_Y|X,T]] for E[Z]·E[e_Y|X,T]
2. Concluding that E[Z·e_Y] - E[Z]·E[e_Y|X,T] = Cov(Z, e_Y) when Cov(Z, e_Y) = E[Z·e_Y] - E[Z]·E[e_Y]

The paper's proof is fundamentally incorrect and the lemma as stated is unproven.

However, let me think about whether the lemma itself (not the proof) might still be correct under additional assumptions.

If Z is independent of (X,T), then E[Z·E[e_Y|X,T]] = E[Z]·E[E[e_Y|X,T]] = E[Z]·E[e_Y]. And then Cov(Z, e_Y - E[e_Y|X,T]) = E[Z·e_Y] - E[Z]·E[e_Y] - (E[Z]·E[e_Y|X,T] - E[Z]·E[e_Y]... no this doesn't simplify nicely.

Actually, if Z ⟂ (X,T), then E[Z·E[e_Y|X,T]] = E[Z]·E[E[e_Y|X,T]] = E[Z]·E[e_Y].

And Cov(Z, e_Y - E[e_Y|X,T]) = E[Z·(e_Y - E[e_Y|X,T])] - E[Z]·E[e_Y - E[e_Y|X,T]]
= E[Z·e_Y] - E[Z]·E[e_Y|X,T] - E[Z]·E[e_Y] + E[Z]·E[e_Y]
Wait, E[E[e_Y|X,T]] = E[e_Y]. So E[Z]·E[e_Y - E[e_Y|X,T]] = E[Z]·(E[e_Y] - E[e_Y]) = 0.

So Cov(Z, e_Y - E[e_Y|X,T]) = E[Z·e_Y] - E[Z·E[e_Y|X,T]]

If Z ⟂ (X,T): E[Z·E[e_Y|X,T]] = E[Z]·E[E[e_Y|X,T]] = E[Z]·E[e_Y]

So Cov(Z, e_Y - E[e_Y|X,T]) = E[Z·e_Y] - E[Z]·E[e_Y] = Cov(Z, e_Y)

So when Z ⟂ (X,T), Cov(Z, e_Y - E[e_Y|X,T]) = Cov(Z, e_Y). Then the condition Cov(Z, e_Y - E[e_Y|X,T]) = 0 implies Cov(Z, e_Y) = 0.

But this requires Z ⟂ (X,T)! And Z = g(X), so Z is a function of X. For Z to be independent of X, g would need to be a constant function (or nearly so), which contradicts the relevance condition (Z must be predictive of T).

So the lemma as stated (without the Z ⟂ (X,T) assumption) is incorrect. And with the Z ⟂ (X,T) assumption, it contradicts the relevance condition.

This confirms that the theoretical grounding is indeed flawed. The paper's attempt to enforce unconfoundedness through the covariance constraint is not theoretically justified.

OK, I'm now even more confident that this is a genuine issue. Score 4.0 is appropriate.

Let me now write the complete review.## Summary

The paper proposes ZNet, a deep learning architecture that learns instrumental variable (IV) representations from observed covariates by encoding the three standard IV assumptions (relevance, exclusion restriction, unconfoundedness) into a multi-part loss function. ZNet trains neural networks $f,g$ to decompose $X$ into confounder $C=f(X)$ and instrument $Z=g(X)$ representations, which can then be fed into standard two-stage IV estimators (TSLS, DeepIV, DFIV) for causal effect estimation. The paper evaluates ZNet on semi-synthetic datasets derived from IHDP covariates across eight data-generating settings (with/without candidate instruments, linear/non-linear, with/without unobserved confounding) and compares against AutoIV, VIV, GIV, and TrueIV baselines.

## Strengths

1. **In-depth empirical evaluation across diverse IV scenarios.** The paper constructs eight distinct dataset types (Disjoint/Mixed/Latent/No Candidate × Linear/Non-linear) plus variants without unobserved confounding, covering a more comprehensive range of IV settings than most prior work. Table 1 reports ATE errors across three downstream estimators (TSLS, DeepIV, DFIV) with 50 bootstrap resamples and statistical significance markings. This is the most thorough evaluation of automated IV generation methods I have seen.

2. **Demonstrated recovery of ground-truth instruments.** In the Mixed Candidate datasets, ZNet's learned $Z$ shows strong multivariate $R^2$ in predicting the true instrument variables $X_{13},X_{14},X_{15}$ (Figure 5a,b). The ablation study (Figure 5c) confirms that each loss component contributes to this recovery. For the Latent Categorical instrument, ZNet recovers the true 5-cluster structure almost perfectly (Figure 4). These results convincingly show that ZNet can leverage its loss constraints to identify instrument information when it exists in the data.

3. **Construction of proxy instruments in No-Candidate settings.** The paper's most interesting finding is that ZNet can produce representations satisfying IV criteria even when no candidate instrument exists in the data. Figure 6 shows: (a) strong relevance F-statistic for $T$ prediction, (b) non-significant F-test for $Z$ in outcome regression (suggesting exclusion restriction holds), and (c) low average absolute correlation (≈ 0.1) between $Z$ and unobserved confounders $U$. In downstream ATE estimation, ZNet achieves competitive or best performance in several No-Candidate rows of Table 1 (e.g., Linear No Candidate with TSLS: error 0.025; Non-linear No Candidate with DeepIV: error 0.260**).

## Weaknesses

### Major

1. **Lemma 1, which provides the theoretical justification for the unconfoundedness constraint, has an incorrect proof and the resulting claim is unsupported.** The proof (Section 3) contains an algebraic error: it replaces $\mathbb{E}[Z \cdot \mathbb{E}[e_Y \mid X, T]]$ with $\mathbb{E}[Z] \cdot \mathbb{E}[e_Y \mid X, T]$, but $\mathbb{E}[e_Y \mid X,T]$ is a *random variable* (a function of $X,T$), not a constant. The equality $\mathbb{E}[Z \cdot \mathbb{E}[e_Y \mid X,T]] = \mathbb{E}[Z] \cdot \mathbb{E}[e_Y \mid X,T]$ does not hold in general and requires independence of $Z$ and $(X,T)$ — a condition violated because $Z = g(X)$ is a deterministic function of $X$. Furthermore, under the law of total expectation and the fact that $Z$ is a function of $X$, one can show $\mathbb{E}[Z \cdot e_Y] = \mathbb{E}[Z \cdot \mathbb{E}[e_Y \mid X,T]]$ regardless of dependence structure, implying $\operatorname{Cov}(Z, e_Y - \mathbb{E}[e_Y \mid X,T]) = 0$ holds automatically when $\mathbb{E}[Z]=0$ (which the KL loss enforces). This means the premise of Lemma 1 is *vacuous* under the method's own setup, and the conclusion $\operatorname{Cov}(Z, e_Y)=0$ does not follow from the stated conditions. The paper explicitly states that Lemma 1 "suggests how to construct a loss term which enforces unconfoundedness" — without a valid lemma, the unconfoundedness constraint $L_{Z \not\leftrightarrow \epsilon_Y}^{PC}$ lacks a theoretical basis.

   **Why this matters:** The paper's central methodological claim is that ZNet forces the learned $Z$ to satisfy *all three IV conditions*, including unconfoundedness. If the unconfoundedness constraint is not theoretically grounded as claimed, the paper's identification narrative is unsupported. The loss term (minimizing $\operatorname{Cov}(Z, Y - \hat{Y})$) may still serve as a useful heuristic regularizer — encouraging $Z$ to not carry information about $Y$ beyond $(X,T)$ — but it does *not* establish $\operatorname{Cov}(Z, e_Y)=0$ as the paper asserts. This is a structural flaw in the paper's contribution claims, not a minor presentational slip.

2. **The hyperparameter tuning protocol for baselines may systematically favor ZNet.** Section 5.3 states that all IV generation methods (ZNet, AutoIV, VIV, GIV) were tuned to maximize the instrument's relevance F-statistic and minimize the C‑Z correlation. These are *exactly* the criteria that ZNet's own loss function optimizes. While tuning on IV validity metrics is not unreasonable per se, this creates an asymmetry: ZNet's architecture and loss are explicitly designed to optimize these quantities, whereas the baselines (AutoIV, VIV, GIV) were designed with different objective functions (variational lower bounds, mutual information). Tuning the baselines on ZNet-centric criteria risks selecting hyperparameter configurations that are suboptimal for the baselines' intrinsic behavior, making it unclear whether ZNet's superiority in Table 1 reflects genuinely better representations or a tuning advantage. A fairer comparison would also tune each method on its own native validation metric (e.g., downstream ATE error) and report results under both protocols.

### Minor

3. **The exclusion restriction constraint is only weakly connected to the structural requirement.** The paper enforces exclusion restriction by minimizing $\operatorname{Cov}(C, Z)$ while maximizing $\operatorname{Cov}(C, Y)$. The exclusion restriction is a *structural* condition: $Z$ must have no direct effect on $Y$ other than through $T$. Zero correlation between $C$ and $Z$ does not guarantee this — $Z$ could influence $Y$ through non-linear interactions that are uncorrelated with $C$ but still affect $Y$. The paper partially addresses this with the empirical test in Figure 6b (F-test for $Z$ in $Y$ regression given $C,T$), but the loss function itself relies on a heuristic. This limitation is acknowledged implicitly ("encouraged" language in Section 3) and is shared with other IV generation methods, but the gap between statistical constraint and structural condition deserves clearer discussion.

4. **The statistical significance markings in Table 1 are not adequately explained.** The caption states that single star (*) means "the two best are significantly better than the third best" and double star (**) means "the best is significantly better than the second best." The paper does not specify what significance test was used, how it handles multiple comparisons across the 50 bootstrap resamples, or what the $\alpha$ level is. This makes the significance claims difficult to interpret or reproduce.

5. **Overclaiming in the abstract and discussion.** The abstract states ZNet "can be used as a plug-in module for causal effect estimation in general observational settings, regardless of whether the (untestable) assumption of unconfoundedness is satisfied." This overstates what the method achieves — ZNet still relies on untestable identifying assumptions (the three IV conditions), and the paper's own Section 7 acknowledges that "IV estimation in general is limited by a lack of theoretical guarantees of identifiability in the general case." The claim that ZNet works "regardless of whether the assumption of unconfoundedness is satisfied" is misleading: the method replaces one untestable assumption (unconfoundedness) with another set of untestable assumptions (the three IV conditions), not eliminates the need for assumptions entirely.

### Trivial

6. The loss notation in Section 5.1 at line 6 of page 5 references $L_{Z \not\rightarrow Y}^{PC}$ which is not previously defined (the defined term is $L_{Z \not\leftrightarrow \epsilon_Y}^{PC}$).

## Nice-to-Haves

- Ablation study on the three-stage training procedure and gradient surgery — does the stage-wise training matter, or could end-to-end training work as well?
- A consistency or convergence result for the learned representations (the paper currently has no theoretical guarantees beyond Lemma 1, which is flawed).
- Investigation of whether the dimensionality of $Z$ (fixed at 10) is appropriate across datasets or if it should be tuned.

## Removed Points

*The harsh critic's claim that "the evaluation and comparison fairness are compromised" because "tuning competing methods on a metric that is directly optimized by the proposed method" — This is a valid concern (retained as Major weakness #2 above), but the harsh critic overstated it as "cannot determine whether ZNet's representations are genuinely better." The downstream ATE comparison (Table 1) is still informative even with the tuning concern, and the paper compares multiple baselines. I have softened the framing to reflect that this is a significant concern rather than a fatal flaw that invalidates all comparisons.*

*The harsh critic's criticism of "TrueIV baseline is the best performer in only a handful" of settings as suggesting "either (a) the downstream estimators are poorly tuned for the TrueIV representations, or (b) the data generation produces a setting where standard IV methods are brittle" — This is speculative and doesn't account for the fact that TrueIV is by construction the baseline that correctly identifies, and its inconsistent performance may reflect the inherent difficulty of the data generation or the estimators' behavior. Removed because it makes a claim about what the results "suggest" without evidence.*

*The harsh critic's claim that "the method's architecture itself allows such paths; the loss function does not close them" (about exclusion restriction) — The paper uses the term "encouraged" not "enforced," and the empirical tests in Figure 6b directly verify whether the exclusion restriction holds. The critic's framing as if the paper claimed to provably enforce the condition is a misreading.*

*The harsh critic's point about "no consistency result" — This is a nice-to-have, not a weakness, as most deep learning papers in this area do not provide consistency results.*

*The harsh critic's point that "ZNet estimates causal effects itself" vs. being a "plug-in module" — The paper correctly states that ZNet provides inputs to downstream estimators; the abstract's "plug-in causal inference estimator" is slightly imprecise but not a real weakness.*

## Novel Insights

Beyond the paper's own contributions, the most notable insight from reading these reviews is the tension between the paper's strong empirical evaluation and the flawed theoretical lemma. The paper would be significantly strengthened by either (a) providing a correct identification argument for the unconfoundedness constraint (perhaps requiring stronger assumptions about the independence of $Z$ from nuisance functions), or (b) reframing the contribution as purely heuristic/empirical and dropping the theoretical claims. The fact that ZNet empirically satisfies all three IV criteria in No-Candidate settings (Figure 6) is genuinely interesting even without a correct lemma, suggesting the loss function may be a reasonable heuristic for reasons other than those claimed.

## Suggestions

1. **Fix or remove Lemma 1.** Either provide a correct proof (likely requiring assumptions beyond what the paper currently states, such as $Z \perp (X,T)$ — but this would conflict with the relevance condition) or drop the claim that the unconfoundedness constraint is theoretically justified and instead present it as a heuristic regularizer that empirically works.

2. **Revise the hyperparameter tuning.** Add an additional tuning protocol where each IV method is tuned on downstream ATE error (its own native objective) and compare results side-by-side with the current protocol. This would address the fairness concern and strengthen the paper's empirical claims.

3. **Clarify the connection between the loss constraint and the exclusion restriction.** The current $\operatorname{Cov}(C,Z)=0$ constraint is a linear proxy for a structural condition. A discussion of when this is sufficient (e.g., under linearity or monotonicity) and when it could fail would improve the paper's intellectual honesty.

4. **Tone down the contribution claims.** Replacing "enforces IV assumptions" with "encourages IV-like properties via heuristic constraints" would more accurately reflect what the method does and avoid the gap between theoretical claims and empirical evidence.

## Score and Decision

**Score:** 4.0

**Decision:** Reject

### Calibration anchor details

| Anchor ID | Avg Score | Round / Query | Comparison to this paper |
|---|---|---|---|
| F7XPZnIUHh | 4.20 | R1-topic-mid / R1-weakness | Shares the failure mode: theoretical error in a core proof. This paper has stronger and more comprehensive experiments, but a similar severity of theoretical flaw. |
| 4u0ruVk749 | 3.00 | R1-topic-low | Lower quality: poorly motivated use of diffusion models for unobserved confounders, fundamentally flawed approach. This paper is clearly better. |
| jFox1iMWUa | 3.40 | R1-topic-low | Poor writing, missing details, questionable method. This paper is better. |
| qDhq1icpO8 | 6.75 | R1-topic-mid | CBRL.CIV — representation learning for conditional IV, accepted with solid theory and experiments. This paper is substantially weaker on theoretical grounding. |
| Oc4ji1iCjQ | 6.75 | R1-topic-mid | ShadowCatcher — learns representations for causal inference under collider bias, strong theory, rejected on evaluation grounds. This paper has weaker theory. |
| 0gqCIaBRQ9 | 5.25 | R2 | Regularized DeepIV — solid theory but incremental, rejected. This paper has weaker theory but more comprehensive empirical scope. |
| 4u0ruVk749 | 3.00 | R2-low | See above. |

**Round 1 bracket:** 3.5–5.5. The paper has a clear theoretical error but strong empirical evaluation, placing it above the 3.0–3.4 papers but well below the 6.75 papers with sound theory.

**Round 2 narrowing:** The closest failure-mode anchor (F7XPZnIUHh, 4.20) had a similar theoretical error and was scored 3,5,5,5,3. This paper has more comprehensive experiments but the same category of flaw. Score 4.0 reflects being slightly below F7XPZnIUHh in overall balance (the theoretical error is more central to ZNet's claimed contribution than the error in that paper) while still recognizing the empirical value.

**What the low-band anchors failed at:** The 3.0–4.2 papers had theoretical errors that undermined their core claims or poorly motivated approaches. This paper shares the theoretical-error failure mode with F7XPZnIUHh (4.20) — the score of 4.0 places it in the same band, reflecting that the empirical contribution is real but the central theoretical claim is unsupported.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>