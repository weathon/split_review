Here is my consolidated meta-review:

---

## Summary

This paper introduces Physics-RW, a benchmark for evaluating physical reasoning in general world models using real-world videos spanning four categories of classical physics: mechanics, thermodynamics, electromagnetism, and optics. The benchmark includes both classification (yes/no QA) and video generation tasks. The authors evaluate 10 models on classification and 2 on generation in a zero-shot setting, finding that even the best models (GPT-4o, Gemini 1.5 Pro) significantly underperform humans. They further analyze common failure modes and explore virtual environment finetuning and physical knowledge prompting as improvement strategies.

## Strengths

- **First real-world video benchmark covering four classical physics categories.** Unlike prior benchmarks that rely on simulator-generated videos and focus narrowly on mechanics (e.g., Physion, CLEVRER), Physics-RW spans mechanics, thermodynamics, electromagnetism, and optics using real-world footage (§1, Table 1). This directly addresses the "reality gap" acknowledged in the literature.

- **Comprehensive zero-shot evaluation across diverse models with a consistent performance gap.** Experiments on 10 classification models (Table 3) reveal that even the best closed-source model (GPT-4o) lags substantially behind human accuracy (Table 5), quantitatively confirming the inadequacy of current general world models for physical reasoning.

- **Human performance baseline provides a meaningful upper bound and diagnostic context.** The three-annotator human evaluation (§4.4, Table 5) establishes that the benchmark is solvable by humans (80–90% ACC), strengthening the claim that models have "significant room for improvement."

- **Diagnostic analysis of common failure modes with concrete examples.** Section 5.1 identifies specific issues (yes-bias in Figure 2, format non-compliance, deficient physical understanding in generation) with illustrated examples (Figure 3), offering actionable directions for future work.

- **Exploration of two improvement strategies on a controlled subset.** The virtual environment finetuning and physical knowledge injection experiments (§5.2–5.3) on domino collisions demonstrate that finetuning on simulated data can transfer to real-world scenarios, which is a practically useful finding.

- **Bilingual instruction set (Chinese and English)** (§3.2) increases the benchmark's accessibility across research communities.

## Weaknesses

### Fatal

None.

### Major

- **The classification evaluation protocol mixes physical reasoning with instruction-following ability.** The paper extracts "yes"/"no" from the first word of model responses; responses not beginning with these words are treated as mispredictions (§4.3). For three models (VideoChat2, Video-LLaMa, LWM) that produce full sentences, the authors resort to a manual re-annotation (†) that classifies outputs into "yes," "no," or "do not know." This is an ad-hoc, irreproducible procedure — the criteria for this manual classification are never specified, and it is applied to only a subset of models. As a result, the quantitative results in Table 3 are confounded: for some models they measure physical reasoning, for others they measure format compliance plus physical reasoning, and for the †-marked models they measure an undocumented human judgment. This is a structural limitation for a benchmark that aims to be a standard evaluation tool.

- **The video generation evaluation is too thin to support broad conclusions.** Only two models are evaluated (NExT-GPT and Open-Sora), and the paper itself acknowledges the limited availability of video-to-video models (§4.1). However, the concluding claim that "current general world models exhibit relatively limited physical reasoning abilities" in generation (§6) is drawn from just these two early-stage baselines. The generation results (Table 4) are better presented as a preliminary pilot than as a substantive evaluation. The benchmark's primary value lies in its classification data; the generation component needs stronger baselines or a clearer downgrading to exploratory status.

### Minor

- **No confidence intervals, error bars, or variance measures reported.** The paper does not report any measure of statistical uncertainty for either classification ACC/F1 or generation FVD scores. With an unknown (likely modest) number of videos per phenomenon category, it is impossible to assess whether observed differences between models are meaningful. This is a standard expectation for benchmark papers.

- **Data quality assurance is underdocumented.** The paper states that videos were "meticulously segmented and selected" (§3.1) and that the dataset was obtained "after manual annotation and verification" (§3.4), but it does not report the number of annotators, inter-annotator agreement, or any filtering criteria. This makes it difficult to assess the reliability of the ground-truth labels.

- **GPT-4o frame interval selection is underspecified.** The paper states that frame intervals of 0.5, 1, 2, and 4 seconds were used based on video length (§4.2), but it does not specify which interval was used for which videos or whether this was tuned per sample. This introduces an uncontrolled variable that could affect reproducibility.

