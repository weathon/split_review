Now I have all the information needed. Let me compose the final review.

---

## Summary

This paper proposes the QK-score and Attention-score, two methods that extract answer predictions from specific "select-and-copy" attention heads in LLMs, rather than from the final output logits. The key finding is that these heads' attention patterns (QK dot products and attention weights) consistently outperform the standard logit-based baseline on multiple-choice QA tasks, yielding 7–16% accuracy gains for LLaMA2-7B across four benchmarks and up to 27% for LLaMA3-8B on HellaSwag. The method requires no fine-tuning, works across model scales (7B–70B), and identifies stable heads (most notably (14,20) and (14,24)) that generalize across datasets, shot settings, and even synthetic tasks with many options.

## Strengths

1. **Consistent and substantial accuracy gains across diverse benchmarks and model sizes.** The QK-score improves LLaMA2-7B by 7–16% on all four real-world datasets in zero-shot (Fig. 3), achieves up to 27% improvement on HellaSwag for LLaMA3-8B (Table 1), and reaches near-perfect accuracy on a synthetic word-matching task where the baseline hovers near random (Fig. 5b). These gains are demonstrated across LLaMA2, LLaMA3, base and chat variants, and model sizes from 7B to 70B.

2. **Identification of stable, universal select-and-copy heads.** The paper shows that heads (14,20) and (14,24) in LLaMA2-7B appear in the top 5% of best heads across all four datasets and multiple shot settings (Fig. 5a). These same heads also maintain strong performance on the synthetic dataset even as the number of options scales up to 24 (Fig. 5b), confirming that they implement a general option-selection mechanism rather than dataset-specific artifacts.

3. **Causal evidence through zero-ablation.** Ablating the top 10 select-and-copy heads causes accuracy to drop sharply (often below random chance), while ablating random heads from the same layers does not (Fig. 4). This provides direct causal evidence that these heads are functionally important for correct MCQA output.

4. **Increased robustness to option order and extra options.** The QK-score achieves higher Permutation Accuracy than both the baseline and PriDe on most datasets (Fig. 3, Table 1), and remains effective when "None of the above" and "I don't know" options are added — a realistic extension that existing debiasing methods (PriDe) struggle with (Section 4.1).

5. **Unsupervised head identification without labeled data.** The paper proposes a heuristic based on attention concentration and cross-option variance that ranks the same stable heads in the top-20 without any labeled validation data (Section 5), making the approach usable when ground-truth labels are scarce.

6. **Systematic analysis of option-representative tokens.** The paper compares end-of-line, label, period, and content tokens across 0-shot and 5-shot settings (Fig. 2b), providing practical guidance for applying the method.

## Weaknesses

### Fatal
None.

### Major
None. The weaknesses are all minor to moderate and addressable.

### Minor

1. **No comparison against a simple probing baseline.** The QK-score accesses intermediate representations. A natural baseline would be a linear probe or logit-lens on the hidden states (e.g., unembedding the last-token or option-token representations to predict the answer). Without this baseline, it is unclear whether the gains stem from the specific QK-score formulation or simply from using intermediate-layer representations instead of the final logits. This is the most significant gap in the evaluation.

2. **PriDe comparison is incomplete for larger models.** PriDe is only compared in the main LLaMA2-7B results (Fig. 3) and is absent from the large-model table (Table 1). While the paper states that QK-score outperforms PriDe "in all cases" (line 190), the data for larger models only includes the Baseline vs. QK-score comparison. This does not invalidate the results but limits the reader's ability to verify the claim across model scales.

3. **The head selection procedure (best head from 5% validation set) would benefit from stability analysis.** The paper selects the single best head based on accuracy on 5% of each dataset (~700 examples for MMLU). While the cross-dataset consistency of heads (14,20) and (14,24) partially mitigates overfitting concerns, the paper does not report variability (e.g., standard deviations, multiple validation splits) to show that the top head is stable rather than a noisy winner. The unsupervised head-finding method (Section 5) helps address this, but a direct stability analysis would strengthen the claim.

4. **The "select-and-copy" mechanism label is partially inferred rather than directly traced.** The ablation experiments and attention maps convincingly show that these heads *select* the correct option. However, the "copy" aspect — i.e., tracing the head's value output to the final residual stream and showing it is responsible for the model's answer — is not directly demonstrated. Targeted interventions such as activation patching of the selected token's value vector would be needed to fully verify the copy claim. This is a nuance that does not undermine the practical results but tempers the mechanistic claim.

5. **MMLU is a clear failure case for larger models that is acknowledged but not deeply analyzed.** For LLaMA2-70B on MMLU, the baseline accuracy (59.7) exceeds QK-score (56.7) (Table 1). The paper notes this briefly (line 193) attributing it to MMLU's focus on general knowledge vs. semantic relations, but does not analyze *why* the select-and-copy mechanism breaks down on this particular combination of dataset and model scale. Understanding this failure mode would help clarify the method's scope.

