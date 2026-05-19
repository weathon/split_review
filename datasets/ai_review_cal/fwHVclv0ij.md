- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 3, 6, 6
Now I have a thorough understanding of the paper and both reviews. Let me compose the final consolidated review.

---

## Summary

This paper proposes an online change-point detection method for black-box LLMs, where the detector has only query access (no model parameters or output log-probabilities). The method combines CUSUM-type detection statistics based on entropy and Gini coefficients (both first-token and N-token variants) with a UCB-based adaptive prompt selection strategy to focus queries on change-sensitive prompts. The approach is evaluated on synthetic watermark and model-version-change scenarios as well as on real-world data collected from 9 LLM APIs over three months, successfully detecting an officially announced Mistral update and flagging two unconfirmed changes in other APIs.

---

## Strengths

1. **CUSUM-type statistics from entropy and Gini, computable from black-box responses.** The method derives detection statistics (FTE, FTG, NTE, NTG) that can be computed purely from sampled token strings, without requiring model parameters or output log-probabilities (Section 3.1). This directly addresses the black-box limitation that rules out white-box methods and likelihood-ratio tests.

2. **UCB-based adaptive prompt selection demonstrably improves detection efficiency.** The algorithm actively selects change-sensitive prompts via an upper-confidence-bound rule. Experiments show it converges to the correct subset (prompts 8, 9, 10, 12, 13 in the version-change experiment, Figures 5a–b) and achieves lower average detection delay than random selection (Figure 6b). This is a novel and well-motivated adaptation of bandit ideas to online LLM change detection.

3. **Real-world detection on live APIs including a confirmed change.** On data from 9 LLM APIs collected over three months, the method detects the officially announced Mistral update on July 24, 2024 (Figure 7), demonstrating practical viability beyond synthetic benchmarks (Section 4.2). This is a non-trivial validation that many similar papers lack.

4. **Controlled synthetic validation covering two distinct change types.** Watermark emergence (soft watermark with δ=2, γ=0.5) and model version transitions (facebook/opt-125m → opt-350m) are both simulated. The detection statistics show the expected behavior — near zero before the change and linear growth after (Figures 3, 4) — supporting the claim that the method generalizes across different kinds of distribution shifts.

5. **Clear problem formulation with realistic constraints.** The setup explicitly accounts for a query budget K, unknown pre/post distributions, unknown change point ν, and the fact that prompt sensitivity varies (Section 2). The use of historical data for normalization and the ADD/ARL performance criteria provide a principled framework aligned with real-world LLM API monitoring.

---

## Weaknesses

### Fatal
None.

### Major

1. **N-token pooled approximation is unvalidated as a proxy for joint-distribution entropy/Gini.** The paper formally defines NTE and NTG based on the joint distribution P(z₁,…,z_N|x) (Section 3.1), but in implementation (Section 3.2) replaces this with the empirical distribution of *all* first-through-Nth tokens pooled across C responses — which is a marginal distribution across positions, not the joint distribution. The paper acknowledges this is "different from the joint distribution" but provides no analysis, theoretical reasoning, or even a small-scale toy experiment to justify that this pooled statistic preserves sensitivity to the same changes. The sole justification is "Through our experiments, we find that setting N=C=20 leads to appealing performances." This gap weakens the paper's core technical contribution: readers cannot tell whether the reported results reflect the claimed joint-distribution metrics or an unrelated proxy. The metrics should be renamed (e.g., "pooled token entropy") or accompanied by evidence linking the pooled statistic to the joint distribution.

2. **Evaluation lacks comparisons to alternative detection methods.** The only comparison made (Figure 6b) is between adaptive selection, random selection, and individual prompts — a comparison of *selection strategies*, not of the detection method itself. No baseline detection method is evaluated: not a simple CUSUM on average token frequency, not perplexity-based detection (even if requiring white-box access for verification of assumptions), not a fixed non-adaptive prompt strategy, not even a basic threshold on the raw metrics without CUSUM accumulation. While the paper identifies a relatively new problem where off-the-shelf methods may not exist, the absence of *any* alternative detection baseline makes it hard to assess the added value of the proposed pipeline over simpler approaches.

### Minor

3. **No false-alarm characterization on real-world data.** The real-world experiment (Section 4.2) shows one confirmed detection and two unconfirmed ones, but never reports false-positive behavior. The method could have raised alarms at many other time points; without showing the detection statistic trajectories over a long presumed-stable period (or reporting empirical false-alarm rates under a null of no change), the claimed "strong evidence" for unconfirmed changes is unsubstantiated. The detection threshold choice for real data is also not specified or justified.

