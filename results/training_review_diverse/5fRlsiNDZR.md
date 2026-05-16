Now I have a thorough understanding of the paper and all claims. Let me compose the final consolidated review.

---

## Summary

This paper introduces FARV, a unit-based vocoder for Video-to-Speech (V2S) synthesis that integrates facial image embeddings (from FaRL) with acoustic unit embeddings inside a HiFiGAN generator. The core idea is to address the known weakness of unit-based vocoders in preserving speaker identity by injecting visual speaker information, while retaining the advantage of unit-based methods in bridging the domain gap between V2S frontend and vocoder without finetuning. Experiments on LRS3-TED, LRS2-BBC, and VoxCeleb2 evaluate intelligibility, speaker identity preservation, and adaptation capability.

## Strengths

- **Novel integration of facial embeddings into a unit-based vocoder for V2S:** The paper proposes fusing visual speaker embeddings (FaRL image encoder) with acoustic unit embeddings inside the HiFiGAN generator (Section 3.3). This design directly targets a known limitation of unit-based vocoders — loss of speaker-specific information — and is the first such integration in a V2S vocoder to the best of available evidence. The approach is well-motivated and technically sound.

- **Strong intelligibility among visual-only V2S methods:** Across LRS3-TED and LRS2-BBC (Table 1), FARV achieves top-1 or top-2 performance on intelligibility metrics (WER, ESTOI, MCD, LSE-C/D) among methods using only visual input — including those that rely on additional speaker embeddings or textual supervision. This demonstrates that integrating the facial embedding does not compromise content recovery.

- **Demonstrated zero-shot robustness to V2S frontend outputs:** Section 4.3.2 (Table 4, Figure 3) shows that while mel-based HiFiGAN suffers severe degradation (e.g., −47.44% NISQA drop) when applied to V2S frontend predictions without finetuning, FARV maintains much more stable performance. This is a genuine advantage arising from the shared acoustic unit vocabulary and is convincingly supported by the controlled frontend-adaptation experiments.

- **Systematic two-sided adaptation analysis:** The paper separately evaluates dataset adaptation (Section 4.3.1) and V2S frontend adaptation (Section 4.3.2) with relative percentage drop rates, providing a rigorous comparison of unit-based vs. mel-based vocoder generalizability. This experimental design cleanly isolates the effect of the shared unit vocabulary.

## Weaknesses

### Fatal
None.

### Major

1. **Unfair comparison in the main V2S tables (Tables 1 and 2) undermines the core claim about speaker identity.** FARV is trained/finetuned on multi-speaker datasets LRS3-TED and LRS2-BBC, while unit-HiFiGAN (used by ReVISE) is evaluated zero-shot from the single-speaker LJSpeech corpus *without any finetuning* on the target datasets. The authors acknowledge this asymmetry (Section 4.2, "Given that finetuning on new datasets can significantly compromise the acoustic quality of Unit-HiFiGAN...") and justify it by noting that finetuning degrades unit-HiFiGAN's quality. However, this justification does not resolve the core problem: the speaker-identity gains observed for FARV (e.g., SECS 0.42 vs. 0.24, EER 8.71% vs. 17.50% on LRS2-BBC) could be substantially driven by training on more speaker-diverse data rather than by the facial embedding itself. The paper's headline results therefore conflate two factors (training data + facial embedding) and do not provide a clean test of whether the facial embedding is responsible for the improvement.

2. **Missing essential ablation: FARV without the FaRL embedding, trained on the same multi-speaker data.** There is no experiment in the paper that trains the unit-HiFiGAN backbone on LRS3-TED or LRS2-BBC *without* the FaRL facial embedding and compares it against FARV. Without this ablation, the reader cannot distinguish between two explanations for FARV's speaker-identity improvements: (a) the FaRL facial embedding provides useful speaker information, or (b) simply training a unit-based vocoder on multi-speaker data (regardless of facial input) improves speaker preservation. Given that the paper's central contribution is the integration of facial embeddings, this omission is significant and directly weakens support for the paper's primary claim.

### Minor

1. **Ambiguity in the dataset-adaptation experimental protocol (Section 4.3.1).** The paper states that FARV is "further trained on the LRS3-TED dataset" (Section 4.3) but earlier says FARV is trained on "LRS3-TED and LRS2-BBC datasets respectively" (Section 4.1.3). It is not explicitly stated which checkpoint is used for zero-shot evaluation on LRS2-BBC (the LRS3-TED-trained model? or the LRS2-BBC-trained model evaluated on held-out test data?) and which for the finetuned condition. While the intended setup can be inferred, the lack of explicit specification makes it harder to interpret the relative performance drops in Figure 2.

