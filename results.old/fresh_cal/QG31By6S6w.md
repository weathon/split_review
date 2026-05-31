Now I have all the evidence I need. Let me construct the final consolidated review.

## Summary

This paper presents **Malenia**, a vision-language pre-training framework for 3D zero-shot lesion segmentation in CT scans. The method introduces: (1) a multi-scale mask-attribute alignment strategy that decomposes radiology reports into eight elemental visual attribute descriptions (location, shape, density, etc.) and aligns them with multi-scale mask embeddings via a multi-positive contrastive (MP-NCE) loss; (2) a Cross-Modal Knowledge Injection (CMKI) module that fuses mask and attribute embeddings through cross-attention, producing two complementary prediction branches that are ensembled. Experiments on MSD, KiTS23, and an in-house dataset across 12 lesion categories show substantial gains over prior zero-shot methods (ZePT, SAM, SAM2, SaLIP, H-SAM) on unseen lesions, with improvements of 6–9% DSC.

## Strengths

- **Novel multi-scale mask-attribute alignment with MP-NCE loss.** Decomposing reports into structured descriptions of eight elemental visual attributes (Section 3.1(2)) and aligning multi-scale mask embeddings with each attribute separately via the MP-NCE loss (Eq. 6) is a well-motivated design grounded in radiological practice. The ablation in Table 3 (rows labeled S₁, S₂, S₃) shows each component contributes monotonic improvements on both seen and unseen lesions.

- **Cross-Modal Knowledge Injection (CMKI) module.** The CMKI module (Section 3.2) fuses mask and attribute embeddings via cross-attention and generates predictions from both enhanced modalities. Table 4's ablation demonstrates deep fusion consistently improves DSC (e.g., pancreas tumor from 41.22 to 43.30), and ensembling both branches outperforms unimodal predictions. Figure 5 provides clear qualitative evidence of complementarity — the text branch reduces false positives and refines blurry boundaries.

- **Large and consistent zero-shot gains.** Table 1 reports DSC/NSD on six unseen lesion types from three datasets. Malenia outperforms all five compared methods (SAM, SAM2, SaLIP, H-SAM, ZePT) by at least 6.40% DSC on MSD, 8.14% on KiTS23, and 9.08% on the in-house dataset. The gains are consistent across all six lesion categories, which is strong evidence of genuine generalization ability rather than task-specific overfitting.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Imprecise caption claim about training data (Table 1).** The caption states "All competing methods are trained on the same dataset." This is imprecise — the paper's own text (line 177) describes SAM/SAM2 as zero-shot methods used directly, SaLIP as "fine-tuning-free," and only ZePT and H-SAM (and Malenia) are trained. The comparison itself is fair and the paper properly distinguishes the methods in the text, but the caption wording conflates distinct zero-shot settings. This should be corrected to avoid misleading readers.

- **Standard deviation not reported for zero-shot results (Table 1).** The zero-shot evaluation in Table 1 reports only point estimates of DSC/NSD without variance. While the large margins make the main conclusions robust, reporting standard deviations or per-sample distributions would help assess result reliability, especially for smaller test subsets.

- **Attribute extraction pipeline not fully reproducible.** The semi-automatic pipeline uses GPT-4 and two radiologists to generate structured attribute descriptions (Section 3.1(2)), but the specific prompts, review criteria, and the final attribute descriptions for the 12 lesion categories are not included in the paper. While "codes will be publicly available" is noted, the prompts and attribute templates are essential for reproducibility of the core data preparation step.

- **CMKI table notation not fully self-contained.** The ablation table for CMKI (Table 4) uses abbreviations TE (text embeddings), MT (mask tokens), DF (deep fusion). The main text (line 323) does define these, but the table caption itself could be more self-explanatory — it currently only says "Ablation study of the Cross-Modal Knowledge Injection module" without decoding the column headers.

### Trivial
- A few minor presentation imprecisions: (1) the shared eight visual attributes (location, shape, density, etc.) are listed but not defined with concrete examples in the main text; (2) the figure reference for qualitative CMKI analysis is labeled Fig. 5 in the text but the figure is captioned as "ABvis" — the paper would benefit from a final proofread on cross-references.

## Nice-to-Haves

- An analysis of which attribute axes (shape vs. density vs. location, etc.) contribute most to zero-shot gains would deepen understanding of the method. A leave-one-attribute-out ablation on a few zero-shot categories could reveal whether all eight are needed or a subset dominates.
- Clarifying whether any patient overlap exists between training and testing sets for the in-house dataset would strengthen the zero-shot claim.
- The paper mentions that text features are stored at inference (removing the text encoder overhead, line 155). Reporting inference speed/memory comparisons would be a nice practical addition.

## Removed Points

- **"Missing fully-supervised nnUNet oracle" (Harsh Critic #2):** The critic claims the paper states "Malenia achieves zero-shot performance comparable to fully-supervised nnUNet" but does not provide the numbers. This is factually wrong — the relevant sentence begins with `%` (LaTeX comment) at line 181 and is NOT part of the visible paper. The paper does not make this claim. **Removed as factually incorrect.**

- **"Reproducibility of attribute extraction pipeline" framed as a critical/fatal issue:** While the attribute pipeline details are not fully specified (kept as a Minor weakness above), the critic's framing as a fatal reproducibility flaw is overwrought. The paper describes the pipeline (GPT-4 extraction → two radiologists review → third adjudicator), the eight attribute categories, and states code/data will be released. This is standard for medical VLP papers. **Downgraded from fatal framing to Minor.**

- **"SAM prompt usage not clarified":** The paper explicitly states (line 179): "Without target data for fine-tuning and accurate manual prompts, the SAM and SAM 2 struggle with lesion segmentation in the zero-shot setting." This makes it clear that no manual prompts were provided. **Removed — concern already addressed.**

- **"Baseline not clearly defined" (naive single-scale mask-report alignment):** The paper defines "Baseline" as "the naive single-scale mask-report alignment performed at the last Transformer decoder block" (line 255). This is unambiguous given the context (standard Mask2Former with mask-text alignment at one resolution, using raw reports). **Removed — sufficiently clear.**

- **Generic/superficial strengths from Strength Finder (semi-automatic pipeline, multi-scale features, ensemble):** These are all real components but are already covered under the core strengths above (multi-scale alignment, CMKI module). Keeping them as separate strengths would artificially inflate the count. **Merged or removed as redundant.**

## Novel Insights

None beyond the paper's own contributions. The reviews raise useful presentational and reproducibility points but do not identify a novel angle on the problem that the paper itself misses.

## Suggestions

1. Correct the Table 1 caption to accurately reflect which methods were trained vs. used off-the-shelf.
2. Release the GPT-4 prompts, radiologist review instructions, and the final structured attribute descriptions for all 12 lesion categories alongside the code.
3. Report variance (standard deviation) for the zero-shot results in Table 1.
4. Add a brief analysis of attribute axis importance — e.g., a leave-one-axis-out ablation on one or two zero-shot categories.
5. Add a patient-level overlap check for the in-house dataset.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>