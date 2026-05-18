Here is my final consolidated review.

---

## Summary

This paper introduces SWIRL (SWitching IRL), a framework for inverse reinforcement learning that models long animal behavior sequences as transitions between short-term decision-making processes, each governed by its own reward function. SWIRL incorporates history dependency at two levels: decision-level (state-dependent transitions between hidden modes) and action-level (non-Markovian reward/policy within each mode). The method is evaluated on simulated gridworld trajectories, mouse labyrinth navigation data, and mouse spontaneous behavior data, consistently outperforming baselines without history dependency.

## Strengths

1. **Novel integration of non-Markovian rewards into time-varying IRL.** SWIRL is the first time-varying IRL framework to make the reward function itself history-dependent (e.g., $r(s_t, s_{t-1})$ rather than just $r(s_t)$). This goes beyond prior multi-intention IRL and Dynamic IRL, which assume Markovian rewards. The simulation experiment (Fig. 2B) directly confirms that this history dependency produces better reward recovery — only S-2 (full SWIRL with both decision- and action-level history) achieves accurate reward recovery, with higher test log-likelihood and segmentation accuracy than all baselines.

2. **Interpretable, experimentally consistent reward maps on real data.** On the labyrinth dataset (Sec. 4.2.1, Fig. 3C), SWIRL recovers a non-Markovian reward at the water port that would be impossible with a Markovian model: high reward for arriving (1.0), moderate for staying (0.7), and high for leaving (0.9). This aligns precisely with the 90-second water restriction design (mice must leave after drinking) and provides a mechanistic account that no prior time-varying IRL model could deliver. This is the paper's strongest qualitative result.

3. **Outperforms dynamics-based models on spontaneous behavior.** On the spontaneous behavior dataset (Sec. 4.3, Fig. 4B), all SWIRL variants achieve higher held-out test log-likelihood than both ARHMM and rARHMM across multiple hidden mode counts, demonstrating that learning reward functions through IRL provides a more principled approach for segmenting animal behavior than purely autoregressive dynamics models.

4. **Scales to longer, non-stereotyped trajectories.** SWIRL processes 500-time-point trajectories from the labyrinth dataset, whereas prior IRL work on the same dataset (Ashwood et al., 2022a; Zhu et al., 2024) was limited to clustered, stereotyped trajectories of only 20 time points. This demonstrates meaningful scalability.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Reward parameter optimization (M-step) is underspecified.** Section 3.4 presents the auxiliary function and EM formulation, but does not describe how the reward parameters $r_z$ are actually optimized in the M-step. The auxiliary function contains $\log \pi_{z_{n,t}}(a_{n,t}|s_{n,t}^L; r_z)$, and the paper states "If we have estimated the current policy $\pi_{z_n}$ based on the current reward estimate $r_z$..." but never specifies how the reward→policy mapping is computed (e.g., soft-Q iteration, maximum entropy IRL gradient steps) or how $r_z$ is updated given the posteriors. While the connection to MaxEnt IRL is suggested and code is provided, a methods paper should spell this out — the reader cannot assess correctness or computational feasibility without it.

2. **"First IRL model to incorporate history-dependent policies and rewards" is slightly imprecise.** The paper's contribution — non-Markovian reward functions in switching IRL for animal behavior — is genuinely novel and well-supported by experiments. However, the blanket phrasing could be read as ignoring POMDP IRL and adversarial IRL with recurrent policies (Finn et al., 2016), which implicitly induce history-dependent policies. The paper would benefit from a more precise qualifier: e.g., "first time-varying IRL model to incorporate history-dependent reward functions" or "first to model both decision-level and action-level history dependency in switching IRL." The current phrasing is likely to draw unnecessary pushback without changing the actual contribution.

3. **Missing quantitative segmentation metrics on the labyrinth dataset.** The paper shows only qualitative segmentation examples (Fig. 3F) and test log-likelihood (Fig. 3E) for the labyrinth experiment, even though the simulation experiment included quantitative segmentation accuracy. While ground-truth segments are unavailable, reasonable proxies exist (e.g., proportion of "water" segments ending at the water port, proportion of "home" segments ending at state 0). The paper's own qualitative analysis in Sec. 4.2.2 makes claims about S-2 producing more interpretable segments — these claims would be significantly stronger with a quantitative summary. The data to compute such metrics is available within the paper's own analysis.

4. **No explicit discussion of how the number of hidden modes was determined for the labyrinth dataset.** For the spontaneous behavior dataset, results are shown across different mode counts (Fig. 4B), but for the labyrinth the authors settle on three modes (water, home, explore) without explaining the selection criterion. A cross-validation or held-out likelihood analysis would strengthen confidence that three modes is the right choice rather than a post-hoc fit.

