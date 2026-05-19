- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5
Now I have a thorough understanding of the paper and can verify each claim. Let me compose the final review.

## Summary

This paper addresses the underexplored problem of audio event relation modeling in Text-to-Audio (TTA) generation. It contributes: (1) a benchmark with a relation corpus covering 4 categories (Temporal Order, Spatial Distance, Count, Compositionality) and 11 sub-relations, (2) an audio event category corpus of 25 everyday sounds each with 5 seed clips, (3) a multi-stage relation-aware evaluation metric (MSR-RiTTA), and (4) a finetuning demonstration on Tango showing improved relation modeling. The key finding is that all 7 benchmarked TTA models score poorly on relation metrics despite scoring well on standard metrics (FAD, KL), revealing a fundamental gap.

## Strengths

1. **Systematic relation corpus covering underexplored audio event relations**: Table 2 defines 11 sub-relations across 4 categories (temporal order, spatial distance, count, compositionality), going substantially beyond prior TTA work that only partially addressed temporal order (Xie et al., 2024). This corpus directly enables the paper's central contribution of benchmarking relation modeling.

2. **Multi-stage relation-aware evaluation metric (MSR-RiTTA)**: Section 3.4 proposes a three-stage pipeline (presence → relation correctness → parsimony) that directly measures whether text-specified relations are reflected in generated audio. Table 5 shows that general metrics (FAD, KL) are inconsistent with relation-aware metrics — the best FAD models are the worst on relation scores and vice versa — proving the metric's necessity and demonstrating the gap.

3. **Finetuning Tango on the benchmark dataset yields clear, multi-metric improvement**: Table 8 shows finetuning improves mAMSR from 0.15 to 0.38 with all sub-metrics (mAPre, mARel, mAPar) improving. This validates both the benchmark's utility and the tractability of the problem.

4. **GPT-4 augmented prompt generation**: Section 3.3 uses GPT-4 to produce 5 diverse text templates per relation, increasing linguistic diversity beyond single-template approaches.

## Weaknesses

### Fatal
None.

### Major

1. **The evaluation pipeline depends on an unvalidated audio event detector (PANNS).** The entire MSR-RiTTA metric (Section 3.4) rests on PANNS's accuracy for detecting presence, timing, and class labels of audio events in both ground-truth and generated audio. The paper reports no verification of PANNS's performance on: (a) the mixed, relation-satisfying audio in the benchmark, (b) the generated audio from TTA models (which may have artifacts), or (c) the specific audio event categories used (e.g., paper shredder, boat horn, sheep bleating — some of which are rare in standard audio tagging benchmarks). Averaging across confidence thresholds (0.5–0.8) mitigates threshold sensitivity but does not address systematic detection failure. Without any validation (e.g., comparing PANNS outputs to human annotations on a subset), the scores in Tables 5, 6, and 8 conflate detection-model errors with genuine relation-modeling failures. This is the single most important issue to address because it affects every quantitative result in the paper.

### Minor

2. **The <Not> relation is acknowledged as problematic but remains in the benchmark without a clean resolution.** The paper itself notes that: (a) general evaluation is skipped for <Not> because it lacks a reference audio (Section 5.2), (b) high presence scores on <Not> are trivially achievable by generating nothing (Section 5.3, Figure 6 analysis), and (c) finetuning causes a performance drop on <Not> attributed to dataset confusion from pairing <Not> with silent audio (Section 5.4). The paper discusses these issues honestly, but including a relation in a benchmark whose evaluation is acknowledged as flawed weakens the benchmark's integrity. Either remove <Not> or reformulate it (e.g., requiring generation of one event and absence of another).

3. **The loudness-based spatial distance proxy is unvalidated.** For <closefirst>, <farfirst>, and <equaldist>, the paper approximates spatial distance via waveform loudness with manually set thresholds (σ₁=0.2, σ₂=0.4, Section 5.2). The paper acknowledges the fundamental limitation ("mono-channel audio, obtaining the absolute distance... is nearly impossible") and restricts evaluation to intra-class events, which partially addresses concerns about cross-class loudness variation. However, no validation is provided that the chosen thresholds correspond to perceptually meaningful distance differences, nor is there an ablation showing the metric's sensitivity to these values. This makes the Spatial Distance scores uninterpretable as measures of distance reasoning.

