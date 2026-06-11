Now I have enough calibration data. Let me finalize the review and score.

**Calibration summary:**

Key anchors retrieved across all rounds:
- **LongWriter** (6.0, Accept): Directly comparable - also long-form generation, training-based method + benchmark. Similar quality evaluation weaknesses. Our paper has a more novel benchmark (volatility).
- **HELMET** (6.0, Accept): Comprehensive long-context benchmark, all 6s.
- **Dynamic Correction Decoding** (6.0, Accept): Very similar structure (attention analysis → decoding method fix). All 6s.
- **Attention Intervention for CoT** (6.5, Accept): Probe-then-fix via attention analysis. Higher score.
- **LongGuide** (5.8, Rejected): Long-form generation enhancement. Weaker contribution.
- **HelloBench** (4.75, Rejected): Long text generation benchmark only, no method.
- **LST-Bench** (2.5, Rejected): Weak benchmark, minimal novelty.

**Round-1 bracket:** 4.5 to 7.0. The paper is clearly above HelloBench (4.75) and LongGuide (5.8), and comparable to LongWriter/Dynamic Correction Decoding (6.0).

**Round-2 narrowing:** Between 5.5 and 6.5. The paper is comparable to the 6.0 anchors (LongWriter, HELMET, Dynamic Correction Decoding) with a more novel benchmark contribution but weaker method evaluation. Not quite 6.5 (Attention Intervention for CoT had cleaner evaluation).

**Final score: 6.0** — comparable to LongWriter and Dynamic Correction Decoding, with a novel benchmark that partially compensates for method evaluation gaps.

## Summary
This paper introduces VOLTBench, a multi-dimensional benchmark for measuring output length volatility across multiple generation runs of LLMs, and SELB (Structural Enforcement via Logits Boosting), a training-free decoding strategy that suppresses failure tokens and forces section transitions. The benchmark covers 8 task types × 2 languages × 3 complexity levels × structured/unstructured formats, scaling to 100k words, and is the first to use multi-sample volatility as a core evaluation axis. SELB reduces length volatility by 69% and improves mean output length by 148% compared to LongWriter-8B while maintaining quality (SCA 100%, UCA 86.7%).

## Strengths
- **Novel and well-scoped problem formulation**: Length volatility across multiple generation runs is genuinely underexplored. Table 1 demonstrates VOLTBench is the only benchmark (out of 8 compared) that includes multiple sampling and stability evaluation, clearly differentiating this contribution from prior work like HelloBench, LIFEBench, and LongGenBench.
- **Comprehensive multi-dimensional benchmark design**: VOLTBench systematically varies four dimensions (task type × language × complexity × format) with chapter-based scalability to 100k words, covering both structured (code, math) and unstructured (story, diary) tasks. This is more comprehensive than any existing long-form generation benchmark.
- **Cross-architecture generalization**: Figure 5 shows SELB applied to three distinct model families (Qwen2.5-7B, Qwen3-8B, Llama-3.1-8B) all closely tracking the y=x reference line across 1k-100k requirements, demonstrating the method generalizes beyond a single model.
- **Training-free and practically deployable**: SELB requires only real-time logit modification during decoding (Equations 1-3), with no additional training, data creation, or complex pipelines, making it immediately deployable on any existing model—contrasting with training-intensive approaches like LongWriter-Zero or Temp-Lora.

## Weaknesses

### Fatal
None

### Major
- **No ablation of SELB components**: SELB has two distinct components—structural enforcement (Eq. 2: logit boosting of title tokens when section length exceeds τ_max) and proactive failure prevention (Eq. 3: banning EOS and conversational filler tokens). The paper provides no ablation showing each component's individual contribution. Without this, it is unclear whether both components are necessary, whether one dominates, or whether their combination is what drives the results. This is the most significant gap in the method evaluation.

