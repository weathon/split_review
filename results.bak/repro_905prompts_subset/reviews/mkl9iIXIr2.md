Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper addresses online inventory optimization (OIO) with carryover stock and capacity constraints in non-stationary environments. The authors propose algorithms based on a two-stage projection strategy that connects OIO to smoothed online convex optimization (SOCO). The key contributions are: (1) the first dynamic regret bound for OIO, achieving $\tilde{\mathcal{O}}(\sqrt{L_{\max}T(1+P_T)})$; (2) an improved static regret bound of $\mathcal{O}(\sqrt{L_{\max}T})$, improving over prior $\mathcal{O}(L_{\max}\sqrt{T})$ by a $\sqrt{L_{\max}}$ factor; and (3) the first lower bound for OIO ($\Omega(\sqrt{L_{\max}T})$), matching the static upper bound. The approach uses a cycle-based analysis to bound the projection gap and a doubling trick to handle unknown $L_{\max}$ and $P_T$.

## Strengths

- **Novel reduction from OIO to SOCO (Lemma 1).** The two-stage projection framework is elegant: the base learner makes decisions independently of carryover constraints, and the projection gap is bounded by switching costs weighted by cycle lengths. This reduction is the key technical innovation and cleanly sidesteps the dynamic carryover constraint that blocked prior two-layer approaches.

- **First dynamic regret bound for OIO.** Theorem 4 provides $\tilde{\mathcal{O}}(\sqrt{L_{\max}(1+P_T)T}) + L_{\max}\log L_{\max}$ dynamic regret without prior knowledge of $L_{\max}$ or $P_T$. This is the first algorithm for OIO that provably competes with a time-varying comparator, which is meaningful for non-stationary demand.

- **Improved static regret with matching lower bound.** The $\mathcal{O}(\sqrt{L_{\max}T})$ static regret improves over the prior $\mathcal{O}(L_{\max}\sqrt{T})$ by a $\sqrt{L_{\max}}$ factor. Theorem 5 provides a matching $\Omega(\sqrt{L_{\max}T})$ lower bound (the first for OIO), establishing near-optimality in the static setting and resolving an open question from Hihat et al. (2023).

- **Clean algorithmic design.** The combination of the two-stage projection, doubling trick for unknown $L_{\max}$, and existing SOCO algorithms as base learners is modular and well-explained. The doubling trick overhead is analyzed carefully (Theorem 2) and shown to be subdominant.

## Weaknesses

### Major

- **"Near-optimal dynamic regret" overclaimed.** The abstract, introduction, and conclusion claim near-optimal *dynamic* regret, but the only lower bound provided (Theorem 5) is for the *static* setting (fixed comparator $u$). The dynamic regret bound contains an extra $\sqrt{L_{\max}}$ factor relative to the standard OCO dynamic lower bound $\Omega(\sqrt{(1+P_T)T})$ from Zhang et al. (2018b), and no lower bound establishes that this factor is necessary in the dynamic case. Section 5 states "Our regret upper bound matches this lower bound up to a logarithmic factor" — this conflates the OCO lower bound (which has no $L_{\max}$ term) with the paper's bound (which does). The dynamic bound remains the first of its kind for OIO and is a valuable contribution, but calling it "near-optimal" goes beyond what is proven. This is fixable: the authors should qualify the claim, e.g., "first non-trivial dynamic regret bound" for the dynamic case, keeping "near-optimal" for the static case where matching bounds exist.

### Minor

- **Lemma 1 presented without proof intuition in the main text.** Lemma 1 is the paper's central technical lemma, but the main text states it without any sketch or intuition about why the cycle decomposition bounds the projection gap as $2G\sum_t L_t^*\|\hat{y}_t - \hat{y}_{t+1}\|_1$. While full proofs are in the appendix (standard practice), a brief intuition (1–2 sentences) about how cycles relate carryover stock to switching costs would substantially improve readability for a broader audience.

- **Section 5 optimality discussion is imprecise.** The sentence "Our regret upper bound matches this lower bound up to a logarithmic factor" (referring to the OCO lower bound $\Omega(\sqrt{(1+P_T)T})$) is misleading because the paper's bound is $\sqrt{L_{\max}}$ times larger. The sentence should clarify that the $\sqrt{(1+P_T)T}$ part matches the OCO lower bound, while the $\sqrt{L_{\max}}$ factor is justified by the separate static lower bound. A more precise formulation would avoid reader confusion.

- **$L_{\max}$ assumption is strong though necessary.** $L_{\max}$ requires that *every* item's cumulative demand reaches $D$ within $L_{\max}$ rounds from *any* starting time. The paper correctly notes that $L_{\max}=\Omega(T)$ forces linear regret, so the assumption is necessary for sublinear regret. However, in practice this is a worst-case condition on the adversary that may not hold even when the problem is otherwise manageable. The probabilistic extension (Remark 3) partially addresses this but is relegated to the appendix.

### Trivial

- Footnote 5 addresses the $x_1 \neq \mathbf{0}$ case with a $GDL_{\max}$ additive penalty; this should be noted in the main algorithm description rather than a footnote.
- The doubling trick restart condition ("if $\max\mathcal{L}_t > L$") would benefit from an explicit statement of how $\max\mathcal{L}_t$ tracks observed cycle lengths with $O(N)$ memory, rather than referencing Eq. (9) and leaving the reader to work out the implementation.

## Nice-to-Haves

