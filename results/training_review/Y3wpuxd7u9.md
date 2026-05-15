Now I have all the information needed. Let me write the consolidated review.

## Summary

The paper introduces GoLLIE, a method that fine-tunes Code-LLaMA to follow annotation guidelines for zero-shot Information Extraction. The key idea is to represent IE tasks as Python code where label definitions become docstrings and representative annotation candidates become code comments, then train the model with regularizations that force it to attend to these guidelines rather than memorizing label names. Across 17 zero-shot evaluation settings, GoLLIE (7B) achieves 55.3 F1 compared to the controlled baseline of 42.3 F1 (+13 points), and the ablation study traces the gain primarily to the guidelines themselves and the representative candidates.

## Strengths

- **Clean controlled internal comparison establishes that guidelines help.** The paper compares GoLLIE against a baseline (Code-LLaMA fine-tuned without guidelines) while keeping the backbone, training data, and procedure identical. The +13 F1 gain provides direct evidence that guidelines improve zero-shot IE, not confounded by model size or data differences.

- **Ablation with statistical testing identifies the key mechanisms.** The paper reports p-values for each regularization component. Removing candidates causes the largest drop (55.3→49.9, p=2.2e-10), and removing guidelines entirely (baseline) drops to 42.3 (p=5.1e-13). This precisely identifies what drives the gain: guidelines help even without candidates (+7.6 F1), and candidates add further benefit.

- **Supervised performance is preserved.** GoLLIE achieves 73.0 average F1 vs. 73.3 for the baseline on supervised datasets (Table 1). The noise injected for generalization does not degrade in-domain performance.

- **Error analysis reveals genuine understanding, not memorization.** The paper shows that GoLLIE handles polysemous labels well (e.g., MultiNERD Media: 13.6→69.1), follows guidelines even when gold annotations are inconsistent (MultiNERD Time), and has interpretable failure modes on ambiguous labels. The "seen vs. unseen labels" analysis (Figure 2) further confirms the model generalizes to genuinely new labels.

- **Code-based representation is well-motivated and practical.** Representing IE tasks as Python classes with docstrings leverages LLMs' code training, ensures parseable output, and provides a natural format for incorporating guidelines. This is a reproducible engineering contribution.

## Weaknesses

### Fatal

None. The core claim (guidelines improve zero-shot IE) is supported by the controlled baseline comparison, and the methodological concerns raised do not invalidate this result.

### Major

1. **Guidelines for some evaluation datasets were created from development-split annotations, creating a transparency issue for the zero-shot claim.** The paper states (line 137): *"When such guidelines are not publicly available, we ask human experts to create them, based on the annotations from the development split."* This is disclosed but not discussed. The paper does not specify which evaluation datasets had public guidelines vs. which were created from development splits, making it impossible to assess whether the zero-shot setting is pure for all datasets. While guidelines are label descriptions (not labeled examples), the practice departs from a strict zero-shot protocol. The paper should (a) disclose per-dataset guideline provenance, (b) discuss whether this inflates results, and (c) ideally rerun on a subset where guidelines are purely public to confirm the finding.

2. **The SoTA comparison is confounded and overclaimed.** The paper claims GoLLIE "outperforms previous attempts at zero-shot information extraction," but the comparison against Instruct-UIE (Flan-T5 backbone, 34 training datasets) and PromptNER (GPT-3.5) differs in backbone, training data size, and representation format. The paper acknowledges these differences (lines 257-258) but still attributes the gains entirely to guidelines. This is logically unsupported — the gain could come from Code-LLaMA being better at code-based tasks, from the specific training data mix, or from QLoRA hyperparameters. The controlled baseline comparison is the valid evidence; the SoTA comparison should be presented as suggestive but not conclusive, and the SoTA claim should be tempered.

3. **The representative candidates for evaluation datasets may come from target-domain labeled data.** For evaluation datasets where guidelines are created from development splits, the paper says candidates are "sampled from the train split based on word frequency or manually curated based on the guidelines" (line 137). The phrase "the train split" is ambiguous but likely refers to the evaluation dataset's own split. If candidates are taken from the evaluation dataset's labeled data and presented at inference time, this blurs the zero-shot distinction — the model sees examples from the target distribution. The ablation showing candidates are the most important component (49.9→55.3, +5.4 F1) makes this especially important to clarify. The paper should report results with candidates sourced only from public guidelines (or from a held-out source) to verify the zero-shot claim.

### Minor

1. **Three of five regularizations are statistically insignificant.** Class order shuffling (p=0.072), paraphrasing (p=0.11), and class name masking (p=0.10) do not significantly affect performance. The paper acknowledges this (line 299) but the method description in Section 3.2 presents the five techniques as a unified approach. The paper would be cleaner and more honest by either (a) simplifying to the components that matter (guidelines, candidates, dropout) or (b) explicitly noting that the ineffective components are retained only because they do no harm.

