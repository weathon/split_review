Now I have a thorough understanding of the paper and calibration anchors. Let me write the consolidated review.

---

## Summary

Steady Thought (ST) is a thought-level preference optimization framework that addresses "under-thinking" in Large Reasoning Models — the tendency to discover promising reasoning paths early but then switch away from them excessively. ST operates in three stages: (1) entropy-based segmentation of model responses into thought sequences, (2) thought completion by suppressing switch-trigger tokens (e.g., "wait," "alternatively") during decoding to generate committed completions, and (3) STPO, a SimPO-style preference optimization objective that trains the model to prefer committed completions over wasteful switching trajectories. Experiments across three model sizes (1.5B, 8B, 14B) and four benchmarks (MATH-500, AIME 2024, GSM8K, LiveCode) report accuracy gains up to 5.3% and token reductions of 19.0%–39.3%.

## Strengths

- **Consistent accuracy-efficiency gains across diverse model scales and tasks.** Across three base models of different sizes and four benchmarks spanning math and code, ST simultaneously improves accuracy (up to +5.3%) and reduces output length (up to −39.3%). The gains are not limited to in-domain math data — ST trained exclusively on math generalizes to code (LiveCode), with Qwen3-8B gaining +5.3% accuracy and −19.0% tokens, suggesting transferable reasoning patterns rather than dataset memorization.

- **The thought-level preference optimization (STPO) outperforms whole-response alternatives.** The ablation in Table 4 shows that STPO beats both SFT (which memorizes shortened outputs and underperforms) and DPO (which suffers from length bias when chosen/rejected pairs have stark length differences). This targeted comparison, though limited to the 1.5B model, provides evidence that thought-level, conditional preference optimization is better suited to the under-thinking problem than holistic alternatives.

- **Empirically motivated problem framing.** Figures 1a–1b provide concrete evidence for the under-thinking phenomenon: models often find a correct thought early (low-rank position) yet continue with numerous additional switches. This grounds the paper's approach in an observable behavioral pattern rather than a purely conceptual claim.

## Weaknesses

### Fatal

None.

### Major

