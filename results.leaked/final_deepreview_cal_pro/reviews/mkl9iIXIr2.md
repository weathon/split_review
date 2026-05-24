Now I have a good set of anchors for calibration. Let me formulate the final review.

**Bracket determination (Round 1):** The weak band (<3.5) returned papers with scores 2-3 that are clearly below this paper. The middle band (3.5-7.5) returned papers scoring 4.25-6.50, closest in spirit to this paper. The high band (>7.5) returned papers at 8.0 that are clearly stronger/cleaner than this paper.

**Bracket:** This paper sits between 6.0 and 7.5.

**Round 2 narrowing:** I pulled anchors in the 6.0-7.5 range. 

Comparing against:
- **qlzxeNESWI (6.50)**: BwAK paper with theoretical bounds + experiments. Our paper has more comprehensive theoretical results (matching lower bounds, novel reduction) but no experiments. Our paper is comparable or slightly stronger theoretically. 
- **mSGcDhQPwm (7.00)**: Pure theory paper (first last-iterate convergence guarantees, matching lower bounds). Similar structure to ours. Our paper has comparable theoretical depth. I'd place ours slightly above or at the same level.
- **wISvONp3Kq (7.33)**: Theory + strong experiments, somewhat different area. Our theory-only paper is slightly weaker due to lack of empirical validation.
- **i8dYPGdB1C (6.80)**: Theory + experiments with strong approximation guarantees. Our paper is comparable in theoretical contribution.

Given these comparisons, I'd place this paper at **7.0**. The theoretical contributions are strong (first dynamic regret for OIO, improved static regret with matching lower bound, elegant reduction), the paper is well-written, and the weaknesses are minor (presentation/exposition issues, no experiments). It's comparable to mSGcDhQPwm (7.00) in theoretical depth and novelty, but lacks even a simple empirical illustration.

---

## Summary
This paper proposes the first algorithm for online inventory optimization (OIO) with near-optimal dynamic regret guarantees under non-stationary (adversarial) demand. The key technical insight is a reduction from OIO to smoothed online convex optimization (SOCO) via a two-stage projection (Lemma 1), which shows that the carryover stock constraint induces a switching cost proportional to the cycle length. The authors combine this reduction with a doubling trick (to handle unknown maximum sell-out period $L_{\max}$) and the SOGD algorithm (to handle unknown path-length $P_T$) to achieve $\tilde{\mathcal{O}}(\sqrt{L_{\max}(1+P_T)T})$ dynamic regret. They also improve the static regret bound from $\mathcal{O}(L_{\max}\sqrt{T})$ to $\mathcal{O}(\sqrt{L_{\max}T})$ and provide a matching $\Omega(\sqrt{L_{\max}T})$ lower bound, establishing near-optimality.

## Strengths
- **First dynamic regret guarantee for OIO**: The paper is the first to provide dynamic regret bounds ($\tilde{\mathcal{O}}(\sqrt{L_{\max}(1+P_T)T})$, Theorem 4) for online inventory optimization, moving beyond the static regret guarantees of all prior work. This directly addresses the well-motivated problem of demand fluctuations (illustrated by the clean Newsvendor counterexample in the introduction).

- **Improved static regret with matching lower bound**: The static regret is improved from $\mathcal{O}(L_{\max}\sqrt{T})$ (state-of-the-art in Hihat et al., 2023) to $\mathcal{O}(\sqrt{L_{\max}T})$ (Theorem 3), and Theorem 5 provides an $\Omega(\sqrt{L_{\max}T})$ lower bound. Together these establish near-optimality and resolve an open question from prior work.

- **Elegant reduction from OIO to SOCO**: Lemma 1 is the core technical contribution, showing that under the two-stage projection the regret gap from the carryover constraint is bounded by a switching cost proportional to cycle length. This connection allows direct use of SOCO algorithms and is both novel and clean.

- **Parameter-free algorithm**: The doubling trick (Algorithm 2) adaptively handles unknown $L_{\max}$ without prior knowledge, and the SOGD base learner handles unknown $P_T$. The resulting algorithm requires no parameter tuning beyond what is standard.

- **Adversarial (non-i.i.d.) setting**: The regret analysis holds under fully adversarial demand, without i.i.d. or statistical assumptions, which is more general than most prior inventory management work (Table 1).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **No empirical validation**: The paper is purely theoretical. While the theoretical contributions are strong and self-contained, even a simple simulation comparing the proposed dynamic strategy against a static baseline (e.g., MaxCOSD) on a synthetic non-stationary demand sequence would substantially strengthen the paper's impact and make the practical benefit concrete. This is not a correctness issue but limits the paper's accessibility to practitioners.

