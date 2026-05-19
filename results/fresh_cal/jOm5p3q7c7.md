Now I have thoroughly reviewed the paper and all reviewer claims against the actual paper content. Here is my consolidated review.

---

## Summary

This paper resolves the open question of optimal sample complexity for learning an optimal policy in uniformly ergodic average-reward MDPs (AMDPs) under a generative model. The main result achieves $\widetilde O(|S||A|\tmix \epsilon^{-2})$, matching the lower bound of $\Omega(|S||A|\tmix \epsilon^{-2})$ from Jin & Sidford 2021 and closing a $\tmix$ gap in prior upper bounds. The approach combines the reduction from AMDP to discounted MDP (DMDP), an improved analysis of the perturbed model-based planning algorithm (Li et al. 2020) that exploits uniform ergodicity via techniques from Wang et al. 2023, and a careful handling of the minimum sample size requirement, which is reduced from $\widetilde\Omega(|S||A|(1-\gamma)^{-3})$ (Wang et al. 2023) to $\widetilde\Omega(|S||A|(1-\gamma)^{-1})$.

## Strengths

- **First optimal sample complexity for uniformly ergodic AMDPs matching the lower bound.** Theorem 4.2 (formal version of Theorem 1.1) establishes $\widetilde O(|S||A|\tminor \epsilon^{-2})$, matching the $\Omega(|S||A|\tmix \epsilon^{-2})$ lower bound. Table 1 clearly shows all prior upper bounds were strictly larger (e.g., $\widetilde O(|S||A|\tmix^2\epsilon^{-2})$ and $\widetilde O(|S||A|\tmix\epsilon^{-3})$), confirming this is a genuine theoretical advance.

- **Improved DMDP analysis achieving optimal sample complexity with substantially lower minimum sample size.** Theorem 3.1 provides error bound $0 \leq v^{*} - v^{\hat\pi_0} \leq \frac{2\zeta}{1-\gamma} + 486\sqrt{\frac{\beta_\delta(\eta_\delta^*)\tminor}{(1-\gamma)^2 n}}$ and sample complexity $\widetilde O(|S||A|\tminor(1-\gamma)^{-2}\epsilon^{-2})$, matching the lower bound while requiring minimum sample size only $\widetilde\Omega(|S||A|(1-\gamma)^{-1})$ — a cubic improvement over Wang et al. (2023)'s $\widetilde\Omega(|S||A|(1-\gamma)^{-3})$, which is critical for the AMDP reduction.

- **Numerical experiments verify optimal dependence on both $\epsilon$ and $\tminor$.** Figure 1a shows log-log slope $\approx -1/2$ (proposed) vs. $-1/3$ (prior work), confirming the $\widetilde O(\epsilon^{-2})$ rate. Figure 1b shows near-zero slopes when varying $\tminor$ with sample size proportional to $\tminor$, confirming linear $\tminor$ dependence. Two different constants ($C=4500$ and $C=18000$) are tested in the $\tminor$ experiment.

- **Honest and thorough discussion of limitations.** Section 5 transparently addresses the need to know $\tmix$ a priori, the restriction to uniform ergodicity, and the desire to extend to $H$-dependent bounds and general state spaces — this strengthens the paper's credibility significantly.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **No proof sketch for Theorem 3.1 in the main text.** The paper presents the theorem and states it builds on "techniques from Wang et al. 2023" but provides no high-level outline of the key analytical steps (e.g., how the Doeblin condition controls the bias of the empirical Bellman operator, how the minimum sample size bound is derived). While full proofs are standardly relegated to the appendix for this venue, a brief sketch would help readers assess the argument without diving into the supplement.

- **Minimum sample size condition stated without motivation.** The condition $n \geq 64\beta_\delta(\eta_\delta^*)(1-\gamma)^{-1}$ is presented without explanation of its origin (e.g., whether it ensures concentration of the empirical kernel uniformly over all policies). A brief remark would improve readability.

- **Experiments use only one MDP family.** The hard instance from Wang et al. 2023 is well-motivated as a worst-case test, but testing on a small number of additional MDP families would increase confidence that the observed rates are not artifacts of a single construction. (That said, the experiments are sufficient for a theory paper; this is a minor gap.)

### Trivial
None.

