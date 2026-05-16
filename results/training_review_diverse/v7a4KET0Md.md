Now I have a thorough understanding of the paper. Let me construct the final review by cross-checking every claim against the actual paper text.

---

## Summary

This paper introduces SWIRL (SWitching IRL), an inverse reinforcement learning framework that models long, naturalistic animal behaviors as sequences of short-term decision-making processes, each governed by a hidden reward function. The key innovations are (1) incorporating history dependency at two levels — decision-level (state-dependent mode transitions) and action-level (non-Markovian rewards/policies within each mode) — and (2) unifying prior time-varying IRL models (Multi-intention IQL, Locally Consistent IRL) as special cases. SWIRL is validated on simulated and two real-world animal behavior datasets (labyrinth navigation and spontaneous behavior), achieving superior held-out log-likelihood and producing interpretable reward maps and mode segmentations.

## Strengths

- **Novel combination of switching rewards with history dependency in IRL**: SWIRL extends time-varying IRL by incorporating both decision-level history (state-dependent switching between hidden modes) and action-level history (non-Markovian rewards/policies). The paper formalizes how these two levels of dependency matter for modeling animal behavior, and the approach demonstrably works better than Markovian baselines in settings where history matters (e.g., the water port with a 90-second refill constraint in the labyrinth experiment).

- **Consistent quantitative improvements over baselines with real-world validation**: Across simulated gridworld, long labyrinth trajectories (500 steps per trajectory), and spontaneous behavior datasets, SWIRL variants outperform MaxEnt, ARHMM, and rARHMM on held-out test log-likelihood (Figs. 2B, 3E, 4B). The labyrinth experiment is particularly compelling because it uses 500-step trajectories — a substantially harder setting than prior work that was limited to 20-step clustered sequences.

- **Interpretable and biologically validated reward maps and segmentation**: SWIRL (S-2) infers reward maps that recover meaningful structure: the water reward map correctly assigns high reward for *leaving* the water port after drinking (matching the 90-second constraint), home reward is high at the entrance node, and an explore mode captures curiosity-driven behavior (Fig. 3B–C). Hidden-mode segments reliably align with behavior — water segments end at the water port, home segments end at the home node (Fig. 3F) — without prior knowledge of port or home locations.

- **Unifies prior time-varying IRL models as special cases**: SWIRL explicitly subsumes Multi-intention IQL (I-1, L=1 with state-independent transitions) and Locally Consistent IRL (S-1, L=1 with state-dependent transitions), providing a principled framework that clarifies the relationship between existing approaches. This is a genuine conceptual contribution.

- **Honest treatment of negative results**: In the spontaneous behavior experiment, history-dependent variants (I-2, S-2) underperform their Markovian counterparts (I-1, S-1). Rather than suppressing this, the paper correctly interprets it as a hypothesis-testing result — the data exhibits only Markovian dependency — and positions this as a demonstration of SWIRL's diagnostic value. This candor strengthens trust in the positive results.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Novelty claim is slightly overbroad**: The paper states it is "the first to incorporate history-dependent policies and rewards into IRL" (lines 4, 14). While the *specific combination* of time-varying switching rewards with history dependency for animal behavior is novel, the blanket claim is imprecise — there is prior work on non-Markovian rewards in IRL (e.g., reward machines, LTL-based reward specification). The claim should be qualified to the context of time-varying switching IRL for behavioral modeling, which is a strong enough contribution on its own.

- **Likelihood comparability across model families is not fully detailed**: The main quantitative metric is held-out test log-likelihood compared across SWIRL, MaxEnt, ARHMM, and rARHMM. The paper argues (line 91) that ARHMM can be viewed as a variant of SWIRL with behavior-cloned policies, making the likelihoods theoretically comparable, but the details of how likelihoods are normalized and computed for each model family are not provided. Since these are different probabilistic models with potentially different normalizing constants, a brief derivation or reference to an explicit likelihood formula would strengthen the comparison.