- **Theorem 2 to dynamic regret gap**: The generic Theorem 2 decomposes the base-learner regret as $L^\alpha \mathcal{R}(T)$ without explicitly showing how the path-length $P_T$ interacts with the doubling-trick analysis across restarts. While the appendix presumably fills this gap and the subsequent theorems demonstrate it works, the main text would benefit from a clearer bridge between the generic doubling-trick statement and the dynamic-regret instantiations.

- **SOGD description is dense**: The description of the SOGD algorithm (Algorithms 4 and 5, Section 4.3) presumes familiarity with Zhang et al. (2022a). A few sentences of high-level intuition before the pseudocode would make the section more self-contained for readers not already familiar with that work.

### Trivial
- **Lemma 1 proof deferred**: The central technical insight (Lemma 1) is stated but not proved in the body. A brief proof sketch would help readers assess its validity without consulting the (stripped) appendix.

- **$L_{\max}$ edge case**: The definition of $L_{\max}$ (Definition 1) relies on the hypothetical $d_{T+1}^i = D$ to ensure non-emptiness, but when total horizon demand of some item is less than $D$, the condition may not be satisfied for any $L \leq T$. The paper should note this is a mild restriction (the problem is degenerate if inventory never needs to be fully utilized).

- **Doubling-trick constant factor**: The actual switching cost coefficient is $2G L_t^*$ (Eq. 8) while the base learner receives $G \cdot (2L)$ (since it is initialized with parameter $2L$ in line 8). The restart condition ensures $L \geq L_t^*$ for completed cycles, but for the current incomplete cycle the parameter may under-estimate until the next restart. This is a constant-factor issue that does not affect the asymptotic order but the exposition could explicitly address it.

## Nice-to-Haves
- Adding a proof sketch of Lemma 1 in the main text would make the central reduction self-contained and more convincing.
- Pulling the high-probability extension of $L_{\max}$ (Remark 3) into the main text would make the setting feel more applicable to stochastic demands.
- Noting the per-round computational cost of the projection onto $\mathcal{C}(x_{t+1})$ (a box-simplex intersection) would reassure practitioners.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh critic's claim about parameter scaling being potentially fatal**: The critic suggested the doubling trick might not ensure the base learner's parameter dominates $2G L_t^*$. This is a constant-factor concern, not a correctness issue. The asymptotic order is unaffected, as the critic themselves acknowledged. Retained as a trivial point about exposition.

- **Strength Finder's "adaptive algorithm without requiring $L_{\max}$ or $P_T$" as a standalone strength**: This is folded into the broader strength about the parameter-free algorithm and is not listed separately to avoid duplication.

## Novel Insights
The paper's reduction from OIO to SOCO via a two-stage projection (Lemma 1) reveals a structural connection between inventory carryover constraints and switching costs in online optimization that was not previously recognized. This connection is bidirectional: not only does it allow importing SOCO algorithms into OIO, but the lower bound (Corollary 1) shows that OIO lower bounds constrain SOCO lower bounds as well, providing an intriguing example of how one problem's hardness can inform another's.

## Suggestions
- Include a minimal simulation (even a single synthetic scenario with fluctuating demand) to demonstrate the practical advantage of dynamic regret over static baselines. This would not require new theory but would greatly increase impact.
- Add a proof sketch of Lemma 1 in the main body, explaining how cycles arise and why their length is bounded by $L_{\max}$.
- Add a paragraph of intuition before the SOGD pseudocode to make Section 4.3 more accessible.

## Score and Decision

### Anchor comparison summary:
- **qlzxeNESWI (6.50)**: Bandits with Anytime Knapsacks — theoretical bounds + experiments. Our paper has more comprehensive theory (matching lower bounds, novel reduction) but no experiments. Comparable or slightly stronger.
- **iZgECfyHXF (6.50)**: Online Nonconvex Optimization hardness — lower bounds + algorithms. Comparable theoretical depth.
- **i8dYPGdB1C (6.80)**: Multi-Agent Submodular Coordination — theory + experiments with approximation guarantees. Our paper's theory is comparably strong.
- **mSGcDhQPwm (7.00)**: Last Iterate Convergence — pure theory, first-of-its-kind guarantees with matching lower bounds. Very similar structure to our paper. Our paper matches this in theoretical contribution.
- **wISvONp3Kq (7.33)**: Sparse GLMs — theory + strong experiments. Slightly above our theory-only paper.

**Round 1 bracket**: 6.0–7.5. **Round 2 narrowing**: The paper is closest to mSGcDhQPwm (7.00) in structure and contribution level. It is stronger than the 6.50 anchors but slightly weaker than the 7.33 anchor due to the lack of empirical validation. I place it at **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>