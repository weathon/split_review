Here is my consolidated final review.

## Summary

This paper proposes three multi-objective optimization (MOO) frameworks — single-level VS-ASR, bilevel VC-ASR, and multilevel VM-ASR — for multilingual multi-task ASR (combining ASR and speech-to-text translation). The central claim is that separating highly conflicting objectives into different optimization levels (MLO) yields better performance than single-level or bilevel MOO. The main experiments on CoVoST 2 show VM-ASR achieving up to 23.7% relative WER improvement and 27.9% relative BLEU improvement over a two-stage pre-training + fine-tuning baseline.

## Strengths

- **Consistent empirical evidence that VM-ASR outperforms baselines on CoVoST 2.** Tables 1 and 2 show VM-ASR (both UAS and USA sequences) surpassing baselines and the single-level/bilevel alternatives across five ASR languages and four S2TT directions, for both 100M and 58M model sizes. The gains are substantial (up to 23.7% relative WER, 27.9% relative BLEU) and hold across languages and model scales.

- **Ablation of penalty parameter importance.** Table 3 compares penalty parameter increase rates of 0.002 vs. 0.02 per epoch, showing that well-calibrated penalties improve ASR WER by 8.3% and S2TT BLEU by 2.2%. This supports finding F4 and provides practical guidance for practitioners.

- **Transparent reporting of computational trade-offs.** The paper explicitly states that MOO methods use ~11.6 GB GPU memory and ~2.8 hours per epoch versus 8.7 GB and 2.25 hours for the baseline, acknowledging the cost while justifying it with performance gains. This is useful for practitioners evaluating deployment feasibility.

## Weaknesses

### Major

- **Claim F3 (task-based hierarchy outperforms language-based hierarchy) has no quantitative supporting evidence.** The paper states this as a finding but shows no experimental comparison. The only hierarchy variants in Tables 1–2 are task-based (UAS: self-supervised→ASR→S2TT; USA: self-supervised→S2TT→ASR). Remark 1 mentions language-based MLO involving LibriSpeech (English) and AISHELL (Chinese) was attempted, but no results, ablations, or even a single number comparing task-based vs. language-based hierarchy appears anywhere in the paper. Figure 3 (referenced as an "illustration of gradient conflicts") might show gradient conflict patterns but does not by itself demonstrate superior accuracy. This is a central claim in the findings that is entirely unsubstantiated.

- **LibriSpeech and AISHELL results are promised but absent.** The abstract states "We conduct an extensive investigation using the LibriSpeech and AISHELL v1 datasets for ASR" and the contributions repeat this. However, all main results (Tables 1–3) are from CoVoST 2 only. No ASR WER numbers for LibriSpeech or AISHELL appear anywhere in the extracted paper. The paper also states "Additionally, we performed experiments with a combination of the LibriSpeech and AISHELL datasets" (Section 5) but no results follow. There is no reference to an appendix containing these results. This omission means the paper cannot support its claims about language-level conflict analysis or the investigation of language-based hierarchy.

- **Mismatch between the formal problem formulations and the actual update rules.** Section 3.2 formulates VC-ASR as a *constrained* vector optimization with an explicit ε-threshold constraint (l_u(θ) − min l_u(θ) ≤ ε), and VM-ASR as a *multilevel* nested optimization problem. However, the update rules in Section 4 (equations 7 and 8) are simple weighted gradient sums with penalty parameters η and η₁ — no constraint satisfaction mechanism, no ε-based projection or feasibility check, and no sequential/nested level-solving. The ε threshold never appears in the algorithm description or hyperparameters (its value is never stated). The VC-ASR update is indistinguishable from adding the self-supervised gradient with a fixed penalty weight, and the VM-ASR update collapses all levels into a single gradient step. The paper needs to clarify whether these are penalty-method approximations and, if so, how they connect to the presented formulations.

### Minor

- **No measures of uncertainty or statistical significance.** All reported WER and BLEU values are single numbers without error bars, confidence intervals, or significance tests. Some differences between methods are small (e.g., VS-ASR vs. VC-ASR for English at 100M: 4.5 vs. 4.7 WER), making it difficult to assess reliability. While single-run evaluation is common in ASR, reporting at least 2–3 seeds for the key comparisons would substantially strengthen the claims.

