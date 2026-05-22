Now I have sufficient calibration data. Let me compile the final review.

**Round 1 bracket:** The paper is clearly above the low-band (2.0-3.0) papers which are on different topics. It's in the middle band (3.5-7.5). Within this band, the most comparable papers are DELIFT (6.0, Accept), 3DS (5.75, Reject), Rule-Based Rating (5.75, Reject), and FEEDER (5.25, Reject).

**Round 2 narrowing:** The paper is empirically more thorough than 3DS and FEEDER (more paradigms, more domains) but has a notable weakness (claiming to replace reward models without testing) that DELIFT doesn't have. It's comparable in quality to 3DS (5.75) and Rule-Based Rating (5.75). 

**Final score:** 5.5 — the paper has a solid core contribution but the gap between its central claim (obviating reward models) and the evidence (no reward model comparison) is significant enough to require major revision.

---

## Summary

This paper proposes High-Entropy Sum (HES), a training-free metric that sums token-level entropy of only the top 0.5% highest-entropy tokens in a reasoning sample, motivated by the idea that these "forking points" capture reasoning complexity. The authors validate HES across SFT, RFT, and RL on math, code, and STEM domains, showing that pruning the lowest-HES data (training on top-80%) consistently outperforms training on full datasets, and that HES-based selection beats other training-free metrics (length, average entropy, difficulty).

## Strengths

- **Clean, well-motivated metric with strong discriminative ability.** Figure 1 shows HES separates correct vs. incorrect reasoning samples far better than average entropy (normalized means 0.29 vs. 0.68 for HES, versus 0.52 vs. 0.53 for AvgE). This directly supports the core intuition that global averaging dilutes critical signals.

- **Comprehensive empirical validation across three training paradigms and multiple domains.** The paper tests HES in SFT (Tables 1–4), RFT (Table 5), and RL (Table 6) on math (AIME, HMMT, OlympMATH), code (LiveBench), and STEM (GPQA) benchmarks. The core claim that pruning the lowest-HES 20% improves over the full dataset is consistent across all settings: top-80% HES outperforms Full-Dataset in Table 1 (35.36 vs. 32.61), Table 3 (39.51 vs. 36.28), and Table 4 (45.48 vs. 44.42).

- **Small-to-large model transfer is convincingly demonstrated.** Using Qwen3-0.6B to rank data for training Qwen3-8B achieves 32.12% average accuracy, nearly matching self-selection (31.14%), while reducing inference cost by an order of magnitude. This is a practical strength.

- **The asymmetric sampling insight in RL is a nice finding.** The RL experiments (Table 6) show that selecting high-HES positives with random negatives (21.30%) beats full-batch (20.63%), while constraining negatives to low-HES harms performance (19.50%). This nuanced result goes beyond simply "HES is good."

## Weaknesses

### Major

- **The paper claims HES "obviates the need for costly external reward models" (abstract, intro, conclusion) but never compares against any reward-model-based selection baseline.** This is the paper's strongest advertised claim, yet not a single experiment tests HES against even a simple trained classifier or process reward model. The baselines used (difficulty, length, entropy variants) are all *training-free* metrics; comparing HES against other training-free metrics shows it is the *best training-free metric*, which is a valid but much weaker claim. The paper as written is non-viable unless either (a) a reward-model baseline is added, or (b) the claim is explicitly moderated to only claim superiority over other *training-free* metrics. The current framing overstates the evidence.

- **No error bars or confidence intervals on any result.** All reported values are point estimates from single runs on small benchmarks (AIME has ~30 problems, HMMT ~25–30). Many comparisons involve differences of 1–3 percentage points (e.g., Table 6: Pos-High, Neg-Rand vs. Full-Batch is 21.30 vs. 20.63 — a 0.67 point gap). Without uncertainty estimates from multiple seeds, it is impossible for any reviewer or reader to assess which differences are real signal versus noise. This is a methodological gap that significantly weakens the quantitative evidence.

### Minor

- **The sensitivity analysis grid is coarse.** The paper tests only four high-entropy token ratios (0.005, 0.05, 0.5, 1.0) and finds 0.005 is consistently best. A wider grid (e.g., 0.001, 0.01, 0.1) would strengthen the evidence that 0.005 is a robust optimum rather than the best among four arbitrarily chosen values. The sensitivity curves (Figures 3–4) are fairly flat for some metrics, suggesting the specific cutoff is not critical — which is fine, but the paper should say so explicitly.

- **The "unified" framing overclaims.** The paper applies HES differently in each paradigm: ranking a static dataset in SFT, selecting among correct generations in RFT, and subsampling rollouts in RL. This is not a single selection *algorithm* but rather a metric that proves useful across multiple selection *settings*. The language should be tempered from "unified data selection framework" to "a metric effective across paradigms."

