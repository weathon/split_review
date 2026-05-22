Now I have all the information needed. Let me produce the final consolidated review.

## Summary
The paper investigates whether translating benchmarks into Arabic can conceal data contamination in LLM evaluation. It fine-tunes four open-weight models on varying proportions (0%, 10%, 50%, 100%) of Arabic-translated test sets from MMLU, XQuAD, and MLQA, then evaluates on the original English benchmarks. It extends the TS-Guessing memorization probe with a choice-reordering strategy (IDR) for multiple-choice settings and proposes a conceptual Translation-Aware Contamination Detection (TACD) framework. The main claim is that translation masks contamination signals while still allowing models to benefit from exposed data.

## Strengths

- **Timely and underexplored research question.** The paper asks whether multilingual translation — specifically into a low-resource language like Arabic — creates a blind spot in contamination detection. This question is genuinely missing from the English-centric contamination literature.

- **Broad experimental design across models, datasets, and contamination levels.** The paper fine-tunes four different model families (Mistral-7B, LLaMA-3.2-1B, Gemma-3-1B, Qwen3-1.7B) on three datasets (MMLU, XQuAD, MLQA) at four contamination proportions (0%, 10%, 50%, 100%) using a consistent PEFT protocol. This breadth enables cross-condition comparisons and reveals model- and dataset-specific patterns that a narrower design would miss.

- **Novel TS-Guessing extension with choice-reordering (IDR).** The index-recall rate (IDR) adapts the TS-Guessing probe to multiple-choice settings by tracking whether a model reproduces the original answer letter after shuffling options. This is a methodologically sound extension of existing probe-based detection.

- **Identification of non-monotonic contamination patterns in extractive QA.** The paper documents that moderate contamination (10%) sometimes improves cross-lingual span extraction while heavier contamination degrades it (the "peak-at-10%" pattern in MLQA), revealing that contamination does not uniformly benefit all task types.

## Weaknesses

### Major

- **Factual contradiction between the central claim in Section 4.2 and the paper's own data.** Section 4.2 states: *"Across contamination levels p ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks."* This is directly contradicted by Table 2. To cite just a few examples: Mistral MMLU jumps from 0.580 (10%) to 0.690 (50%); Gemma XQuAD rises from 0.481 (10%) to 0.577 (50%) to 0.606 (100%); LLaMA XQuAD goes from 0.459 (10%) to 0.558 (50%); Qwen XQuAD goes from 0.429 (10%) to 0.510 (50%) to 0.564 (100%). Many metrics show substantial and meaningful variation across contamination levels. The paper's own Section 4.1 accurately documents these trends (calling MMLU "generally monotonic increase"), so Section 4.2's "approximately equal" claim is an internal inconsistency. This error is not a minor phrasing issue — it is the core evidential claim on which the "translation masks contamination" narrative rests, and the data do not support it as stated.

- **Confound between contamination and cross-lingual transfer is not addressed.** The experimental design fine-tunes models on Arabic-translated test sets and evaluates on English. The observed gains (especially on MMLU) could arise from cross-lingual transfer: seeing semantically equivalent questions in Arabic may help models learn better representations that generalize to English, without any memorization of answer strings. The paper repeatedly attributes performance increases to "contamination-driven memorization" (Section 4.1, Section 4.3) but never controls for this alternative mechanism. A control condition — for example, fine-tuning on Arabic translations of non-overlapping material and measuring English benchmark performance — is absent. Without it, the paper cannot conclusively attribute the observed gains to contamination rather than to genuine cross-lingual learning.

- **TS-Guessing signals are too weak and inconsistent to carry the argument.** The IDR values in Table 3a are low across the board: Mistral shows 0.000 IDR at all contamination levels; Gemma drops from 0.350 (10%) to 0.005 (100%); Qwen hovers around 0.2–0.26; only LLaMA shows notable IDR (0.643 at 50%, 0.410 at 100%). For XQuAD (Table 3b), EM scores are below 0.02 for all models except Mistral (0.074–0.103). The paper argues that translation "masks" these signals, but this creates a circular evidential chain: TS-Guessing fails to detect contamination because translation masks it, yet we are supposed to believe contamination exists because performance rises. If the dedicated memorization probe cannot detect contamination even at 100% exposure, the claim that contamination is the mechanism driving performance gains requires additional evidence beyond what is presented.

- **TACD framework is presented but not validated.** The proposed Translation-Aware Contamination Detection framework is described as "a forward-looking blueprint rather than a complete implementation" with no experiments validating any of its components. No results are shown for cross-translation benchmarking, TS-Guessing across translation variants, or back-translation consistency. This limits the contribution to a conceptual suggestion, and the paper would benefit from even a single proof-of-concept experiment demonstrating that TACD can surface contamination that English-only checks miss.

### Minor

- **No evaluation of existing contamination detection methods on translated data.** The paper claims that standard English-only checks fail on translated benchmarks but never tests this claim. Running Min-K% Prob or a guided-prompt method on the Arabic-translated data and showing they fail would substantiate the "blind spot" argument and is a natural experiment given the paper's setup.

- **No Arabic-language evaluation is reported.** The paper only evaluates on English. Reporting Arabic performance on the Arabic test sets would help separate contamination from transfer: if a model trained on Arabic MMLU translations also scores higher on Arabic MMLU, that could indicate contamination; if it scores higher on English MMLU but not Arabic, it points more toward transfer through shared representations.

