## Summary

This paper introduces an automated pipeline for extracting linear "persona vectors" from LLM activations, requiring only a natural-language trait description as input. The vectors are validated across three negative traits (evil, sycophancy, hallucination) on two open-source models (Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct) and applied to five distinct tasks: causal steering, deployment-time monitoring, tracking fine-tuning-induced shifts, a novel "preventative steering" method that suppresses unwanted trait acquisition during fine-tuning while preserving capabilities, and pre-training data screening via projection-difference metrics. The preventative steering and data-screening contributions are the most novel and compelling.

## Strengths

- **Automated, generalizable pipeline.** The extraction process takes only a trait name and description, automatically generates contrastive prompts, evaluation questions, and a scoring rubric using Claude 3.7 Sonnet, and produces effective persona vectors validated via causal steering (Figure 2, Section 3.2). This democratizes access to representation-level personality control.

- **Preventative steering is a genuinely novel and well-demonstrated contribution.** Steering *toward* the undesired persona vector *during* fine-tuning (rather than away from it at inference) suppresses trait acquisition while preserving MMLU accuracy and task-specific performance, whereas inference-time steering degrades both (Figures 5–6). The fact-acquisition case study (Section 5.2) cleanly demonstrates this trade-off: hallucination is reduced to baseline while new-fact accuracy and MMLU are preserved — a striking and practically important result.

- **Strong, multi-faceted empirical validation across models and traits.** All key claims are tested on two different model architectures and across three focal traits, with replication of steering (Fig. 2), monitoring (Fig. 3), fine-tuning shift tracking (Fig. 4, r = 0.76–0.97), data screening (Fig. 7, r = 0.88–0.95), and sample-level separability (Fig. 8). The paper also compares against alternative interventions (regularization penalties, CAFT) and provides complementary baselines (Appendix L).

- **Honest and transparent about limitations in the main text.** The paper explicitly acknowledges that monitoring correlations arise mainly from distinguishing between prompt types and are "more modest when controlling for prompt type" (Section 3.3), discusses cross-trait correlations (footnote 6, up to r = 0.86), and notes that computing the projection-difference metric is expensive (Section 6.1). This degree of self-critical candor strengthens rather than weakens the paper.

- **Practical breadth of a single tool.** A single persona vector per trait serves monitoring, control, prediction, and prevention across deployment and training — a compelling demonstration of representational engineering's utility across the LLM lifecycle.

## Weaknesses

### Fatal

None.

### Major

- **Data-screening predictions lack a held-out evaluation in the main text.** The projection-difference metric shows impressively high correlations (r = 0.88–0.95, Figure 7), but these are computed over the same 24 datasets used in the fine-tuning experiments. There is no cross-validation, train-test split, or prospective experiment where the metric is computed on a new dataset before fine-tuning and trait expression is then measured. The paper references Appendix N for real-world dataset experiments and Appendix M for complementary LLM-filter comparisons, but the main text itself provides no quantitative evidence of generalization to unseen data. This limits confidence in the practical screening claims above and beyond what Figure 7 alone demonstrates.

### Minor

- **LLM-judge validation details are absent from the main text.** The pipeline's extraction, steering assessment, monitoring correlations, fine-tuning shift measurements, and data-screening correlations all depend on GPT-4.1-mini trait-expression scores. The paper states that the judge was validated against human evaluators and external benchmarks (Section 2.1) but defers all quantitative validation results to Appendix D. Readers of the main text cannot gauge agreement rates, correlation strengths, or confidence intervals. Including even a brief quantitative summary (e.g., "human-judge agreement was r = 0.X across N samples") would substantially strengthen the evidential chain without requiring much space.

- **Monitoring claims in the abstract are slightly broader than what is demonstrated.** The abstract states the vectors can "monitor fluctuations in the Assistant's personality at deployment time," implying fine-grained sensitivity. The main text honestly clarifies that the strong correlations (r = 0.75–0.83) "arise primarily from distinguishing between different prompt types … with more modest correlations when controlling for prompt type" and that vectors "may be less reliable for more subtle behavioral changes." The abstract should be brought into alignment with this more precise characterization.

### Trivial

- **All-layer vs. single-layer steering inconsistency could use a brief justification in the main text.** Most experiments use single-layer steering, but the fact-acquisition case study (Section 5.2) switches to all-layer steering "given the strength of this persona shift." The paper references Appendix L.3 for multi-layer results, but a one-sentence explanation in the main text would improve coherence.

## Nice-to-Haves

