Now I have a thorough understanding of the paper. Let me write the final consolidated review.

---

## Summary

This paper proposes Classifier-Constrained Alternating Training (CCAT), a two-stage framework for mitigating modality imbalance in multimodal learning. The key idea is to pretrain a shared cross-modal classifier with a regularization term that penalizes contribution disparity, then freeze it during alternating training to prevent classifier-level bias toward dominant modalities. Modality-specific LoRA adapters handle distribution mismatch during alternating optimization, and a sample-level secondary update targets severely imbalanced samples. Experiments on CREMA-D, Kinetic-Sound, and MVSA show consistent improvements over prior methods, including MLA, MMPareto, and LFM.

## Strengths

1. **Well-motivated problem and clean solution.** The paper identifies a genuine limitation of existing alternating-training approaches—that they address encoder-level interference but leave the classifier vulnerable to bias from early-converging dominant modalities. The two-stage design (pretrain an unbiased classifier → freeze it as a stable anchor) is a natural and reasonable response to this diagnosis. The ablation study (Table 2) convincingly validates each component: removing classifier freezing drops CREMA-D multimodal accuracy from 85.89% to 82.80%, and removing any single component degrades performance.

2. **Consistent improvements across three diverse benchmarks.** CCAT outperforms all prior methods on all three datasets for multimodal accuracy, with gains of +1.35% (CREMA-D), +6.76% (Kinetic-Sound), and +1.92% (MVSA) over the best prior method. The improvement holds across different modality combinations (audio-visual and image-text) and dataset scales, demonstrating generalizability.

3. **Thorough ablation and hyperparameter analysis.** Table 2 systematically ablates all four components (classifier freezing, alternating training, secondary updates, LoRA) across all three datasets. Table 3 and Figure 4 provide grid searches over LoRA rank and the imbalance threshold β, with values tuned per dataset. This makes the method's design choices transparent and reproducible.

## Weaknesses

### Fatal
None.

### Major

1. **Numerical inconsistency in the motivating figure.** The introduction (line 80) states that MLA "reduces initial contribution disparity (1.00 → 0.92)." However, the table in Figure 1 shows MLA ending at A=0.90, B=0.10, a disparity of 0.80—not 0.92. The figure data itself is clear and the trend is interpretable, but this inconsistency between the text and the data table undermines confidence in the paper's central motivating evidence. The authors should correct this number and clarify how "contribution disparity" is computed.

2. **Figure 1 caption wording is confusing.** The caption states: "The 'Ours' lines show a more pronounced imbalance, with Modality A decreasing to ~0.65 and Modality B increasing to ~0.35." Since CCAT's distribution (0.65/0.35) is *more balanced* than MLA's (0.90/0.10), the phrase "more pronounced imbalance" is the opposite of what the figure shows. The intended meaning (a more pronounced *correction* of imbalance) is clear from the data, but the wording as written is misleading and undermines the paper's presentation.

3. **Large gain on Kinetic-Sound is not supported by variance.** CCAT outperforms LFM by +6.76% (79.29 vs. 72.53) on KS, a jump that is substantially larger than the gains on the other two datasets. While the paper reports averages over three random seeds, it does not provide standard deviations or confidence intervals. Without variance information, it is difficult for readers to assess whether this result is robust or an artifact of a particular run/split. The paper would be significantly strengthened by reporting per-seed results or standard deviations for all metrics.

### Minor

1. **Theoretical "isomorphism" is overstated.** Section 3.1 draws an analogy between class-imbalance and modality-imbalance gradient dynamics, which is an insightful observation. However, the paper describes it as "a new theoretical framework" and "a profound theoretical isomorphism." The derivation amounts to writing down the standard cross-entropy gradient (Eq. 1) and observing that weak-modality features are attenuated just as minority-class features are. This is a useful conceptual link, not a formal theoretical framework. The paper would benefit from toning down these claims and either providing a more substantive analysis or simply presenting the analogy as motivation.

2. **Mutual information estimator (Eq. 5) lacks explanation.** Equation (5) presents an MI estimator that appears to be a variant of InfoNCE with an unusual log(N) term outside the expectation, but the paper does not derive, justify, or cite a source for this specific form (the citation to Zhou et al. 2025b covers the general approach but does not validate this exact expression). Since this estimator is central to the contribution quantification used throughout the method, a brief explanation of why this form is valid would be helpful.

3. **No discussion of computational overhead.** The method requires additional computation for the secondary update pass and MI estimation per sample. A brief discussion of wall-clock time, FLOPs, or training-time overhead relative to baselines (especially MLA, the closest competitor) would contextualize the method's practical deployment cost.

### Trivial

- The "-" in the MVSA-LFM cell of Table 1 lacks a footnote explaining that LFM's original paper did not report MVSA results.
- "faithfully" at the end of the contribution list (line 84) appears to be a stray word.

## Nice-to-Haves