## Nice-to-Haves
- A brief remark verifying that the lower-bound construction from Jin & Sidford 2021 satisfies the same parameter regime used in the upper bound, to formally close the loop on optimality. (The paper's parameters automatically satisfy the DMDP assumptions for all $\epsilon\in(0,1]$, but explicitly noting this would preempt reader confusion.)
- A note on the relative sizes of $H$ and $\tminor$ in worst-case uniformly ergodic examples, contextualizing why the $\tminor$ dependence in this paper's bound is preferable to the $H^2$ dependence in Zhang et al. 2023 (the paper notes $H \leq 8\tmix$ but does not leverage this comparison).
- A third experiment verifying the $|S||A|$ dependence, or a note that this scaling is standard and not separately tested.

## Removed Points

*These points were raised by reviewers but are removed after verification against the paper; they are preserved here for completeness.*

1. **"Proof assumptions may not fully align with the stated problem scope"** (from Harsh Critic, Critical Issue 1) — **REMOVED.** The critic claims the $\tminor \leq (1-\gamma)^{-1}$ and $\gamma \geq 1/2$ assumptions restrict $\epsilon$ relative to $\tminor$. Verifying against the paper: Algorithm 2 sets $\gamma = 1 - \epsilon/(19\tminor)$. Then $\gamma \geq 1/2 \iff \epsilon \leq 9.5\tminor$, which holds automatically since $\epsilon \in (0,1]$ and $\tminor \geq 1$. And $\tminor \leq (1-\gamma)^{-1} = 19\tminor/\epsilon \iff \epsilon \leq 19$, which also holds automatically. Both conditions are satisfied for the entire stated regime — the critic's concern is factually incorrect.

2. **"The lower bound is cited but not shown to be tight under the same assumptions"** (from Harsh Critic, Critical Issue 2) — **REMOVED.** The critic worries whether the lower-bound construction satisfies $\tminor \leq (1-\gamma)^{-1}$, but this condition is only relevant to the DMDP analysis (Section 3.1). The AMDP lower bound is directly for AMDPs under uniform ergodicity and involves no $\gamma$. The upper and lower bounds operate under the same uniform ergodicity assumption; no additional compatibility check is needed.

3. **"Table 1 comparison with Wang 2022a uses different parameters"** (from Harsh Critic, Section-by-Section) — **REMOVED.** The paper explicitly distinguishes the two parameter regimes in the table caption and the literature review (Section 1.1). Wang 2022a uses $H$ under the weaker "weakly communicating" assumption; this paper uses $\tmix$ under uniform ergodicity. The differences are clearly explained; the comparison is appropriate.

4. **"Experiments: stronger verification needed for $\tminor$ dependence"** (paraphrased from Harsh Critic) — **REMOVED.** The critic claims "Stronger verification would involve multiple values of $C$ and a demonstration that the error scales as $1/\sqrt{n}$ when $n$ is varied independently of $\tminor$." In fact, the paper already uses two constants ($C=4500$ and $C=18000$) in Figure 1b, and the first experiment (Figure 1a) already verifies the $1/\sqrt{n}$ scaling by varying $n$ independently.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's core claims and identify minor presentation improvements, but offer no new analytical perspectives not already present in the paper.

## Suggestions

- Add a 2–3 sentence proof sketch for Theorem 3.1 in Section 3.1, outlining how the Doeblin condition is used to control the bias of the empirical Bellman operator and how the minimum sample size bound arises.
- Add a brief remark (even one sentence) in Section 3.2 or in a remark to Theorem 4.2 confirming that the reduction parameters automatically satisfy the DMDP assumptions ($\gamma \geq 1/2$, $\tminor \leq (1-\gamma)^{-1}$, $\epsilon \leq \sqrt{\tminor/(1-\gamma)}$) for all $\epsilon \in (0,1]$ and $\tminor \geq 1$.
- Add a sentence motivating the $n \geq 64\beta_\delta(\eta_\delta^*)(1-\gamma)^{-1}$ condition intuitively (e.g., "ensures concentration of the empirical transition kernel uniformly over all stationary policies").

## Score and Decision

**Originality:** High — resolves an open problem with a novel combination of existing techniques.  
**Importance of research question:** High — optimal sample complexity for AMDPs is a recognized open problem in RL theory.  
**Claims well-supported:** Yes — the main theorems are stated precisely with all conditions, the proof chain is clear, and experiments validate the predicted rates.  
**Soundness of experiments:** Adequate for a theory paper — the key predictions ($\epsilon^{-2}$, linear-in-$\tminor$) are verified.  
**Clarity of writing:** Good — clear motivation, well-organized tables, transparent limitation discussion.  
**Value to the community:** High — provides the first matching upper bound for this setting and provides a DMDP analysis of independent interest.

MY FINAL SCORE: <score>8.5</score>
MY FINAL DECISION: <decision>Accept</decision>