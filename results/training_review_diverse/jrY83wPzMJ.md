Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper proposes a synchronous (jointly trained) scene text spotting and translation method for Text Image Machine Translation (TIMT). The key technical contribution is a Bridge and Fusion (BAF) module that fuses visual features with textual features from the recognition decoder before feeding them to a Transformer-based translation module. The authors also create the STST800K dataset combining synthesized and real images with paragraph-level bilingual annotations. Experiments on OCRMT30K, ReCTS, HierText, and CTW1500 show the method outperforms both pipeline baselines (MCTIT) and end-to-end text-spotting baselines (UNITS) on translation quality.

## Strengths

- **Synchronous joint learning outperforms pipeline methods with convincing margins.** Tables 2–4 show the proposed method achieves higher SacreBLEU and COMET scores than MCTIT (pipeline) on all four datasets and both translation directions. Table 4 is particularly informative: even when both methods receive ground-truth OCR input, the synchronous model outperforms MCTIT, especially on the complex-layout ReCTS dataset, demonstrating that joint learning reduces error propagation beyond what OCR errors alone explain.

- **The BAF module's multi-modal fusion benefit is validated through ablation.** Table 7 shows the full model (Best) outperforms variants using only visual features or only textual features, confirming that multi-modal fusion contributes positively. The comparison between "Best" and "Remove BAF" (which switches to separate training) provides evidence that joint training also matters.

- **The STST800K dataset is a tangible contribution to the field.** The paper describes a careful synthesis pipeline (COCO backgrounds + WMT22 text pairs, depth/segmentation masking, SynthText-based rendering) and relabeling of multiple real benchmarks. Having a standardized set of 800K images with paragraph-level coordinates, reading order, and bilingual pairs addresses a genuine data scarcity problem for Scene TIMT.

- **Qualitative analysis in Figure 4 illustrates real advantages.** The case studies on ambiguity, proper nouns, and recognition/reading-order errors provide concrete visual evidence for how multi-modal fusion and joint learning help in difficult scenarios that pipeline methods fail on.

## Weaknesses

### Fatal
None.

### Major
None that rise to the level of invalidating the core contribution. See Minor section for the most important concerns.

### Minor

- **UNITS baseline adaptation is poorly documented and yields implausibly low scores.** The paper states that UNITS was "trained for translation instead of recognition" but provides no details on how this was done — what loss function, what decoding procedure, whether architecture modifications were needed, or how long training ran. The resulting scores (e.g., BLEU 1.30 on ReCTS with GT Coord, 0.59 on CTW1500) are extremely low. While the paper acknowledges these scores are low and uses MCTIT as the stronger baseline, the lack of documentation makes it impossible for readers to assess whether this comparison is meaningful. The paper would be stronger if it either properly configured these baselines or dropped the UNITS comparison entirely and focused on MCTIT.

- **Test set labels were modified, clouding external SOTA comparisons.** Section 4.1.2 states that reading order and translation labels for test subsets of ReCTS and HierText were manually created, and other data were relabeled via an LLM API with human proofreading. This means the test splits differ from those used in prior published work. The paper's *internal* comparisons (its method vs. MCTIT/UNITS run on the same modified data) are fair. However, the claim of "state-of-the-art translation performance" relative to the broader literature is less clean since absolute scores are not directly transferable. The paper should clarify this caveat explicitly.

- **No comparison with existing synchronous TIMT methods.** The paper cites several synchronous TIMT papers (Ma et al., 2022; 2024; Lan et al., 2024) and contrasts its approach with them in Section 2, yet the experiments include zero synchronous baselines. The justification that these methods are limited to "simple layout cases with a single paragraph and scanning reading order" is reasonable, but at minimum a comparison on simpler benchmarks (e.g., synthetic single-paragraph images) would ground the contribution and clarify the novelty relative to the synchronous line of work.

- **The "Remove BAF" ablation confounds two variables.** This condition removes BAF *and* switches from joint training to separate training simultaneously. The difference between "Best" and "Remove BAF" therefore conflates the effect of multi-modal fusion with the effect of joint learning. An additional ablation (joint training but no BAF) would cleanly isolate the BAF module's contribution.

- **Detection performance for the full method is not reported.** The paper reports Hmean for detection only in the "Remove BAF" ablation (which lacks the BAF module). Since detection quality directly affects translation, and since the method uses shared visual features for all tasks, knowing whether detection accuracy is competitive with existing text spotters is important for assessing the overall system.

### Trivial

- **WMT22 text-pair filtering threshold not specified.** The paper says "deleting long text" reduced 55M pairs to 39M but does not state the threshold.
- **The position embedding concatenation in the BAF module** (2D global + 1D local) is described textually but not formalized mathematically.
- **No standard deviations or confidence intervals reported** for any of the main results (common in large-scale training but worth noting).

## Nice-to-Haves

- An error propagation analysis: feed perfect recognition to the translation module vs. predicted recognition and measure the translation quality drop. This would directly support the paper's motivation that joint learning reduces error propagation.
- Parameter count and inference speed comparison with baselines (the paper notes its model is the largest among "small models" but does not quantify).
- Inter-annotator agreement or label quality metrics for the manually created test set labels and LLM-generated translations.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No mention of code release, model weights, or dataset availability" / "paper does not state whether the dataset will be released."** Per the hard rules, criticisms questioning release status of cited artifacts should be removed. The paper was likely submitted with an appendix covering these details; the review should not penalize what the parser strips.
- **"The paper does not report whether this score matches the original paper's numbers" (re: MCTIT).** The paper runs its own baselines on its own evaluation setup, which is standard practice when test labels differ. The internal comparison is what matters.
- **"Missing related works"** — The review should not add missing citations without external verification.
- **"Table 1 is partially garbled by the parser"** — This is a parser artifact, not an author error.
- **Generic/conflicting strengths from Strength Finder removed** (e.g., "State-of-the-art performance across multiple scene text translation benchmarks" — this conflicts with the verified weakness about test set label modifications; the internal comparison is valid but the "SOTA" framing is imprecise, so the strength is demoted to the weaker claim already captured in Strength 1).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not already articulate.

## Suggestions

1. **Document the UNITS baseline adaptation in detail** — or replace it with a baseline you can fairly configure. If the UNITS architecture is structurally unsuited for translation, explain why and use a different set of end-to-end baselines. Consider adding at least one existing synchronous TIMT method (Ma et al., 2022; Lan et al., 2024) evaluated on simpler subsets.
2. **Add an ablation with joint training but no BAF** to separate the contributions of joint learning and multi-modal fusion.
3. **Explicitly state in the abstract and results section** that test set labels were modified from original datasets and that comparisons with absolute numbers from prior papers should account for this difference.
4. **Report detection Hmean for the full method** (not just the Remove BAF variant) to allow readers to assess whether translation improvements come at a cost to text spotting quality.

## Score and Decision

The paper makes a solid technical contribution — the synchronous framework with BAF module is well-motivated and the ablation study generally supports the design choices. The STST800K dataset addresses a genuine need. However, the experimental section has several issues that prevent the contribution from being fully convincing: the UNITS baseline is inadequately documented, test set labels differ from standard protocols without sufficient caveats, and existing synchronous methods are not compared against. These are addressable in revision but are nontrivial gaps in the current submission.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>