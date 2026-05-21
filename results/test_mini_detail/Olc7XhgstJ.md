## Summary

This paper proposes Steady Thought (ST), a three-stage framework to mitigate "under-thinking" in large reasoning models—where models abandon promising reasoning trajectories too early. ST segments model responses into thoughts (via entropy-based segmentation), generates forced completions that suppress switching keywords, and performs thought-level preference optimization (STPO) that conditions on individual thoughts rather than entire responses. Experiments across three model scales (1.5B, 8B, 14B) and four benchmarks show accuracy improvements of up to 5.3% alongside token reductions of up to 39.3%, with behavioral evidence that the model commits more deeply to promising thoughts.

## Strengths

- **Novel and well-motivated formalization of under-thinking as a thought-level preference problem.** Section 2.1 cleanly defines commit vs. switch trajectories, and Section 3.3 derives STPO (Equation 7), a reference-free, length-normalized objective conditioned on a specific thought prefix. This is a principled departure from prior token-level or representation-level suppression methods that apply switching suppression globally.

- **Consistent empirical improvements across multiple model sizes and benchmarks.** Table 1 shows ST improves accuracy over vanilla models on 10 of 12 model×dataset combinations while simultaneously reducing output length. The improvements hold on LiveCode (an OOD code benchmark), which provides evidence that the method teaches a generalizable reasoning pattern rather than dataset-specific memorization.

- **Behavioral evidence supporting the claimed mechanism.** Figure 2 shows that ST increases the proportion of the final (answer-producing) thought substantially (e.g., 28.95% → 54.36% for DeepSeek-R1-Distill-Qwen-1.5B on MATH-500). Table 2 shows a reduction in correct intermediate thoughts that the model abandons, confirming more purposeful switching. Table 4 provides a clean ablation showing STPO outperforms both SFT and DPO on the same data.

- **Systematic threshold analysis.** Table 3 explores entropy threshold values (2.8, 3.0, 3.2) and documents their effect on segmentation granularity and downstream performance, supporting reproducibility.

## Weaknesses

### Major

- **No data contamination analysis despite likely training/test overlap.** The training set (omni-math) is a large collection of mathematical problems that almost certainly includes problems from MATH and past competitions. The test sets MATH-500 (a subset of MATH), AIME 2024, and GSM8K are standard benchmarks that have existed for years and are commonly included in large math corpora. The paper provides no decontamination procedure, no overlap analysis, and no discussion. While the OOD LiveCode results partially mitigate the concern (since ST improves on a code task despite training only on math), the math benchmark improvements remain uninterpretable without knowing the overlap rate. This is the most serious weakness — it directly affects the core empirical claims on three of the four evaluation datasets.

- **No statistical uncertainty or significance reporting.** AIME 2024 has only 30 problems; a single-problem shift changes accuracy by ~3.3%. MATH-500 has 500 problems but the paper reports only point estimates. For AIME, the paper averages 8 runs but reports no standard deviations, confidence intervals, or significance tests. Without this information, a claimed improvement of +3.7% on AIME (Qwen3-8B) or +5.3% on LiveCode could reflect sampling noise rather than a reliable gain. The paper should report at minimum bootstrapped confidence intervals.

- **Questionable baseline configurations.** NOWAIT suppresses specific trigger tokens (e.g., "wait", "alternatively"). On Qwen3-8B, NOWAIT collapses accuracy from 91.4% to 61.0% on MATH-500 and from 62.1% to 26.3% on AIME 2024 — a catastrophic degradation that suggests the suppression strength was grossly mismatched for this model. The paper provides no information about how baseline hyperparameters (NOWAIT's suppression strength, SEAL's steering coefficient α) were set or whether they were tuned per model. As presented, the baseline comparisons may substantially underestimate the relative performance of those methods.

### Minor

- **Entropy threshold analysis limited to one model size.** Table 3 reports threshold tuning only for DeepSeek-R1-Distill-Qwen-1.5B. The paper states in Section 4.4.3 that results for other models are in Appendix D (which is stripped), leaving the reader unable to assess whether the same threshold (3.0) is appropriate for 8B and 14B models or whether the method is sensitive to model scale. Given that this is a core hyperparameter, at least the main-text threshold analysis should span multiple models.

- **The entropy-based segmentation and analysis metrics use the same fixed threshold for both base and ST models.** Figure 2 and Table 2 report thought counts and proportions measured with the same entropy threshold on both vanilla and ST models. Because ST changes the model's token distribution, a fixed threshold may behave differently under the shifted distribution, confounding the comparison. A sensitivity analysis showing that the behavioral trends are robust across multiple threshold settings would strengthen the claims.

