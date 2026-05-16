Now I have a thorough understanding of the paper. Let me compose the consolidated review.

## Summary

This paper proposes SpikSSD, a full-spiking SNN-based object detector that improves both feature extraction (via MDS-ResNet, which stabilizes membrane synaptic input distributions) and feature fusion (via SBFM, the first spiking bi-directional fusion module). The system achieves state-of-the-art results among SNN-based detectors on GEN1 (40.8% mAP, first full-spiking SNN above 40%), VOC 2007 (76.0% mAP@0.5), and competitive results on COCO 2017, all at ultralow energy consumption.

## Strengths

- **MDS-ResNet provides a principled improvement to spiking feature extraction, supported by convincing empirical evidence.** Figure 1 and Table 1 (rows 1–4) demonstrate that MDS-ResNet18 achieves higher mAP (30.3%) with a lower firing rate (5.9%) compared to EMS-ResNet18 (28.9% mAP, 7.1% firing rate). The variance stabilization mechanism is well-motivated and the firing pattern visualizations credibly show sparser, more uniform activity across layers. The ablation showing monotonic improvement with depth (Table 1 rows 5–7: 30.3% → 33.5% mAP from ResNet18 to ResNet50) further corroborates that gradient flow is maintained.

- **SpikSSD achieves state-of-the-art results among SNN-based object detectors on multiple benchmarks while maintaining ultralow energy.** On GEN1, SpikSSD-L reaches 40.8% mAP — the first full-spiking SNN above the 40% threshold — consuming only 0.80 mJ versus 5.03 mJ for the prior best SNN (EAS-SNN). On VOC 2007, it achieves 76.0% mAP@0.5 (best among SNNs). These results establish a new benchmark for SNN object detection and demonstrate that the system-level integration of backbone + fusion improvements is effective.

- **Membrane-addition-based fusion is a clean alternative to concatenation-based spiking fusion.** Rather than concatenating spike trains (which expands channels and complicates feature alignment), SBFM adds membrane synaptic inputs from different scales, then processes the result with spiking depthwise separable convolution in the MDSF-Block. This design preserves spiking properties and avoids the non-spiking operations present in prior SFM (which used SEW-Block internally).

- **Comprehensive ablation study.** Table 1 systematically examines backbone choice, model depth, fusion module, event time window, and input scale — providing practical design insights (e.g., 100ms/200ms training/inference scheme yields best results).

## Weaknesses

### Fatal
None.

### Major

- **The claimed benefit of *bi-directional* fusion over one-way fusion is not adequately supported.** The paper cites bidirectional fusion as a core contribution ("the first time realiz[ing] bi-direction fusion of spiking features"). However, the ablation (Table 1 rows 8–10) only compares models *with* SBFM versus *without any fusion* — this shows that fusion helps, but does not isolate whether the second (up-down) pass in the bi-directional design provides additional benefit over a one-way (down-up only) design. A controlled comparison between a one-way variant and the full bi-directional variant (with the same backbone and detection head) is missing. The only existing one-way fusion method (SFM) operates on a different backbone (DenseNet), making cross-table comparisons confounded. This weakens the evidential support for a central claimed contribution. The authors could add this ablation and likely resolve this issue — in its current form the claim outstrips the evidence.

### Minor

- **The theoretical gradient analysis (Section 3.3) overreaches and is not essential to the paper's contributions.** The argument that LIF neurons qualify as "general linear transforms" is asserted via citation rather than justified in the text. Given that the empirical evidence (deeper MDS-ResNets improve performance) already adequately supports good gradient flow, the theoretical treatment is unnecessary and risks appearing hand-wavy. The paper would be stronger by either providing a rigorous justification or removing the section entirely.

- **The abstract's "around 10% firing rate" is inconsistent with the actual reported rates.** The abstract claims "only around 10% firing rate" but Table 1 shows MDS-ResNet18 at 5.9% and Table 2 shows SpikSSD firing rates of 5.7% and 7.6% (per the reviewer's reading). These are notably lower than 10%; the phrasing should be corrected to reflect the actual numbers (e.g., "under 8%" or the specific values).

- **Architectural specificity for reproducibility:** The MDSF-Block uses "spiking depthwise separable convolution" but does not specify whether LIF neurons follow each of the depthwise and pointwise convolutions separately, or only once after the combined operation. This should be clarified for reproducibility.

- **No explicit limitations discussion.** The paper lacks a limitations section. While the conclusion mentions future work on detection heads, a brief discussion of failure cases (e.g., small object detection, high-speed event scenarios) would strengthen the paper.

### Trivial

- The energy calculation method is deferred entirely to the supplementary; a one-paragraph summary in the main text (e.g., synaptic operations vs. MACs, assumed bit precision) would improve transparency without burdening the reader.

## Nice-to-Haves

- A controlled ablation comparing one-way (down-up only) vs. bi-directional fusion would directly support the bi-directional fusion claim. This is the single highest-leverage addition.
- Gradient norm histograms during training (as a simpler alternative to the Block Dynamical Isometry analysis) would empirically validate the gradient flow claim.
- Visual evidence of membrane potential distributions across layers (beyond firing rates) would further support the claimed mechanism of MDS-ResNet.

## Removed Points

These points from the input are flagged to be removed; treat them with caution:

- **"The supplementary is referenced but cannot be evaluated"** → Removed because appendices/supplementary are stripped by the parser and do exist in the original submission.
- **"The claim that 'the only fusion method designed for SNNs is SFM' may be too absolute"** → Removed per the rule against mentioning missing related works; I cannot independently verify whether other fusion methods exist.
- **"Table is garbled in extraction"** → Removed as a parser artifact, not an author error.
- **"The comparison of backbones includes DenseNet121-24... the claim of 'similar parameter sizes' is not supported by shown numbers (table is garbled)"** → Removed as a parser artifact; the original table reports parameter counts.

## Novel Insights

The most valuable insight from the review process is the recognition that the paper's strongest contribution is MDS-ResNet (supported by clean empirical evidence and ablation), while the SBFM contribution would benefit from sharper experimental design. The review also surfaces that the theoretical gradient analysis is largely ornamental — the empirical scaling with depth already makes the point. The firing rate discrepancy in the abstract is a small but meaningful presentation issue. Beyond these, no novel insight emerges beyond what the paper itself provides.

## Suggestions

1. **Add a controlled ablation**: Compare one-way (down-up only) vs. bi-directional fusion with the same backbone (MDS-ResNet) and detection head. This directly supports the core SBFM claim.
2. **Correct the abstract's firing rate claim** to match the actual reported numbers (e.g., "under 8%" or state the specific rates).
3. **Either substantiate or remove the Block Dynamical Isometry analysis** — the current treatment is too thin to be convincing and the paper does not need it.
4. **Clarify the LIF neuron placement** in the spiking depthwise separable convolution within MDSF-Block.
5. **Add a brief limitations paragraph** discussing failure modes or boundary conditions.

## Score and Decision

The paper makes genuine contributions: MDS-ResNet is a well-motivated and empirically validated improvement to spiking feature extraction, SpikSSD achieves SOTA among SNN detectors across three benchmarks with ultralow energy, and the system-level design is coherent. The main weakness is that the bi-directional fusion claim lacks a controlled ablation isolating the effect of the second fusion direction. This is a significant gap but is addressable (a single ablation experiment) and does not invalidate the paper's other contributions or its overall empirical standing. I recommend acceptance with the expectation that the authors address the missing ablation and minor presentation issues.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>