Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper investigates whether translating benchmarks into Arabic can mask data contamination in LLMs. The authors fine-tune four open-weight models on Arabic translations of MMLU, XQuAD, and MLQA at varying contamination levels (0%, 10%, 50%, 100%) and evaluate on the original English benchmarks. They extend TS-Guessing with a choice-reordering strategy for MCQs. The key finding is that MMLU accuracy rises monotonically with contamination even after translation, while XQuAD/MLQA show non-monotonic patterns and TS-Guessing probe signals are often low — suggesting that translation-based contamination evades probe-based detection while still inflating closed-book accuracy. A Translation-Aware Contamination Detection (TACD) framework is conceptually proposed but not implemented.

## Strengths

- **Systematic, multi-dimensional contamination setup.** The paper fine-tunes four models across three datasets at four contamination levels (0/10/50/100%), producing a controlled 48-condition grid. Table 2 cleanly shows that MMLU accuracy rises monotonically with contamination for all four models (e.g., Mistral: 0.577→0.690; LLaMA: 0.332→0.431), while XQuAD/MLQA trends are non-monotonic and model-specific. This controlled design usefully demonstrates that translation-based contamination inflates closed-book MC accuracy without consistently improving extractive QA.

- **Novel extension of TS-Guessing with choice-reordering for multilingual MCQs.** Section 3.3 and Figure 1 introduce a choice-reordering strategy for MMLU (shuffling answer letters before masking) and a masked-token strategy for XQuAD/MLQA. The IDR metric captures whether models retain pre-shuffle answer positions. Table 3a shows non-trivial signals for some models (e.g., LLaMA-3.2-1B achieves IDR=0.643 at 50% contamination), providing initial evidence that memorization cues survive translation even when standard probes miss them.

- **The core observation — MMLU rises through translation while XQuAD/MLQA do not — is genuinely interesting.** The divergence between closed-book MC accuracy and extractive QA performance under translated contamination is a non-trivial finding. It suggests that contamination benefits are task-dependent and that translation does not "decontaminate" uniformly, which has practical implications for multilingual evaluation pipelines.

## Weaknesses

### Fatal

None.

### Major

- **Section 4.2 text is inconsistent with the data in Table 2.** The paper states: *"Across contamination levels p ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks. This near-flat trend indicates that Arabic→English translation is effectively masking contamination effects"* and references *"Tables 2 and 3a."* But Table 2 shows MMLU increasing monotonically from 10%→50%→100% for every model (e.g., Mistral: 0.580→0.690→0.690, LLaMA: 0.381→0.389→0.431). These are not "approximately equal" or "near-flat." This wording conflates standard evaluation results with the TS-Guessing probe results, creating a contradiction between the paper's own text and its data. The central claim is salvageable (the abstract already acknowledges MMLU rises), but Section 4.2 must be rewritten to clearly separate "standard evaluation shows contamination effects" from "probe-based detection fails to detect them."

- **Missing English-only contamination baseline.** The paper never fine-tunes models on English versions of the same benchmarks at the same proportions. Without this control, it is impossible to know whether translation actually *conceals* contamination or merely *attenuates* it. If English contamination yields even larger MMLU gains, then translation partially masks; if it yields similar gains, translation is not masking at all (the contamination is just standard fine-tuning effects). This is the single most important missing control experiment for the paper's core claim.

- **TS-Guessing probe is not validated on an English-only condition.** The paper interprets low TS-Guessing scores as evidence that translation "masks" contamination signals. But without showing that TS-Guessing detects contamination when applied to English-only contaminated models (same setup, no translation), the low scores could simply mean the probe is not working under this experimental paradigm — rather than that translation is actively masking. This is especially relevant given that Table 3a shows *some* non-trivial IDR values (LLaMA at 0.643) that the paper does not analyze in depth. A validation experiment on English-only contamination is needed to distinguish probe insensitivity from genuine masking.

- **No statistical significance or variance reporting.** All results in Tables 2 and 3 are single-point estimates. Contamination differences are often small (e.g., Qwen MMLU: 0.553→0.581; Gemma MMLU: 0.220→0.284). Without multiple seeds, confidence intervals, or statistical tests, it is impossible to assess whether the observed differences reflect real contamination effects or random variation. The non-monotonic patterns in XQuAD/MLQA (declines and partial recoveries) could easily be noise. For an empirical study making quantitative claims about contamination masking, this is a significant methodological gap.

### Minor

- **Translation source and quality are not disclosed.** The paper states that MMLU uses *"Arabic translations of the test items"* and XQuAD/MLQA use their *"Arabic split,"* but does not specify whether these are human translations, machine translations (and if so, which system), or pre-existing dataset splits. Translation quality directly affects whether contamination is detectable, and this missing detail harms reproducibility.

- **TACD framework is entirely conceptual.** Section 5 describes a framework for Translation-Aware Contamination Detection with three components (cross-translation benchmarking, TS-Guessing across variants, back-translation consistency), but none are implemented or tested. The paper accurately calls it a *"forward-looking blueprint,"* but the contribution is limited to the idea. A single proof-of-concept experiment (e.g., back-translation consistency on one model/benchmark) would significantly strengthen this section.

- **No measurement of model Arabic capability.** The paper asserts that contamination benefits are *"particularly [for] those with stronger Arabic capabilities"* but never measures Arabic proficiency of the four models. A simple Arabic NLP benchmark would ground this claim.

### Trivial

- The paper uses "terra bytes" instead of "terabytes" at one point (Section 2.3).

## Nice-to-Haves

