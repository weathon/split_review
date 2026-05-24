Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper addresses the under-explored problem of length volatility in long-form LLM generation — the tendency of models to produce outputs of inconsistent length when given the same prompt multiple times. The authors make three contributions: (1) **VOLTBench**, a benchmark spanning unstructured and structured tasks in English/Chinese up to 100k words, with metrics (LSD, LVC, MLA) designed specifically to quantify multi-generation length volatility; (2) a **probing analysis** of attention traces that identifies "Attention Collapse" and "Attention Instability" as internal signatures preceding volatile outputs; and (3) **SELB** (Structural Enforcement via Logits Boosting), a training-free decoding strategy that enforces section structure and suppresses failure-mode tokens.

## Strengths

- **First benchmark to systematically operationalize length volatility as a core evaluation dimension.** VOLTBench introduces LSD, LVC, and MLA (Section 3.2), and Table 1 convincingly shows that no prior benchmark (HelloBench, LongBench, LongGenBench, etc.) checks "Multiple Sampling" or "Stability Eval." This fills a genuine gap — the community has no standard way to measure whether a model produces consistent outputs. The multi-dimensional design (structured/unstructured, English/Chinese, 5–100k words, simple/complex/fine-grained-constraint instructions) surfaces failure modes that single-prompt benchmarks miss.

- **Fine-grained constraint analysis provides precise, quantitative failure characterization.** Section 4.2 introduces character-level, keyword, and theme constraints embedded in prompts, enabling automatic quality assessment. Section 4.3.1 shows stark results: at 500 sections, no model delivered more than 40 correct constrained sections out of 100 required. This is a concrete, reproducible finding about current model limitations.

- **Comprehensive model zoo and baseline coverage.** Table 2 evaluates 9 diverse models (GPT-4o mini, Claude-3.5-Sonnet, Deepseek-R1/V3, Mamba-7B, Qwen2.5-1.5B/7B, Llama3.1-8B, LongWriter-8B) plus 4 decoding strategies on 6 metrics, providing a thorough empirical picture of the stability-quality-length trade-off landscape.

- **SELB achieves quantitatively large improvements in length adherence.** Even accounting for comparison issues (see Weaknesses), Figure 5 shows clearly that Qwen2.5-7B+Ours, Qwen3-8B+Ours, and Llama3.1-8B+Ours all track the target-length reference line far more closely than any baseline, with dramatically reduced variance.

## Weaknesses

### Major

- **Headline percentage claims compare SELB to a non-corresponding baseline, rendering the numbers in the abstract and conclusion misleading.** The abstract and conclusion claim SELB "improves the mean output length of the base model by 148% and reduces the length volatility by 69%." Section 6.3 reveals these percentages are computed against **LongWriter-8B** (mean length 6,320 words, LVC 45.4%), *not* against the model that SELB actually modifies. The proper comparison for, say, Qwen2.5-7B+SELB (mean ~15,651, LVC ~14%) would be Qwen2.5-7B alone (mean 445 words, LVC 17.0%), which gives a ~3,400% length increase and a ~17% volatility reduction — very different numbers. The term "base model" in the abstract is ambiguous: it could mean "baseline model" (LongWriter-8B) or "the underlying model SELB is applied to," and readers would reasonably assume the latter. The paper needs to: (a) clearly state which model SELB is applied to when reporting the 15,651-word / 14.02%-LVC results; (b) compute headline percentages relative to that same model's unmodified version; and (c) separately report comparisons to LongWriter-8B as an external baseline, not as "the base model."

- **The probing analysis claiming to identify "common internal patterns of length volatility" is too thin to support the weight placed on it.** The attention trace analysis (Section 5) examines only **two models** (Qwen2.5-7B, Qwen2.5-3B) on a **single task** (diary generation, 40 sections). The paper asserts Attention Collapse and Attention Instability are "common internal patterns" (line 246), but provides no statistical quantification: no frequencies across models, tasks, seeds, or volatility levels, no correlation coefficients linking trace features to volatility metrics, no evidence that these patterns occur beyond the two shown traces. This part of the three-stage contribution (benchmarking → probing → mitigation) is the weakest link; the narrative that SELB specifically targets these identified patterns is speculative given the evidence provided.

