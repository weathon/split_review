Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

OG-MARL addresses a critical gap in offline multi-agent reinforcement learning by providing the first standardized, comprehensive repository of offline MARL datasets across 10 diverse environments (SMAC v1/v2, MAMuJoCo, PettingZoo pixel-environments, Flatland, CityLearn, Voltage Control, etc.), each with Good/Medium/Poor/Replay dataset variants. The paper profiles datasets with violin plots and mean/std statistics, provides initial baseline results from state-of-the-art offline MARL algorithms on novel pixel-observation PettingZoo environments, and releases open-source tooling for generating new datasets.

## Strengths

- **First comprehensive, standardized benchmark for offline MARL.** The paper fills a clear and well-motivated gap: prior offline MARL works all generated their own uncomparable datasets (Section 2, paragraph 3), making it impossible to measure progress. OG-MARL provides datasets across 10 environments with standardized quality tiers, enabling reproducible comparisons that did not previously exist.

- **Systematic coverage of practically relevant properties.** The task properties section (Section 4) carefully considers dimensions that prior benchmarks neglect: heterogeneous/homogeneous agents, partial observability, pixel observations, sparse rewards, procedural generation, energy management domains, variable agent counts (2–27), and both discrete and continuous actions. This goes well beyond the game-like environments common in prior work.

- **Proper statistical methodology in baselines.** The paper uses 10 independent seeds, performance profiles with 95% confidence bands via percentile bootstrap (Figure 4), and a fixed online evaluation budget — following best practices from Agarwal et al. (2021) and Gorsane et al. (2022). This is a significant step up from typical evaluation in the offline MARL literature.

- **Transparent dataset profiling.** Violin plots (Figure 3) visualize the full distribution of episode returns per dataset, including median, IQR, and min/max, going beyond the misleading mean-only reporting common in prior work (Section 6, paragraph 2).

- **Open-source tooling and extensible design.** The OfflineLogger wrapper (Figure 1 code snippet) allows researchers to easily generate new datasets, and the paper commits to a growing repository. Pre-release versions have already been adopted by follow-up works (Formanek et al. 2023, Zhu et al. 2023), demonstrating practical value.

- **Honest discussion of limitations.** The paper explicitly acknowledges its cooperative focus, RL-only behavior policies, and the need for future work on human/hand-designed controllers and sequence modeling baselines (Section 8).

## Weaknesses

### Fatal

None.

### Major

- **Dataset generation methodology is underspecified for a benchmark reference.** The paper states that datasets were collected from "partially trained online algorithms" (QMIX, IDQN, ITD3, MATD3) using "3 independently trained joint policies" with "a small amount of exploration noise" (Section 6). However, it does not specify: how many environment steps were used to train each behavior policy, at what performance thresholds the policies were frozen, how many episodes were collected per dataset, what exploration noise schedule was applied, or how the three policies were selected (different seeds? different checkpoints?). For a paper whose central contribution is a standardized benchmark resource, these details are essential for reproducibility and for other researchers to generate comparable datasets for new environments. While the datasets themselves are released, the lack of specification means the methodology cannot be replicated by the community.

- **Dataset coverage analysis is limited to return distributions.** The paper characterizes datasets only through mean/std of episode returns and violin plots (Section 6). For offline RL, state-action coverage is equally critical — yet the paper provides no metrics such as number of unique state-action pairs, action entropy of the behavior policy, state visitation frequency distributions, or proxies for coverage. Datasets labeled "Good" based on return alone could still have narrow coverage that makes offline RL trivially easy or impossible. This significantly limits the paper's ability to serve as a diagnostic benchmark.

### Minor

- **Quality category thresholds are not disclosed.** The paper states boundaries for Good/Medium/Poor were "assigned independently for each environment and were related to the maximum attainable return" (Section 6), but never reports what these thresholds actually are for any environment. The "Replay" dataset is described merely as "a mixture of the previous three" with no detail on mixing proportions or sampling strategy. While the violin plots give readers some ability to infer the distributions, explicit threshold reporting would be straightforward to add and would significantly improve transparency.

- **The human behavior dataset is included but uncharacterized.** The Knights, Archers & Zombies dataset (Section 5) is collected from an unspecified number of human players who were "given no instruction" and played "a maximum of 20 episodes." The paper provides no analysis: no dataset size, no return distribution, no baseline results (e.g., Behavior Cloning), no evidence that the data is usable for offline MARL. While including this dataset as a forward-looking contribution is reasonable, its complete lack of characterization weakens the paper's credibility as a rigorous benchmark repository. At minimum, return statistics and a BC baseline should be reported.

- **Hyperparameter tuning details are insufficient.** The paper states hyperparameters were tuned "on Co-op Pong and kept fixed for Pursuit" (Section 7), but does not disclose which hyperparameters were tuned, over what range, how many trials were performed, or what the final values were. The 50,000 training step and 32 batch size budget is reported without justification. These omissions do not invalidate the results but reduce reproducibility.