- **Discussion section is too brief and lacks limitations**: Section 5 is only two sentences (lines 103–105). Important considerations go unaddressed: (1) the assumption of optimal behavior in IRL, which may not hold for suboptimal animals; (2) how the number of hidden modes is chosen (no model selection criterion is discussed); (3) computational cost of the EM procedure; (4) sensitivity to the history window length L. These omissions prevent readers from understanding the method's practical limitations.

- **No statistical significance testing for key comparisons**: Figures show boxplots and shaded error regions, but there are no formal significance tests (e.g., paired tests or bootstrapped confidence intervals) for the key comparisons — most importantly S-2 vs. S-1 in the labyrinth test LL (Fig. 3E). While the boxplot separation appears convincing, significance testing would rule out the possibility that the improvement is due to small-sample variance.

### Trivial

- **Simulation experiment is a sanity check under the method's own assumptions**: The gridworld generates data from the same model class that SWIRL assumes (non-Markovian water reward, state-dependent mode transitions). That S-2 recovers the correct reward maps is a useful implementation check but does not provide evidence about robustness to model misspecification. This would be a major concern if the paper relied solely on simulation, but it is a minor point given the strong real-world validation in the labyrinth experiment.

## Nice-to-Haves

- An ablation where simulated data is generated with Markovian rewards to test whether SWIRL correctly identifies that history dependency is unnecessary (mirroring the spontaneous behavior result).
- A brief note on computational cost (EM iteration count, runtime per trajectory) to help practitioners assess scalability.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Missing method sections 3.1–3.3 and 3.5**: The harsh critic claimed these sections are absent and the paper is un-reviewable. However, the paper references Sec. 3.5 in lines 15 and 91, confirming its existence in the original submission. The gap is a parser extraction artifact, not an author omission. The rules instruct that formatting/parser artifacts should not be held against the paper. *Removed per parser-artifact rule.*

2. **Criticism that non-Markovian IRL works are not cited**: The harsh critic named specific papers (Camacho et al., 2020; De Giacomo et al., 2020; Toro Icarte et al., 2020) as missing from the related work. Per the instructions, I cannot confirm the existence or relevance of these references, and the instruction explicitly says "DO NOT mention missing related works, as you do not have external sources to confirm their existence." The general point about the novelty claim being overstated (kept above) stands without requiring specific missing citations. *Removed per missing-related-works rule.*

3. **"Simulation experiment is circular" as a major weakness**: The harsh critic presented this as a methodological gap. But generating data from a known model and recovering it is standard practice for sanity checks, and the paper's main evidence comes from real animal data. This is at most a trivial point. *Downgraded to trivial, then moved here as it was already captured as a trivial weakness.*

## Novel Insights

Beyond the paper's own contributions, the reviews surface a nuanced tension: the paper's empirical strength lies in the *interpretability* of its results (the water reward map revealing the 90-second constraint, the mode segments aligning with behavior) more than in raw predictive performance. The spontaneous behavior experiment, where the more complex model (S-2, I-2) underperforms simpler variants, is actually one of the paper's strongest assets — it demonstrates that SWIRL can be used as a diagnostic tool to reject the hypothesis of non-Markovian dependency when the data does not support it. This is a valuable methodological principle for computational neuroscience that the paper could emphasize more explicitly.

## Suggestions

- Qualify the novelty claim throughout to read "first IRL model to *combine time-varying switching rewards with history dependency* for animal behavior" rather than "first to incorporate history dependency into IRL."
- Add a supplementary section detailing the likelihood computation for each model family, including normalizing constants, so readers can verify the comparisons are on equal footing.
- Expand the Discussion to include limitations: the optimality assumption, sensitivity to mode count, choice of history window L, and computational cost.
- Add statistical significance tests (bootstrapped confidence intervals or paired tests) for the key labyrinth comparison between S-2 and S-1.

## Score and Decision

The paper presents a well-motivated, technically sound extension to time-varying IRL with clear biological relevance. The core claim — that incorporating history dependency at both decision and action levels improves modeling of naturalistic animal behavior — is supported by consistent quantitative results and compelling qualitative interpretability. The weaknesses (imprecise novelty claim, missing likelihood details, brief discussion) are addressable in revisions and do not undermine the contribution. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>