- **Statistical significance is not reported.** Given that the paper makes claims about trends across contamination levels (monotonic, non-monotonic, flat), confidence intervals or significance tests would help assess whether observed differences (e.g., Mistral MMLU 0.580→0.690) are reliable or within noise ranges.

### Trivial

None.

## Nice-to-Haves

- Adding a control condition (fine-tuning on Arabic translations of non-overlapping benchmarks) to isolate the contamination mechanism from cross-lingual transfer.
- Running existing contamination detectors (Min-K% Prob, guided prompting) on the Arabic-translated data to empirically demonstrate their failure.
- Validating TACD with at least one simple experiment (e.g., TS-Guessing on a French translation of MMLU after Arabic training).
- Reporting confidence intervals or variance across runs.

## Removed Points
These points were raised by reviewers but removed after verification against the paper:
- *Criticism about missing appendix/proofs* — Removed per hard rules: the parser strips appendix sections from all papers.
- *Criticism about undisclosed hyperparameters* — Removed per hard rules: hyperparameters are deferred to appendix A which exists in the original submission.
- *Criticism that the paper does not compare findings to what prior methods would detect* — Partially removed because the paper does discuss existing methods extensively in Section 2; however, the point about not *running* existing detectors on the translated data is retained as a Minor weakness.
- *Strength about "rigorous multi-model design"* — Retained but merged with conciseness.

## Novel Insights
None beyond the paper's own contributions. The observation that non-monotonic contamination effects appear in extractive QA (the "peak-at-10%" pattern) is interesting but the reviews did not surface a deeper or different interpretation.

## Suggestions

1. **Correct the misrepresentation of Table 2 in Section 4.2.** Remove or carefully qualify the "approximately equal performance" claim, which is factually contradicted by the data. The paper should acknowledge which benchmarks show sensitivity to contamination levels and discuss this rather than asserting flatness.

2. **Add a control for cross-lingual transfer.** Fine-tune the same models on Arabic-translated *non-test-set* material (e.g., Arabic versions of datasets not used for evaluation) and measure English performance on the target benchmarks. If the gains vanish, contamination is supported; if they persist, transfer is at play.

3. **Validate at least one component of TACD.** Even a single experiment — running TS-Guessing with IDR on a non-Arabic translation variant (e.g., French MMLU) after Arabic training — would demonstrate whether the proposed cross-lingual approach can surface contamination that English-only checks miss.

4. **Run existing detectors on the Arabic-translated data.** Directly test the claim that standard English-only methods fail on translated data by applying Min-K% Prob or Golchin & Surdeanu's method to the Arabic-translated benchmarks.

5. **Report statistical significance or variability estimates** to assess whether observed differences across contamination levels are meaningful.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| MyotJECv0D (Correlation Analysis of Evaluation Metrics for MT) | 2.50 | R1 (low) | Much weaker; no contamination analysis. Our paper is clearly stronger. |
| fSbPwHjdDG (Llamas think in English) | 3.00 | R1 (low) | Different topic, comparable writing quality. Our paper has more experimental breadth. |
| JQbqaQjV7D (Industrial Benchmarking of LLMs) | 3.00 | R1 (low) | Tangential topic, similar quality. Our paper is slightly more focused. |
| Nk1MegaPuG (Evading Data Contamination Detection) | 4.25 | R1 (mid) | Most directly comparable — similar topic (contamination evasion), similar level of rigor. Both have interesting ideas but execution flaws. |
| rAylWUIKtu (Benchmark Inflation) | 4.25 | R1 (mid) | Comparable quality. Both have reasonable contributions undermined by execution limitations. |
| lwtaEhDx9x (Elephants Never Forget) | 4.75 | R2 (mid) | Slightly stronger — more specific methodological tests, less internal contradiction. Our paper is below this anchor. |
| QiyQJqpcYe (Linguini benchmark) | 4.75 | R2 (mid) | Tangential topic, similar quality level. |
| Nsms7NeU2x (How much can we Forget) | 6.75 | R1 (mid) | Substantially more rigorous with both theory and controlled experiments. Our paper is clearly below this anchor. |
| m2NVG4Htxs (To the Cutoff and Beyond) | 6.75 | R1 (mid/strong) | Accepted paper with clean design and clear evidence. Our paper is below this anchor. |
| jOmk0uS1hl (Training on the Test Task) | 8.00 | R1 (strong) | Much stronger contribution and rigor. Not comparable. |

**Round 1 bracket:** 3.5–5.5 (between the weak and middle bands)

**Round 2 narrowing:** The paper sits near the low-to-mid end of this bracket, comparable to "Evading Data Contamination Detection" (4.25) and "Benchmark Inflation" (4.25), slightly below "Elephants Never Forget" (4.75). It is substantially below the 6.75 anchors in both experimental rigor and the quality of claims relative to evidence.

**Final score: 4.0**

This paper identifies a genuinely relevant and underexplored question, and the multi-model multi-dataset experimental design shows ambition. However, it suffers from (a) a factual contradiction between its central claim in Section 4.2 and its own data in Table 2, (b) an unaddressed confound between contamination and cross-lingual transfer that undermines causal attribution, (c) weak and inconsistent TS-Guessing probe results that the paper cannot reconcile with its own narrative, and (d) an unvalidated TACD framework. These issues collectively prevent the paper from convincingly establishing its main conclusions. The paper could be substantially strengthened by correcting the misrepresentation, adding a control condition, and validating at least a component of TACD.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>