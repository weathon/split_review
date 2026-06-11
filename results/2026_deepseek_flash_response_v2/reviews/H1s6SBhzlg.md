## Summary

This paper proposes two aggregation methods for combining LLM responses: Optimal Weight (OW), a Bayesian-optimal linear weighting scheme using first-order accuracy information, and Inverse Surprising Popularity (ISP), a second-order correlation-based method. The paper provides theoretical guarantees (Theorems 1–3) showing OW is optimal among all aggregators and ISP provably outperforms majority voting, and validates the methods across simulated data, UltraFeedback, MMLU, and a real-world healthcare dataset (ARMMAN). The core contribution is a principled information-theoretic framework for LLM aggregation that goes beyond standard majority voting.

## Strengths

- **Theorem 1 (Bayesian optimality among all aggregators):** The paper proves that the proposed OW weighting scheme attains maximal expected accuracy among *all* possible aggregation functions (not just linear ones) under conditional independence (Section 3, line 86). This is a non-trivial guarantee absent from most weighted voting schemes in the LLM literature.

- **Theorem 2 (closed-form expressions ranking ISP, MV, SP):** The paper derives exact formulas for the expected advantage of ISP over MV and MV over SP, with interpretable dependence on accuracies, number of agents N, and number of choices K (lines 207–215). The Θ(1/K) scaling of ISP's advantage is a clean theoretical prediction that experiments confirm.

- **Theorem 3 (finite-sample guarantee):** The paper bounds the degradation from estimated second-order information with an Õ(√(1/M log(1/δ))) penalty (lines 229–235), providing a non-vacuous statistical guarantee not available for most voting-based LLM aggregation methods.

- **Principled motivation for ISP:** The paper diagnoses *why* the surprisingly popular (SP) rule underperforms MV for LLMs (systematic biases that SP exploits in human crowds are weaker in LLMs) and designs ISP to invert the bias, yielding provable improvement over both MV and SP (Section 4.1–4.2).

- **Two unsupervised pipelines (OW-L, OW-I):** Since accuracies (first-order information) require ground-truth labels unavailable in practice, the paper shows how to estimate them from second-order information via ERM (OW-L) or ISP pseudo-labels (OW-I), bridging the gap between theory and practice (Section 5.2).

- **Empirical validation on a real-world healthcare task (ARMMAN):** The methods improve accuracy from 85.24% (MV) to 85.78% on a maternal health dropout prediction task, with t-statistic 3.22, demonstrating deployable value beyond standard NLP benchmarks (Table 3).

## Weaknesses

### Major

- **OW-L and OW-I produce identical results without explanation:** In Table 3, OW-L and OW-I achieve exactly the same accuracy on all three datasets (73.66%, 90.37%, 85.78%). Table 4 shows they make identical per-question predictions (same discrepancy counts: 2545/1727, 1821/659, 264/195). Since OW-L solves an ERM problem over the second-order correlation matrix (Eq. 7) while OW-I uses ISP outputs as pseudo-labels (Section 5.2), these are fundamentally different estimation procedures. The paper does not discuss this convergence, leaving the reader to question whether this is a reporting artifact, a pipeline bug, or a genuine property that should be analyzed. On ARMMAN, even ISP matches at 85.78%, further compounding the concern. While this does not undermine the ISP vs. MV comparisons (which show distinct, consistently different numbers), it weakens the paper's claim that OW-L and OW-I are meaningfully distinct approaches.

### Minor

- **No variance or uncertainty reported for experimental results:** Tables 2 and 3 report single-point accuracy numbers without error bars, standard deviations, or confidence intervals. For improvements of 0.5–1.5% absolute, it is difficult to assess stability. The reported t-statistics (12.53, 23.39, 3.22) lack accompanying p-values, degrees of freedom, or a description of the test structure (paired? per-question? across model ensembles?), reducing the interpretability of the significance claims.

- **Theorem 2 proves ordering of expected advantage, not expected accuracy:** The paper proves ISP > MV > SP in expected advantage for the true label. Since all three methods select the arg max of their advantage, a higher expected advantage is suggestive of higher accuracy, but the theory section does not formally bridge this gap. The experiments measuring accuracy partially address this, but the theoretical claim ("ISP outperforms MV") is slightly stronger than what is formally proven.

- **Sigmoid function inconsistency:** The abstract (line 25) defines σ_K(x) = x²/(K-1+x²), while Section 3 (line 73) defines it as σ_K(x) = eˣ/(K-1+eˣ). The main-body definition (eˣ) is correct and matches the standard logistic function in Corollary 1 for K=2; the abstract definition is a different function and should be corrected.

### Trivial

- Algorithm 1's arg max expression (line 82) has imprecise notation ("s ∈ Σ ..." where Σ is a summation operator, not a set). The intended meaning is clear from context.

## Nice-to-Haves

