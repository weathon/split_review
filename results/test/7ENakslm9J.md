Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper studies bandit learning in two-sided matching markets where participants may have indifferent (tied) preferences, relaxing the strict-preference assumption made by all prior theoretical work in this area. The authors propose AE-AGS, an algorithm that combines arm-guided adaptive exploration with the Gale-Shapley procedure, and prove a stable regret bound of O(NK log T / Δ²) — the first polynomial regret guarantee under indifference without requiring knowledge of the minimum preference gap. Experiments in small-to-medium markets show AE-AGS consistently outperforming the only two baselines that can be extended to handle indifference.

## Strengths

- **First polynomial regret bound for matching markets with indifference, without knowing Δ.** The paper proves that AE-AGS achieves O(NK log T / Δ²) stable regret. Prior results either require knowledge of Δ (Liu et al., 2020) or suffer exponential regret (Basu et al., 2021) when extended to indifference. This is a genuine theoretical advance over a well-defined limitation in the literature (Table 1, Section 1).

- **Novel arm-guided adaptive exploration that sidesteps the never-ending-exploration problem.** Under indifference, existing explore-then-GS strategies never finish exploration because arms with tied preferences cannot be distinguished, leading to O(T) regret (Section 1). AE-AGS eliminates this by having players explore only arms that propose to them and adaptively eliminate sub-optimal arms using UCB/LCB comparisons (Algorithm 3). This design cleanly separates the learning goal from the stability goal.

- **Well-motivated relaxation of a restrictive assumption.** The paper explicitly motivates the need for indifference by citing labor markets, school admissions, and crowdsourcing platforms where ties are unavoidable (Section 1). Example 3.1 further demonstrates that player-optimal stable matchings may not exist under indifference, establishing that the problem is genuinely more complex than the strict-preference setting.

- **Experimental evidence consistent with the theoretical bounds.** Across varying market sizes (N=K ∈ {3,6,9,12}) and preference gaps (Δ ∈ {0.1,0.15,0.2,0.25}), AE-AGS outperforms C-ETC and P-ETC (Figures 1–2). The observed dependency — regret increases as Δ decreases and as N/K increase — aligns with the O(NK log T / Δ²) bound. The paper includes both stable regret (for small markets) and market unstability (for larger markets), providing complementary evidence.

## Weaknesses

### Fatal

None.

### Major

- **The stable regret definition is nonstandard, making the claimed comparison with prior work imprecise.** The paper defines stable regret relative to the *minimum* reward across all stable matchings (the worst stable outcome for the player). Under strict preferences, prior work defines stable regret relative to the *player-optimal* stable matching (the best stable outcome). The paper acknowledges that player-optimal matchings may not exist under indifference (Section 3, Example 3.1), which justifies adopting a different baseline, but it does not acknowledge that this changes the nature of the comparison. The abstract and introduction repeatedly state that the result is "only O(N) worse than the state-of-the-art result in the strict preference setting" — but this comparison is apples-to-oranges because the two definitions of regret are not equivalent. A reader could achieve the paper's bound but still have arbitrarily large regret under the prior definition. The paper should either (a) clearly state that the baseline used is weaker and explain why this comparison is still meaningful, or (b) adopt a stronger baseline (e.g., the supremum over stable matchings, though this may be unattainable). As it stands, the headline comparison is potentially misleading.

- **Limited evaluation scale and baseline rigor.** Experiments are conducted only up to markets with 12 participants, which the paper justifies by noting that computing stable regret requires enumerating all stable matchings (exponential cost). However, the paper could report market unstability for larger markets (e.g., N=K=50 or 100) without needing to compute stable regret, which would significantly strengthen the evidence that the algorithm scales. Additionally, the two baselines (C-ETC, P-ETC) are compared without specifying how they were extended to handle indifference (e.g., how unknown Δ is set for C-ETC). This makes it difficult to assess whether the baselines are fairly configured.

### Minor

- **The mechanism for handling zero-gap (tied) arms in the regret bound lacks intuitive explanation in the main text.** The regret bound is stated in terms of Δ, the *minimum non-zero* preference gap. The paper describes the UCB/LCB comparison mechanism that avoids eliminating indistinguishable arms (Algorithm 3, Line 4), but does not give a clear conceptual explanation of why exploring equal-preference arms does not incur linear regret. While the full analysis would appear in the (stripped) Section 5, a brief intuition in the main text — e.g., noting that arms with equal means are interchangeable for stability and that the adaptive exploration automatically limits their sampling cost — would greatly improve reader confidence. As it stands, readers may reasonably wonder whether the bound actually holds when ties are present.

