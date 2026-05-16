I've now verified all reviewer claims against the paper. Let me produce the final consolidated review.

## Summary

This paper proposes Replay across Experiments (RaE), an extremely simple method for off-policy RL: mix prior data from previous experiments with online data at a fixed 50/50 ratio during replay, without tuning, algorithmic changes, or additional infrastructure. The authors show RaE improves asymptotic performance across locomotion, manipulation, and RL Unplugged benchmarks using four different algorithms (DMPO, SAC-Q, CRR, D4PG). Extensive ablations on data quantity, quality, and mixing ratios demonstrate robustness, and an iterative application shows progressive gains.

## Strengths

- **Simplicity with strong empirical performance**: The method requires only a fixed-ratio mix of prior and online data, no additional hyperparameters, no algorithmic modifications. Despite this simplicity, RaE consistently matches or exceeds more complex baselines (AWAC, fine-tuning, random weight resetting) across five diverse domains. The vision-based Locomotion Soccer task shows a particularly notable improvement (Figure 2).

- **Algorithmic generality across diverse off-policy agents**: RaE improves performance with four distinct underlying algorithms — DMPO (locomotion), SAC-Q (manipulation), CRR (RL Unplugged), and D4PG (ablation, Figure 4b) — without per-algorithm tuning. This breadth directly supports the claim that RaE is a general workflow extension rather than a method tied to a specific agent.

- **Robustness to data quantity and quality in systematic ablations**: Table 1 evaluates RaE across three data regimes (high/mixed/low return), two dataset sizes (10k and 100k episodes), and four mixing ratios. Gains exceeding 100% of online-only performance (blue cells) occur in 14 of 24 configurations, including with only 10k low-return episodes (97–113%). This thorough ablation is the strongest evidence for the method's robustness.

- **Increased robustness across seeds demonstrated**: Figure 4(c) shows that mixing data from multiple random seeds (where only one seed achieved high reward) yields robust performance matching or exceeding the best single seed, supporting the practical claim that RaE adds resilience to variance across runs.

## Weaknesses

### Fatal
None.

### Major

- **Unfair advantage given to the fine-tuning baseline via seed selection**: The fine-tuning baseline (line 117) explicitly chooses the *best performing seed* from offline CRR runs and fine-tunes that seed online. This cherry-picking gives fine-tuning a systematic advantage that RaE does not receive — RaE is evaluated from a single offline dataset without seed selection. A fair comparison would either (a) fine-tune each seed independently and report the mean/median, or (b) apply the same seed-selection procedure to RaE if run from multiple offline seeds. This asymmetry undermines the primary comparisons in Figures 2 and 3, and is the most serious evidential issue in the paper. The core claim may still hold, but the main experimental evidence for it is compromised.

### Minor

- **Missing learning curves for locomotion and manipulation main results**: Figure 2 shows only bar plots of final asymptotic returns for Locomotion Soccer and Manipulation domains. Without learning curves, the reader cannot assess whether RaE improves performance through faster learning, a higher asymptote, or both — nor whether baselines simply needed more steps to converge. This is particularly relevant since the paper motivates RaE as improving "research iteration times," which requires evidence of speed, not just final performance.

- **The "state-of-the-art" claim is unsupported**: The paper states in its contributions (line 31) that RaE "demonstrate[s] state-of-the art performance," yet compares only to AWAC, fine-tuning, and random weight resetting — a narrow baseline set. Other offline-to-online methods (e.g., IQL+finetuning, CQL+finetuning, calibrated Q-ensembles, or more recent approaches like BEDD-RL or DrQ+finetuning) are not included. On Locomotion Soccer and Manipulation, no external published results are cited to establish SOTA. This claim should be removed or substantially qualified.

- **Iterative improvement ablation conflates "more data" with "iterative reuse"**: In the iterative experiment (Figure 4a), RaE is applied starting from 1e4 episodes, and each iteration adds new online data. The observed improvement could be entirely explained by the accumulation of more data rather than by the benefits of iterative re-initialization. A baseline running a single RaE run for the same total number of steps would be needed to isolate the effect of iterative reuse. The paper's suggestion that "it may be preferable to break a single training run into smaller runs" is not directly supported by the data presented.

- **Data collection details under-specified for locomotion and manipulation prior datasets**: The paper states (line 104) that training data of 4e5 and 2e5 episodes were gathered for state and vision respectively, and (line 107) that the manipulation dataset consists of 15e4 episodes "from a prior experiment with the same algorithm." It is not specified how many seeds were used to generate these datasets, whether the data came from a single converged run or multiple runs, or how the seed-variance of the data-generating policy affects downstream RaE performance. This limits reproducibility.

### Trivial

- Figure 3 (RL Unplugged learning curves) reports standard deviation rather than confidence intervals, while Figure 2 reports "95% confidence interval." This statistical reporting inconsistency is minor but worth standardizing.

## Nice-to-Haves

- Adding time-to-threshold or area-under-learning-curve metrics to the locomotion/manipulation results would directly substantiate the "research iteration time" motivation.
- A brief discussion of storage costs for accumulating prior data across many seeds and hyperparameter sweeps would strengthen the practical framing.
- A simple heuristic for choosing the mixing ratio (e.g., scale inversely with dataset size) would increase practical utility, since the ablations show the optimal ratio varies across regimes.

## Removed Points

- *"The comparison with random weight resetting does not isolate the effect of data reloading because RaE resets weights once and the baseline resets periodically."* — This is a valid observation about experimental design, but it does not constitute a weakness of the paper's own method; it is a by-design feature of the ablation. The baseline exists to test whether weight resets alone explain RaE's gains, and the paper acknowledges the comparison is imperfect. Removed as it does not weaken the paper's core claims.

- *Strength Finder's "state-of-the-art" language in Strength 1* — Removed because it conflicts with the verified weakness about unsupported SOTA claims.

## Novel Insights

The reviews converge on an unusual pattern: the paper's core contribution (a simple, no-tuning, fixed-ratio data mixing strategy) is genuinely novel in its radical simplicity, and the ablative evidence for robustness is strong. Yet the main experimental comparison is undermined by a straightforward methodological flaw (cherry-picking the best seed for fine-tuning) that is entirely fixable and does not affect the ablations. This creates a paper where the supporting evidence is stronger than the headline results — an inversion from the typical pattern. The most valuable insight from the reviews is that the authors could substantially strengthen the paper by de-emphasizing the direct comparison to fine-tuning (which the current design inflates) and foregrounding the ablations (Table 1, algorithmic generality, seed robustness), which are clean and independently convincing.

## Suggestions

1. **Fix the fine-tuning baseline comparison**: Average over seeds rather than selecting the best seed, or apply identical seed-selection criteria to RaE. This is the single most impactful change.
2. **Add learning curves** for the locomotion and manipulation main results (Figure 2) so readers can assess speed and asymptotic benefits separately.
3. **Remove or qualify the "state-of-the-art" language** in the contributions unless additional contemporary baselines are added.
4. **Add a longer-run baseline** to the iterative improvement ablation to separate the effect of more data from the effect of iterative restarts.
5. **Specify data collection details** (number of seeds, convergence criteria) for the locomotion and manipulation prior datasets.

## Score and Decision

The paper presents a simple, practical, and intuitively plausible method with strong ablative evidence. However, the main experimental comparison is weakened by a methodological asymmetry (seed selection for fine-tuning) that undermines the headline results. The core contribution is real and could be convincingly demonstrated with relatively minor revisions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>