Now I have a thorough understanding of the paper and can produce the consolidated review.

## Summary

This paper presents Dynamic-SUPERB Phase-2, a community-driven benchmark for instruction-based universal speech/audio models. It expands from 55 to 180 tasks (the largest such benchmark), introduces a two-level task taxonomy (17 domains across speech, music, and audio), describes a community contribution pipeline that accepted 91 new tasks, and evaluates 8 models. The core contributions are the benchmark scale, taxonomy, and community process; the evaluation findings are secondary.

## Strengths

- **Largest benchmark for speech and audio evaluation**: With 180 tasks, Dynamic-SUPERB Phase-2 surpasses all prior benchmarks (SUPERB: 13, SLUE: 7, HEAR: 19, MARBLE: 13, AIR-bench: 19) by a wide margin (Table 1). This directly supports the paper's central claim of scale.

- **First detailed task taxonomy in speech/audio benchmarking**: The paper introduces a two-level taxonomy with 8 speech domains and 9 audio/music domains (Figures 2–3), developed with reference to INTERSPEECH sessions and IEEE SPS EDICS. This enables targeted capability analysis beyond simple task lists.

- **Diverse task types beyond classification**: Unlike Phase-1 (classification only), Phase-2 includes regression and sequence generation tasks (Section 3.2), with distinct evaluation pipelines for each type (Section 4.2), enabling coverage of tasks like MOS prediction and ASR.

- **Community-driven expansion with quality control**: The paper describes a call-for-tasks process with editor review, receiving 145 proposals and accepting 91 new tasks between March–July 2024 (Section 3.3). This demonstrates a sustainable model for evolving the benchmark.

- **Core task subsets for efficient evaluation**: Tasks from SUPERB, MARBLE, and HEAR are reformulated into the instruction format with reduced data sizes, enabling quick-round experiments while bridging established encoder benchmarks with the instruction-following paradigm (Section 3.4).

- **Open-source commitment and standardized evaluation**: All task data and the evaluation pipeline will be open-sourced (Reproducibility Statement), with GPT-4o temperature set to 0 for evaluation consistency, facilitating future benchmarking.

## Weaknesses

### Fatal
None.

### Major

- **LLM-as-judge evaluation pipeline is used without any validation.** GPT-4o serves as a referee for classification tasks and as a post-processor for regression tasks (Section 4.2), yet the paper reports no human agreement rates, inter-rater reliability, or even a small-scale sanity check. For classification, accuracy is defined as the percentage of outputs the LLM judge considers aligned with ground truth, but no evidence is provided that GPT-4o's judgments are correct or consistent. For regression, the N/A rate scaling (multiplying by 1−N/A when higher-is-better, dividing by 1−N/A when lower-is-better) is ad-hoc and conflates instruction-following with task performance in an unvalidated manner. The paper claims this approach is "widely adopted in the NLP community" (Section 4.2) but does not validate its application to the diversity of speech/audio tasks here. The reported domain-level scores and comparative claims (e.g., "spoken language models outperform music models on music tasks") are therefore of unknown reliability. This is the paper's most significant weakness because the evaluation results are a substantial part of the presented analysis.

- **Domain-level relative-score aggregation is fragile and can misrepresent performance.** The paper averages relative improvements over a single baseline (Whisper-LLaMA) across tasks within a domain (Section 5.1). This method is sensitive to outlier tasks (acknowledged by the authors), and the choice of baseline strongly influences all scores. For music and audio domains, Whisper-LLaMA is arguably meaningless because Whisper cannot transcribe non-speech content; the paper excludes tasks where Whisper-LLaMA scores zero, but this creates selection bias that limits what the domain scores represent. The resulting domain scores (Figure 4) mix tasks with vastly different metrics and scales, making it impossible to interpret the practical significance of a given score difference. While the paper acknowledges some of these limitations (Section 5.1, Figure 4 caption), the aggregation scheme is presented as a primary analytical tool and its fragility undermines the strength of the domain-level conclusions.

### Minor

- **Community task acceptance criteria are unspecified** (Section 3.3). The paper reports that 91 of 145 proposals were accepted after editor review, but no criteria for acceptance or rejection are given. Without understanding what fraction of tasks are trivial variants or why tasks were rejected, the claim that 180 tasks constitute the "largest benchmark" is meaningful primarily in count, not in demonstrated coverage or challenge.

- **Taxonomy leaf coverage is not documented.** The taxonomy is presented at two levels (Figures 2–3), but no table or analysis shows how many tasks fall under each leaf, which leaves are thin, or whether the taxonomy was validated by independent raters. This limits the ability to assess how representative the benchmark is of real-world spoken language understanding.

- **"First detailed taxonomy" claim is made without comparison.** The paper states it is "the first to provide such a detailed task taxonomy in speech processing" (Section 3.4) but does not compare its taxonomy's granularity against existing benchmark groupings (e.g., SUPERB's four categories, AIR-bench's organization). A brief comparison would substantiate this claim.

- **Core task data reduction is undocumented.** The paper states core tasks are "reduced subsets" (Section 3.4) but does not report how data was subsampled or whether the reduced subsets preserve original task difficulty. If subsets are small or easy, core-task results may not reflect true model capability.

