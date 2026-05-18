Now I have a clear calibration picture. Let me write the final consolidated review.

Here is my assessment based on the paper, the reviews, and the calibration anchors:

**Round 1 bracket**: The paper sits between 4.5 and 7.0, most likely in the 5.0–6.5 range. It is clearly stronger than the 2–3 score papers (incoherent/insubstantial works) and the 4.75 survey study, but not as strong as the 7.5 analysis paper which has a different contribution type. The best comparisons are the 6.0-scoring PETL papers (ProPETL, META).

**Round 2 narrowing**: The most comparable anchors cluster at 6.0. The HST paper has a broader experimental scope than ProPETL (classification + detection + segmentation vs. segmentation only), a more novel architectural contribution, and similarly thorough ablations. Its main deficiency relative to these anchors is the concretely empty efficiency section (Section 4.5) — a flaw that is more visible than ProPETL's comparable omissions. On balance, the paper is on par with the 6.0 anchors.

---

## Summary

This paper proposes Hierarchical Side-Tuning (HST), a parameter-efficient transfer learning method for Vision Transformers. HST introduces a lightweight Hierarchical Side Network (HSN) that runs in parallel with a frozen ViT backbone, receiving both multi-scale image features and intermediate ViT activations via a Transformation Bridge (T-Bridge) with two injection pathways (Meta-Global and Fine-Grained). A single-token Meta-Register inserted into each ViT block extracts global context. Experiments span image classification (VTAB-1K, FGVC), object detection (COCO), instance segmentation, and semantic segmentation (ADE20K), where HST achieves new SOTA among PETL methods with only 0.78M trainable parameters and approaches or surpasses full fine-tuning on several dense prediction settings.

## Strengths

- **State-of-the-art results on VTAB-1K with extreme parameter efficiency.** Table 1 shows HST-B achieves 76.12% average Top-1 across 19 tasks with 0.78M trainable parameters — surpassing all prior PETL methods (best prior: NOAH 73.20%) and full fine-tuning (65.57%) by 10.5 points. The improvement is consistent across all three VTAB-1K splits (Natural, Specialized, Structured).

- **Consistent dense-prediction gains over existing PETL methods.** On COCO Mask R-CNN 3×+MS (Table 3), HST achieves 43.9 AP^b vs. LoRA's 39.3; on Cascade Mask R-CNN 3×+MS (Table 4), HST reaches 49.5 AP^b, surpassing full fine-tuning (48.7) — the only PETL method to do so. On ADE20K semantic segmentation (Table 6), HST achieves 47.0 mIoU with UperNet, outperforming the next-best PETL method (SSF, 44.9) by 2.1 points.

- **Well-designed architecture with clear motivation.** The HSN's cross-attention mechanism has O(2Ld) complexity (Eq. 3), linear in the sequence length. The Meta-Register design avoids the costly per-task prompt-length search required by VPT. The component ablation (Table 7) cleanly isolates the contribution of each module (LN tuning, weight sharing, GlobalT, FG Injection), showing that full HST adds 4.0% on VTAB-1K and 10.3 AP^b on COCO over the HSN-alone baseline.

- **Robustness across two pre-training paradigms (ImageNet-21K and MAE).** Table 2 shows that under MAE pre-training — where most PETL methods degrade sharply — HST outperforms full fine-tuning on Oxford Flowers (91.2 vs. 90.9) and Stanford Cars (83.7 vs. 91.5) and narrows the gap on others, demonstrating versatility across foundation models.

## Weaknesses

### Major

- **Section 4.5 (Efficiency Analysis) is completely empty.** The subsection exists at line 376 (`\subsection{Efficiency Analysis}`) but has zero content — it is immediately followed by `\subsection{Visualizations}`. Given that parameter efficiency and computational overhead are central claims of the paper, this is a substantive omission. The paper reports parameter counts but provides no FLOPs, training/inference time, memory footprint, or throughput comparisons against other PETL methods. Since HST's side network with cross-attention blocks may incur nontrivial inference overhead, the practical advantage over full fine-tuning or other PETL methods is unquantified. This section must be filled for any public version.

### Minor