- **The connection between high-entropy tokens and semantic "forking points" is asserted but not empirically validated.** The paper relies on the intuition from Wang et al. (2025) but provides no qualitative analysis showing that the top 0.5% entropy tokens correspond to actual decision points (e.g., via human annotation or contrastive examples). A case study with 2–3 annotated examples would strengthen the paper's interpretability.

### Trivial

None.

## Nice-to-Haves

- A cost comparison of computing HES versus alternative selection methods (e.g., wall-clock time for scoring 100k samples) would help the reader evaluate the practical efficiency claim.
- Testing HES computed from a different model family (not within the Qwen family) would further support the claim that HES captures intrinsic data properties rather than model-specific artifacts.
- A qualitative analysis showing what the top 0.5% high-entropy tokens look like in a few reasoning traces.

## Removed Points

The following points from the input reviews were removed with justification:

- **"Inconsistent quantitative evidence — reversal of trends between Table 1 and Table 2"** — Removed because the core pruning claim (top-80% > full dataset) is *consistent* across both tables (35.36 > 32.61 and 32.35 > 30.22). The top-20% result varies (underperforms full in Table 1, overperforms in Table 2), but this is an expected variation across different models/datasets and does not undermine the paper's main claim about pruning.
- **"Suspiciously identical numbers in Table 5 Difficulty rows"** — Removed because the numbers are not identical (28.13 vs. 28.12, 36.93 vs. 33.27 for k=2 vs. k=4). The similarity likely reflects the nature of medium-difficulty selection, which would select from a stable pool across k values.
- **"Control using completely unrelated model's entropy"** — Demoted to nice-to-have. In-family transfer is a standard and sufficient control.
- **"Forking-Only baseline does not isolate OOD confound"** — This is a valid point but too narrow to retain as a standalone weakness. It is subsumed by the broader point about limited qualitative validation of the forking-token connection.
- Several generic strengths from the Strength Finder (e.g., "addresses an important problem") were removed as superficial.

## Novel Insights

None beyond the paper's own contributions. The asymmetric sampling result in RL (high-HES positives + random negatives > high-HES positives + low-HES negatives) is the most interesting nuance that emerged from the experiments, and it is already discussed in the paper.

## Suggestions

1. **Add a reward-model baseline or temper the central claim.** This is the single most important revision. Either (a) add a comparison against a small trained binary classifier or PRM scoring correctness, and show HES performs comparably, or (b) reframe the paper's contribution as "the best *training-free* metric for reasoning data selection" and remove all claims about obviating reward models.

2. **Report results with multiple seeds (at least 3) for all key comparisons.** Provide standard deviations or confidence intervals, especially for the core comparisons (full vs. top-80% HES in SFT; Highest-HES vs. Random in RFT; Pos-High, Neg-Rand vs. Full-Batch in RL).

3. **Add a 2–3 example qualitative analysis** showing the tokens identified by the top 0.5% entropy threshold, to connect HES to the claimed "forking points" intuition.

4. **Tone down the "unified" framing.** Describe HES as "a metric effective across SFT, RFT, and RL" rather than a single "unified data selection framework."

## Score and Decision

The paper introduces a simple, well-motivated metric with broad empirical evaluation. However, the strongest advertised claim (obviating external reward models) is entirely unsupported by the experiments, and the lack of error bars significantly weakens the quantitative evidence. The paper needs major revision before it meets the acceptance bar.

**Round-1 bracket:** (3.5, 7.5) — clearly above weak papers (2–3), within the middle band.

**Round-2 narrowing:** Compared against DELIFT (6.0, Accept), 3DS (5.75, Reject), Rule-Based Rating (5.75, Reject), FEEDER (5.25, Reject). The HES paper has broader empirical validation than 3DS and FEEDER but a more significant gap between claims and evidence than DELIFT. Positioned slightly below 3DS and Rule-Based Rating due to the unsubstantiated reward model claim.

**Anchor papers used:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| OdoS6cH8MP (textual data valuation) | 2.00 | 1 | Much weaker topic, different paper type |
| EOPLy80bBm (data pruning) | 3.00 | 1 | Different scope, weaker paper |
| diKRhKs5yl (FEEDER) | 5.25 | 1,2 | Similar data selection scope, HES is stronger empirically |
| I5p1Gm8GFS (3DS) | 5.75 | 1,2 | Similar data selection type, HES is broader empirically |
| Fty0wTcemV (DELIFT) | 6.00 | 1,2 | Most comparable: data selection across stages/paradigms. DELIFT accepted; HES has weaker claim-evidence alignment |
| SpTzsQjgxF (Rule-Based Rating) | 5.75 | 2 | Different method (LLM-based rules + DPP), comparable quality |
| GtpubstM1D (JiuZhang-8B) | 5.71 | 2 | Analysis paper on math data, comparable quality |
| 1hQKHHUsMx (pretraining data for reasoning) | 6.75 | 2 | Different type (analysis/interpretability), higher score |
| che9LCwPQM (Gradient Trajectory Pursuit) | 4.75 | 2 | Different method (gradient-based), weaker quality |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>