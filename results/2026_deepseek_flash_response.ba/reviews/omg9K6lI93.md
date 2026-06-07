Now I have enough calibration data. Let me write the final review.

## Summary

This paper investigates whether translating benchmark data into Arabic can mask data contamination in LLM evaluation. The authors fine-tune four open-weight models on controlled proportions (0%, 10%, 50%, 100%) of Arabic-translated test data from MMLU, XQuAD, and MLQA, then evaluate on the original English benchmarks. They extend the TS-Guessing probe with a choice-reordering strategy to detect memorization signals. Results show MMLU accuracy rises monotonically with contamination across models (e.g., Mistral: 0.577→0.690) despite the Arabic→English language gap, while the TS-Guessing probe returns low detection rates for several models. The paper also sketches a Translation-Aware Contamination Detection (TACD) framework.

## Strengths

- **Controlled causal evidence that contamination persists through translation (Table 2, Section 3.1).** The paper systematically varies contamination proportion (0%, 10%, 50%, 100%) via Arabic-translated test data while keeping training protocols fixed. Table 2 shows clear monotonic MMLU gains across all four models (e.g., Mistral: 0.577→0.690; LLaMA: 0.332→0.431; Gemma: 0.220→0.284; Qwen: 0.553→0.581), establishing that contamination effects persist even when training data is in a different language from evaluation. This controlled design isolates the contamination variable more cleanly than post-hoc detection studies.

- **Choice-reordering extension to TS-Guessing with IDR metric (Section 3.3, Table 3a).** The paper adds a random choice-reordering step before masking an incorrect answer for MCQ items. The Index-Recall Rate (IDR) captures whether models reproduce pre-shuffle answer positions — a pure memorization signal orthogonal to content-level reasoning. Table 3a shows LLaMA-3.2-1B at 50% contamination achieves IDR=0.643, demonstrating that answer-position memorization survives Arabic translation in at least some settings.

- **Differential contamination dynamics across task formats (Table 2).** The paper reveals that contamination through translation affects MCQ (MMLU) and extractive QA (XQuAD/MLQA) in qualitatively different ways. MMLU shows monotonic improvement, while extractive QA exhibits non-monotonic, model-specific patterns (e.g., Mistral XQuAD: 0.455 at 10% → 0.114 at 100%). This task-level granularity is more actionable than blanket contamination warnings.

## Weaknesses

### Major

- **Missing English-only contamination control.** The paper cannot support its central claim that "translation masks contamination" (as opposed to "translation reduces the magnitude of contamination benefit") because it never compares Arabic-translated contamination against English-only contamination at matched proportions. The experimental setup trains models on `D_EN^d ∪ D_AR^d(p)` — the English test set is always present, and Arabic portions are added on top. Without a condition where only English test items are added at the same proportions (10%, 50%, 100%) and evaluated with the same TS-Guessing probe, the paper cannot distinguish whether translation specifically reduces detectability or simply produces a smaller effect that any probe would struggle to detect. If English contamination at 10% gives +0.10 on MMLU while Arabic contamination at 10% gives +0.003, the correct conclusion is that translation nearly eliminates the benefit — not that it "masks" it. This control is essential to the paper's thesis and its absence is a fundamental evidential gap.

- **TS-Guessing probe is not calibrated against a known-positive condition.** The TS-Guessing probe returns near-zero detection rates for several models even at 100% contamination (e.g., Mistral-7B IDR=0.000 at all levels on MMLU; Table 3a). The paper interprets this as evidence that translation conceals contamination signals (lines 201–218). However, without demonstrating that TS-Guessing *does* detect English-language contamination in the same models when it is known to exist, the near-zero results may simply reflect an ineffective probe. LLaMA's IDR=0.643 at 50% shows the probe can work, but this only deepens the ambiguity: why does the probe work for LLaMA but not Mistral? The obvious alternative explanation — that the probe is poorly calibrated for this setting — is not ruled out.

- **Section 4.2 contradicts Table 2.** The paper states that "Across contamination levels p∈{10,50,100}%, the models exhibit approximately equal performance on all evaluated benchmarks" and that "scores remain broadly stable as p increases" (lines 201–217). This is directly contradicted by Table 2, where MMLU scores rise substantially between 10% and 100% (e.g., Mistral: 0.580→0.690, a +19% relative increase; LLaMA: 0.381→0.431). The paragraph appears to conflate the TS-Guessing probe results (which are indeed flat for some models) with the evaluation results (which are not). This is a significant presentation error that undermines reader trust.

### Minor

- **The p=0 baseline leaks English test data.** The training set at p=0 is `D_EN^d` — i.e., the English test set itself. This means the "0% contamination" condition is already contaminated with English benchmark items. All higher contamination levels add Arabic-translated items on top of this already-leaked English set. Comparisons between p=0 and p>0 therefore do not measure "clean vs. contaminated" but rather "English-only contamination vs. English+Arabic contamination." This weakens the interpretability of the baseline.

- **TACD is a sketch, not a contribution (Section 5).** The proposed framework is described in three bullet points and explicitly labeled "a forward-looking blueprint rather than a complete implementation" (line 252). It is neither implemented nor evaluated. As such, it carries no evidentiary weight and cannot be considered a validated contribution.

