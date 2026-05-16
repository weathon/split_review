Now I have verified the paper content thoroughly. Let me construct the final review.

## Summary

This paper proposes a multilingual visual speech recognition (VSR) method using a single model. The key idea is to discretize visual speech features from a self-supervised model (mAV-HuBERT) into **visual speech units**, which reduces input data size to 0.016% of raw video and enables efficient pre-training in a unit-to-text translation framework. A curriculum learning strategy gradually transitions from audio-visual to visual-only inputs. The model is then finetuned on continuous features. Experiments on 5 languages show the single multilingual model achieves best or second-best WER on all five compared to prior language-specific methods.

## Strengths

1. **First successful sentence-level multilingual VSR with a single model.** The paper demonstrates that a single model can match or exceed the performance of prior language-specific models across five languages (Table 7). It achieves best WER on Es (12.4%), It (15.1%), and Fr (11.6%), and second-best on En (24.4%) and Pt (14.2%), all with one model versus multiple specialist models.

2. **Dramatic training efficiency via visual speech units.** The input data size is reduced to 0.016% of raw video (Section 3.1), enabling a ~12× faster total training time compared to standard VSR training (6.6 h pre-training + 34.9 h finetuning vs. 52.5 h standard), with a 6× batch size increase (Table 3). This efficiency gain is a core practical contribution.

3. **Multilingual AV-HuBERT (mAV-HuBERT) and its impact.** mAV-HuBERT is trained on 5,512 hours across 9 languages. Table 2 shows it outperforms English-only AV-HuBERT by >10% WER on non-English languages (Es, It, Fr, Pt) for multilingual VSR, directly enabling multilingual visual speech unit extraction.

4. **Curriculum learning with progressive audio masking is critical.** Section 3.2 describes a curriculum where audio speech units are progressively masked from 0% to 100%. Table 5 shows removing this curriculum causes dramatic drops (e.g., Es WER rises from 14.7% to 36.2%, Pt from 9.9% to 36.8%), confirming it is essential for learning from visual speech units.

5. **New state-of-the-art multilingual VSR results.** Table 6 shows the proposed method outperforms the AV-HuBERT multilingual baseline by >4% WER on all non-English languages. Table 7 shows it achieves best or second-best scores across all five languages relative to prior monolingual SOTA methods.

6. **Systematic ablation study.** Table 5 isolates the effect of each component (unit pre-training, curriculum learning, finetuning), with each removal degrading performance, providing clear evidence that all proposed components contribute.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Efficiency comparison (Table 3) mixes metrics and epoch counts, reducing interpretability.** The baseline is defined in the text as "standard VSR method that uses raw video as inputs" (Section 4.3.2), but the comparison reports "Test Acc" (subword-level prediction accuracy without beam search) rather than WER used everywhere else in the paper. It also compares 11 pre-training epochs against 8 standard-training epochs, making the "~12× speedup" claim harder to interpret. Reporting WER at comparable optimization progress would make this core selling point more convincing.

2. **Visual speech unit analysis lacks a direct quantitative measure of content preservation.** Section 4.3.3 provides qualitative phoneme mapping (Figure 2) and speaker verification EER (Table 4), which together show the units suppress speaker information. However, the claim that units "mainly contain viseme information" would be strengthened by a direct content-retention metric (e.g., phone classification accuracy or ABX discriminability). The VSR results indirectly validate content preservation, but the analysis section itself would be more rigorous with such a measure.

3. **The dramatic importance of curriculum learning (Table 5) is noted but not explained.** The "−Curriculum" condition causes WER to jump from 14.7% to 36.2% on Es and 9.9% to 36.8% on Pt — a much larger effect than removing unit pre-training itself. The paper does not discuss why this matters so much (e.g., is it simply that visual-only discrete training is too hard from scratch, or does the audio initialization provide a qualitatively different optimization landscape?). A brief explanation would help readers understand the mechanism.