- **D4RL normalization constants are not reported.** The paper says it "adopts the normalisation procedure from D4RL" (Section 7, Aggregated Results) but does not specify the random/expert return normalization constants used for each environment. Without these, the aggregated performance profiles cannot be independently reconstructed.

- **Dataset storage format and train/validation split are not documented.** For a dataset release paper, technical details like the storage format (e.g., HDF5, ReplayBuffer), recommended train/validation split protocol, and compatibility with common offline RL data structures should be described or referenced to the code repository.

### Trivial

None.

## Nice-to-Haves

- A table for each environment listing number of episodes, total transitions, and the percent contribution of each behavior policy would be a useful addition.
- Baselines on the competitive MPE datasets would strengthen the repository's completeness, though the paper frames these as forward-looking contributions (Section 5), which is defensible.
- Evaluating the sensitivity of results to the 50,000-step training budget would increase confidence in the baselines.

## Removed Points

These points were flagged for removal; treat them with caution:

- **"SMACv2 datasets claim not verified"** — Removed per hard rule: the paper cites SMACv2 (Ellis et al. 2022), a publicly released benchmark. The claim of being "first" is a factual assertion by the authors that may be true or false, but questioning it based on the reviewer's lack of knowledge about repositories falls under "doubting existence of a cited entity" (hard rule).
- **"MAMuJoCo claim not accompanied by comparison"** — Removed per hard rule: same reasoning. The paper provides the specific comparison (Pan et al. 2022 "only provided a single dataset on 2-Agent HalfCheetah"), which is a stated fact.
- **"Competitive MPE datasets feel like an afterthought"** — Removed per hard rule about evaluating against the wrong class of expectations. A dataset paper can include datasets that are not benchmarked, especially when explicitly scoped as encouraging future work (Section 5, last paragraph).
- **"All other results relegated to an appendix"** — Removed per hard rule: the parser strips appendix sections. The paper states additional results are in the appendix, which exists in the original submission.
- **"Baseline evaluation too thin" emphasis** — Weakened from the harsh critic's framing. The paper's choice to put novel pixel-observation environments in the main text and other results in the appendix is standard practice. The remaining concerns about hyperparameter disclosure and training budget justification are retained as Minor weaknesses above.
- **Generic strengths from Strength Finder** — Dropped several that were generic/superficial (e.g., "addressed an important problem") or that conflict with verified weaknesses (e.g., "inclusion of human behaviour policies" is listed as a strength but the human dataset is uncharacterized — weaknesses win in case of conflict).

## Novel Insights

The reviews surface a productive tension: the paper's greatest value — being a standardized benchmark — is also where its rigor is most uneven. It does many things *right* that the offline MARL community has done wrong (diverse environments, proper statistical methodology, transparent return profiling), but it stops short at the very places where a benchmark needs to be most precise (reproducible generation methodology, coverage diagnostics, disclosure of thresholds). This suggests the paper is a strong *contribution* that needs a final pass of completeness rather than a structural overhaul. Notably, both the harsh critic and the strength finder agree on the core value proposition and on the specific nature of the gaps — there is no fundamental disagreement about what the paper is or what it needs.

## Suggestions

1. **Add a reproducibility table** in the main paper or supplementary material listing for each environment: number of training steps for behavior policies, performance thresholds used to define dataset quality tiers, exploration noise parameters, number of episodes collected, and how the three policies were selected (seeds vs. checkpoints).
2. **Add coverage diagnostics** beyond return distributions: at minimum, estimate the effective number of distinct (observation, action) tuples or proxy metrics (action entropy, state-visitation counts), and discuss implications for offline RL difficulty.
3. **Characterize the human dataset** with basic statistics (size, return distribution, number of players) and at least one BC baseline to establish that learning is possible from this data.
4. **Report the D4RL normalization constants** used for each environment in the aggregated results.
5. **Document the dataset storage format** and recommended train/validation split protocol, either in the paper or by pointing to a clearly marked section in the code repository.
6. **State the hyperparameter search space** (ranges, number of trials, final values) for the algorithms tuned on Co-op Pong.

## Score and Decision

**Originality**: 4/5 — First standardized benchmark for offline MARL; fills a clear gap.  
**Importance of research question**: 5/5 — Lack of standardized benchmarks is a recognized barrier to progress.  
**Claims supported**: 3/5 — Core claim of providing datasets is supported, but claims about reproducibility and coverage are partially undermined by missing details.  
**Soundness of experiments**: 3/5 — Baselines are well-executed statistically but too narrow in disclosure of methodology.  
**Clarity of writing**: 4/5 — Well-structured and clearly written; easy to follow.  
**Value to community**: 4/5 — High potential value; already adopted by follow-up work.

The paper addresses a real and important gap. Its core contribution — standardized offline MARL datasets — is sound and valuable. However, the missing generation details, coverage analysis, and quality threshold disclosures are significant omissions for a benchmark paper, as they undermine the very reproducibility and comparability the paper aims to enable. These are all fixable and do not require new experiments, only better documentation and analysis. The overall assessment is that this is a borderline paper that would be a clear accept with the suggested revisions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>