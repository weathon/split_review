Now I have a clear picture. Let me write the consolidated review.

## Summary

CLIP-DETR integrates pretrained CLIP knowledge into DETR-based object detectors through two training-only modules: AlignNet (which refines encoder feature maps via category- and scale-aware contrastive alignment using GT boxes) and DynQL (which injects noise-varied prompted queries into the decoder to improve query-object correspondence learning). The method is evaluated on COCO, LVIS, and open-vocabulary COCO, showing consistent improvements over DETR baselines.

## Strengths

- **Consistent improvements across multiple DETR baselines and datasets.** On COCO (Table 1), CLIP-DETR with ResNet-50 achieves a +3.9% mAP gain over Deformable-DETR, and +5.1% with a CLIP image encoder backbone. On LVIS (Table 2) it outperforms Co-DETR across configurations. On open-vocabulary COCO (Table 3), it adds +1.4% and +1.7% AP50 on novel categories for OV-DETR and CORA respectively. These results directly support the paper's central claim.

- **Strong ablation evidence for both components.** Table 4 shows that AlignNet and DynQL each independently improve the baseline, and their combination yields the largest gain — confirming complementarity. Tables 5–7 provide thoughtful ablations on scale-aware alignment, noise diversity, and the number of DynQuery sets.

- **Insightful finding about translation invariance in feature alignment.** Table 5 reveals that aligning with [w,h] (scale only) outperforms full [cx,cy,w,h] alignment. The authors correctly attribute this to translation invariance — a non-obvious practical design insight.

- **Inference-time efficiency preserved.** Both modules are training-only (Figure 1), so CLIP-DETR incurs no additional computational cost at inference compared to the baseline DETR — a practical strength for deployment.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Unspecified training schedule for the headline 3.9% gain (line 175).** The paper reports "an mAP gain of 3.9% over the baseline" but does not say whether this refers to the 12-epoch or 36-epoch schedule (both are described in the Setup, line 169). The ablation studies (line 187) explicitly use a 12-epoch setup, but the main result text simply says "over the baseline" without qualification. The table images cannot be read in this parsed format to cross-check; this ambiguity makes the central quantitative claim needlessly hard to verify. The authors should state which schedule this refers to.

- **Open-vocabulary evaluation scope.** The OV experiments compare against only two baselines (OVDETR and CORA), both DETR-based. The paper claims "state-of-the-art" open-vocabulary performance, which is not defensible without comparison to a broader set of contemporary OV methods. This does not invalidate the contribution — the paper's scope is a DETR training scheme, and the DETR-focused comparison is reasonable — but the "state-of-the-art" language should be tempered. Reporting only AP50 (standard for this benchmark, as the paper notes) is acceptable within the OV-COCO convention.

- **Missing limitations discussion and training cost analysis.** The paper does not discuss when CLIP-DETR might underperform (e.g., if CLIP text embeddings are poorly aligned with the detection domain) and provides no analysis of the added training cost from DynQL's extra queries (up to 5× the number of instances per batch). While not a fatal omission, both would help readers assess the method's practical trade-offs.

- **Limited motivational specificity.** The introduction frames the problem as "limited refinement for object features" leading to "inferior inherent understanding of objects" (line 4), which is vague. The motivation would be sharper if it connected a specific observed failure mode of DETR (e.g., small objects, rare categories) to the design of AlignNet and DynQL.

### Trivial

- **Notation in Eq. 1:** The summation index runs `i` over `L` levels, but `i` already denotes the instance ID. It should be `l` (the level index). Likely a parser artifact, but worth checking the original.

## Nice-to-Haves
- A sensitivity analysis on the number of DynQuery sets and noise range across multiple datasets (currently only COCO).
- A direct head-to-head comparison with DN-DETR/DINO under identical noise levels to isolate the benefit of using CLIP-derived prompts versus random noise.
- A failure case analysis showing which object categories or scales benefit most from each module.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh Critic Claim 1 (numerical inconsistency between text and table):** The reviewer speculates that the table shows 43.9 while the text implies 46.0. The tables are embedded as images in the original PDF and cannot be read in this parsed format; the numbers 42.1, 43.9, and 46.0 do not appear anywhere in the paper's text. This criticism is based on unverifiable guesswork from garbled parser output, not an actual discrepancy in the submission. The genuine sub-issue (unspecified schedule) is retained under Minor.

- **Harsh Critic Claim 2 (unclear baseline construction and fairness):** The paper explicitly states (line 159–160): "we chose Deformable-DETR as the foundational detector and built all models upon it to ensure a fair comparison." The reviewer's concern about unreported re-implementation differences is addressed directly by this statement. Removed as a misreading.

- **Criticism about only AP50 for OV detection (Section 4.2):** The paper notes (line 182) that "standard practice for OV-COCO" is reporting AP50. This is correct — it is the established convention in the open-vocabulary detection literature. Removed.

- **Criticism about missing comparison to ViLD, RegionCLIP, Detic, BARON:** These are non-DETR methods. The paper's scope is a training scheme for DETR-based detectors; comparing against non-DETR baselines is outside the paper's stated scope. Moved from Weaknesses to Removed Points.

## Novel Insights

None beyond the paper's own contributions. The reviews raise no observation about the method or results that the paper itself does not already state or imply.

## Suggestions

1. Specify in the Results section (line 175) which training schedule (12-epoch or 36-epoch) the 3.9% gain refers to, and add a direct cross-reference to the specific table row.
2. Tone down the "state-of-the-art" claim for open-vocabulary detection given the limited DETR-only baseline set, or add non-DETR OV baselines to the comparison.
3. Add a brief limitations paragraph and a note on training-time overhead (GPU-hours or time per epoch).
4. Sharpen the introduction's motivation by connecting to a concrete failure mode of DETR (e.g., small object recall or rare-category performance) that AlignNet/DynQL specifically address.

## Score and Decision

The paper presents a clean, well-ablated method with two novel components (AlignNet and DynQL) that consistently improve DETR-based detection. The main weaknesses are presentational — an ambiguous specification of which training schedule the headline number refers to, and overclaimed "state-of-the-art" language relative to the OV baseline set — neither of which undermines the core contribution. The ablations are thorough and the design insights (e.g., scale-only alignment outperforming full bbox alignment) are genuinely informative. The paper makes a solid contribution to DETR-based object detection.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>