- Exploring whether preventative steering induces genuinely different internal representations versus simply making the model resistant to the fine-tuning loss would strengthen the mechanistic story.
- Measuring degradation of general capabilities (e.g., MMLU) during pure steering experiments (Figure 2) would provide a fuller picture of the steering–capability trade-off.
- Discussing the scalability of the pipeline to a large portfolio of traits and the orthogonality of extracted vectors for simultaneous multi-trait monitoring would anticipate natural follow-up questions.

## Removed Points

These points are flagged to be removed, treated with caution:

- **"LLM-judge circularity" as a fatal flaw.** The paper explicitly references validation against human evaluators and external benchmarks (Appendix D). While the validation details belong in the main text, the existence of validation removes the circularity concern as a fatal or structural problem. Demoted from Critical to Minor.

- **"Selection bias from filtering responses by trait-expression score >50/<50."** This is standard practice in contrastive activation extraction (used by Turner et al. 2024, Panickssery et al. 2024, Zou et al. 2025) and the filtering thresholds are symmetric. No evidence in the paper suggests this introduces a specific distortion beyond what any contrastive method entails. Speculative concern, removed.

- **"Mechanistic interpretation of preventative steering is unexplained."** The paper does not claim to provide a mechanistic explanation; it presents preventative steering as an empirical method. Demanding mechanistic analysis is scope creep. Moved to Nice-to-Have.

- **Request for human ratings of steering outputs beyond judge scores.** While human evaluation would strengthen any single experiment, the paper's replication across two models, three traits, and multiple applications provides convergent validity that mitigates this concern. Moved to Nice-to-Have.

- **"Cross-trait correlations up to 0.86 are understated."** The paper explicitly discusses this with a detailed footnote (footnote 6) and references Appendix I.2. The concern is already addressed in the paper. Removed.

- **Formatting/presentation nitpicks.** Parser artifacts, not author issues. Removed.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an important methodological tension: the field's increasing reliance on LLM judges for evaluating LLM behaviors creates a calibration problem that is acknowledged but not yet solved. This paper exemplifies both the power (automated, scalable evaluation enabling broad experiments) and the risk (validation deferred to appendices, scores taken as ground truth) of this approach. The paper's own data-screening results — showing that persona-vector filtering can flag samples that LLM judges miss (Appendix M) — ironically underscores the limitation: if an LLM judge can be systematically blind to certain trait expressions, then trait scores produced by that same judge may carry systematic blind spots. This tension is not unique to this paper but is rendered unusually visible by its scope.

## Suggestions

- Add a short quantitative summary of the LLM-judge validation to Section 2.1 (e.g., correlation with human raters, accuracy vs. external benchmarks). This requires minimal space and would address the most significant evidential gap in the main text.
- Include a held-out or cross-validated evaluation of the projection-difference metric, or clearly scope the data-screening claim to "on the evaluated dataset collection" until generalization evidence is available.
- Align the abstract's monitoring language with the main text's honest characterization (replace "fluctuations in the Assistant's personality at deployment time" with something like "shifts in persona induced by explicit prompting").

## Score and Decision

**Bracketing (Round 1):** Searched for weak anchors (<3.5), middle anchors (3.5–7.5), and strong anchors (>7.5) on activation steering and representation engineering. Initial bracket placed this paper between ~5.0 (ActAdd, score 5.0) and ~8.0 (Sparse Feature Circuits, score 8.0).

**Narrowing (Round 2):** Searched within 5.0–8.0 for more precise anchors. Key comparators:
- "Identifying and Tuning Safety Neurons" (6.20, Accept): comparable applied scope; Persona Vectors broader in applications, more automated, but similar evaluation rigor.
- "Beyond Single Concept Vector" (6.75, Accept): more theoretical; Persona Vectors more applied and empirically broader.
- "Not All Language Model Features Are Linear" (7.0, Accept): stronger theoretical grounding and cleaner evaluation; Persona Vectors has broader practical scope but slightly looser evaluation on judge validation and data screening.
- "Improving Instruction-Following through Activation Steering" (7.0, Accept): similar steering approach, tighter evaluation but narrower application scope.

**Comparison:** This paper sits above the 6.20 anchor (broader scope, more applications, comparable rigor) and below the 7.0 anchors (which have tighter evaluation of core claims). The novel preventative steering and data-screening contributions are strong, but the evidential chain has two addressable gaps (judge validation in appendix, data screening without held-out evaluation). The paper is honest about its limitations.

**Final placement: 6.5.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>