- **Insufficient detail on the MoDo weight computation algorithm.** The dynamic weights λ in equations (5)–(8) are computed using the "MoDo algorithm" (Chen et al., 2023), but no description of MoDo is given, nor any adaptation details for this setting. Whether λ is recomputed at each gradient step, how the quadratic programming or gradient aggregation is performed, and how the weights for self-supervised and supervised objectives interact are all unspecified.

- **The ε threshold for VC-ASR is never specified or ablated.** The VC-ASR formulation (Section 3.2) introduces a constraint l_u(θ) − min l_u(θ) ≤ ε, but the value of ε is never stated in the hyperparameters section (Section 5) or anywhere else. It is unclear whether ε was set to zero, some small value, or simply not enforced.

- **Generic limitations section.** The limitations paragraph (Section 6) only says "further theoretical analysis would be interesting" without acknowledging any of the evaluation gaps, the missing dataset results, the formulation-algorithm simplification, or the lack of ablation on key design choices.

### Trivial

- **Figure 1 (radar plots)** is described only in its caption and is not discussed in the body text or tied to specific numerical results. An in-text explanation would improve interpretability.

- **Minor presentational issues:** The paper contains some misspellings ("confilcting" appears multiple times), and the text overflow formatting in equations could be cleaner.

## Nice-to-Haves

- A comparison of task-based vs. language-based hierarchy (if the experiment was run, as Remark 1 suggests) would allow the paper to substantiate or remove F3.
- A gradient conflict analysis (cosine similarity between objective gradients) would strengthen the motivation for MLO beyond the descriptive statements.
- An ablation of multiple ε values (for VC-ASR) and η penalty schedules would demonstrate algorithm robustness.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Section 5.2 content is empty in extracted text:** The harsh critic notes that Section 5.2 appears cut off. This is a parser artifact — the content exists in the original submission. Not a real weakness.
- **Criticism about Figure 1 being "decorative."** Figure 1 is referenced and described with a caption. While it could be better integrated into the text, this is a trivial presentation preference, not a substantive weakness.
- **"The paper should also cover Y / additional domains."** The paper's scope is clear (multilingual multi-task ASR on the chosen datasets). Demands for broader coverage constitute scope creep.
- **Strength Finder's claim that F3 is demonstrated.** The strength finder asserts this is supported, but verification shows no experimental comparison exists. This strength is removed because the corresponding weakness is verified.
- **Criticism about "not a multilevel algorithm in any standard sense."** Many practical MLO methods use penalty-based single-level reductions. The criticism is somewhat overstated; the real issue is the presentation gap between formulation and algorithm, not that the algorithm is fundamentally wrong.

## Novel Insights

The reviews surface one insight beyond the paper's own claims: the paper's core empirical finding (VM-ASR > VC-ASR > VS-ASR) on CoVoST 2 is credible and practically useful, but the paper's presentation overpromises in ways that could be fixed without changing the experiments. The formulation-algorithm mismatch is the deepest structural issue because it blurs what "multilevel optimization" actually means in this context — the paper's VM-ASR is effectively a penalty-weighted gradient aggregation scheme that prioritizes objectives via fixed penalty schedules, not a solver for the nested optimization problem written in Section 3.2. Recognizing this would let the authors reframe the contribution more honestly as an empirical study of objective-level separation via penalty-based weighting, which is itself a valid and useful finding.

## Suggestions

1. **Either remove claim F3 or provide the missing comparison.** If language-based hierarchy experiments exist (Remark 1 suggests they were run), include the results in a table. If they were not run, remove F3 entirely.
2. **Reconcile the formulations with the algorithms.** Explicitly state that VC-ASR and VM-ASR use penalty-method approximations of the constrained/multilevel formulations. Specify the ε value for VC-ASR or remove ε from the formulation and describe VC-ASR as a weighted-sum method with a separate penalty on the SSL loss.
3. **Add LibriSpeech and AISHELL results** to support the abstract's promises, or remove references to these datasets from the contributions.
4. **Add error bars or confidence intervals** for at least the key comparisons (VM-ASR vs. top baseline) with 2–3 random seeds.
5. **Provide MoDo adaptation details** sufficient for reproducibility: describe how λ weights are computed, how often they are updated, and whether any modifications were made for the ASR setting.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>