- **Multi-audio input concatenation is not validated.** For models without multi-input interfaces, audio files are concatenated with 0.5s silence (Section 4.1). This workaround could affect temporally sensitive tasks (speaker verification, diarization), but no ablation or comparison with models that natively support multiple inputs is provided.

- **Whisper 30-second limit impact is not quantified.** The paper mentions Whisper's 30-second limit (Section 4.1) but never reports how many test samples across the 180 tasks exceed this duration, making it impossible to gauge the impact on model results.

- **No human or random baselines.** The paper reports no human performance or random-guess baselines for any task. Even a simple majority-class baseline for classification tasks would contextualize the reported numbers and help distinguish genuine capability from chance.

- **Instruction sensitivity is not analyzed.** Each task has multiple instruction templates (Section 3.2), but no analysis is given of whether model performance varies significantly across different phrasings of the same task. If it does, the benchmark's reliability as a measure of capability is weakened.

- **No confidence intervals or variance measures.** Given the LLM-as-judge evaluation pipeline and reduced core task data sizes, the absence of bootstrap confidence intervals or variance estimates for any result (Table 2, Figure 4) is a gap.

### Trivial
- None of consequence beyond what is covered in Minor.

## Nice-to-Haves

- Validate the GPT-4o evaluation pipeline on a subset of tasks by comparing with human judgments (e.g., Cohen's kappa on 50–100 samples per task type). This would dramatically strengthen the credibility of all evaluation findings.
- Replace the ad-hoc N/A scaling with a more principled approach (e.g., reporting metric on valid outputs and N/A rate separately, or using a simple product of metric × (1−N/A) consistently).
- Replace the relative-score aggregation with a rank-based method (average rank per model across tasks) or normalize scores within each task to [0,1] before averaging, to reduce sensitivity to baseline choice and outlier tasks.
- Provide a table showing the distribution of tasks across taxonomy leaves to demonstrate coverage and reveal which domains are thin.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Strength about "Domain-level relative-score analysis" being an interpretable strength**: Removed because it conflicts with the verified weakness that the aggregation is fragile and potentially misleading. A verified weakness takes precedence over a conflicting strength.
- **Criticism about "no persistent DOI or versioned release"**: Removed per hard rule — the paper states materials will be open-sourced; citing a DOI is a formatting/reproducibility nitpick that does not affect the paper's core claims.
- **Criticism about "datasets with proper licenses" constraint not being discussed**: Removed as it asks for additional depth on a logistical detail that would not change the paper's contribution or believability.
- **Criticism that the paper doesn't discuss whether models were disadvantaged by text instruction format**: Removed because the paper explains the design choice and its rationale (Section 3.2); the concern is speculative without evidence of actual disadvantage.
- **Criticism about the paper not being able to be accepted**: Re-framed — the benchmark contribution is strong enough to support acceptance despite the evaluation methodology issues requiring major revision.

## Novel Insights

The reviews surface a clear tension between the paper's genuine contributions (largest benchmark, detailed taxonomy, community process) and the reliability of its evaluation methodology. The key insight is that the LLM-as-judge pipeline—unchallenged within the paper—is the weakest link. If the evaluation findings were de-emphasized or validated, the benchmark contribution alone would be solid. Conversely, if the paper is read primarily for its evaluation claims about which models excel where, those claims are not yet trustworthy. This tension is not fatal because the benchmark itself is the primary artifact, but it means the paper needs either (a) validation of the evaluation pipeline or (b) a reframing that clearly distinguishes the benchmark contribution (strong) from the preliminary evaluation findings (qualified).

## Suggestions

1. Add a human-validation experiment for the GPT-4o judge on at least 3–5 diverse tasks (classification + regression), reporting Cohen's kappa or percentage agreement. Even a small-scale check (50–100 samples per task) would substantially increase confidence in all reported results.
2. Replace the N/A scaling in the domain-level analysis with separate reporting of (a) metric on valid outputs and (b) N/A rate, or use a consistent product formulation (metric × (1−N/A)) for all metrics.
3. Consider reporting average ranks instead of relative scores for domain-level aggregation, or normalize all task metrics to a common scale (e.g., [0,1]) before averaging.
4. Add a table showing the count of tasks per taxonomy leaf to demonstrate coverage.
5. Add random-guess / majority-class baselines to Table 2 for all classification tasks.

## Score and Decision

**Originality**: 7/10 — The benchmark scale and community process are novel contributions; the taxonomy is a useful organizational contribution but not conceptually surprising.  
**Importance of research question**: 8/10 — A comprehensive benchmark for universal speech models is timely and needed.  
**Claims well supported**: 5/10 — The benchmark scale claim is well supported; the evaluation findings are not, due to the unvalidated LLM judge.  
**Soundness of experiments**: 5/10 — The evaluation methodology has significant unaddressed risks (LLM judge validity, aggregation fragility, no baselines).  
**Clarity of writing**: 7/10 — Generally clear; the taxonomy and task formulation are well explained.  
**Value to the research community**: 8/10 — The 180-task benchmark and open-source release will be valuable resources even with evaluation methodology caveats.

The paper's primary contribution—the 180-task benchmark and its taxonomy—is real and valuable. The evaluation methodology, however, has significant weaknesses that undermine the secondary findings about model capabilities. The paper merits acceptance primarily for the benchmark contribution, with the understanding that the evaluation results should be treated as preliminary and that the methodology requires validation in future work or a revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>