- **SELB's results are not placed in the main comparison table.** Table 2 lists 9 models and 4 decoding strategies across 6 metrics, but SELB is absent. Its results are reported only in separate text (Section 6.3) and a figure (Figure 5). This omission makes direct per-metric comparison against the baselines in Table 2 impossible in a single view. SELB for at least one base model should be added to this table.

### Minor

- **Missing ablation: what does SELB gain beyond hard-coded structural enforcement?** SELB combines (a) structural enforcement (forcing section transitions at `τ_max`, boosting title tokens) with (b) failure prevention (banning filler phrases, blocking early EOS). No baseline receives any equivalent structural hints. An ablation that compares "SELB without the proactive failure-prevention components" vs. "full SELB" vs. "a version of SELB that only enforces section structure without any logits-boosting" would isolate what the attention-analysis-motivated components add over simple rule-based enforcement. Without it, the critic's counterclaim that "the gains could be achieved by any hard-coded truncation and section-forcing routine" cannot be refuted from the paper as written.

- **Decoding baselines lack hyperparameter specifications.** Repetition Penalty, Entropy-Stopping, Length Constraint, and Lookahead Decoding (Section 4.1) are compared against SELB, but the paper does not report their hyperparameter settings (e.g., penalty strength, entropy threshold, lookahead window size) or describe whether these were tuned on a validation set. This makes the comparison difficult to reproduce and raises the question of whether the baselines were used in their strongest configurations.

- **5 runs per condition for volatility measurement.** LSD and LVC are computed over N=5 generations. For a metric designed to measure *stability*, 5 samples provide only a coarse estimate of the standard deviation. While larger N is computationally expensive at 100k-word outputs, the paper should acknowledge this limitation and ideally provide a pilot study or bootstrapped confidence intervals to justify that 5 runs yield stable estimates.

- **Section 5 references the wrong figure.** The probing analysis text says "As shown in Figure 2" (the benchmark overview) when it clearly refers to the attention trace plots (Figure 4). This is a minor presentational error but creates confusion for the reader trying to follow the analysis.

### Trivial

- The paper uses "our model" throughout Section 6.3 without specifying which base model SELB is applied to for the reported numbers (15,651 words, 14.02% LVC, 78.25% MLA). From Figure 5, SELB is applied to three models; the paper should state explicitly which one produced these figures.

## Nice-to-Haves

- **Stronger probing analysis.** The attention-trace analysis could be substantially strengthened by (a) computing correlations between trace features (e.g., peak frequency, post-peak attention drop rate) and output volatility metrics across many seeds and tasks, and (b) demonstrating that these patterns are reliably absent in stable generations. This would make the claimed "mechanistic insight" connection credible.

- **Free-form generation results should be in the main text.** The generalization to free-form (SELB-Hybrid, Section 6.4) reports impressive numbers (97% MLA, 12.1% LVC on 20k-word novel writing) but defers to Appendix I for details. If the appendix is available in the full submission, these results should be summarized in the main paper with at least one comparison table.

## Removed Points

These points are flagged for removal; treat them with caution:

