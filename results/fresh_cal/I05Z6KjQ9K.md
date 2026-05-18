## Summary

This paper studies cross-prompt adversarial attacks on Vision-Language Models (VLMs) — generating a single image perturbation that transfers across diverse text prompts. The authors identify a "non-stationarity" problem when naively optimizing with multiple prompts and propose GrCPA, a method that clips the k largest/smallest gradient elements in the Attention and MLP blocks of the LLM during backpropagation to reduce overfitting. Experiments on Flamingo, BLIP-2, LLaVA-1.5, and InstructBLIP across four task types show GrCPA consistently outperforms Single-P, Multi-P, and CroPA baselines, and improves attack stability.

---

## Strengths

- **Consistent empirical improvement over prior SOTA (CroPA).** Table 1 shows GrCPA beats CroPA on all four task types for Flamingo across multiple target answers (e.g., VQA_specific: 0.58 vs. 0.49; Image Classification: 0.45 vs. 0.37). The improvement, while sometimes modest, is directionally consistent, supporting the method's practical value.

- **Quantified improvement in attack stability.** Table 2 directly measures output consistency across iterations 900–1000, showing GrCPA improves stability over CroPA (e.g., VQA_specific: 0.82 vs. 0.70; Image Classification: 0.64 vs. 0.52). This addresses the non-stationarity problem the paper identifies and provides a secondary evaluation axis beyond raw ASR.

- **Ablation confirms both visual and textual modalities matter.** Table 5 (ablation of single-modality regularization) shows that regularizing only visual or only textual features reduces ASR (from 0.44 to 0.38/0.34), supporting the design choice and distinguishing GrCPA from single-modality heuristics.

- **Evaluated across multiple VLMs and task types.** The paper tests on Flamingo, BLIP-2, LLaVA-1.5, and InstructBLIP across image classification, captioning, general VQA, and specific VQA. Multi-model, multi-task evaluation strengthens the generality claim.

---

## Weaknesses

### Major

1. **ASR evaluation metric is underspecified and lacks a clean baseline.**  
   The paper reports ASR by "inducing the model to output specific text" (§4.1) but never states whether success requires an exact match, substring match, or semantic equivalence. Target texts include "unknown", "not sure", "very good", "too late", "metaphor" — some of which (e.g., "very good") could appear naturally in model outputs without any attack. No clean (unperturbed) ASR is reported for any target. Without this baseline, it is impossible to quantify how much of the reported ASR is attack-driven versus intrinsic model behavior, which weakens all quantitative comparisons.

2. **Claim that traditional transferability methods fail is stated without experimental evidence.**  
   The introduction asserts that MI-FGSM, Input Diversity, and Variance Tuning "did not increase, but even decreased" cross-prompt transferability, yet no experiment or table in the paper supports this claim. Given that these methods are standard baselines in the transferability literature, their omission from the main experiments means a reader cannot assess whether GrCPA genuinely outperforms the best available combination of existing techniques (e.g., MI-FGSM applied to Multi-P). The paper dismisses an entire family of relevant methods without evidence, which weakens its claimed novelty.

3. **No ablation of the core hyperparameter \(k\) (number of clipped gradients).**  
   Only \(k=1\) is used in all experiments. The paper argues that large gradients cause overfitting and clipping them mitigates this, but never shows that \(k=1\) is better than \(k=0\) (no clipping, i.e., Multi-P) or that larger \(k\) degrades performance. This is the central design parameter of the method, and its non-ablation leaves the proposed mechanism under-supported. Without this, the contribution reduces to a heuristic whose sensitivity is unknown.

4. **Discrepancy between the paper's framing and its experimental setup.**  
   The introduction motivates the problem by stating that adversarial attacks on VLMs "usually require a large number of iterations, such as 10,000, to succeed" — attributing the overfitting problem to long optimization. Yet all experiments use only 1000 iterations. Figure 3's curves appear to still be rising at 1000 iterations, and the paper's own claim that performance "gradually stabilizes after 1000 iterations" is not clearly supported by the figure. This disconnect casts doubt on whether the experiments actually test the scenario the paper frames as the core problem.

### Minor