- **Overclaiming relative to full fine-tuning in the abstract.** The abstract states HST "even surpassed full fine-tuning" on dense prediction tasks. This is true for Cascade Mask R-CNN (49.5 vs. 48.7 AP^b) but not for Mask R-CNN 3×+MS (43.9 vs. 45.1, −1.2 AP^b) or ATSS (46.0 vs. 46.7, −0.7 AP^b). The introduction more cautiously says "comparable performance" (line 29), creating an inconsistency with the abstract. The paper should qualify the claim to match the mixed empirical picture.

- **Parameter-controlled comparison not provided for dense prediction.** HST uses slightly more total trainable parameters than competing PETL methods in detection (e.g., Mask R-CNN 1×: HST 30.6M vs. LoRA 28.4M, SSF 28.0M). The paper notes that HST's smaller FPN dimensions [64,128,256,384] partially offset this (line 159), but does not provide an ablation where HSN width is reduced to match baseline parameter counts. Without this, it is unclear how much of HST's ∼4–5 AP^b gain over LoRA comes from extra parameters versus architectural design.

- **Missing comparison with LST despite discussing it as prior work.** The related work discusses LST (NLP side-tuning) and notes it "has not been proven to be effective in vision models" (line 54), but no experiment compares HST to an LST-like vision baseline. This would directly contextualize HST's improvements.

### Trivial

- The cosine similarity diagnostic in Figure 3 is not described in enough detail (which ViT layers, whether measured on validation or training data).
- Notation inconsistency: Table 7 column header has two `${\rm AP^b}$` entries.

## Nice-to-Haves

- **Statistical significance / variance reporting.** Many VTAB-1K tasks have small training sets where single-run results can be noisy. Reporting standard deviations across 3 seeds would increase confidence.
- **Side block depth ablation.** The HSN depth is set to match ViT depth (3-3-3-3 for ViT-B). Ablating with fewer blocks per stage would clarify whether gains come from depth or the injection design.
- **Ablation of fusion method (addition vs. concatenation/gating) for the Fine-Grained Injection.**

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *"Reproducibility: detail level for intermediate feature extraction"* — The paper cites prior work (li2021benchmarking) for the upsampling/downsampling approach and states the mapping (align Side blocks with ViT blocks, evenly distribute across 4 stages). This level of detail is standard for a conference paper; the removed section would be restored with camera-ready supplementary.
2. *"VPT-Deep also uses fixed prompt count"* — The critic's claim that the Meta-Register vs. VPT distinction is "not as sharp as implied" is a minor framing preference; the ablation (Table 5) convincingly shows single-token MR works, which is the substantive claim.
3. *"Full fine-tuning baseline on VTAB-1K is suboptimal"* — This is speculative. The paper uses the numbers reported in the VPT paper, which is the standard comparison protocol used throughout the PETL literature.
4. *"Figure 3 not methodological enough"* — The figure is a diagnostic, not a method component. Its description is adequate for its purpose.
5. Generic strengths from the Strength Finder that conflict with verified weaknesses or lack concrete evidence have been removed.

## Novel Insights

The reviews do not surface genuinely novel observations about the paper beyond the paper's own contributions. The main value of the reviews is in identifying the gap in the efficiency analysis and the need for parameter-controlled comparisons.

## Suggestions

1. **Fill Section 4.5 with concrete efficiency metrics** — report FLOPs, training/inference time (samples/sec), and peak GPU memory for HST vs. full fine-tuning and at least 2–3 PETL baselines (LoRA, SSF, VPT-Deep) on a representative task (e.g., Mask R-CNN 1×). This is the single most impactful improvement.
2. **Add a parameter-controlled variant** for the detection experiments — reduce HSN width so total trainable params match LoRA or SSF, then re-report key metrics. If HST still outperforms, the architecture claim is much stronger.
3. **Harmonize the abstract's claim about full fine-tuning** with the mixed empirical picture on dense prediction (e.g., "surpasses full fine-tuning on several settings" rather than the blanket "even surpassed full fine-tuning").
4. **Add an LST-style baseline** to the dense prediction experiments, since LST is discussed in related work as the closest inspiration.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>