4. **Drift parameter d=0.5 is used uniformly without sensitivity analysis.** The paper sets d=0.5 for all metrics and all experiments but does not explain how this value was chosen, whether it is appropriate after normalization, or how sensitive the results are to this choice. A brief ablation study would substantially strengthen the paper.

5. **No evidence that the four parallel metrics are complementary.** The paper motivates monitoring all four statistics by stating "not all changes can be effectively captured by the distribution of the first token," but never shows a concrete scenario where FTE/FTG fail while NTE/NTG succeed (or vice versa). Without such evidence, the parallel-monitoring design feels like over-engineering rather than a principled choice.

6. **The UCB reward design is not analyzed under no-change conditions.** The reward is defined as the increment in the max-of-four detection statistic W(t;x). When no change has occurred, these increments oscillate near zero and the UCB scores may drift randomly. The paper does not discuss or analyze whether the selection module can itself trigger false alarms by focusing on prompts with larger random fluctuations.

### Trivial

- ADD values in Figure 6b are reported as averages of 20 runs without confidence intervals or standard errors, making it impossible to assess the variability of the comparison.
- The phrase "strong evidence" for unconfirmed changes (Section 4.2) overstates what a single detection statistic trajectory can establish without false-positive control.

---

## Nice-to-Haves

- A small-scale toy-vocabulary experiment comparing the true joint-distribution NTE/NTG against the pooled approximation would clarify the relationship between the two and is the most straightforward way to address Weakness 1.
- Adding perplexity or average token log-probability as a baseline (even if requiring white-box access in a simulated setting) would contextualize the method's performance.
- Reporting the threshold calibration procedure and resulting ARL values for the real-world experiments would greatly improve reproducibility and trust in the unconfirmed-change claims.
- A brief note on computational cost (the method requires computing empirical entropy/Gini over C responses per selected prompt per round) would help practitioners assess deployment feasibility.

---

## Removed Points

These points were removed from the review with justification:

- **"Prompt set (Table 1) not listed in the paper body"** — Tables and appendices exist in the original submission; the parser strips these. Not a valid criticism.
- **"Missing related works"** — Per guidelines, the reviewer cannot confirm missing citations exist.
- **"Missing appendix, missing proofs in appendix"** — Parser strips appendix content; not an author error.
- **"No analysis of computational cost"** — This is a minor omission but more of a nice-to-have than a weakness. Moved to Nice-to-Haves.
- **"No comparison to existing methods" framed as fatal** — The problem is relatively new and the paper does compare adaptive vs random selection; reframed as Major weakness 2 with appropriate nuance.
- **Generalized area-of-concern sweeps** (e.g., "evidence is weak for the claims" without specific anchor, "could the metric be measuring a proxy?" without specific evidence) — removed as they lack concrete anchors in the paper.
- **"Shows a failure case for FTE/FTG that NTE/NTG catches"** — A nice-to-have but not a required part of the contribution.
- **Pure formatting/style nitpicks and typo claims** — These are parser artifacts or not meaningful.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews are largely consistent in what they identify as strengths and weaknesses; the harsh critic correctly identifies the N-token approximation gap and the evaluation limitations, while the strength finder correctly identifies the method's novel framing and real-world validation. The novel insight from synthesizing both is that the paper's core contributions (black-box CUSUM + adaptive selection) are independently valuable and survive the critique of the N-token approximation — the approximation is a presentation/justification gap, not a fatal flaw, because the method demonstrably works in experiments regardless of what name is used for the N-token metric.

---

## Suggestions

1. Rename the N-token metrics (e.g., "Pooled Token Entropy" and "Pooled Token Gini") to accurately reflect what is computed, and add a small-scale experiment or theoretical argument connecting the pooled statistic to the joint distribution it approximates.
2. Include at least one simple detection baseline: a CUSUM on the raw empirical frequency of the most common token(s), or a CUSUM on average token log-probability in a controlled synthetic setting.
3. Report the false-alarm rate or ARL for the real-world experiments by running the detector over a long stable period (e.g., the first 20 days of each API before any known change).
4. Add a sensitivity analysis for the drift parameter d (e.g., vary d in {0.1, 0.3, 0.5, 0.7, 1.0}) to show robustness.
5. Show at least one case where FTE/FTG fail to detect a change that NTE/NTG detect (or vice versa) to justify parallel monitoring of all four statistics.
6. Add confidence intervals or error bars to the ADD-ARL curves in Figure 6b.

---