- **The manual re-annotation (†) criteria are not specified.** The paper says outputs were manually classified into "yes," "no," and "do not know" (§4.3) but provides no rubric, guidelines, or examples of this process. This makes the †-marked results irreproducible and their meaning unclear.

- **The virtual environment finetuning analysis is narrow.** It covers only domino collisions (one sub-phenomenon of mechanics) and only one model (MiniGPT4-Video) (§5.2). The paper's conclusion that "virtual environment finetuning can enhance physical reasoning" would be stronger if this were acknowledged as preliminary evidence rather than as a general finding.

- **The physical knowledge injection experiment uses a single static prompt** (§5.3) without exploring variations (e.g., more detailed explanations, chain-of-thought). The finding that prompting had "less significant impact" than finetuning is based on one prompt formulation and cannot be generalized.

### Trivial

- Figure 1 shows instructions visually but the paper would benefit from a concrete text example of a video–question pair in the body.
- The paper does not provide a plain-text version of Table 2's statistics (though the image is present in the original submission).

## Nice-to-Haves

- **Comparison to prior benchmarks (Physion, CLEVRER).** Running the same models on an existing simulated benchmark and showing that performance drops on Physics-RW would directly demonstrate the "reality gap" that motivates the paper, strengthening the central claim.
- **Systematic error type breakdown.** Beyond the yes-bias analysis, a categorized breakdown of errors (visual ambiguity vs. physics misunderstanding vs. instruction misinterpretation) across all models would be more informative than the anecdotal examples in Figure 3.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Table 2 image not legible after OCR"** — Parser artifact, not an author error.
- **"Open release not committed"** — Per hard rules, remove criticisms questioning release status or availability of cited artifacts.
- **"No example instruction in main text"** — Figure 1 does show instruction placeholders; the concern is overstated.
- **"Missing related works"** — Per hard rules, I cannot verify externally.
- **"Missing appendix/proofs"** — Parser strips these sections; they exist in the original submission.
- **"Weaknesses about formatting/style"** — Pure formatting nitpicks are removed per instructions.
- **"Weaknesses complaining about model/baseline preferences"** — The choice of video-to-video models is explained; the generation task is inherently limited by available systems.

## Novel Insights

The reviews converge on an important observation that the paper itself partially misses: the tension between the benchmark's ambition (comprehensive, general-purpose evaluation of physical reasoning) and the fragility of its evaluation protocol. The first-word parsing rule and the manual re-annotation together reveal that the benchmark's classification task is really testing *instruction-following + physical reasoning* simultaneously, not physical reasoning alone. This insight suggests that the benchmark would be most impactful if the evaluation were redesigned — e.g., using multiple-choice or forced-choice formats — so that the task cleanly isolates physical reasoning from format compliance. The paper's own analysis of yes-bias (Figure 2) inadvertently supports this: if models already have a propensity to say "yes," a yes/no format conflates that bias with reasoning ability.

## Suggestions

1. **Redesign the classification task** to use a forced-choice or multiple-choice format (e.g., "Which of the following statements about this video is correct? A) ... B) ...") so that output parsing is unambiguous and the task cleanly measures physical reasoning rather than instruction-following.

2. **Document the dataset thoroughly**: report per-category sample counts, video length statistics, annotator counts, and inter-annotator agreement in the main text. Report classification results with confidence intervals (e.g., bootstrap) to convey reliability.

3. **Present the generation evaluation as explicitly preliminary** and either expand the model set or clearly state that the generation component is intended as a pilot test, not a comprehensive evaluation.

4. **Specify the manual re-annotation rubric** (or, better, remove the †-adjusted results and report only the clean first-word parsing with an explicit discussion of which models are penalized for format non-compliance).

## Score and Decision

The paper addresses a real gap — real-world physical reasoning evaluation — and the benchmark itself is a useful contribution. However, the evaluation methodology has a structural flaw (the classification protocol confounds instruction-following with physical reasoning) that undermines the reported quantitative results. The benchmark's dataset contribution is still valuable, but the paper in its current form overclaims based on a fragile evaluation. A major revision focusing on fixing the evaluation protocol would make this a strong contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>