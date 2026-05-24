## Summary

DeepScientist is an LLM-based multi-agent system that iteratively discovers improved methods on challenging AI tasks. Operating over month-long runs with a persistent Findings Memory, it generated ~5,000 ideas, validated ~1,100, and produced methods that surpass human-designed SOTA on agent failure attribution (up to 183.7% relative accuracy improvement), LLM inference acceleration (+1.9% tokens/second), and AI text detection (+7.9% AUROC, +190% latency reduction). Five autonomously generated papers received human expert ratings averaging 5.00 (ICLR 2025 average: 5.08). The system's progressive discovery trajectory in text detection — from T-Detect to TDT to PA-TDT — demonstrates genuine self-directed conceptual advancement.

## Strengths

- **First large-scale empirical demonstration of an autonomous system progressively advancing SOTA on real, high-cost AI tasks.** The paper reports 20,000+ GPU hours of computation, ~5,000 ideas, ~1,100 implementations, and 21 progressive findings across three tasks with independently strong baselines (ICML 2025 Spotlight, ACL 2025 Outstanding, ICLR 2024). The scale and scope go well beyond prior AI Scientist systems that operate on synthetic or narrowly-scoped problems.

- **The progressive discovery trajectory on AI text detection is compelling.** The system produced three methods (T-Detect → TDT → PA-TDT) that shift the paradigm from global distributional statistics to non-stationary time-frequency analysis. Each method explicitly addresses a limitation of its predecessor, demonstrating self-directed conceptual advancement beyond random search or incremental optimization. Figure 5's t-SNE visualization and the paper's narrative support this claim.

- **Generated papers received human expert ratings comparable to ICLR 2025 submissions.** Three reviewers (including an ICLR Area Chair) gave DeepScientist's papers an average rating of 5.00, matching the ICLR 2025 average of 5.08, with inter-rater reliability α = 0.739. Two papers scored 5.67, exceeding the human average. This provides credible evidence that the system's outputs have genuine scientific value beyond what automated metrics can capture.

- **Quantitative bottleneck analysis provides actionable insights for the field.** The analysis of 300 failed implementations attributing 60% to implementation errors and 40% to non-improving results is a concrete contribution. It surfaces the correct bottleneck — code generation quality, not scientific reasoning — which directly guides future work on AI Scientist systems.

## Weaknesses

### Fatal
None.

### Major

- **The "Bayesian Optimization" framing does not match what is actually implemented.** The paper formalizes discovery as a Bayesian Optimization problem (Section 3, Equation 1, repeated references to "Bayesian surrogate model"), but the surrogate is an LLM prompted to output three integer scores (v_u, v_q, v_e ∈ [0,100]), with no probabilistic model, no posterior over the value function, and no uncertainty quantification in the statistical sense. The acquisition function is UCB applied to these deterministic scores. This is a heuristic search policy with UCB-inspired selection, not Bayesian Optimization. The core system — LLM-driven iterative search with Findings Memory — is valuable and does not need this framing. The mismatch undermines confidence in the paper's presentation of its methodology.

- **The "comparable to three years of human research" claim is misleading.** Figure 1 shows human progress from ~0.66 AUROC (2019) to ~0.80 (2024), while DeepScientist goes from ~0.79 to ~0.86 in 15 days. DeepScientist started from the 2024 SOTA (Binoculars, ~0.80) that the human community produced. Its 0.06 AUROC improvement over 15 days is compared against the cumulative 0.14 AUROC from the entire research community over ~5 years that established the baseline. The framing conflates incremental improvement from a strong starting point with the foundational work that created that starting point. The underlying achievement — improving on a competitive 2024 SOTA in two weeks — is impressive on its own and should be presented as such without the apples-to-oranges temporal comparison. This same concern applies to the 183.7% improvement headline, which is a large relative gain on a baseline of 12.07% accuracy — the paper does not explain why 12% is a competitive SOTA for this task, nor does it report chance level. The absolute performance remains low (29.31% and 47.46% accuracy).

- **The "near-linear scaling law" claim is unsupported.** Figure 6 shows 5 data points (1, 2, 4, 8, 16 GPUs) with values 0, 0, 1, 4, 11 — small integer counts with no error bars, confidence intervals, or multiple trials. The single "Overall" series sums across tasks, conflating task-specific differences. A claim of a "near-linear relationship" (Section 4.3 and Figure 6 caption) is not warranted from these data. The finding that more GPUs yield more discoveries is not surprising; the specific functional form claim is not supported.

### Minor

- **The 1.9% improvement in inference acceleration (190.25 → 193.90 tokens/second) lacks any statistical testing.** No confidence intervals, standard deviations, or significance tests are reported. Given the small effect size, it is unclear whether this improvement is real or within measurement noise. The text states the task as "highly optimized," making small gains harder to attribute.

- **The selection weighting (w_u = w_q = κ = 1) is not ablated.** The paper states "ablations" after describing the equal-weight configuration but does not actually show a comparison against alternative weightings in Figure 4(b) — that figure compares "with Selected" vs random selection, not different weighting schemes. The ablation of the acquisition function's exploitation-exploration balance, which is central to the claimed methodological innovation, is absent.

- **Automated review uses a system from the authors' own group.** Table 2 uses DeepReviewer-14B (Zhu et al., 2025a), developed by the same research group. While the paper also provides human evaluation, the automated comparison against other AI Scientist systems would be more credible with an independent review system. The 60% vs 0% accept rate for DeepScientist relative to others should be interpreted with this confound in mind. (The human evaluation in Table 3 partially addresses this concern.)

### Trivial