1. **"Unfair comparison because SELB has structural enforcement that baselines lack"** (Harsh Critic #2) — This criticism is overbroad. SELB is a new method whose mechanism *is* structural enforcement; comparing it against standard decoding strategies that do not use structure is standard practice. The paper's stated contribution includes structural enforcement as part of SELB. However, the *ablation* aspect of this criticism (what does SELB add beyond enforcement?) is kept as a Minor weakness above.

2. **"Misleading presentation" claim that the paper uses "a different, non-corresponding baseline" with intent to misrepresent** — The critic's factual observation (SELB compared to LongWriter-8B, not to its own base model) is kept as a Major weakness. The imputation of intent is removed.

3. **Strength Finder #6 ("Generalization to free-form via SELB-Hybrid")** — Removed because the results are deferred to an unavailable appendix and cannot be verified from the main text.

4. **Strength Finder #2 ("Identifies internal patterns via attention trace analysis")** — Weakened from a full strength to an observation; the evidence is too thin to present this as a supported strength without heavy qualification.

5. **"The method's novelty is low"** (Harsh Critic) — This is a subjective assessment. The paper's contribution is not in algorithmic novelty per se but in the full pipeline (benchmark → probing → mitigation). The claim is demoted to being implicit in the evaluation weaknesses rather than a standalone fatal flaw.

6. **"FAD and SCA don't measure quality"** — Not a claim made by any reviewer in a substantiated way; removed as not clearly anchored.

7. **Strength Finder strengths that are generic/unsupported** — Generic statements like "the paper addresses an important problem" are removed. Only concrete, evidence-grounded strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the assessment that VOLTBench is the paper's strongest contribution — it fills a genuine measurement gap — while the probing and mitigation stages are weaker and would benefit from more rigorous evaluation and claims calibration. The calibration analysis reveals that the paper's benchmark is more comprehensive than HelloBench's (4.75, rejected), but its method evaluation is less clean than LongWriter's (6.00, accepted), placing it in the middle band where acceptance is unlikely without substantial strengthening of the weaker stages.

## Suggestions

1. **Reframe the headline numbers.** In the abstract, conclusion, and contributions, report percentages relative to the model SELB is applied to (e.g., "Qwen2.5-7B+SELB achieves X% length increase and Y% volatility reduction over Qwen2.5-7B"). Report comparisons to LongWriter-8B separately as a cross-model baseline. This is the most impactful fix the authors can make.

2. **Add SELB to Table 2** for at least one base model (e.g., Qwen2.5-7B+SELB and Llama3.1-8B+SELB) so readers can make direct per-metric comparisons against all baselines in a single view.

3. **Add an ablation study** isolating the effects of structural enforcement (section forcing) from proactive failure prevention (banned tokens, EOS suppression). This would disentangle the contribution of the attention-analysis-motivated components from the simple rule-based enforcement.

4. **Strengthen or restructure the probing section.** Either expand the attention analysis to multiple models × tasks with quantitative correlations, or reframe the claims from "identifying common internal patterns" to "illustrating two observed failure signatures on representative examples."

5. **Provide hyperparameter details for all decoding baselines** in the main text or appendix, and state whether they were tuned on a validation set.

## Score and Decision

**Calibration details:**

**Round 1 (Bracketing, score bands on "benchmark for long-form text generation"):**
- Weak band (<3.5): *Mind Scramble* (3.00, Reject), *Structure-Rich Text Benchmark* (3.25, Reject), *Instruction Following is not all you need* (3.00, Reject), *LST-Bench* (2.50, Reject) — lower-quality or unrelated papers; the current paper is clearly above these.
- Middle band (3.5–7.5): *HelloBench* (4.75, Reject), *NovelQA* (6.40, Accept), *LongWriter* (6.00, Accept), *HELMET* (6.00, Accept) — the most relevant comparators. The current paper's benchmark is more comprehensive than HelloBench's, but its method evaluation has issues that HelloBench (a pure benchmark paper) does not face.
- Strong band (>7.5): *BigCodeBench* (9.00, Accept), *MMIE* (8.00, Accept) — substantially more rigorous papers; the current paper is clearly below these.

**Round 2 (Narrowing, score bands 3.5–5.5 and 5.5–7.5 on "decoding strategy for long text generation"):**
- Lower-middle (3.5–5.5): *Length Representations* (4.00, Reject), *MAP's not dead yet* (5.25, Reject), *Reflection Window* (4.75, Reject), *Anticipatory Text Generation* (4.25, Reject). The current paper is stronger than *Length Representations* (unclear methodology) and *Anticipatory Text Generation* (limited scope), and comparable to *MAP's not dead yet* (good insights, weak experiments) — slightly above these.
- Upper-middle (5.5–7.5): *LongWriter* (6.00, Accept), *Approximately Aligned Decoding* (5.75, Reject), *E2LLM* (5.60, Reject). The current paper is weaker than *LongWriter* (cleaner evaluation, clearer contribution) and comparable to *Approximately Aligned Decoding*.

**Initial bracket:** 3.5–6.5 → **Narrowed to:** 4.5–5.5 → **Final score:** 5.0

The paper sits near the *HelloBench* (4.75) / *MAP's not dead* (5.25) level. It has a stronger and more novel benchmark contribution than HelloBench, but the evaluation issues surrounding the method (misleading comparison baseline, thin probing analysis) are more severe than those faced by either accepted middle-band papers (LongWriter at 6.00, HELMET at 6.00). A score of 5.0 reflects a paper with a real contribution (VOLTBench) that is undermined by how its central claims are framed and evidenced, placing it below the acceptance threshold.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>