Now I have all the information needed. Let me produce the final consolidated review.

## Summary

SWIRL is a novel IRL framework for modeling time-varying, history-dependent reward functions in long, naturalistic animal behavior. It incorporates history dependency at two levels: decision-level (mode transitions depend on state and past decisions) and action-level (reward/policy depends on trajectory history, not just current state). The paper demonstrates SWIRL on simulated gridworld data and two real mouse behavior datasets, showing improvements over models lacking history dependency, both quantitatively (test log-likelihood, reward recovery, segmentation accuracy) and qualitatively (interpretable reward maps and mode segments).

## Strengths

1. **First IRL model to incorporate history-dependent policies and rewards at two levels.** The paper introduces decision-level (state-dependent mode transitions) and action-level (history-dependent reward/policy) dependency into switching IRL. This directly addresses a gap in prior time-varying IRL methods (multi-intention IQL, locally consistent IRL) that lacked such structure — a limitation clearly recognized in the animal behavior literature (Kennedy, 2022; Hattori et al., 2019).

2. **Strong empirical evidence on both simulated and real animal datasets.** In the gridworld simulation (Section 4.1), S-2 achieves the highest Pearson correlation for reward recovery and test segmentation accuracy, with only state-dependent models robustly recovering correct segments. On the labyrinth dataset (Section 4.2), S-2 yields superior held-out test log-likelihood (Fig. 3E) and produces interpretable mode segments where water-port visits consistently end water-mode segments, unlike baselines (Fig. 3F). On the spontaneous behavior dataset (Section 4.3), all SWIRL variants outperform ARHMM and rARHMM in test log-likelihood.

3. **Interpretable, biologically meaningful reward maps that capture non-Markovian structure.** SWIRL infers a history-dependent water-port reward (Fig. 3C) reflecting the non-Markovian task constraint: high reward (1.0) for arriving, lower reward (0.7) for staying, highest (0.9) for leaving — structure that "would not be captured by a Markovian reward function." The model discovers three interpretable modes (water, home, explore) without prior knowledge of reward locations (Section 4.2.1).

4. **Demonstrates SWIRL as a hypothesis-testing tool for neuroscience.** In the spontaneous-behavior experiment (Section 4.3), the finding that Markovian variants (S-1, I-1) outperform non-Markovian ones (S-2, I-2) leads to the testable conclusion that these behavioral syllables exhibit only Markovian dependency — showing how SWIRL can validate or challenge hypotheses about behavioral structure.

5. **Handles substantially longer trajectories than prior IRL work on the same data.** The labyrinth dataset uses trajectories of 500 time points, whereas previous IRL applications were "limited to clustered, stereotyped trajectories of only 20 time points" (Section 4.2), enabling analysis of extended naturalistic behavior.

## Weaknesses

### Fatal

None.

### Major

- **The M-step of the EM algorithm is not specified.** The paper provides the E-step auxiliary function (Section 3.4) and states it uses forward-backward message passing, but never describes how the reward parameters \(r_z\) and policies \(\pi_z\) are updated given the posterior probabilities over modes. The sentence "if we have estimated the current policy \(\pi_{z_n}\) based on the current reward estimate \(r_z\)" assumes the reader already knows the procedure for obtaining \(r_z\) from data. This is the core optimization step of the method, and omitting it makes the paper incomplete as a standalone methodological description. While the code is available at an anonymous repository (mitigating irreproducibility), the paper itself should at minimum sketch the optimization objective and update rule for the reward parameters. This is the single most important gap in the paper.

- **Number of modes set without justification or model selection.** The paper sets the number of hidden modes to 2 (simulation), 3 (labyrinth), and 5 (spontaneous) without discussing how these values were chosen (held-out likelihood, prior knowledge, or other criteria). Since mode count directly affects the interpretability and validity of inferred segments, the lack of discussion weakens the evaluation.

### Minor

- **Optimality assumption undiscussed for the spontaneous behavior dataset.** The paper explicitly states "we assume the mice acted optimally" for the labyrinth experiment (citing Rosenberg et al., 2021), but does not discuss this assumption for the spontaneous behavior dataset (Markowitz et al., 2023), where animals freely explore an empty arena with no explicit reward. If the optimality assumption fails, inferred rewards and modes could be artifacts. The paper would benefit from a brief discussion of how sensitive the conclusions are to this assumption, and whether the Boltzmann-rational (soft-optimal) formulation commonly used in IRL provides sufficient robustness.