2. **No correction for multiple comparisons in the ablation.** The p-values are one-sided and uncorrected for the six hypothesis tests. Given that 3/6 comparisons are "not significant," correcting for multiplicity would only strengthen that conclusion, so this is not a fatal issue, but it should be noted.

3. **The origin of the "fixed pool of 10 candidates per class" is unspecified.** The paper says candidates are sampled from a pool of 10 per class but does not explain how the pool is constructed. This is a reproducibility gap.

4. **Minor overstatement: "Average SoTA" vs. "Average all" are computed over different dataset subsets.** Table 4 reports "Average SoTA" (42.6) over 7 datasets where prior results exist, while "Average all" (42.3 for baseline, 55.3 for GoLLIE) is over all 17 evaluation settings. The paper should make this discrepancy explicit to avoid misleading comparisons.

### Trivial

- The ablation table uses "w/o" (without) inconsistently in formatting.
- The sentence about "detailed representative annotation candidates" is truncated in the abstract (line 7-8).

## Nice-to-Haves

- **Per-dataset guideline provenance table:** A supplementary table listing each evaluation dataset, whether its guidelines were publicly available or created from the development split, and where candidates came from. This is the single most impactful addition for assessing the zero-shot claim.
- **Candidate-source ablation:** Rerun zero-shot evaluation with candidates from a held-out source (e.g., unrelated domain's guidelines) to measure how much of the gain depends on candidates being from the target distribution.
- **Controlled SoTA comparison:** Fine-tune Flan-T5 (or another backbone) using the code representation with and without guidelines to isolate the guideline effect from backbone effects.

## Removed Points

These points were raised by reviewers but are removed or downgraded after cross-checking against the paper:

- **"The zero-shot evaluation is contaminated — this is structural and unfixable"** (Harsh Critic #1, fatal framing). This overstates the issue. Guidelines are label descriptions, not training examples. The practice of creating guidelines from dev splits is disclosed (line 137). The controlled baseline comparison shows guidelines help; this result is not invalidated by the guideline source, though transparency about which datasets are affected is needed. Moved from "Fatal" to "Major" (#1 above) with adjusted severity.

- **"The model may simply pattern-match to candidates rather than generalize"** (Harsh Critic, end of Issue 4 and calibration section). The ablation shows even without candidates, GoLLIE (49.9) significantly outperforms the baseline (42.3) by +7.6 F1. So the model does generalize from definitions alone. The concern about over-reliance on candidates is valid but the data show the model doesn't collapse without them.

- **"The guidelines for MultiNERD Time... if created from dev split, this success is circular"** (Harsh Critic, Section 6 comment). This misreads the error analysis. The paper's point is that the model follows the guideline correctly even when the dataset annotations are inconsistent (years labeled as Time per guidelines but not annotated in the gold data). This demonstrates guideline-following regardless of guideline source. Removed.

- **"Training data selection (12 vs 34 datasets) may favor test domains by coincidence"** (Harsh Critic, Issue 2). This is speculative without evidence that the selection favors test domains. The paper explicitly chose training data from News/Biomedical and evaluation from diverse domains to avoid this. Removed.

- **Strength Finder's generic framing** (e.g., "large and consistent zero-shot gains"). Some strengths were reproduced but verified against explicit experimental evidence. Retained strengths cite specific numbers from tables.

## Novel Insights

The reviews surface an important nuance: GoLLIE's gain decomposes into two parts — a ~7.6 F1 gain from label definitions alone (guidelines docstrings, w/o candidates → baseline gap) and an additional ~5.4 F1 from in-target-distribution candidate examples (full GoLLIE → w/o candidates gap). The fact that three of five regularizations designed to force guideline-following are statistically insignificant (shuffling, paraphrasing, masking) while candidate sampling dominates suggests the model may be leveraging guidelines more as a disambiguation signal (via concrete examples) than as abstract rules. This raises a deeper question for the field: does "following annotation guidelines" in LLMs primarily mean understanding definitions, or does it mean pattern-matching to representative examples? The paper's error analysis supports both interpretations, and future work should disentangle them.

## Suggestions

1. **Add a per-dataset provenance table** showing which evaluation datasets had public guidelines, which had guidelines created from dev splits, and where candidates were drawn from. This is essential for the zero-shot claim to be verifiable.

2. **Temper SoTA claims** to focus on the controlled baseline comparison. Present the Instruct-UIE/PromptNER comparisons as suggestive but acknowledge confounders.

3. **Simplify the method description** to accurately reflect which regularizations matter. Either drop shuffling, paraphrasing, and masking from the final method, or explicitly frame them as "harmless additions" rather than core components.

4. **Clarify candidate sourcing:** Specify exactly which split's train data is used for candidate sampling when guidelines are not public. If candidates come from evaluation-dataset splits, discuss the implications for the zero-shot framing.

5. **Report results without candidates** (already in ablation but could be elevated) to make clear that the core contribution — using label definitions — works even without any target-domain examples.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>