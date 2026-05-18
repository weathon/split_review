Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper introduces the **update-equivalence framework** for decision-time planning (DTP) in imperfect-information games, an alternative to the dominant public-belief-state (PBS) paradigm. Instead of solving subgames, DTP algorithms are viewed as implementing the updates of last-iterate algorithms. From this framework, the authors derive **Mirror Descent Search (MDS)** for cooperative games—proving monotonic policy improvement (Theorem 1)—and **MMD Search (MMDS)** for adversarial games. In Hanabi, MDS matches or exceeds state-of-the-art PBS methods while using two orders of magnitude less search time, and in games with virtually no public information, MMDS reduces exploitability substantially.

## Strengths

- **Novel, well-motivated framework that addresses a genuine limitation of PBS-based DTP.** The paper clearly identifies why PBS-based planning scales poorly with non-public information ("distributes its computational budget across all decision points supported by the PBS," §1) and proposes update equivalence as a principled alternative that focuses computation on the agent's actual decision point. This conceptual contribution is clean and its motivation is compelling.

- **Provable policy improvement guarantee for MDS in common-payoff games.** Theorem 1 establishes that mirror descent with action-value feedback yields monotonic improvement in common-payoff POSGs (strict when not at a local optimum), and Proposition 1 shows the DTP algorithm inherits this guarantee asymptotically. This gives MDS a sound theoretical foundation that PBS-based search methods like SPARTA and RLSearch do not formally possess.

- **Strong empirical results in Hanabi with dramatically lower search cost.** In 5-card Hanabi (Table 1), MDS achieves 24.62±0.02—matching the best PBS methods—while using ~2s per move vs. 180–450s. In 7-card Hanabi (Table 2), a variant designed to stress PBS scalability, MDS scores 24.28±0.02, outperforming all PBS baselines (best 24.18) while again using orders of magnitude less time. This is the first demonstration of a non-PBS method exceeding PBS performance in a domain they have historically dominated.

- **Effective in adversarial settings with minimal public information.** In 3×3 Abrupt Dark Hex and Phantom Tic-Tac-Toe—games where PBS methods are essentially inapplicable—MMDS reduces approximate exploitability of a uniform random blueprint from 74→50 and 78→50 (Table 3), outperforming all non-MMD baselines. This demonstrates the framework's applicability beyond the cooperative setting.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Theorem 1 does not quantify the stepsize condition.** The theorem states monotonic improvement holds "for any sufficiently small stepsize η > 0" but provides no bound on η, no proof sketch in the main text, and no characterization of what "sufficiently small" means (e.g., η ≤ 1/(max reward range), or a Lipschitz condition). Since the stepsize is a key hyperparameter that governs the improvement guarantee's validity, this makes the theoretical claim less actionable. The paper's own experiments (Figure 3) show performance varies substantially with η, and at large η the guarantee could fail—but the theorem gives no guidance on where the threshold lies.

- **The Hanabi comparisons involve confounding factors that complicate attribution.** MDS uses a PPO blueprint (+ Seq2Seq belief model) while the top PBS baselines use an R2D2 blueprint (with exact beliefs). Although the blueprint raw scores are closely matched (24.24 vs. 24.23, Table 1 caption), this does not control for potential differences in search-friendliness (policy entropy, action-value smoothness) that could asymmetrically favor one search algorithm. Additionally, MDS plays the argmax of the updated policy rather than sampling from it (footnote, §4)—a deviation from Algorithm 1—with no analysis of how this affects the theoretical improvement guarantee. These factors do not invalidate the results but make it harder to attribute MDS's advantage specifically to the update-equivalence framework rather than to implementation choices.

- **The finite-sample gap between Definition 1 (exact equality) and Algorithm 1 (asymptotic convergence) is not discussed.** The paper is clear that MDS "inherits the improvement property…as the computational budget increases" (§3), but does not discuss how large the budget needs to be for the guarantee to approximately hold, nor provide any rate of convergence or finite-sample bound. This is common for rollout-based search algorithms but contrasts with the paper's framing of MDS as a "provably sound search algorithm" (abstract), which suggests a stronger categorical property than what is actually established for finite compute budgets.

- **MMDS is empirically validated only in a narrow setting.** The adversarial experiments are limited to 3×3 games with a uniform random blueprint and a crude 10-particle posterior. MMDS's guarantee is conditional on an empirical observation from prior work ("if the observation of MMD's reliable last-iterate convergence…holds," §3), with no theorem or rigorous conjecture stated. The approximate exploitability numbers (50 vs. MMD's 20 at 10M steps) show meaningful improvement over the blueprint but still leave a large gap to MMD itself (which is not a search method). The paper is appropriately cautious about MMDS, but the validation is sufficient only as a preliminary proof of concept.

### Trivial
None.

## Nice-to-Haves

- **Experimental comparison or discussion of JPS** (cited §5) as another non-PBS approach with improvement guarantees for common-payoff games would help position the framework's novelty. The paper currently cites it in related work but doesn't discuss how update equivalence differs from or improves upon JPS's decomposition-based approach.
- **A controlled ablation in Hanabi** keeping the blueprint fixed (e.g., using PPO for all methods) and varying only the search algorithm would isolate MDS's advantage from blueprint differences. The paper already includes one such comparison (single-agent SPARTA with the same PPO+Seq2Seq, Table 1) but a full ablation would strengthen the attribution.
- **Reporting the specific η used for the main Hanabi results** (different from the sweep in Figure 3) would improve reproducibility.

## Removed Points

These are points from the reviews that were removed per the review instructions (see "Hard Rules"):
- **Theorem 1 missing proof / appendix reference**: Removed because the appendix is stripped by the parser; the proof exists in the original submission.
- **Missing comparison with JPS as a weakness**: The paper cites JPS in related work; the critic acknowledged this comparison is not required. Demoting to a nice-to-have.
- **"Last-iterate algorithm" definition being loose**: This is a presentation nitpick that does not affect the paper's contribution. Removed.
- **Claim about outperformance needing caveat for 7-card only**: The paper already acknowledges this nuance in context (§4, Tables 1–2). Removed as already addressed.
- **Formatting/style nitpicks and grammar issues**: Per instructions, these are parser artifacts. Removed.

## Novel Insights

The most striking insight from the reviews is the tension between the paper's clean theoretical framing and the practical reality of its implementation: Definition 1 posits exact update equivalence as the foundation, but Algorithm 1 delivers only asymptotic approximation, and the Hanabi experiments further deviate by playing argmax instead of sampling. This gap between the elegant theory and the messier practice is itself informative—it suggests that the update-equivalence framework may be most valuable as a *design principle* for generating algorithms (analogous to how policy gradient theorems guide but do not exactly describe practical RL), rather than as a tight analytical tool for finite-sample guarantees. The fact that MDS succeeds despite these gaps actually strengthens the case that the framework captures something fundamentally right about regularized search, even if the formal guarantees are asymptotic.

## Suggestions

1. Add a quantified bound on η to Theorem 1 (or at least a proof sketch establishing what "sufficiently small" means concretely) to make the theoretical claim actionable.
2. Add a brief paragraph explicitly acknowledging that MDS's guarantee is asymptotic and that the finite-sample behavior depends on the number of rollouts, concentration properties, and the deviation from exact argmax sampling.
3. Run a controlled ablation in Hanabi using the same blueprint for MDS and at least one PBS method, or discuss why this is infeasible, to strengthen causal attribution.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>