- Report standard deviations or per-seed results for all main table entries.
- A controlled experiment validating the class-imbalance analogy (e.g., showing that standard class-imbalance remedies also help modality imbalance) would turn the current conceptual link into an empirical demonstration.
- An analysis of the secondary update mechanism's sample counts per epoch and whether it converges or overfits.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- **"Figure 1 is self-contradictory / cannot be trusted."** The figure data (both the graph and the embedded table) is internally consistent. The contradiction is between the text's number (0.92) and the table's values (0.90/0.10 → 0.80 disparity). This is a minor numerical typo in the text, not a figure-level issue that invalidates the paper's motivation.
- **"Unimodal comparisons across method families are invalid."** The paper transparently describes how unimodal results are obtained (differently for methods with different architectures). This is a disclosure, not a flaw. The primary comparisons are on multimodal accuracy, where the evaluation is apples-to-apples.
- **"Suspicion that baselines were re-implemented with different optimizers."** The paper states that "all models were optimized via SGD" with the same hyperparameters. The reviewer's speculation that this disadvantages baselines published with Adam is not supported by evidence in the paper.
- **"The secondary update risks severe overfitting."** This is a reasonable concern but purely speculative; there is no evidence of overfitting in the reported results. The authors could address it, but as raised it is not a demonstrated weakness.
- **"The 'not yet released' concern."** Removed per hard rules: cited references and baselines are assumed to exist.

## Novel Insights

The observation that alternating training methods (like MLA) prevent encoder-level interference but still produce biased classifiers—because the classifier has already learned a structural preference for the dominant modality during early alternating updates—is genuinely useful. Most prior work focuses on encoder-level dynamics; shifting attention to the classifier as an independent source of modality imbalance is the paper's most important insight. The combination of freezing a pretrained classifier with LoRA adapters is a clever way to preserve the stability of a fixed anchor while still allowing modality-specific feature adaptation.

## Suggestions

1. Correct the numerical value in the text ("0.92" → the correct disparity value) and fix the caption wording ("more pronounced imbalance" → "more pronounced correction of imbalance" or "more balanced distribution").
2. Add standard deviations or per-seed results, particularly for the Kinetic-Sound benchmark where the gain is largest.
3. Tone down the claims about the "theoretical framework" and "profound isomorphism"—the class/modality imbalance analogy is a useful motivation but not a formal theory.
4. Add a brief explanation or citation for the MI estimator (Eq. 5) to clarify its validity.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Queried three bands on "multimodal learning modality imbalance."

- **Low band (< 3.5):** Anchors at 3.00 (ProMoBal), 3.00 (Multi-Faceted), 2.67 (Mind the Interference), 2.50 (MAIL) — all clearly weaker than CCAT (limited experiments, unclear methods, withdrawn/rejected).
- **Middle band (3.5–7.5):** Anchors at 4.50 (GOAL), 5.00 (Plug-Play-Fortify), 4.00 (MultiMisD), 3.60 (D5ZLr0lZhf). CCAT is stronger than GOAL (4.50, rejected) which has novelty concerns, and comparable to Plug-Play-Fortify (5.00, poster accept) but with somewhat more comprehensive evaluation.
- **High band (> 7.5):** Anchors at 8.00 (Generative Universal Verifier, Text-to-3D, Embodied Navigation, Efficient RL) — these are very different paper types (generative models, RL, navigation) and much stronger overall.
- **Round 1 bracket:** 4.5–6.5

**Round 2 (Narrowing):** Queried (4.5–6.5) and (5.5–7.5). Key anchors:
- **Landscape Smoothness (5.00, Reject):** Had more ambitious theory but weaker empirical validation and overly strong assumptions. CCAT has stronger experiments but more modest theoretical contribution. Slightly stronger than this anchor.
- **Norm Discrepancy MLLM (6.00, Poster):** Strong theoretical analysis with clean experiments. CCAT has similar experimental breadth but weaker theory and the presentation issues noted above. Weaker than this anchor.

**Final score placement:** CCAT is clearly stronger than the 4.5–5.0 rejected papers (GOAL, Landscape Smoothness) due to better experimental validation, ablation, and a well-motivated method. It is weaker than the 6.0 paper (Norm Discrepancy MLLM) due to presentation issues and theoretical overclaiming. This places it between these anchors.

**Anchors consulted (all rounds):** EIdbBjL6mJ (3.00), dADwCplxyC (3.00), 6Kfbi3ngT1 (2.67), caMnGCyONx (2.50), I3uFqoUZ2Y (4.50), 7KluEfmiXG (5.00), E0udlUz8wQ (4.00), D5ZLr0lZhf (3.60), DM0Y0oL33T (8.00), kI27Niy4xY (8.00), kkBOIsrCXh (8.00), oBXfPyi47m (8.00), RHPqr2egJO (5.00), PWzsvHXNHM (5.00), cYZkZp3m8F (5.00), GVVNG2EMQv (6.00), bZqCBgm2N0 (6.50), iedlZOdI0d (6.50), XLiUcvHfzS (6.00).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>