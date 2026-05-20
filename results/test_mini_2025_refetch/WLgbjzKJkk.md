Now I have sufficient calibration data. Let me produce the final consolidated review.

## Summary

This paper tackles a key issue in end-to-end Transformer-based multi-object tracking (e2e-MOT): the unbalanced label assignment where tracking queries dominate positive samples while detection queries receive mostly negatives (only newborns). The authors propose CO-MOT with two components — Coopetition Label Assignment (COLA), which assigns tracked objects to detection queries in intermediate decoders to improve detection query utilization, and Shadow Sets, which augment each query with multiple shadow queries for one-to-set matching. Results on DanceTrack (69.4% HOTA), BDD100K (52.8% TETA), and MOT17 (60.1% HOTA) show consistent improvements over the MOTR baseline, competitive with MOTRv2 (which uses an external YOLOX detector) while using far fewer parameters (40M vs 139M).

## Strengths

1. **Well-diagnosed problem with strong empirical evidence**: Table 1 quantitatively shows that removing tracking queries during inference raises MOTR's detection mAP from 42.5% to 60.6% (+18.1%), and retraining without tracking queries yields 66.1% — cleanly demonstrating that tracking queries suppress detection queries, establishing a concrete problem for the paper to solve.

2. **Mechanistic evidence via attention analysis**: Figure 3 shows detection queries predicting the same object contribute >15% attention weight to corresponding tracking queries in decoders 3–6, and sometimes exceed tracking self-attention (T2T). This provides direct evidence that COLA enables detection queries to pass semantic information to tracking queries, rather than being speculative.

3. **Clean component ablation**: Table 3a isolates each contribution: COLA alone adds +3.8% HOTA (+5.1% AssA), and adding shadow sets yields +5.4% HOTA total, while DetA barely changes (71.8%→73.5%). This demonstrates the improvements are driven by association quality, not detection quality.

4. **Efficiency advantage over MOTRv2 without external detector**: CO-MOT achieves 69.4% HOTA with 40M parameters vs MOTRv2's 139M parameters, and ~1.4× faster inference, all without requiring a pretrained YOLOX detector. Even accounting for the query-count increase from shadow sets, the architecture-level comparison to MOTRv2 (which adds an entire external detection pipeline) remains valid.

5. **Systematic hyperparameter study**: Tables 3b-c exhaustively test combinations of representative selection strategies (λ, φ), initialization methods, and shadow counts, grounding design choices empirically.

## Weaknesses

### Fatal
None.

### Major

- **FLOPs/efficiency claim lacks explanation for increased query count**: The paper reports CO-MOT at 173G FLOPs and 19 FPS — identical to MOTR — despite multiplying queries by N<sub>S</sub>=3 (from ~300 to ~900). With self-attention scaling O(N²·d) and cross-attention O(N·K·d), the computational cost should increase measurably. The paper invokes "deformable attention" but deformability only affects cross-attention sampling sparsity, not the quadratic self-attention. The paper provides no mechanism (e.g., query grouping, sparse attention patterns, shared computation) that would explain unchanged FLOPs/FPS. This is the most significant weakness because it undermines a headline claim. *However*, this does *not* invalidate the core contribution: the comparison to MOTRv2 (455G FLOPs, 139M params, +external YOLOX detector) remains favorable even if CO-MOT's true FLOPs moderately exceed MOTR's, because the main efficiency claim is relative to MOTRv2's entire pipeline.

### Minor

- **BDD100K LocA gap is acknowledged but not analyzed**: CO-MOT's LocA (38.7%) trails MOTRv2 (49.5%) by 10.8 points. While the paper acknowledges this and correctly notes that AssocA (56.2%) exceeds MOTRv2 (51.9%), no analysis is given for why localization degrades so substantially. Is this a side-effect of COLA pulling detection queries toward tracked objects with imprecise boundaries, or of the shadow set's representative-selection strategy? An ablation isolating the source would strengthen credibility.

- **Shadow hyperparameter (λ, φ) selection on abbreviated schedule**: The λ and φ sweep in Table 3b is run on a 5-epoch schedule without COLA, but the final model uses 20 epochs with COLA. The resulting choices (λ=max, φ=min) are intuitive and validated indirectly by the full-model results, but the evidence for optimality under the final protocol is thin.

- **Single-run results without variance estimates**: All reported results are single-seed. DETR-style training is known to have non-trivial variance. While not unusual for the field, this omission limits confidence in the reported margins.

### Trivial
- Figure axes in the paper's caption text overlap labels (parser artifact from figure extraction).

## Nice-to-Haves
- An intervention study (e.g., ablating self-attention between detection and tracking queries while keeping COLA) to strengthen the causality claim for the attention mechanism.
- Ablation of different decoder-split configurations for COLA (e.g., how many intermediate decoders use cooperation vs. competition).
- Comparison on MOT20 (densely crowded scenes) which would better test the shadow set's claimed benefits for dense scenarios.