5. **No sensitivity analysis for history length $L$.** Only $L=1$ and $L=2$ are tested. For the labyrinth dataset, it would be informative to see whether $L=3$ or higher improves further, or whether $L=2$ already captures all relevant history. This is an easy ablation to add.

### Trivial

- Boxplots are presented without statistical tests or effect sizes. For the simulation experiment with 200 trajectories, confidence intervals or permutation tests would help assess reliability of the reported improvements, though this is not uncommon in IRL papers.
- The labyrinth environment dynamics (deterministic graph transitions vs. learned from data) are not explicitly clarified for the reader, though the auxiliary function notes that environment transitions are not optimized.

## Nice-to-Haves

- **DIRL baseline comparison:** The paper acknowledges DIRL (Ashwood et al., 2022a) as related work but does not compare against it, citing DIRL's requirement for clustered, similar trajectories. This is a reasonable justification, but a comparison — perhaps on a subset where DIRL is applicable — would be informative, especially on the same dataset where DIRL was originally applied.
- **Runtime and convergence criteria:** The paper does not report computational cost or convergence behavior. Given the EM algorithm's susceptibility to local optima and the long trajectories involved, practical guidance on initialization strategies and convergence diagnostics would aid reproducibility.
- **Sensitivity analysis for spontaneous behavior preprocessing:** The paper uses merging of consecutive identical syllables and filtering to the 9 most frequent syllables, following prior work. A brief discussion of how sensitive the conclusions are to these choices would be useful.

## Removed Points

- **"Incomplete paper: model sections missing"**: The extracted text jumps from Section 2 to Section 3.4, with Sections 3.1–3.3 and 3.5 absent. This is a PDF extraction artifact — the original submission contains these sections (the paper repeatedly references Section 3.5). Per policy, extraction artifacts are not author errors and should not be held against the paper. The review proceeds based on the content that is present and evaluable.
- **"Spontaneous behavior preprocessing choices are arbitrary"**: The paper states these preprocessing steps follow Markowitz et al. (2023), a prior publication on the same dataset. The choices are standard for this data and not arbitrary.
- **"POMDP IRL invalidates the first-to-claim novelty"**: The paper's actual contribution is about non-Markovian *reward* functions (not just policies) in switching IRL for animal behavior — a distinct claim not invalidated by POMDP IRL, which typically uses Markovian rewards. The phrasing concern is preserved as Minor weakness 2, but the stronger claim that the novelty is invalid is removed.

## Novel Insights

None beyond the paper's own contributions. One observation worth noting from cross-referencing the harsh critic's comments with the paper: the critic's most severe complaint (missing model sections) turns out to be a pure extraction artifact, and the paper's actual methodological description — while brief — is coherent enough to understand the core EM inference procedure and experimental setup. The main exposition gap (M-step details) is real but standard enough in the IRL literature that the paper's contribution is not threatened by it, especially given code availability.

## Suggestions

1. In Section 3.4, add 2–3 sentences specifying how reward parameters $r_z$ are optimized in the M-step (e.g., "We use gradient-based maximum entropy IRL to optimize $r_z$, where the policy $\pi_z$ is obtained via soft-Q iteration on the current reward estimate, and the gradient of the expected log-likelihood w.r.t. $r_z$ is computed using the difference between empirical and expected state-action visitation frequencies under the current posterior"). A brief algorithm box would be ideal.

2. Add a table reporting quantitative segmentation quality for the labyrinth dataset, e.g., the fraction of water-mode segments that end at the water port, fraction of home-mode segments ending at state 0, across all SWIRL variants. This would directly support the qualitative claim in Sec. 4.2.2.

3. For the labyrinth experiment, show held-out test log-likelihood or segmentation coherence for varying numbers of hidden modes (2–5) to justify the choice of three modes.

4. Add a brief ablation showing test log-likelihood for $L=3$ on the simulated and/or labyrinth data to demonstrate that $L=2$ captures sufficient history.

5. Qualify the novelty claim in the introduction more precisely (e.g., "first time-varying IRL model to incorporate history-dependent reward functions that depend on trajectory suffixes of length $L$").

## Score and Decision

The paper presents a well-motivated methodological contribution with clear experimental support across simulated and real-world animal behavior datasets. The principal weakness — underspecification of the M-step reward optimization — is addressable and does not threaten the core claims. The missing model sections are a parser artifact, not an author error. The paper meaningfully advances the state of time-varying IRL for neuroscience applications.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>