4. **Overclaim about "all potential relations in real-world scenarios."** The abstract and conclusion state that the relation corpus covers "all potential relations in real-world scenarios." The actual corpus covers 4 categories and 11 sub-relations, omitting important relation types such as causality, repetition patterns, duration qualifiers, and relations involving more than two events (explicitly left for future work in Section 3.1). This framing overstates the benchmark's scope.

5. **Limited text template diversity per relation may lead to template overfitting.** Only 5 text templates are generated per relation (Section 3.3), but the test set contains 720 pairs per relation. This means the same 5 templates appear many times, which could allow models to pattern-match on template wording rather than learn the underlying relation. While this is mitigated for TTA (which generates audio, not text), it should be discussed.

### Trivial

6. **The finetuning hyperparameters are not reported in the paper.** The paper states "follow the finetuning strategy outlined in Tango 2" (Section 5.4) but omits specifics (learning rate, batch size, training steps, GPU type). While these are available in the cited paper, noting the actual values used would aid reproducibility.

## Nice-to-Haves

- Validate PANNS on a subset of the benchmark audio with human annotations (e.g., 200 pairs) and report per-class precision/recall. If detection fails on certain classes, flag or remove them.
- Report the three MSR-RiTTA sub-scores (Pre, Rel, Par) separately for each relation category in a main table (they are already reported in Figure 6 and Table 5, but a per-category breakdown in the main results table would aid interpretation).
- Include a discussion of how scores on this synthetic benchmark might relate to performance on naturally-occurring multi-event audio (e.g., AudioSet).
- Consider including WavJourney as a baseline for compositionality relations, while acknowledging its fundamentally different architecture (LLM + post-mixing).

## Removed Points

These points were flagged in the reviews but removed (with justification):

- *"Sub-scores are not reported separately"* — **Removed (factually wrong).** Table 5 reports mAPre, mARel, mAPar, and mAMSR. Figure 6 visualizes all four sub-scores for the top-3 methods across all 11 sub-relations. The paper already provides this.
- *"WavJourney should be benchmarked"* — **Removed (scope creep).** The paper focuses on end-to-end TTA models. WavJourney is a compositional system using LLM + post-mixing, discussed in Related Work with its limitations noted. Its omission does not weaken the paper's claims about end-to-end TTA models.
- *"Missing hyperparameters for finetuning"* — **Demoted to Trivial.** The cited Tango 2 paper contains the strategy; reporting exact values would be a minor improvement.
- *"Confidence threshold range (0.5–0.8) not justified"* — **Removed.** The paper states it follows the "prior COCO object detection evaluation strategy" (Section 3.4), which is standard practice.
- *"No comparison to natural audio"* — **Weakened to Nice-to-Have.** The paper's scope is a synthetic benchmark for isolating specific relation types, which is standard practice in ML (e.g., CLEVR). The relevance to natural audio is an acknowledged future direction.
- *"GPT-4 prompt not specified"* — **Removed (trivial).** The approach is described clearly; the exact prompt engineering is a minor implementation detail.

## Novel Insights

The most interesting observation emerging from the reviews — beyond the paper's own contributions — is the severity of the gap between standard TTA metrics (FAD, KL) and relation-aware metrics. The paper shows a 200× difference between models on relation metrics despite minimal differences on standard metrics (e.g., AudioLDM (S-Full) has the best FAD but the worst relation scores). This inversion suggests that optimizing for audio quality metrics may actively work against relation modeling, which opens a meaningful research question about whether current TTA training objectives are fundamentally misaligned with compositional generation.

## Suggestions

1. **Validate the PANNS detector** on a random subset of the benchmark (e.g., 200 audio pairs). Have human annotators label event presence, timing, and class, then compare to PANNS outputs. Report per-class precision/recall. If certain classes have poor detection, either remove them or flag them as unreliable. This single change would substantially strengthen the paper's quantitative claims.

2. **Either fix or remove the <Not> relation.** A better formulation: require generation of a specified audio event *and* absence of another specified event (e.g., "generate dog barking but not cat meowing"). This tests the model's ability to selectively generate rather than simply generating silence.

3. **Tone down the "all potential relations" claim.** Replace with language like "a first systematic relation taxonomy covering four key categories." The actual contribution is strong enough without overclaiming.

4. **For spatial distance, validate the loudness proxy.** At minimum, conduct a small perceptual study or synthetic attenuation experiment showing that the σ₁=0.2 and σ₂=0.4 thresholds correlate with human distance judgments. Alternatively, acknowledge this as a rough proxy and present it accordingly.