- A proof sketch or intuition for Lemma 1 in the main text (1–2 sentences on why cycle length $L_t^i$ bounds the projection gap) would help readers who do not immediately see the connection.
- A dynamic lower bound that jointly involves $L_{\max}$ and $P_T$ (e.g., $\Omega(\sqrt{L_{\max}(1+P_T)T})$) would fully justify the "near-optimal dynamic regret" claim. This is the natural next step beyond the current paper.
- The linear capacity constraint (Eq. 3) is explicitly acknowledged as less general than Hihat et al.'s convex constraint. The paper could briefly note whether the cycle-based analysis extends to convex constraints or where the specific difficulty lies.

## Removed Points

The following points from the inputs were removed after verification:

1. *"Lemma 1 is presented without even a sketch of the proof"* — downgraded from Critical Issue to Minor. Deferring proofs to appendix is standard in theoretical ML papers. A brief intuition would help but its absence is not a major flaw.
2. *"The lower bound (Theorem 5) does not match the contribution being claimed"* — merged with the "near-optimal dynamic regret" overclaim in Major. The static lower bound is valid and well-matched; the issue is specifically about the dynamic claim.
3. *"OGD switching cost assumption"* — the paper transparently handles this; OGD trivially satisfies the condition with $\beta>1$. This is a non-issue.
4. *"No discussion of computational complexity"* — the paper does discuss it (lines 335–336 of the main text).
5. *"x_1 = 0 assumption"* — Footnote 5 explicitly addresses this, stating the algorithm works for $x_1 \neq \mathbf{0}$ with an $GDL_{\max}$ additive penalty.
6. *"Doubling trick underspecified"* — the description (lines 6–9 of Algorithm 2, Eq. 9) and Lemma 2 provide sufficient specification for a theoretical paper. The $O(N)$ memory tracking is noted.
7. *"The role of $L_{\max}$ in the dynamic regret bound is circular"* — this claim is unsupported. $L_{\max}$ is a well-defined problem parameter, and its role in the bound follows from the cycle analysis. There is nothing circular about it.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct the "near-optimal dynamic regret" claim.** In the abstract, introduction (Section 1.1), and conclusion, replace "near-optimal dynamic regret" with a more precise statement, e.g., "the first non-trivial dynamic regret bound for OIO" or "a dynamic regret bound that improves over naive OCO-based approaches by a $\sqrt{L_{\max}}$ factor in the static setting and extends to the dynamic setting via a SOCO connection." Reserve "near-optimal" for the static regret bound, where matching upper and lower bounds are proven.

2. **Clarify the optimality discussion in Section 5.** Replace the sentence "Our regret upper bound matches this lower bound up to a logarithmic factor" with something like: "For the $(1+P_T)$ dependence, our bound matches the OCO lower bound $\Omega(\sqrt{(1+P_T)T})$ from Zhang et al. (2018b) up to logarithmic factors. The additional $\sqrt{L_{\max}}$ factor is shown to be necessary via the static lower bound (Theorem 5). Whether the product $\sqrt{L_{\max}(1+P_T)T}$ is necessary for dynamic regret in OIO remains an open question."

3. **Add a brief intuition for Lemma 1 in the main text.** One or two sentences explaining that when $y_t^i > \hat{y}_t^i$, the item is in a cycle where the projection creates a "gap" that accumulates until demand draws the carryover stock below $\hat{y}_t^i$, and that this duration is bounded by $L_{\max}$, would greatly aid reader comprehension without adding significant length.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing.** Searched three bands for papers related to online convex optimization with inventory constraints and dynamic regret.

- *Weak anchors (score < 3.5):* J7hbPeOZ39 (avg 3.00, dynamic assortment/pricing — rejected), HLxWF7xqiK (avg 3.00, dynamic pricing — rejected). Both substantially weaker than this paper (limited theory, narrow scope).
- *Middle anchors (3.5–7.5):* Rdb0HxGJa3 (avg 4.50, OCO with predictions — rejected; weak motivation, incremental), iZgECfyHXF (avg 6.50, ONCO hardness — accepted; tight matching bounds, novel lower bounds), RR70yWYenC (avg 6.25, continual finite-sum — accepted), 5sixirvG0I (avg 5.33, Whittle index for inventory — accepted; good contribution but less theoretical depth).
- *Strong anchors (> 7.5):* All avg 8.00 — substantially stronger papers (tight lower bounds under smoothness, novel loss functions, complete characterization).

**Round 1 bracket:** 5.0 – 6.5.

**Round 2 — Narrowing.** Searched inside the bracket.

- *Lower-middle (4.5–6.0):* WIerHtNyKr (avg 5.25, convex-concave — rejected; incremental, unclear novelty), G0uhaIXmFw (avg 4.75, safe RL — rejected), G1DoOVM3xZ (avg 5.25, RL — rejected).
- *Upper-middle (6.0–7.5):* iZgECfyHXF (avg 6.50, ONCO — accepted), OvU9u6wS2J (avg 7.00, trading volume — accepted; complete characterization), RR70yWYenC (avg 6.25, finite-sum — accepted).
- *Additional:* pA8Q5WiEMg (avg 6.00, OWO meta-learning — accepted; solid improvement but some algorithms not implementable).

**Final comparison:** This paper is clearly stronger than the rejected middle anchors (4.50–5.25) which suffered from weak motivation or incremental novelty. It has a genuinely novel technical reduction (OIO→SOCO), the first dynamic regret bound for its setting, and a matching static lower bound. However, it is not as strong as the upper-middle papers (6.50–7.00) which had complete characterizations with tight matching bounds across all settings they studied. The overclaim about dynamic near-optimality is a real flaw. The paper most closely resembles the 6.00 OWO meta-learning paper (accepted) in terms of strength: a solid theoretical contribution with a meaningful improvement over prior work and a clear novel technique, but with a weakness that should be addressed (overclaim in this case, non-implementable algorithms in that case).

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>