6. **No error bars or significance tests are reported.** All accuracy numbers are reported as point estimates without variance. Given the single-run evaluation and the head selection on a small validation set, this omission weakens statistical confidence in the reported gains. (This is somewhat mitigated by the pattern of consistent improvement across many datasets and models.)

### Trivial

1. **Ambiguous phrasing of "increases by almost 60%."** The abstract states accuracy on the synthetic dataset "increases by almost 60%." The baseline is ~25%, and the method achieves ~85% (near perfect). This is ~60 percentage points or ~240% relative increase. The phrasing could be read as ambiguous ("60% absolute" vs. "60% relative"), though the context ("achieving nearly perfect accuracy") makes the intended meaning clear. This should be clarified to e.g., "increases by almost 60 percentage points."

2. **Permutation Accuracy (PA) uses a single random permutation.** The paper defines PA using one random permutation of options (line 175–180), whereas some prior work averages over multiple permutations. Using only one permutation makes the PA metric noisier. Clarifying whether multiple permutations were considered would be helpful.

## Nice-to-Haves

- **Add a probing/logit-lens baseline:** Train a linear probe on the hidden states at the last token or option-representative token positions and compare accuracy to the QK-score. This would isolate whether the gains come from the QK-score formulation or simply from using intermediate representations.
- **Report head selection stability:** Use cross-validation or multiple random validation/test splits with standard deviations to show that the top head is not a noisy winner on the 5% validation set.
- **Evaluate the unsupervised head selection method on test accuracy directly:** The paper shows that unsupervised heads rank in the top-20 (Section 5), but does not report their actual test accuracy. If these heads match the task-specific heads' performance, the method becomes substantially more practical.
- **Analyze the MMLU failure case more deeply:** Investigate which types of MMLU questions cause the QK-score to underperform, and whether this is related to option content similarity, knowledge type, or something else.
- **Quantify computational overhead:** Report the additional cost (inference time or memory) of extracting QK-scores across all heads vs. a standard forward pass.

## Removed Points

The following criticisms from the reviewer have been removed as they are factually incorrect or based on a misunderstanding of the paper:

- **Criticism about QK-score omitting positional information (Point 4 from harsh critic):** The critic claimed the QK-score omits RoPE "without justification" and that the dot product is not comparable across positions. However, the paper *explicitly and intentionally* removes positional encoding from the QK-score ("In QK-score we do not apply positional transformation," line 117) precisely *because* it aims to compare tokens based on semantic content rather than position (line 88: "to mitigate the effect of the relative position shift"). The QK-score uses raw query and key vectors before RoPE is applied, so positional disparity is *not* a confound. This criticism reflects a misreading of the paper.
  
- **Criticism that SSD results don't support the "knowledge trapped by format" claim (part of Point 3):** The critic argued the SSD baseline failure shows "the model does not understand the instruction" rather than that knowledge is "trapped by format." But the paper's framing is consistent: the model possesses the correct answer (which is literally given in the question) but the *output format* (selecting the letter) blocks it. The method succeeds by reading internal representations. The SSD result cleanly supports this interpretation. The nuance the critic raises does not contradict the paper's claim.

## Novel Insights

The reviews surface one genuinely novel insight beyond the paper's own contributions: the fact that the two most stable heads, (14,20) and (14,24), have *complementary* selection biases — one favors A/D while the other favors B/C (Section "Selection bias," line 303). This suggests the model may route information through multiple parallel option-selection channels, and that the QK-score could potentially be improved further by combining heads rather than picking a single one. This observation is mentioned but not deeply explored in the paper.

## Suggestions

1. **Add a probing/logit-lens baseline** to distinguish the QK-score's contribution from the general informativeness of intermediate representations.
2. **Report head selection stability** via multiple validation splits or bootstrap estimates.
3. **Provide error bars** (e.g., variance across validation splits) for the main accuracy numbers.
4. **Include PriDe on larger models** in the main table for completeness, or clearly state why it was omitted.
5. **Clarify the "60%" phrasing** and the PA permutation count.

## Score and Decision

The paper makes a genuine and well-supported contribution: it identifies a previously underappreciated functional class of attention heads and derives a simple, zero-cost scoring method that consistently improves MCQA accuracy without any training. The empirical scope (multiple datasets, multiple model sizes up to 70B, zero-shot and few-shot) is solid. The main weaknesses — the absence of a probing baseline and the lack of error bars — are addressable and do not threaten the core findings. The cross-dataset consistency of the identified heads and the unsupervised selection heuristic partially compensate for the validation-set stability concern.

**Originality:** Good — QK-score and the select-and-copy head characterization are novel.  
**Importance:** Good — improving MCQA evaluation is practically relevant.  
**Claims supported:** Adequate — core results are well-supported; some mechanistic claims (e.g., "copy") are partially inferred.  
**Soundness:** Adequate — methodology is reasonable but missing a probing baseline and error bars.  
**Clarity:** Good — the paper is clearly written and well-structured.  
**Value to community:** Good — the method is simple, model-agnostic, and can be applied by any practitioner running MCQA.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>