- **Novelty claim ("first") is stated without rigorous substantiation.** The claim that "our paper is the first to incorporate history-dependent policies and rewards into IRL" appears twice (abstract, introduction) but the paper does not systematically rule out related work that might have addressed non-Markovian IRL (e.g., via recurrent policies, feature constructions, or other indirect approaches). While the claim is likely correct for the specific formulation, it would benefit from a more careful literature positioning.

- **No runtime, convergence, or initialization sensitivity analysis.** The paper does not report number of EM iterations, runtime, or sensitivity to initialization. These are especially relevant given that the EM algorithm for switching models can be sensitive to initialization and local optima.

### Trivial

None.

## Nice-to-Haves

- Algorithm pseudocode or a graphical model summarizing the full inference pipeline.
- A model selection procedure (e.g., held-out likelihood, BIC, cross-validation) for choosing the number of modes.
- Runtime and convergence analysis for future applications on larger datasets.

## Removed Points

These points were flagged by reviewers but removed after verification against the paper:

- **"Limited baseline comparisons"** (Harsh Critic's Critical Issue 2): The reviewer claimed the baselines are "nested special cases" making the comparison "circular" and that BNP-IRR/DIRL should have been included. This misreads the paper's ablation design. The I-1/I-2/S-1/S-2 framework is a principled ablation that cleanly isolates each type of history dependency: I-1→I-2 isolates action-level history (under independent transitions), I-1→S-1 isolates state-dependent transitions, S-1→S-2 isolates action-level history (under state-dependent transitions). I-1 corresponds to the published multi-intention IQL (Zhu et al., 2024) and S-1 to locally consistent IRL (Nguyen et al., 2015) — both are existing methods from the literature. DIRL is excluded with justification (requires clustered trajectories). The comparison is not circular; it is a properly designed ablation.

- **"ARHMM connection not formalized"**: The reviewer stated the connection to ARHMM is "gestured at but not formalized" and "no derivation or mapping is provided." However, the paper references Section 3.5 for this formalization. Section 3.5 was stripped by the parser and exists in the original submission. The paper also explicitly states this connection in Section 4.3: "the ARHMM can be viewed as a variant of SWIRL that learns the policy through behavior cloning."

- **"Spontaneous behavior explanation is post-hoc"**: The reviewer claimed the paper's explanation for why history dependency fails on spontaneous behavior data "seems post-hoc" and that "the preprocessing choices are the authors' own." The paper openly acknowledges this limitation and offers a testable hypothesis (syllable merging leading to poorly defined time intervals). This is good scientific practice, not a weakness.

- **"No algorithm pseudocode or graphical model"**: While a pseudocode would improve presentation, the absence is not a substantive weakness given the EM auxiliary function is provided and code is available. Moved to Nice-to-Haves.

- **Formatting/style nitpicks and criticisms about missing sections/appendices**: Removed per parser artifact rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between methodological completeness (the M-step gap) and the paper's genuine empirical contributions, but do not identify novel connections the authors missed.

## Suggestions

1. **Specify the M-step.** Provide the exact objective and update rule (or optimization algorithm) for learning reward parameters given the posterior over modes. Even a concise description (e.g., "we optimize \(r_z\) via gradient descent on the expected complete-data log-likelihood using the soft-Q policy parameterization") would close the most significant gap.

2. **Add a brief discussion of model selection** for the number of hidden modes, including how the chosen values were determined for each dataset.

3. **Discuss the optimality assumption** for the spontaneous behavior dataset, and whether the Boltzmann-rational (soft-optimal) formulation used in the IRL framework provides robustness to suboptimal behavior.

4. **Add a brief runtime/convergence note** for reproducibility and to help future users gauge computational requirements.

## Score and Decision

The paper tackles a genuinely important problem — modeling time-varying, history-dependent reward functions in long, naturalistic animal behavior — and the experiments on real datasets demonstrate real promise. The SWIRL framework's ability to infer interpretable, non-Markovian reward maps and meaningful behavioral segments (especially on the labyrinth dataset) supports its core claim that history dependency improves behavioral modeling. However, the paper's main methodological weakness is the incomplete specification of the M-step, which is central to the paper's contribution as a method. This gap is partially mitigated by the availability of open-source code. The paper is a solid contribution with clear potential impact in computational neuroscience and animal behavior analysis, but the M-step gap should be addressed before it can be considered fully reproducible as a standalone methods paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>