- **Headline comparison is cross-model and SELB lacks a results table**: The abstract claims "improves the mean output length of the base model by 148% and reduces the length volatility by 69%." These numbers compare SELB on Qwen2.5-7B (15,651 words, LVC 14.02%) against LongWriter-8B (6,320 words, LVC 45.4%)—a different model entirely. The natural comparison is Qwen2.5-7B with SELB vs. Qwen2.5-7B without it (445 words from Table 2), yielding a ~3,400% increase. While cross-model comparison against a specialized long-form model is informative, the abstract's phrasing "of the base model" is misleading. Additionally, SELB's results appear only in prose (Section 6.3) and Figure 5—there is no row for SELB in Table 2 or any dedicated results table with all six metrics (LSD, LVC, MLA, FAD, SCA, UCA).

### Minor
- **Probing-mitigation narrative connection is indirect**: Section 5 identifies Attention Collapse and Attention Instability via attention trace analysis, and Section 6 claims SELB "targets the identified internal patterns." However, SELB operates on logits (banning tokens, boosting title tokens), not on attention. The connection is diagnostic-to-symptom (attention patterns reveal failure modes → logit interventions target those symptoms) rather than mechanistic. A reader skipping Section 5 loses nothing in understanding SELB's design.

- **Attention analysis limited to two models on one task**: Section 5 analyzes only Qwen2.5-7B and Qwen2.5-3B on a diary task with 40 sections (Figure 4), yet the paper claims to identify "common internal patterns of length volatility." Two model traces on one task configuration is insufficient to establish commonality.

- **Hyperparameter values not specified concretely in the main text**: β is defined as "a large positive constant" (Section 6.1) and τ_max as a section length threshold, but no concrete numerical values are given. The Reproducibility Statement claims "all hyperparameters are provided in Section 6," but Section 6 only defines them symbolically in Equations 2-3. (Appendix material may contain these values but is stripped from this version.)

- **Quality evaluation is thin for 15k+ word outputs**: SELB produces 15,000+ word outputs, but quality assessment relies on SCA (execution-based, primarily structural) and a single UCA metric (LLM-as-a-Judge, 86.7%). There is no human evaluation, no assessment of inter-section coherence or narrative consistency, and no factual consistency check—limitations that are particularly concerning at this output length.

## Nice-to-Haves
- A "Qwen2.5-7B + SELB" row in Table 2 with all six metrics for direct comparison against the base model and all other baselines.
- Per-dimension results for SELB (not just the 100-section, English, simple configuration), since the benchmark is multi-dimensional.
- Sensitivity analysis over β and τ_max.
- Comparison to SELB-Hybrid in the main text rather than only in Appendix I, since free-form generation is a major use case.

## Removed Points
These points are flagged to be removed, treat them with caution:
- "SCA is partly an artifact of forced section generation" — SCA measures execution-based content correctness (e.g., code runs correctly), not just structural presence. Forcing sections doesn't guarantee correct content. The criticism overstated this.
- "N=5 is low for reliable volatility estimation" — While technically true, N=5 is reasonable given the computational cost of generating 100k-word outputs multiple times. This is a practical constraint, not a methodological flaw.

## Novel Insights
The paper's most genuinely novel contribution is reframing long-form generation evaluation from single-output quality to multi-output volatility. The observation that the same prompt can yield wildly different output lengths across runs (e.g., LongWriter-8B's standard deviation reaching 103% of its mean) is practically important and has been systematically overlooked. The benchmark design and volatility metrics (LSD, LVC) provide a useful evaluation framework for future work.

## Suggestions
- Add an ablation table showing (a) structural enforcement only, (b) failure prevention only, (c) both, applied to at least 2 base models.
- Include SELB results as a row in Table 2 with all six metrics.
- Report β and τ_max values explicitly in Section 6 (or in a hyperparameter table).
- Broaden the attention analysis to 3-4 models with quantitative summary statistics (e.g., when collapse/instability occurs relative to generation length).

## Reporting

**All anchors retrieved:**