4. **The paper trains mAV-HuBERT on 9 languages but evaluates VSR on only 5 (En, Pt, Es, Fr, It).** The reason is implicit (the other 4 languages — De, Ru, Ar, El — lack text labels from the automatic labeling pipelines cited). This is a reasonable limitation but should be stated explicitly in the main text, along with a discussion of how automatic label noise may affect results, especially for lower-resource languages.

### Trivial
None.

## Nice-to-Haves

- **Confidence intervals or variance estimates.** All WER numbers are reported as single values. Given the computational cost of multiple seeds this is understandable, but even a small number of repeated runs would strengthen reliability.
- **Direct quantitative content-retention metric for visual speech units** (e.g., phone classification accuracy from forced alignments), as noted above.
- **Discussion of automatic label noise.** The paper uses noisy labels from Ma et al. (2023) and Yeo et al. (2023c). A brief discussion of how label quality might vary across languages and affect results would be appropriate.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic Critical Issue 1 (baseline "never explicitly defined"):** The paper explicitly states in Section 4.3.2: "We compare the batch size, training iteration time, and total training time between the **standard VSR method that uses raw video as inputs** and the proposed method." The baseline IS defined. The confusion about mixed metrics is kept in Minor Weakness 1 above, but the claim of non-definition is factually wrong and removed.
- **Harsh Critic Critical Issue 2 (first-work claim "misleading"):** The reviewer argues the paper trains AV-HuBERT as a baseline, contradicting its "first work" claim. However, Section 4.3.5 states "Since there is **no prior work** exploring multilingual VSR with a single model, we train AV-HuBERT to perform multilingual VSR and set it as the baseline." The AV-HuBERT baseline is the authors' own creation for comparison, not a prior published work. The claim is about the published literature and is not contradicted. Removed as a misunderstanding.
- **Strength Finder "analysis confirms linguistic content and speaker suppression":** This is accurate and supported. However, the weakness about lacking a direct quantitative content measure (Minor Weakness 2) partially constrains the strength — the analysis is useful but incomplete. The strength stands but is implicitly qualified by the weakness.
- **Strength Finder "ablation study systematically validates each component":** Accurate and kept.

## Novel Insights

The key insight from the reviews is that the paper's contributions are largely solid, but the **efficiency argument** — a central selling point — needs more careful framing. The mixed metrics (Test Acc vs. WER) and epoch counts in Table 3 mean readers cannot easily verify the claimed speedup against a performance-matched baseline. A clearer comparison (e.g., hours to reach a given WER threshold for both methods) would eliminate this ambiguity. Additionally, the outsized impact of the curriculum learning component (dwarfing even the unit pre-training effect in some languages) is under-analyzed and could reveal deeper insights about why multi-modal initialization helps discrete visual speech modeling.

## Suggestions

1. Revise Table 3 to report WER (not Test Acc) for both methods at comparable optimization steps. Compare total wall-clock time to reach a specific WER threshold rather than mixing epoch counts and metrics.
2. Add a sentence explaining the dramatic curriculum learning effect: is it purely about optimization difficulty, or does the audio-visual initialization provide a qualitatively different learning signal?
3. Explicitly state why only 5 of the 9 mAV-HuBERT languages are used for VSR (lack of text labels for De, Ru, Ar, El) and briefly discuss the impact of automatic label noise.
4. Add a quantitative content-preservation metric (e.g., phone classification accuracy) for the visual speech unit analysis, or at minimum acknowledge this as a direction for future work.

## Score and Decision

**Originality:** High — visual speech units for multilingual VSR are novel; using discrete pre-training for efficiency is well-motivated.

**Importance of research question:** High — multilingual VSR is an underexplored area with practical significance.

**Claims well-supported:** Mostly yes — core VSR claims are well-supported by Tables 6-7 and ablations. The efficiency claim (Table 3) is the weakest due to metric/epoch mixing.

**Soundness of experiments:** Solid — systematic ablations, comparisons to both multilingual and monolingual baselines, and analysis of visual speech units. No fatal flaws.

**Clarity of writing:** Good overall, with some room for improvement in the efficiency comparison presentation.

**Value to community:** High — the approach and mAV-HuBERT model will be useful resources.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>