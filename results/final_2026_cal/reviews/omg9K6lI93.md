Now I have a solid calibration set. Let me synthesize the final review.

## Summary of Calibration

**Round 1 bracket**: The paper sits between the weak contamination-detection papers (avg 3.0–3.33) and the mid-range ones (avg 4.67–5.5). It has a genuinely novel research question (translation masking contamination) that the weak anchors lack, but its experimental design and internal inconsistencies are more problematic than the mid-range anchors.

**Round 2 narrowing**: 
- *Fighting Fire with Fire* (3.33, Reject): Similar deliberate fine-tuning approach but cleaner execution. Current paper is slightly better due to novel angle.
- *Sensitivity of SLMs* (4.00, Reject): More systematic contamination study (23 models, multiple transformation types), but less novel question. Current paper is slightly weaker due to design issues.
- *Impact of Post-training* (4.67, Reject with mixed scores): More realistic contamination setup (pretraining vs. fine-tuning) and clearer findings. Current paper is notably weaker.
- *CoDeC* (5.33, Accept Poster): Clean idea with extensive validation. Current paper is substantially weaker in experimental rigor.

**Final score**: 3.5. The paper asks a timely question and has a nice methodological touch (choice-reordering TS-Guessing), but the experimental design cannot cleanly support the core claim and, more critically, the paper's interpretation directly contradicts its own data. The claim of "near-flat" performance is falsified by the monotonic MMLU increases shown in Table 2.

---

## Summary

This paper investigates whether translating benchmark data into Arabic masks data contamination while preserving its effects on model performance. The authors fine-tune four open-weight LLMs on varying proportions (0%, 10%, 50%, 100%) of Arabic-translated test sets of MMLU, XQuAD, and MLQA at *the same time* as the English test set, then evaluate on English benchmarks and probe memorization via a choice-reordering extension of TS-Guessing. They also propose an unimplemented Translation-Aware Contamination Detection (TACD) framework.

## Strengths

1. **Novel and timely research question.** The idea that translation into a lower-resource language could obscure contamination from standard English-only detection methods is genuinely important and underexplored. This paper is among the first to systematically probe this blind spot.

2. **Clean methodological extension to TS-Guessing.** The choice-reordering strategy for multiple-choice items (shuffling answer options before masking, then checking whether the model recalls the pre-shuffle index) is a concrete, reproducible improvement that strengthens the TS-Guessing probe. The IDR metric is well-motivated and provides interpretable evidence of index-based memorization (e.g., LLaMA-3.2-1B IDR of 0.643 at 50% contamination in Table 3a).

3. **Demonstrates task-type differentiation in contamination dynamics.** The paper's observation that MMLU (MCQ) exhibits monotonic accuracy gains with contamination while XQuAD/MLQA (extractive QA) show more erratic, model-specific patterns is a genuinely interesting finding that goes beyond treating contamination uniformly. This is clearly documented in Section 4.1 (e.g., Mistral MMLU 0.577→0.690 while XQuAD collapses from 0.455→0.114).

## Weaknesses

### Fatal
None.

### Major

1. **The paper's own data contradicts its core interpretive claim.** Section 4.2 states "the models exhibit approximately equal performance on all evaluated benchmarks" and "this near-flat trend indicates that Arabic→English translation is effectively masking contamination effects." But Table 2 shows *every* model's MMLU accuracy rising monotonically with contamination (Mistral: 0.577→0.690, a 20% relative increase; LLaMA: 0.332→0.431, a 30% relative increase). Even excluding p=0 (looking only at p∈{10,50,100}% as Section 4.2 specifies), Mistral jumps from 0.580→0.690 and LLaMA from 0.381→0.431. The TS-Guessing IDR values in Table 3a also show large swings (LLaMA 0.287→0.643→0.410). These are not "approximately equal" or "near-flat" by any reasonable standard. The paper's narrative is in direct tension with its empirical results. This is not a matter of minor overstatement — it is a fundamental mismatch between the data and the claimed interpretation.

2. **Experimental design does not isolate the effect of translation on contamination.** The training set is defined as D_EN ∪ D_AR(p), where D_EN is the *English test set itself*. Every condition (including p=0) already contains the full English test set as training data. This means:
   - The p=0 model is already contaminated with the exact evaluation material.
   - All comparisons between p=0 and p>0 conditions confound the *effect of translation* with the *effect of additional data* on top of an already-contaminated model.
   
   To support the claim that "translation conceals traditional contamination signals," the design needs at minimum: (a) a clean model with no test set exposure, (b) a model contaminated only via Arabic translation, and (c) a model contaminated only via English data to calibrate what "detectable" contamination looks like in this exact setup. Without these, the study cannot separate whether translation masks contamination or whether the effects are driven by the fact that all models (including the baseline) already memorized answers from the English test set.

3. **No clean baseline or same-language contamination comparison.** Related to point 2: the paper makes claims about translation "masking" contamination, but there is no condition where contamination is introduced in English alone. Without this control, claims about what is "masked" by translation are unsupported. A model trained on the English test set only (which is what p=0 essentially is) is not a "clean" baseline — it is a fully contaminated model.

### Minor

1. **Limited ecological validity.** The experiment fine-tunes models directly on test set items formatted as MCQ or QA pairs. Real contamination typically occurs during *pretraining*, where benchmark data appears as natural text within a massive corpus, not as explicit test items with answer options. This gap limits the practical relevance of the findings and should be explicitly discussed as a limitation.