Round 1 (bracketing):
- SaOxhcDCM3 (Self-Consuming Training Loop): 3.20 — weaker, different focus
- jvRCirB0Oq (Text Diversity Measurement): 3.40 — weaker, narrow scope
- 2wwPG1wpsu (LST-Bench): 2.50 — much weaker, minimal contribution
- ly10tMV6cD (Structure-Rich Text Benchmark): 3.25 — weaker, simple benchmark
- A6juYCULJO (PRISM Decoding Strategies): 6.00 — comparable scope but narrower contribution
- vXf8KYTJmm (MAP Decoding): 5.25 — different focus, weaker
- QM2WoPu1It (HelloBench): 4.75 — similar domain, weaker (benchmark only, no method)
- aS1IhKdLPP (Reflection Window): 4.75 — different approach, weaker
- jOmk0uS1hl (Training on Test Task): 8.00 — stronger, different area
- HnhNRrLPwm (MMIE): 8.00 — stronger, multimodal benchmark
- QEHrmQPBdd (RM-Bench): 8.00 — stronger, different domain
- d8w0pmvXbZ (Small-scale Proxies): 8.00 — stronger, training instabilities

Round 2 (narrowing):
- uMEsKEiB7J (NovelQA): 6.40 — comparable benchmark contribution
- 514rdneWOX (LongHalQA): 5.25 — weaker, rejected
- WQwy1rW60F (LV-Eval): 6.00 — comparable benchmark paper, rejected
- 293V3bJbmE (HELMET): 6.00 — comparable benchmark, accepted
- kQ5s9Yh0WI (LongWriter): 6.00 — most comparable, accepted, similar domain
- Dj9wssUmLn (LongGuide): 5.80 — similar domain, rejected, weaker
- 0KHW6yXdiZ (Logits Watermarking): 5.25 — different focus
- KRnsX5Em3W (LLM Hallucination Representations): 6.50 — probe-then-use, accepted
- r42tSSCHPh (Catastrophic Jailbreak): 7.00 — decoding exploitation, stronger
- sKYHBTAxVa (LiveBench): 7.33 — strong benchmark, accepted
- 9OevMUdods (Pinocchio): 6.75 — benchmark + analysis, accepted
- 1tBvzOYTLF (RevisEval): 6.00 — evaluation method, accepted
- E8gYIrbP00 (Human Uncertainty): 6.75 — evaluation analysis, accepted
- oqsQbn4XfT (Synthetic Data Diversity): 5.80 — rejected, weaker
- zpENPcQSj1 (Length Generalization): 6.33 — different area, accepted
- bEbQBiMpUI (Self-correction): 5.40 — rejected, weaker
- nwZHFKrYTB (How to Train Long-Context): 5.80 — rejected
- 9WbNpRuFuS (Aligned Decoding): 5.75 — rejected, different focus
- VipcVxaTnG (Vocabulary Key Space): 6.50 — accepted, different focus
- W6yIKliMot (Attention Intervention CoT): 6.50 — very similar probe-then-fix structure, accepted
- 4z3IguA4Zg (Dynamic Correction Decoding): 6.00 — very similar (analysis → decoding method), accepted

**Round-1 bracket:** 4.5 – 7.0 (clearly above HelloBench at 4.75, comparable to 6.0 anchors)

**Round-2 narrowing:** 5.5 – 6.5. The paper is comparable to LongWriter (6.0, Accept) and Dynamic Correction Decoding (6.0, Accept), with a more novel benchmark contribution but weaker method evaluation (missing ablation, misleading headline numbers). Not quite at 6.5 level (Attention Intervention for CoT had cleaner evaluation and was accepted at 6.5).

**Final positioning: 6.0.** The paper sits squarely among the accepted 6.0 anchors. The novel volatility benchmark pushes it above weaker rejected papers (HelloBench at 4.75, LongGuide at 5.8), while the missing ablation and presentation issues prevent it from reaching 6.5.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>