2. **Vague description of which video frame provides the facial embedding.** Section 3.3 states only that the vocoder takes "a visual frame cropped from the input video as input." It is not specified whether this is the first frame, a randomly sampled frame, the center frame, or an averaged representation. This is a reproducibility gap.

3. **Embedding capability experiment (Section 4.4) is on a small, controlled dataset and provides limited support.** The linear classification on RAVDESS (24 speakers, controlled recording conditions) showing 100% gender accuracy for FARV's embedding is not strong evidence of practical benefit. The near-perfect accuracy is unsurprising for a FaRL-derived embedding on a small set, and the experiment does not directly measure whether this embedding information translates to improved synthesis quality on large-scale, in-the-wild V2S test sets.

4. **No statistical significance or variance reporting.** All metrics are reported as point estimates without standard deviations or confidence intervals. Given the moderate size of V2S test sets and the natural variability of speaker identity metrics (EER, SECS), the significance of observed differences is unknown. This is a common gap but nonetheless limits confidence in the rankings.

### Trivial
None.

## Nice-to-Haves

- **Human listening study (MOS):** The paper relies entirely on NISQA-MOS (an automated predictor). A small-scale listening test comparing FARV, finetuned unit-HiFiGAN, and ReVISE on speaker similarity and naturalness would strengthen the claims about the "balance between speaker characteristics preservation and acoustic quality."

- **Failure case analysis:** Discussion of conditions where FARV's facial embedding may hurt performance (e.g., occluded faces, non-frontal poses, mismatched speaker identity between the image and the utterance) would improve the paper's thoroughness and help practitioners understand limitations.

- **Computational cost reporting:** Model size, inference speed, and training GPU-hours are not reported, which would be useful for practical deployment assessment.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Tables 1 and 2 are not visible in the extracted text":** This is a PDF parser artifact, not an author error. The original submission contains these tables.
- **"No human evaluation (MOS)" — framed as a core weakness rather than a nice-to-have:** While a listening study would strengthen the paper, NISQA-MOS is a standard automated metric in the V2S literature, and its absence is not a structural flaw in a conference paper with sufficient automatic evaluation.
- **"Missing related works":** Not included as no reviewer raised this, and I cannot independently verify claimed omissions.
- **"No analysis of failure cases" — framed as a weakness:** This is a scope-creep expectation; failure analysis is valuable but not a standard requirement for this type of paper.
- **Pure formatting nitpicks:** None present in the original input from reviewers.

## Novel Insights

None beyond the paper's own contributions. The key insight — that facial embeddings can be fused with acoustic units in a vocoder to improve speaker identity preservation in V2S — is clearly stated by the authors. The reviews surface a methodological gap (lack of controlled ablation) but do not introduce any new conceptual insight that the paper itself does not articulate.

## Suggestions

1. **Add a controlled ablation:** Train a version of FARV without the FaRL embedding on exactly the same multi-speaker data (LRS3-TED or LRS2-BBC) using the same training schedule, and compare its speaker-identity metrics (SECS, EER) against the full FARV. This would directly test whether the facial embedding contributes beyond simply having access to more speaker-diverse training data.

2. **Replace or supplement the main V2S comparison:** Compare FARV against unit-HiFiGAN finetuned on LRS3-TED/LRS2-BBC (the same multi-speaker data, under the same training budget) as a secondary comparison in the main tables, even if its acoustic quality degrades — the relative trade-off would still be informative. Place the zero-shot comparison in a separate table with explicit caveats.

3. **Clarify the evaluation protocol:** Precisely specify which exact model checkpoint (trained on which dataset) is used for each zero-shot and finetuned condition in the dataset-adaptation experiments. Specify how the input video frame for FaRL is selected.

4. **Report error bars** (e.g., standard deviation across non-overlapping test splits or bootstrap confidence intervals) for at least the primary speaker-identity metrics (SECS, EER) and NISQA-MOS.

## Score and Decision

The paper addresses a real problem in V2S (speaker identity loss in unit-based vocoders) with a well-motivated and technically sound approach. The frontend-adaptation experiments (Section 4.3.2) are a genuine strength and convincingly demonstrate the advantage of unit-based methods over mel-based ones for V2S deployment. The intelligibility results are competitive.

However, the central contribution — that facial embeddings improve speaker identity preservation — is **not adequately supported** by the experiments as presented. The two major weaknesses (unfair comparison confounded by training data differences, and missing ablation controlling for data) mean the paper's primary claim cannot be cleanly validated from the provided evidence. The secondary experiments (embedding classification on RAVDESS) are on too small a scale to fill this gap.

The paper has clear merit and the idea is worth pursuing, but the experimental validation needs substantial revision before the core claim can be accepted. With fair comparisons and a proper ablation, this could become a solid contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>