- The visual legend in Figure 4(a) is difficult to read; the bar chart text mentions values like "7 total, 600 progress, 2,472 implemented" that could be more clearly annotated.

## Nice-to-Haves

- **Compare against simpler selection strategies.** The current ablation ("w/o Selected" = random) is the weakest possible baseline. A comparison against a strategy that uses the same LLM scoring but picks only on v_u (utility) without v_e (exploration) would directly test whether the UCB-like exploration-exploitation balance adds value.

- **Add error bars or multiple trials to the scaling experiment.** Running the scaling study multiple times at each GPU count would turn the suggestive trend into a more reliable finding. The "near-linear" claim should be softened to "suggestive of a scaling trend" in the meantime.

- **Explain the agent attribution task's difficulty level.** The paper should clarify the task's chance accuracy (e.g., random guessing in the multi-agent failure log space), the number of agents and steps, and why 12.07% constitutes a competitive SOTA, since the absolute numbers are low.

## Removed Points

These points were flagged by reviewers but are removed or downgraded here for the following reasons:

- **"Human reviewers are from the same institution as the authors":** The paper text does not explicitly state the reviewers' institutional affiliations. This claim cannot be verified from the paper as written and is removed.
- **"t-SNE axes unlabeled":** The axes are labeled "t-SNE Component 1" and "t-SNE Component 2," which is standard for such plots. This is a trivial formatting complaint, removed.
- **"Parser garbled numbers in Figure 4(a)":** These are parsing artifacts from PDF extraction, not author errors. Removed.
- **"Smooth curve with only 4 data points":** This is standard visualization practice and not a meaningful weakness. Removed.
- **"Missing related work":** The meta-reviewer cannot verify the absence of related work without external sources. Removed per protocol.
- **Strength Finder's "Bayesian optimization with persistent Findings Memory"**: Given the verified BO framing issue, this claimed strength is in tension with the weakness and is removed.
- **Strength Finder's "Multi-LLM orchestration with role specialization"**: This is a design choice described in the paper, not a demonstrated strength over alternatives. Removed as generic.

## Novel Insights

Beyond the paper's own contributions, the reviews surface two observations not fully developed in the paper. First, the 60% implementation error bottleneck reveals that the system's scientific discovery capacity is fundamentally gated by LLM code generation reliability, not by reasoning or hypothesis quality. This shifts the key engineering question from "how to generate good ideas" to "how to reliably execute any idea" — a different challenge than most AI Scientist literature addresses. Second, the progressive discovery trajectory on text detection (T-Detect → TDT → PA-TDT) shows a pattern of conceptual paradigm shifts (global statistics → non-stationary signal analysis) emerging from a purely LLM-driven process. Whether this is a property of the underlying LLM's scientific knowledge or an emergent property of the iterative selection loop is an open question worth investigating.

## Suggestions

1. **Drop or rename the Bayesian Optimization framing.** Present the method for what it is: an LLM-based heuristic search with a UCB-like acquisition function and a persistent Findings Memory. The system's real contribution does not depend on the BO vocabulary.

2. **Reframe the "three years" and "183.7%" comparisons.** Present the improvements transparently: "improved from 0.80 to 0.863 AUROC in 15 days, starting from the 2024 SOTA" and "improved from 12.07% to 29.31% on a challenging multi-agent attribution task." Let the reader assess the significance without inflated framing.

3. **Add statistical rigor to the inference acceleration result** (confidence intervals or standard deviations) and **error bars to the scaling experiment** (multiple trials at each GPU count).

4. **Explain the agent attribution task's difficulty** (chance level, number of agents/steps, why 12% is competitive) so the reader can properly interpret the improvement magnitude.

5. **Ablate the acquisition function weighting** (vary w_u, w_q, κ or compare UCB against alternative selection strategies) to substantiate the claim that the exploration-exploitation balance matters.

## Score and Decision

**Calibration summary:**

*Round 1 (Bracketing):* Searched for AI scientist / automated scientific discovery papers. Weak band (avg < 3.5): FIRE-Bench (3.00), WetBench (2.00), Toward Experiment-Guided Hypothesis Ranking (2.67) — all rejected. Middle band (3.5–7.5): SR-Scientist (6.00, Accept Poster), Hypothesis Hunting (4.50, Reject), OSCAgent (4.50, Reject), PiFlow (5.00, Reject), LGBO (5.00, Accept Poster). Strong band (>7.5): Gaia2 (8.00, Accept Oral), La-Proteina (8.00, Accept Poster) — these are top-tier papers on different topics. Initial bracket: 4.5–6.5.

*Round 2 (Narrowing):* Searched same topic area within (4.5, 7.5). Returned anchors including SLDAgent (6.67, Accept Poster), PiFlow (5.00, Reject), NewtonBench (5.00, Accept Poster), LGBO (5.00, Accept Poster), SR-Scientist (6.00, Accept Poster). DeepScientist has broader scope and larger-scale real-task validation than PiFlow (rejected) and OSCAgent (rejected). It is comparable in ambition to SR-Scientist and SLDAgent but has more significant overclaiming/presentation issues than either. The core experimental results are real and impressive, placing the paper clearly above the reject-tier papers (~4.5–5.0) but below the cleanly-presented accept-tier papers (~6.0–6.67) due to the framing issues detailed above.

*Final score:* **5.5** — the paper makes genuine contributions (large-scale autonomous discovery on real tasks, progressive trajectory on text detection, competitive human evaluation) that warrant consideration, but the Bayesian Optimization mislabel, unsupported scaling claim, and misleading temporal/incremental comparisons significantly undermine the presentation and must be corrected.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>