- **No multiple seeds or statistical confidence.** Results are reported from single runs with no error bars. Given LoRA fine-tuning variance, some small differences could be noise (e.g., Qwen MMLU: 0.553→0.560→0.562→0.581). Non-monotonic patterns that receive substantive interpretation (e.g., Mistral XQuAD: 0.302→0.455→0.272→0.114) need replication to establish reliability.

- **Claim about "models with stronger Arabic capabilities" is untested.** The abstract claims contamination particularly benefits models "with stronger Arabic capabilities," but no Arabic proficiency metric is measured or reported for any model. This assertion is unsupported.

### Trivial

- Section 4.2 conflates evaluation results (Table 2, which shows trends) with TS-Guessing probe results (Table 3, which is flat), creating confusing and contradictory text.

## Nice-to-Haves

- Adding an English-only contamination condition at matched proportions (0%, 10%, 50%, 100%) with the same TS-Guessing probe would directly test whether translation specifically reduces detectability versus merely reducing effect size.
- Running experiments with ≥3 random seeds and reporting standard deviations would strengthen confidence in observed trends.
- Measuring models' Arabic proficiency on an Arabic-language benchmark (e.g., ArabicMMLU or similar) would substantiate or remove the unsupported claim about Arabic capabilities.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Experimental design does not test what it claims / studies test-set fine-tuning not pre-training contamination":** The paper does not claim to simulate pre-training contamination. It studies a controlled fine-tuning scenario to isolate the effect of translation on contamination dynamics. This is a valid research design for its stated question, even though it differs from incidental pre-training exposure. The critic's framing overstates the problem.

- **"TS-Guessing probe fails to detect contamination where it is known to exist":** Overstated. LLaMA-3.2-1B achieves IDR=0.643 at 50%, showing the probe can detect contamination. The real issue (retained above) is the lack of calibration, not complete probe failure.

- **"MMLU improvement is the expected outcome of training on test-set answers":** The paper's finding is that this improvement persists through Arabic→English translation, which is non-trivial. The critic dismisses the novel aspect.

- **"Translation perturbs tokens but not measured":** The paper mentions measuring embedding similarity (Section 4.3), though the analysis is presented at a high level without a dedicated figure or detailed numbers in the main text.

- **Litany of formatting, grammar, and style nitpicks from the harsh critic:** These are parser artifacts or minor presentation issues irrelevant to the scientific contribution.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add the English-only control.** Fine-tune models on English test data at the same proportions (0%, 10%, 50%, 100%) without any Arabic, and run the same TS-Guessing probe. If the probe detects English contamination effectively but Arabic contamination at matched levels is undetected, the masking claim is supported. If the probe fails on both, the probe is simply weak. This single experiment resolves the two major weaknesses simultaneously.

2. **Revise Section 4.2** to clearly separate discussion of evaluation trends (Table 2) from TS-Guessing results (Table 3a), and remove the "near-flat" characterization of Table 2, which is factually incorrect for MMLU.

3. **Run at least 3 random seeds** and report means with standard deviations, or explicitly acknowledge the single-run limitation and its implications for the non-monotonic patterns.

4. **Remove or substantiate the "stronger Arabic capabilities" claim** with actual measurements on an Arabic-language benchmark.

## Score and Decision

**Calibration Anchors:**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| "Evading Data Contamination Detection" (Nk1MegaPuG) | 4.25 | R1/R2 | Similar thesis (evading detection via transformation). That paper's main claim was cleaner to test; mine has more controlled experiments but more severe structural gaps in the central comparison. Slightly weaker. |
| "Benchmark Inflation" (rAylWUIKtu) | 4.25 | R2 | Similar ambition level. Both rejected due to methodological limitations that undercut the headline claims. Comparable. |
| "Elephants Never Forget" (lwtaEhDx9x) | 4.75 | R2 | Tabular memorization study. Better-executed within its scope. My paper is slightly weaker due to the missing control condition. |
| "Crosslingual Capabilities" (BCyAlMoyx5) | 5.67 | R1/R2 | Broader cross-lingual study with mixed reviews (8,6,3). Similar types of weaknesses (limited languages, missing controls). My paper is narrower and has less rigorous execution. Weaker. |
| "How much can we Forget" (Nsms7NeU2x) | 6.75 | R1 | Extensive controlled experiments + theory. My paper lacks this level of rigor and has unresolved methodological gaps. Clearly weaker. |
| "To the Cutoff... and Beyond" (m2NVG4Htxs) | 6.75 | R1 | Accepted. Clever longitudinal methodology with rigorous statistical analysis. My paper has a more novel research question but weaker methodology. Weaker. |
| "Training on the Test Task" (jOmk0uS1hl) | 8.00 | R1 | Strong accept. Polished, well-executed, clear central thesis. Not comparable in quality. |

**Round-1 bracket:** (3.5, 5.5)

**Round-2 narrowing:** Comparison to anchors at 4.25 and 4.75 places this paper below "Elephants Never Forget" (4.75) and roughly on par with or slightly below "Evading Contamination Detection" (4.25) and "Benchmark Inflation" (4.25). The paper has a genuinely interesting research question and real experiments, which puts it above 3.5. But the two structural weaknesses (missing English control, uncalibrated probe) prevent the evidence from supporting the headline claims, capping it at ~4.0.

**Final Score: 4.0** — A paper with a legitimate question and non-trivial experiments, but whose central claims are not supported by the current experimental design due to two major, addressable gaps. Would need substantial revision to be competitive at a top venue.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>