## Removed Points
- **"Shadow set adds little novelty beyond Group-DETR/H-DETR"**: The paper explicitly cites these works and distinguishes "one-to-set" from "one-to-many." The adaptation to tracking (inheriting the set assignment across time, using shadow queries for tracking continuity) is non-trivial. Removed as a strawman.
- **"Missing comparison to newer methods (DiffMOT, MambaTrack)"**: From reviewer 3's comment about ICLR2024 resubmission. This is a generic "add more baselines" critique without specific evidence that these methods are applicable to the e2e-MOT setting or would change the conclusions. Removed.
- **"Reproducibility details about how lost objects are handled"**: The paper states "zero if disappearing" for handling lost objects. Removed as already addressed.
- **Criteria-related speculative concerns from the harsh critic's section-by-section notes**: e.g., "The analysis is suggestive, not definitive" about attention weights. This is a generic validity concern without a concrete flaw in the analysis. Removed.
- **Strengths that are generic or conflict with verified weaknesses**: "Major efficiency gain over MOTRv2" is retained as a valid strength despite the FLOPs qualification, because the headline comparison (CO-MOT vs MOTRv2's full pipeline including YOLOX) still holds. The strength is not removed; it's incorporated with appropriate caveats in the final review.

## Novel Insights
The intersection of the harsh critic and the human reviewers surfaces a consistent pattern: the paper's central technical idea (using COLA to let detection queries assist tracking queries via self-attention) is genuinely well-motivated and empirically supported. The main unresolved tension is that the paper simultaneously claims "no extra cost" while introducing N<sub>S</sub>=3 shadow queries. The human reviewers gave this a 6 despite flagging the same issue, suggesting the community considers the COLA contribution strong enough to outweigh an imperfect efficiency characterization. The BDD100K LocA gap is a second-order concern that the paper should analyze but does not undermine the core contribution — the AssocA improvement (56.2 vs 51.9) is the headline for that benchmark, consistent with the paper's thesis.

## Suggestions
1. **Clarify the FLOPs measurement**: Explain whether the reported FLOPs count the decoder's self-attention at N×N<sub>S</sub> queries or whether shadow queries are processed differently than described. If the FLOPs figure is a miscalculation, provide a corrected number and recalibrate the efficiency comparison. Even if CO-MOT's FLOPs are moderately higher than MOTR's (say 200-250G), the comparison to MOTRv2 at 455G still strongly supports the efficiency claim.
2. **Analyze the BDD100K LocA gap**: Provide an ablation or analysis isolating whether COLA or the shadow set causes the localization degradation, and discuss whether this is a fundamental trade-off or an artifact of hyperparameter choices.
3. **Add variance estimates**: Report results across 2-3 seeds for the main benchmark, or at minimum note the observed variance.

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|-------------------------|
| /home/wg25r/review_agent/human_reviews/0ov0dMQ3mN.md (this paper) | 6.00 | R1, R2 | **Direct anchor** — human reviewers gave 6,6,6,6; accepted as Poster |
| /home/wg25r/review_agent/human_reviews/T6hhDEnAoo.md | 2.20 | R1 | Much weaker — remote sensing DETR with significant flaws |
| /home/wg25r/review_agent/human_reviews/FV5nsugDY1.md | 3.75 | R1 | Weaker — contrastive tracking with weak experiments |
| /home/wg25r/review_agent/human_reviews/V7QRVEZ0le.md | 4.33 | R1 | Weaker — Mamba-tracker with incremental contribution |
| /home/wg25r/review_agent/human_reviews/vyF5aim4US.md | 5.25 | R2 | Weaker — DETR detection method, accepted but less impactful |
| /home/wg25r/review_agent/human_reviews/oRlANEuqG5.md | 6.00 | R2 | Comparable — online point tracking, accepted Poster |
| /home/wg25r/review_agent/human_reviews/QlqdXrzzD1.md | 6.67 | R2 | Slightly better — 3D point cloud tracking with unified model |
| /home/wg25r/review_agent/human_reviews/Yen1lGns2o.md | 7.60 | R1 | Stronger — oral-level contribution, much broader scope |
| /home/wg25r/review_agent/human_reviews/Ha6RTeWMd0.md | 9.00 | R1 | Much stronger — foundation model (SAM 2) |

**Round-1 bracket:** 5.0 – 7.0  
**Round-2 narrowing:** The paper's own human reviews anchor it at 6.0 across all four reviewers (accepted as Poster). Compared to QFree-Det (5.25, rejected), this paper has clearer motivation and stronger experimental support. Compared to Track-On (6.0, accepted poster), the contribution weight is similar. The paper does not reach the level of 7+ papers (e.g., oral-level work or foundational models).

**Final score:** 6.0 — consistent with the human assessment of this paper: a solid, well-motivated contribution with a clear weakness (FLOPs claim) that is real but not fatal, and several minor gaps that do not undermine the core results.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>