- Including a confidence-weighted aggregation baseline (weighting each LLM's vote by self-reported confidence, as noted in the related work) would strengthen the empirical positioning, though the paper's unsupervised setting (no ground-truth labels) differs from methods requiring confidence outputs.
- An analysis of robustness to violations of the conditional independence assumption (Assumption 1) in the real-world experiments would be valuable, since the paper acknowledges this assumption may not hold for LLMs.
- A practical recommendation for the number of questions M needed to stabilize second-order estimates would help practitioners apply the method.
- The paper could foreground the "disagreeing subset" results (2.78%, 3.36%, 1.16% gains) more prominently, as these are more meaningful than the full-dataset numbers where most questions have unanimous agreement.

## Removed Points

The following points from the source reviews were moved here with justifications:

1. **"Deeply suspicious / vanishingly improbable" characterization of OW-L/OW-I identical results** — The identical results are a genuine concern, but the framing as undermining *all* experimental credibility is too strong. The ISP vs. MV comparisons (73.26% vs. 72.21%, 90.01% vs. 89.32%, 85.78% vs. 85.24%) show different, consistent improvements. The concern is localized to OW-L vs. OW-I. The identical results *do* need explanation, but they do not invalidate the paper's core empirical claim.

2. **Missing confidence-weighted baselines as a major gap** — The paper scopes itself to the unsupervised setting without ground-truth labels. Confidence-weighted methods (Chen et al., 2023a; Fu et al., 2025) require LLMs to output confidence probabilities alongside answers, which is a different type of information in a different setting. The paper's central claim is about outperforming majority voting, and it does so consistently. Comparing against confidence-weighted methods would be informative but is not a standard baseline for this setting.

3. **Strawman claim about Algorithm 1 formatting as a "defect"** — Kept as Trivial; the intended expression is clear.

4. **Generic strengths from Strength Finder** (e.g., "addressed an important problem," "well-motivated") — Removed as they lack specific evidence anchors.

## Novel Insights

The most insightful observation emerging from the review process is that the paper's theoretical framework does double duty: it derives a Bayesian-optimal aggregator requiring first-order information (Theorem 1), then shows how to reconstruct that information from second-order correlations through two complementary pipelines (OW-L via ERM, OW-I via ISP pseudo-labels). This creates a natural hierarchy from zero-order (MV) → second-order (ISP) → first-order (OW) information, with diminishing returns at each level that the theory precisely characterizes (Θ(1/K) for the ISP improvement over MV). The healthcare application (ARMMAN) is a rare and welcome example of LLM aggregation research being validated in a real-world high-stakes setting rather than only on standard NLP benchmarks.

## Suggestions

1. **Explain the identical OW-L/OW-I results.** Either confirm they genuinely converge to the same predictions (and analyze why) or fix the reporting if this is an error. The per-question predictions being identical across thousands of questions is the most notable unresolved issue.

2. **Add error bars or distributional statistics.** Bootstrapped confidence intervals or results across multiple random splits would substantially strengthen the empirical claims.

3. **Clarify the hypothesis testing methodology.** Provide p-values, degrees of freedom, and describe whether the t-test is paired and across which units.

4. **Fix the sigmoid function definition in the abstract** to match Section 3 (eˣ form, not x² form).

5. **Discuss the practical implications of the Θ(1/K) gap in ISP's advantage over MV** more prominently — the method is most useful precisely when K is small (2–4), which covers many practical settings.

## Score and Decision

---

### Calibration Anchors

**Round 1 (Bracketing):**
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/yCEf1cJDGh.md` — *Truthful Aggregation of LLMs* (5.25) — Weaker incremental contribution, missing baselines, no theory. Our paper is stronger.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/WVWZ6SnM4t.md` — *RoundTable* (4.75) — Limited novelty, no theoretical guarantees. Our paper is stronger.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Dl6nkKKvlX.md` — *Balancing Act* (6.25) — Similar topic, weaker theory, SOTA on one benchmark. Our paper is slightly stronger.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/HSGCCUwH7r.md` — *Model Swarms* (6.75) — Different approach, no comparable theory. Not directly comparable.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/NN6QHwgRrQ.md` — *MAP* (8.00) — Different topic, much stronger paper. Our paper is weaker.

**Round 2 (Narrowing):**
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/grM2Yv49cI.md` — *Model aggregation: minimizing empirical variance* (6.00) — Weaker theory (no Bayesian optimality result), fewer experiments. Our paper is stronger in theory but has an unexplained experimental result.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/tbx3u2oZAu.md` — *Theory for Token-Level Harmonization in RAG* (6.00) — Different topic, similar rigor level. Comparable quality.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/33XGfHLtZg.md` — *Conformal Risk Control* (7.00) — Cleaner paper with strong theory and experiments. Our paper has more experimental gaps.

**Bracket progression:** Round 1 placed the paper in (5.5, 7.0). Round 2 narrowed to (6.0, 7.0). The 6.00 anchor (Model aggregation) has weaker theory and fewer experiments; the 6.25 anchor (Balancing Act) has comparable scope but weaker theoretical guarantees. The paper's theoretical depth (Theorem 1's Bayesian optimality among *all* aggregators) is stronger than typical 6.0 papers, but the unexplained OW-L/OW-I identical results prevent it from reaching 7.0. Final score: **6.5**.

**Round 1 bracket:** (5.5, 7.0)
**Round 2 narrowing:** (6.0, 7.0)
**Final:** 6.5 — The paper has genuinely strong theoretical contributions that elevate it above the 6.0–6.25 range, but the unresolved OW-L/OW-I identical results and lack of error bars keep it below 7.0.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>