- **No discussion of lower bounds or optimality.** The paper mentions this as future work (Section 7), but even a weak lower bound or a conjecture about optimality would help contextualize the O(NK log T / Δ²) result. Without any lower bound, it is unclear whether the O(N) factor relative to the strict-preference setting is inherent to indifference or an artifact of the algorithm.

### Trivial

- The experimental section would benefit from a structured table summarizing the setup (how baselines are parameterized, how ties are broken in experiments, how the minimum stable reward is computed for regret calculation). The current description is spread across paragraphs and is somewhat sparse.

## Nice-to-Haves

- Reporting market unstability for larger markets (e.g., N=K=50 or 100) without computing stable regret would strengthen the scaling evidence.
- A brief intuitive explanation in the main text of why zero-gap arms do not cause linear regret would improve readability.
- A discussion of the lower bound for the indifference setting, even a weak one, would help contextualize the result.

## Removed Points

These points were raised by reviewers but are removed or downgraded for the following reasons:

- **"The decentralized version of AE-AGS is not described"** — Removed. The paper mentions the algorithm works for both centralized and decentralized settings (Section 4, line 66: "we first present the centralized version"), and the decentralized version may appear in the appendix, which was stripped by the parser. Per policy, parser-stripped content is not a valid weakness.

- **"The zero-gap arms handling is not explained, threatening the regret bound"** — Removed in its strong form. The paper describes the UCB/LCB comparison mechanism (Algorithm 3) that handles ties, and the full proof would be in the stripped Section 5. The concern is addressed at a conceptual level in the main text; the remaining clarity issue is moved to Minor.

- **"Baselines may be unfairly handicapped"** — Removed. This is speculation without evidence. The paper compares against the only two baselines it identifies as applicable to indifference.

- **"Liu et al. (2020) and Basu et al. (2021) applicability to indifference requires justification"** — Removed. The paper specifically states these are the baselines that can be extended to indifference (Table 1, Section 6). Without evidence otherwise, this is a claim about the literature that the reviewer questions but does not refute.

- **"Theoretical analysis (Section 5) is missing"** — Removed. This is a parser artifact; the original submission would contain Section 5.

- **"Clarify and defend the stable regret definition" in the "Strengthening" section** — Partially removed. The paper already justifies using the minimum stable reward (player-optimal/pessimal may not exist under indifference, Example 3.1). The remaining concern about comparability with prior work is kept in Major.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. In the introduction and Section 3, add a sentence noting that the stable regret definition used (minimum over stable matchings) differs from the player-optimal baseline used in prior strict-preference work, and explain why the "only O(N) worse" comparison is still meaningful (e.g., because any sublinear regret under this definition guarantees convergence to a stable matching, which is the fundamental goal).

2. Add a brief intuitive paragraph in Section 4 or at the end of Section 3 explaining why tied arms do not cause linear regret: arms with equal means are interchangeable for stability, the algorithm's UCB/LCB mechanism never eliminates them as sub-optimal, and the arm-guided exploration automatically limits their sampling cost because the algorithm does not chase an infinite exploration loop.

3. Include a table in the experimental section (Section 6) that concisely describes the experimental setup: how baselines were extended to indifference, how Δ was set for C-ETC, how ties were resolved, and how the minimum stable reward was computed.

4. Add a larger-scale experiment (e.g., N=K=50) reporting only market unstability (not stable regret), which does not require enumerating all stable matchings and would demonstrate scalability.

5. Add a brief lower-bound discussion or at minimum a conjecture about optimality, even if only for a restricted case, to help readers understand the gap to optimality.

## Score and Decision

The paper addresses a genuinely open gap in the bandit-matching literature — indifference — with a theoretically grounded algorithm and the first polynomial regret bound for this setting. The core technical contribution is solid and the experimental results are supportive. The main weaknesses are (a) a nonstandard regret definition that makes the headline comparison with prior work imprecise, and (b) somewhat thin experimental evaluation. Neither is fatal; both are addressable in revision. The paper makes a real contribution to a well-defined problem.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>