- **Training data construction via logit suppression is a significant methodological concern, though not fatal.** In the Thought Completion stage (Section 3.2), the method forcibly suppresses the logits of switch-trigger words during decoding to generate committed completions \(T_i'\). These forced completions are then used as the "chosen" response in preference optimization. The suppressed decoding constitutes an artificial intervention — the generated completions would not occur under natural decoding. The paper verifies these completions only by final-answer correctness, not by logical soundness or coherence of the intermediate reasoning. If the suppression produces completions that reach the right answer through superficial or unsupported leaps, the preference optimization signal is training the model toward potentially shallow reasoning patterns. This concern is mitigated by two factors: (a) the suppression is used only during training data generation, not at inference (the optimized model reasons without any logit manipulation), and (b) the consistent downstream accuracy improvements suggest the completions carry useful signal. However, without a quality evaluation of the forced completions (beyond final-answer correctness) or an ablation showing that unsuppressed completions from promising thoughts also work, the concern remains open.

- **Primary comparisons against test-time-only baselines do not isolate ST's contribution.** The main baselines (NoThink, NOWAIT, SEAL) are test-time-only methods with no additional training, while ST undergoes training on thousands of in-domain math problems. Any fine-tuning on domain-relevant data can improve performance and alter output length. The paper includes a training-method ablation (SFT vs. DPO vs. STPO) in Table 4, which partially addresses this, but only for the 1.5B model on two datasets. For the 8B and 14B models that anchor the headline claims, there is no comparison against a trained baseline (e.g., DPO or SimPO on full-trajectory preference pairs constructed from the same data). This makes it impossible to attribute the gains specifically to ST's thought-level design rather than to training in general, for the larger models.

### Minor

- **Entropy-based thought segmentation lacks external validation.** The segmentation (Section 3.1) uses a fixed entropy threshold tuned for downstream performance (Section 4.4.3). There is no comparison with human-annotated thought boundaries or alternative segmentation schemes. The behavioral analyses in Sections 4.4.1–4.4.2 (number of thoughts, proportion of last thought, percentage of correct intermediate thoughts) all depend on this unsupervised segmentation. If the segmentation is unreliable, these analyses may reflect measurement artifacts rather than genuine behavioral changes. The post-training model likely has different token distributions and hence different entropy patterns, making before-vs-after comparisons using a fixed threshold potentially confounded. The method's downstream success provides implicit validation, but the analyses would be strengthened by segmentation robustness checks.

- **The Steadiness Score formalism (Section 2.1) is disconnected from the actual optimization.** Section 2.1 motivates the problem through a latent Steadiness Score and Bradley-Terry model. However, the STPO loss (Equation 7) is simply SimPO applied to conditional log-probabilities — no explicit steadiness score is estimated or used. The formalism over-promises relative to what the method delivers, creating a gap between the conceptual framing and the technical implementation.

- **SFT baseline in Table 4 uses an artificially disadvantaged setup.** The SFT baseline trains on the shortened, suppression-induced completions as targets, which the paper itself acknowledges leads to memorization of short outputs. A fairer SFT baseline would train on the full correct solutions from the original data, which would help distinguish whether preference optimization is genuinely necessary or whether standard SFT on correct solutions could achieve similar gains.

- **The "Overall" column in Table 1 averages across datasets of very different sizes and difficulty levels** (e.g., 30-problem AIME vs. 1,319-problem GSM8K), which can mask per-dataset regressions (e.g., the 1.5B model loses 0.6% accuracy on GSM8K while the Overall shows a gain). The per-dataset results are clearly presented, so this is a presentational rather than evidential issue.

### Trivial

- The set of suppressed trigger words ("wait," "alternatively") is acknowledged as predefined and is clearly incomplete as a comprehensive list of switching signals (Section 3.2). This is a minor hand-engineering limitation that the paper is transparent about.
- When the original model response is correct but contains switching, there is ambiguity in whether subsequent thoughts should be treated as "rejected" (Section 3.3). The paper does not discuss how such edge cases are handled.

## Nice-to-Haves

- **Quality evaluation of forced completions.** Report automatic or human assessments of the logical soundness of \(T_i'\) completions beyond mere final-answer correctness, to address the concern that suppression-induced completions may contain unsupported reasoning leaps.
- **Variance reporting.** The paper takes multiple runs for AIME 2024 (8 runs) and LiveCode (2 runs) but reports no standard deviations or confidence intervals. For small datasets like AIME 2024 (30 problems), variance information would help readers assess reliability of the reported gains.
- **Trained baselines for all model sizes.** Extend the DPO/SimPO baseline comparison in Table 4 to the 8B and 14B models, using preference pairs constructed from the same training data, to isolate the contribution of ST's thought-level design.
- **Ablation on the logit suppression itself.** Generate completions without suppressing switching tokens (letting the model continue naturally from \(T_i\)) and check whether those trajectories also frequently lead to correct answers, to test whether the suppression is actually necessary for generating useful training data.

## Removed Points

These points are flagged to be removed — treat them with caution.

1. **"Structural: The training data construction (Thought Completion) relies on an artificial intervention that invalidates the method's core mechanism"** — softened and retained as a Major weakness rather than fatal. The suppression is used only during training data generation, not inference, so it does not "invalidate" the method, but the concern about completions being artificial remains valid.

2. **"No variance, confidence intervals, or significance tests"** — moved to Nice-to-Haves. Multiple runs are taken (8 for AIME, 2 for LiveCode), and requesting CI/statistical tests for this type of benchmark evaluation is not universally standard. However, it would improve the paper.

3. **"The scatter plots show negative correlation but this doesn't demonstrate under-thinking"** — weakened. The paper explicitly acknowledges that some switching is necessary (Introduction: "potentially limiting the model's flexibility to explore alternative reasoning thoughts when necessary"), so it does not claim all switching is wasteful. The scatter plots serve as motivation, not proof.

4. **"Section 4.4.1: post-training model has different entropy patterns, invalidating before-vs-after comparison"** — retained but folded into the Minor weakness about segmentation validation rather than treated as a separate fatal issue.

5. **Pure formatting/style nitpicks** — removed per hard rules.

6. **Missing appendix / missing proofs / absent references concerns** — removed per hard rules. The parser strips appendix sections; they exist in the original submission.

7. **"The set of suppressed tokens is clearly incomplete" / hand-engineering concerns** — kept as Trivial since the paper is transparent about this limitation.

## Novel Insights

The paper's framing of under-thinking as a preference optimization problem at the thought level — specifically, treating the divergence point after a promising thought as the optimization juncture — is a useful conceptual contribution. Rather than globally suppressing switching behavior (as prior work does), ST targets the specific decision point where a model should commit versus explore, preserving flexibility while encouraging depth. The empirical finding that thought-level conditional preference optimization (STPO) outperforms both SFT and whole-trajectory DPO, even when the chosen/rejected pairs have extreme length differences, provides evidence that SimPO's length normalization is particularly well-suited to this setting.

## Suggestions

- The paper would benefit from a clearer separation between (a) the training-data generation pipeline (which uses logit suppression as a tool) and (b) the final inference behavior (where no suppression is used). This distinction is currently present but could be made more prominent to preempt the natural concern about artificial completions.
- Include a small human evaluation or case study showing side-by-side examples of a forced completion \(T_i'\) versus the original subsequent thoughts \(T_{i+1},...,T_n\) for both a success and failure case, to let readers judge whether the chosen completions represent genuine "deeper commitment" or shortcuts.
- The entropy segmentation threshold is tuned once per model. Consider reporting whether the optimal threshold changes after training, which would help address the confound concern in the behavioral analyses.

## Score and Decision

**Calibration anchors considered:**

| Path | Avg Score | Decision | Comparison to current paper |
|------|-----------|----------|----------------------------|
| `IaEqjWXd1d` (AceReason-Nemotron 1.1) | 6.50 | Accept (Poster) | AceReason has far more thorough experiments (systematic SFT-RL synergy study, comprehensive ablations, SOTA results). ST has a novel angle but less experimental depth. ST is clearly below this. |
| `N5kWa3sRJt` (OptimalThinkingBench) | 5.33 | Accept (Poster) | This benchmark paper was accepted with a wide score spread (2,8,6). ST has similar strengths (clear motivation, useful contribution) and similar weaknesses (methodological concerns, incomplete validation). Comparable quality. |
| `FUp0KeEEBs` (Preference Data for Alignment) | 5.50 | Accept (Poster) | Well-executed preference optimization paper with strong empirical coverage. ST has a more novel problem framing but weaker experimental validation. Slightly below. |
| `TMgONf7crm` (THINK-Bench) | 4.50 | Reject | Benchmark paper with evaluation framework. ST has more methodological contribution (proposes and validates a method, not just evaluation). ST is stronger. |
| `WOIf5MGJXB` (ESTAR) | 3.50 | Reject | Similar topic (reasoning efficiency). ESTAR has narrower model coverage and significant presentation issues. ST has broader experiments and clearer writing. ST is clearly above. |
| `esXvdhwUQ5` (Token Bayesian Optimization) | 3.50 | Reject | Test-time method with weaker results. ST trains models and shows consistent improvements. ST is above. |
| `5iuWQAWcob` (Self-Guided Thinking) | 3.00 | Withdrawn/Reject | Similar theme (when to think). SGT has limited backbone diversity and missing baselines. ST covers 3 model sizes and 4 benchmarks. ST is above. |
| `STqzFFKyuV` (Adaptive Margin RLHF) | 3.50 | Reject | Different topic. ST has stronger empirical results. |

**Scoring rationale:**

- **Strengths that lift the score relative to anchors:** The consistent accuracy-token improvements across 3 model sizes and 4 benchmarks, including OOD generalization to code, demonstrate a robust empirical signal that the rejected papers in the anchor set (ESTAR at 3.50, TBO at 3.50, SGT at 3.00) do not match. The STPO ablation (Table 4), though limited to 1.5B, provides targeted evidence that thought-level preference optimization is better than alternatives — a contribution-level signal. These strengths pull ST above the 3.0–4.0 band.

- **Weaknesses that cap the score:** The major weakness — training data constructed through logit suppression with no quality validation beyond final-answer correctness — means the core mechanism is not fully validated. The primary baseline comparisons are against test-time-only methods, and the training-method ablation is not extended to larger models. These gaps prevent full confidence in the headline claims and keep ST below the 6.0+ band occupied by papers like AceReason (6.50), which has comprehensive ablations across all experimental dimensions. The paper sits in the borderline zone: a clear contribution with non-trivial methodological concerns.

ST is stronger than the rejected papers in the anchor set (which typically have narrower experiments, weaker results, or more fundamental flaws) but has gaps that prevent the level of confidence associated with clear accepts at 6+. It is comparable to OptimalThinkingBench (5.33) in having a clear, well-motivated contribution with some methodological questions that reasonable reviewers could disagree about.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>