- **Potential unnaturalness of forced-completion trajectories.** The thought-completion stage (Section 3.2) suppresses switching keywords via logit manipulation to generate "chosen" trajectories. This forced decoding may produce unnatural or brittle continuations. The paper notes computational cost is discussed in an appendix but does not discuss the quality or naturalness of these forced completions. While the method only keeps completions that lead to correct answers, the risk remains that the model learns to imitate a style of reasoning that is effective only because it was force-generated rather than genuinely produced.

### Trivial

- None significant.

## Nice-to-Haves

- The paper could strengthen its claims by evaluating on a held-out math dataset that is known to be disjoint from omni-math (e.g., a newly curated problem set) rather than relying solely on the OOD LiveCode results.
- The latent "Steadiness Score" abstraction in Section 2.1 is conceptually elegant but not used operationally after the problem formulation is connected to DPO/SimPO. The paper could be simplified by directly stating the preference without this abstraction, though this is a presentation choice.

## Removed Points

These points were flagged by the reviewers but are removed from the main review with justification:

1. **"Demand for a larger dataset / more models"** — The paper already evaluates on 3 model sizes and 4 datasets, which is adequate for the scope. Generic requests for more is scope creep.
2. **"Missing related works"** — Cannot be verified without external knowledge. The paper's related work section covers over-thinking, under-thinking, and preference optimization adequately.
3. **"Reproducibility concerns about undisclosed hyperparameters"** — The paper describes the method clearly (entropy threshold, trigger words, preference optimization). Not listing every training detail is standard for a 9-page submission.
4. **"Missing appendix content / proofs"** — The parser strips these sections; they exist in the original submission.
5. **"Stylistic / formatting nitpicks"** — Parser artifacts, not author errors.
6. **"Concern that the method 'may overfit to a no-switching style'"** — This is speculation about a potential future issue, not a verified problem with the paper as presented.
7. **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem") — These are too generic to retain; only concrete, evidence-tethered strengths are kept.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the familiar tension between a cleanly-motivated method and incomplete experimental hygiene (missing decontamination, no significance testing). The most interesting observation from the cross-review analysis is that the baseline comparison concern (NOWAIT's extreme degradation) points to a broader methodological issue: papers that propose training-based methods often compare against inference-time baselines at a single, possibly suboptimal, configuration. This asymmetry could systematically overstate the advantage of the proposed method and deserves more attention in the community.

## Suggestions

1. **Add a decontamination analysis.** Compute n-gram overlap between the omni-math training set and each test set (MATH-500, AIME 2024, GSM8K). Report the overlap rate and, if any problems overlap, re-evaluate on a decontaminated subset. This is essential for the math benchmarks.
2. **Report statistical uncertainty.** Provide standard deviations or 95% confidence intervals (e.g., via bootstrapping) for all accuracy and token-count metrics, especially for AIME (30 problems) and LiveCode.
3. **Document baseline tuning.** Report how NOWAIT's suppression strength and SEAL's α were chosen per model. Show that the reported baseline results are near-optimal, or acknowledge that they serve as lower bounds.
4. **Include threshold tuning for larger models.** If the appendix contains these results and space is tight, at minimum summarize the findings (e.g., "the optimal threshold was also 3.0 for Qwen3-8B and 3.2 for DeepSeek-R1-Distill-Qwen-14B, with performance within X% of the optimum").
5. **Add a limitations section.** Explicitly discuss the risk of unnatural forced-completion trajectories and the assumption that correct-answer completions of suppressed-decoding runs reliably identify "promising" thoughts.

## Score and Decision

**Round 1 (Bracketing):** Three queries returned papers with avg scores 3.0 (weak), 4.75–6.5 (middle), and 8.0 (strong). The paper clearly falls in the middle band — the method and evaluation are substantially stronger than the weak-band papers (e.g., "Planning in Strawberry Fields" at 3.0), but not at the level of the strong-band papers (e.g., MetaMath at 8.0, WizardMath at 8.0). Initial bracket: **5.0–6.5**.

**Round 2 (Narrowing):** Anchors in the bracket:
- *TPO* (6.33, accept poster): Similar contribution (preference optimization for reasoning). TPO has a more complex framework but similar evaluation scope. SteadyThought has cleaner formalization but weaker experimental hygiene (no decontamination, no significance). Slightly below TPO.
- *Making LLMs Better Reasoners* (5.5, reject): Less novel. SteadyThought is more original and better motivated. Above this.
- *EURUS* (6.5, accept poster): Stronger paper with comprehensive evaluation and dataset contribution. SteadyThought is below.
- *LoT* (4.75, reject): Confused framing, unclear method. SteadyThought is clearly above.
- *PROFILE* (5.33, reject): Different area, comparable execution quality.
- *Self-Improvement Reversal* (6.5, accept poster): More rigorous analysis paper.

**Final calibration:** The paper is closest to TPO (6.33, accepted) but has more serious empirical gaps (no decontamination, no significance). It is stronger than the rejected anchor at 5.5 in terms of novelty and clarity but has experimental weaknesses that make it fall short of the acceptance bar in current form. Final score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>