- Analysis of translation quality and lexical/semantic overlap between English and Arabic items, extending the brief cosine similarity mention in Section 4.3.
- Systematic analysis of why MLQA and XQuAD show non-monotonic patterns (e.g., measuring lexical overlap between Arabic training items and English evaluation items).
- Multiple random seeds (≥3) for each condition.

## Removed Points

- **"TS-Guessing probes yield near-zero scores"** (Harsh Critic Major/Structural Weakness #2): Factually inaccurate. Table 3a shows LLaMA-3.2-1B achieves IDR=0.643 at 50% contamination and Qwen achieves 0.261/0.251/0.208 across levels — well above near-zero. The critic's claim that scores are "consistently very low (mostly <0.1)" is contradicted by the paper's data. The underlying point (probe needs validation) is retained above but the factual error is stripped.

- **"The central claim is contradicted by the paper's own evaluation results"** framed as a *structural/fatal* flaw: The abstract clearly states *"models still benefit from exposure"* alongside *"translation into Arabic conceals traditional contamination signals,"* so there is no contradiction at the paper level. The inconsistency is confined to Section 4.2's wording, which I retained as a Major weakness above. The fatal framing is removed.

- **Strength Finder's TACD strength**: Overstated. Framing a proposed-but-unimplemented framework as a strength is too generous; it's moved to a conceptual proposal noted in the summary.

- **Strength Finder's "translation masks but does not eliminate contamination"** strength: Circular with the paper's own central claim and redundant with the first listed strength. Removed.

- **Criticism about missing related work**: Removed per instructions (cannot verify existence of missing references).

## Novel Insights

The harsh critic makes an astute observation that the core tension in the paper — MMLU rising while TS-Guessing stays low — is better interpreted as "TS-Guessing fails to detect contamination under translation" rather than "translation masks contamination." This reframing is more precise than the paper's current wording and would make the contribution clearer. However, the strongest reviewer observation is that the paper lacks the one experiment (English-only contamination baseline) that would resolve whether translation actively masks or merely attenuates contamination. Without this baseline, the paper's headline claim rests on an untested comparison.

## Suggestions

1. **Rewrite Section 4.2** to clearly separate two observations: (a) standard evaluation (Table 2) shows that MMLU contamination effects persist through translation, and (b) the TS-Guessing probe (Table 3) fails to detect this contamination. The current text conflates these and claims "broadly stable" performance, which the MMLU data directly contradicts.

2. **Add an English-only contamination baseline** where the same models are fine-tuned on English benchmark items at the same proportions. If English contamination yields larger MMLU gains, translation is partially masking; if gains are similar, translation is not masking but the probe is simply insensitive.

3. **Validate TS-Guessing on an English-only condition** to establish that the probe detects contamination when translation is absent. Run the full TS-Guessing protocol (choice-reordering + masking) on models fine-tuned on English contaminated data. If IDR scores are high for English but drop with Arabic, the "translation masks probes" claim is supported. If IDR is low for both, the probe is simply ineffective in this setting.

4. **Run experiments with ≥3 random seeds** and report means ± standard deviations. The non-monotonic patterns in XQuAD/MLQA need statistical support.

5. **Disclose translation sources** (human vs. machine, which system, quality metrics) and provide simple Arabic NLP benchmark scores for the models to ground the claim about "stronger Arabic capabilities."

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `jOmk0uS1hl` — *Training on the Test Task Confounds Evaluation and Emergence* | 8.0 | Much stronger: clean conceptual contribution with thorough experiments. Current paper is notably weaker. |
| `KS8mIvetg2` — *Proving Test Set Contamination in Black-Box LMs* | 7.5 | Much stronger: provable guarantees, rigorous empirical methodology. Current paper substantially weaker. |
| `m2NVG4Htxs` — *To the Cutoff... and Beyond? A Longitudinal Perspective* | 6.75 | Stronger: clean natural experiment, more thorough analysis. Current paper is weaker. |
| `Nsms7NeU2x` — *How much can we Forget about Data Contamination?* | 6.75 | Stronger: combines theory with extensive controlled experiments. Current paper is weaker. |
| `Nk1MegaPuG` — *Evading Data Contamination Detection is (too) Easy* | 4.25 | Similar topic, comparable quality. Current paper has more systematic experiments but similar methodological gaps. |
| `rAylWUIKtu` — *Benchmark Inflation: Revealing LLM Performance Gaps* | 4.25 | Comparable quality. Both have interesting ideas but incomplete validation. |
| `RuY1r1PDdQ` — *FAITHQA benchmark* | 3.0 | Current paper is clearly stronger — more coherent framing, more systematic experiments. |
| `OdoS6cH8MP` — *Language Models for Textual Data Valuation* | 2.0 | Current paper is substantially stronger — clear research question, proper experimental design. |

Placed relative to these anchors, the paper sits between the 4.25 cluster and the 6.75+ cluster. It identifies a genuine and underexplored problem, has a systematic experimental design, and produces an interesting (if inconsistently described) finding about MMLU rising through translation. However, the missing critical baseline (English-only), unvalidated probe, lack of statistical rigor, and the inconsistency in Section 4.2 prevent it from being a strong paper.

**Score: 4.5** — The paper identifies a real problem and has a reasonable experimental foundation, but the evidence is incomplete in ways that undermine the central claim in its current framing. The missing controls and Section 4.2 contradiction are fixable, but in the current form the paper does not convincingly establish that translation "masks" contamination rather than merely attenuating it or evading a probe that may not work in this setting.

**Decision: Reject**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>