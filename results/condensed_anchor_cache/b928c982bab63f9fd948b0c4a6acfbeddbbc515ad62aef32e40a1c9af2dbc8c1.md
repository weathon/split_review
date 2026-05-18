- Decision: Accept
- Scores: 6, 6, 6, 6

## Merged Review

### Summary
HiSplat introduces a coarse-to-fine strategy to construct hierarchical 3D Gaussians for generalizable 3D Gaussian Splatting from two-view sparse input. The method uses an Error Aware Module and a Modulating Fusion Module to enhance inter-scale interactions, jointly optimizing hierarchical representations. Experiments on multiple datasets demonstrate better reconstruction quality and cross-dataset generalization than prior single-scale methods.

### Strengths
1. **First hierarchical 3D Gaussian representation in generalizable 3DGS** (R1, R2). The multi-scale design is well-motivated: not all image points are equally important, and different scales capture large-scale structure and fine details simultaneously (R2, R3).
2. **Clever module design** (R3, R4): The Error Aware Module and Modulating Fusion Module are interesting and effectively filter errors from photometric loss in a simple, feed-forward way. The Error Aware part is particularly praised for incorporating reconstruction error refinement (usually gradient-based) into the feed-forward model; this idea could benefit other tasks (R3).
3. **Complete and informative ablation study** (R1, R2, R3). Fig. 4 effectively demonstrates how the hierarchical representation improves reconstruction by showing primitives from different stages (R1). The analysis in Sec. 4.4 is very informative and useful, showing how multi-scale features help reconstruction quality (R3).
4. **Extensive experiments** showing SOTA performance and convincing results (R4). Generalization to unseen datasets like DTU is noted as interesting (R2). The paper is easy to follow and well-written (R1,R3,R4).

### Weaknesses
1. **Model complexity and efficiency** (R1, R2, R3). The method introduces many modules, slowing inference compared to MVSplat (Tab. 4) (R2). The overall model is complex, containing MVSformer++, DINOv2, and multiple UNets/MLPs; it is unclear which modules are trainable vs. fixed (R3). Memory, FLOPs, and inference time are not discussed, yet the hierarchical representation is likely memory-intensive (R1). A complexity analysis is requested (R1,R3).
2. **Marginal improvement over baseline in some cases** (R2). While overall metrics show SOTA, one reviewer found the improvement over MVSplat not very significant from their perspective. Some visualized cases (e.g., Fig. 6 last line, Fig. 1 left red bounding box) do not show clear improvement (R2). Another reviewer considers the results convincing (R4), so the evidence is somewhat mixed.
3. **DINO feature necessity not convincingly demonstrated** (R1). The performance gain from including the DINO feature is marginal, and experiments do not clearly justify the added complexity and computational overhead. A more detailed discussion of its importance is needed. (This point overlaps with model complexity.)
4. **Limited to two input views; extension to more views not explored** (R1, R4). Most experiments use only two perspectives. Reviewers would like to see discussion on how the method could handle more input views, like FreeSplat does, or an exploration of how quality improves with more perspectives (R1,R4).
5. **Missing comparisons and discussions with related works** (R4). FreeSplat (also uses cost-volume with multi-scale strategy), Splatt3R, and CasMVS (cascade MVS) are not discussed. The architecture has similarities to CasMVS; deeper analysis of technical differences and more valuable comparison are needed.
6. **Number of Gaussian primitives unclear** (R2). It is unclear how the hierarchical structure changes the total primitive count compared to baseline methods. A comparison of primitive numbers is requested.
7. **Claim about fewer artifacts in occluded areas needs stronger evidence** (R2). The example in Fig. 6 (first example) is suggestive, but may be coincidental. More rigorous justification or additional examples are required.
8. **Minor issues** (R1, R3): Spelling errors (lines 73, 106, 508; L298 “fellow” → “follow”); typo “MVSpalt” → “MVSplat”; citation format does not follow ICLR template (use `\cite`/`\citep` properly) (R3).
9. **Depth coefficient η selection** (R3): It is unclear whether η is a fixed value per stage after training; the choice of η values is not explained.
10. **Pose-free extension** (R3): A question about whether the method can handle unknown camera poses from sparse views in real-life scenarios; if easy to implement, examples would be appreciated. (This is a missing experiment/discussion point.)