2. **No error bars or variance reporting.** Tables 2 and 3 report only point estimates with no confidence intervals or significance tests. While single-run evaluation is common in some LLM settings, the paper's core claims about "flatness" vs. "change" across conditions would benefit substantially from some measure of uncertainty.

3. **The TACD framework is purely conceptual.** Section 5 describes an interesting research direction but contains no implementation, experiments, or validation. As presented, it does not constitute a research contribution beyond restating the obvious implication of the paper's findings. This should be kept or cut to a brief future-work paragraph.

4. **Model Arabic proficiency is asserted but not measured.** The paper claims models with "stronger Arabic capabilities" benefit more from contamination but provides no measure of Arabic language ability. This claim is untested.

### Trivial
None.

## Nice-to-Haves
- A same-language (English-only) contamination condition at matching proportions would decisively settle whether translation actually attenuates detection.
- Testing on held-out Arabic benchmarks to verify whether the model actually learned Arabic capabilities or simply memorized answer patterns.
- Including a pre-trained Arabic model or a model with verified Arabic proficiency to strengthen the cross-lingual analysis.

## Removed Points
- Criticisms about the paper not releasing code/data before acceptance → the paper states code will be released upon acceptance, which is standard.
- The claim that "the literature review is disconnected from the experiment" → the review competently covers the landscape and motivates the gap the paper addresses; some disconnect is inherent in a review section.
- The claim that "monotonic MMLU gains show contamination is not being masked" → this is an overstatement; the gains could still be masked from *detection* methods (TS-Guessing) while remaining behaviorally measurable, which is exactly what the paper explores.
- The formatting/style nitpicks and missing appendix complaints → these are parser artifacts or standard deferred material.
- Speculative criticism about "pretraining vs. fine-tuning" being a fatal flaw → this is a valid limitation but is acknowledged as minor; the paper focuses on fine-tuning contamination explicitly.
- Various generic strength claims from the Strength Finder (e.g., "addresses an important problem") → removed as not specific enough.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Redesign the experiment** to include a clean baseline (no test set exposure), an Arabic-only contamination condition, and an English-only contamination condition at matching proportions. This three-way comparison would cleanly isolate whether translation masks contamination relative to the same-language setting.
2. **Reconcile the interpretation with the data.** The monotonic MMLU increases in Table 2 are real and interesting — they show that even after the model has seen the English test set, additional Arabic-translated data further inflates scores. Frame this honestly rather than claiming "near-flat" trends.
3. **Add error bars or confidence intervals**, particularly for the TS-Guessing results where IDR values vary substantially across models and contamination levels.
4. **Either implement and validate the TACD framework** with concrete experiments, or remove it — an unimplemented "blueprint" does not constitute a contribution and can be 2-3 sentences in the conclusion.
5. **Include a dedicated limitations section** that acknowledges: the baseline contamination issue, the lack of a clean model, the fine-tuning versus pretraining gap, and the absence of Arabic proficiency controls.

## Score and Decision

**Score: 3.5**
**Decision: Reject**

**Calibration anchors used (all rounds):**

| anchor_id | avg_score | round | comparison |
|-----------|-----------|-------|------------|
| WERLf030OU (LogProber) | 3.00 | R1 | Same topic, similar design issues; current paper is slightly better due to novel angle |
| Ubi631nNbI (Variant Contamination) | 3.00 | R1 | Similar conceptual space; current paper has less rigorous validation |
| YsoabhpS7z (Auditing Test Data) | 3.00 | R1 | Contamination detection; current paper is more novel in question |
| jCkmwIN9kz (Fighting Fire with Fire) | 3.33 | R1/R2 | Most similar design (deliberate fine-tuning on test sets); current paper slightly better |
| WFGxFzFDmQ (Watermarking) | 5.00 | R1 | Cleaner execution and theoretical grounding; current paper is significantly weaker |
| l9jJYx9tnl (Poly-FEVER) | 5.00 | R1 | Unrelated benchmark paper; not directly comparable |
| C15sPKE4uR (Self-Bias) | 5.50 | R1 | Related translation topic but different task; not directly comparable |
| 29ETLxTQAN (Publishing Benchmarks) | 5.50 | R1 | Different problem framing; not directly comparable |
| GFDSGlEks2 (Post-training Impact) | 4.67 | R2 | More realistic contamination setup (pretraining); current paper is notably weaker |
| x4vwdjckZ6 (Sensitivity of SLMs) | 4.00 | R2 | More systematic study with multiple transformation types; current paper slightly weaker |
| YlpaaYxx4t (CoDeC) | 5.33 | R2 | Clean idea with extensive validation; current paper substantially weaker in rigor |
| 1BXojAgNrg (MedAraBench) | 4.67 | R2 | Arabic benchmark paper; not directly comparable |

The paper asks an important question and has a clever TS-Guessing extension, but it has two problems that preclude acceptance: (1) the experimental baseline is already contaminated with the English test set, so the design cannot cleanly separate the effect of translation from the effect of added data, and (2) the paper's central interpretive claim ("near-flat" performance, translation "masking" contamination) is directly contradicted by its own Table 2 data, which shows clear monotonic increases. A redesigned experiment with proper controls could yield a much stronger paper, but in its current form the claims are not adequately supported.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>