- **Ablation of \(\lambda\) (fraction of Transformer layers regularized) shows minor differences** — Table 6 reports that the best is \(\lambda=1/4\) but the differences are "relatively minor" (paper's own words). This is not a weakness per se, but it means the paper's explanation that "preserving low-level features" drives the improvement is not strongly supported.

- **Ablation of which component (Attention vs. MLP) drives improvement is missing.** Table 5 appears to ablate modalities (visual vs. text), but there is no ablation showing whether clipping in just Attention blocks, just MLP blocks, or both is responsible for the gains.

- **Hyperparameter sensitivity is limited.** Only one set of hyperparameters (\(k=1\), \(\lambda=1/4\), \(T=1\)) is used throughout. A sensitivity analysis (especially for \(k\) and \(\lambda\)) would strengthen confidence in the method's robustness.

- **Prompt construction for "image classification" and "image captioning" tasks is underspecified.** The paper mentions these tasks but does not describe the prompt templates used to convert them into VQA format. This affects reproducibility.

### Trivial

None.

---

## Nice-to-Haves

- A wall-clock time or FLOPs comparison between GrCPA and baselines would quantify the computational trade-off of the gradient clipping.
- Testing on prompts with varied lengths, natural language variations, or misspellings would strengthen the cross-prompt transferability claim.
- Reporting variance over random restarts for ASR would strengthen the stability analysis beyond the five-checkpoint consistency measure in Table 2.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength Finder's Claim #4 ("Demonstration that single-modal transferability methods fail"):** The paper asserts this claim but provides no experimental evidence. Since a strength requires concrete support in the paper, and a verified weakness (Weakness #2 in Major) confirms the absence of this evidence, this claimed strength is dropped.

- **Criticism about Algorithm 1 being in the appendix:** The instruction states to remove weaknesses about missing appendix content, as such sections are stripped by the parser. Algorithm 1 exists in the original submission.

- **Criticism about Figure 1 x-axis being unlabeled:** This is a formatting/presentation nitpick (the figure caption states "attack iteration process").

- **Criticism about "non-stationarity" being vague and "Figure 1 is unclear":** These are subjective style judgments. The non-stationarity concept is described in the text and illustrated via Figure 1; the critique amounts to a presentation preference.

- **Strength Finder's generic strengths** such as "the paper addressed an important problem" — filtered as generic/superficial.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Clarify the ASR metric** (exact match vs. substring) and report clean ASR (unperturbed images) for all target texts. This is essential for interpreting results.
2. **Include a direct experimental comparison** between GrCPA and MI-FGSM / DIM / Variance Tuning baselines (applied to Multi-P). Either your claim that they fail is supported, which strengthens the paper, or the claim needs retracting.
3. **Ablate \(k\)** — show results for \(k = 0, 1, 2, 5, 10\). This is the single most important missing experiment and directly supports your claimed mechanism.
4. **Add an ablation separating Attention-block and MLP-block gradient clipping**, to isolate which component drives the improvement.
5. **Address the 10,000 vs. 1000 iteration gap** — either run experiments at 10,000 iterations or re-frame the motivation to align with the 1000-iteration setting used.

---

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/WyEdX2R4er.md (Visual Data-Type Understanding) | 8.00 | Much stronger — clean empirical study with clear framing and no missing baselines. Our paper is significantly weaker on completeness. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/nc5GgFAvtk.md (An Image Is Worth 1000 Lies — CroPA) | 6.80 | Same topic (cross-prompt attacks), accepted with well-motivated max-min optimization and thorough experiments. Our paper's gradient clipping method is simpler but its evaluation is less complete. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/wvFnqVVUhN.md (Failures to Find Transferable Image Jailbreaks) | 6.25 | Large-scale empirical study with clear negative result and clean methodology. Our paper has weaker ablations and underspecified metrics. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/1BuWv9poWz.md (Gradient Normalization Scaling for ViTs) | 5.33 | Accepted paper on gradient regularization for transferability. Similar methodological gaps (incomplete ablations) but more comprehensive comparisons. Our paper is comparable in quality. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/7OO8tTOgh4.md (MIE — Non-targeted Attacks on VLMs) | 5.25 | Rejected for insufficient comparisons and weak ablations. Our paper has better empirical breadth but similar issues with missing baselines and underspecified metrics. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/2ozEpaU02q.md (Multiple Randomized Trajectories) | 4.00 | Rejected — lacked clear contribution over prior methods. Our paper is slightly stronger due to consistent multi-model results. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/zQXX3ZV2HE.md (Adversarial Instance Attacks for HOI) | 3.00 | Weak paper with unclear writing and insufficient validation. Our paper is clearly above this level. |

**Relative assessment:** The paper's core idea (gradient clipping in Transformer blocks for cross-prompt transferability) is clean and the experiments show consistent improvement. However, the underspecified ASR metric, missing clean baseline, unsubstantiated claim about traditional methods failing, and absence of \(k\) ablation are significant gaps that prevent the paper from being competitive with accepted works at the 6+ level. It is stronger than papers scoring 3–4 (which have core methodological flaws or poor writing) but weaker than the accepted CroPA paper (6.80) due to less complete evaluation. I position it near the 4.5–5.0 boundary based on anchor comparison.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>