## Summary

GroupLane proposes a novel 3D lane detection architecture that, for the first time, applies row-wise classification in bird's eye view (BEV) space. It uses channel-wise grouping (group convolution) so that each feature group corresponds to a lane instance, and a single-win one-to-one matching (SOM) strategy to associate predictions with labels during training. This design eliminates the need for post-processing (NMS), enabling fully end-to-end detection with only convolutional layers. On OpenLane, GroupLane with ConvNext-Base achieves 64.1% F1 (+13.6% over PersFormer), while the ResNet18 variant runs at 38 FPS (7× faster than PersFormer) with only 13.3% of its FLOPs, establishing a clear accuracy–efficiency Pareto improvement.

## Strengths

1. **Substantial accuracy–efficiency gains over published SOTA.** GroupLane with ResNet18 surpasses PersFormer by 4.9% F1 (55.4 vs. 50.5) on OpenLane while being ~7× faster (38.17 vs. 5.58 FPS) and using only 13.3% of PersFormer's FLOPs (Table 3). The ConvNext-Base variant achieves 64.1% F1, a 13.6% absolute improvement. This is documented in Tables 1 and 3 and represents a genuine Pareto improvement.

2. **First adaptation of row-wise classification to BEV for 3D lane detection, with explicit support for horizontal lanes.** The paper devises separate vertical and horizontal head groups performing row-wise classification in BEV. The horizontal head group nearly doubles performance on OpenLane-Huawei (F1: 31.00 → 35.82; DET-L: 9.34 → 17.07, Table 4), validating the design for crossroad/horizontal lane scenarios where prior row-wise methods fail.

3. **End-to-end detection via channel grouping + SOM, thoroughly ablated.** The channel grouping (group convolution) enables each feature group to act as a learned "query" without attention, and SOM provides train-time label assignment. The SOM ablation (Table 6) shows it boosts F1 from 24.5 to 60.2 on OpenLane, demonstrating that the matching strategy is critical for end-to-end learning.

4. **Fast convergence.** GroupLane converges in ~4 epochs on OpenLane (Fig. 2), compared to the 100 epochs required by PersFormer — a practical advantage for development cycles.

5. **Consistent strong results across three real-world benchmarks.** GroupLane achieves SOTA on OpenLane (64.1%), Once-3DLanes (80.73% with ResNet18), and OpenLane-Huawei (35.82%), suggesting the design generalizes across datasets with different characteristics.

6. **Thorough ablation studies.** The paper ablates channel group number (Table 5), group convolution vs. standard convolution (Table 5), category head design (Table 7), horizontal head group (Table 4), and SOM matching (Table 6), providing controlled evidence for each component.

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled BEV transformation confound (LSS vs. IPM).** The paper adopts LSS (from BEVDepth) to produce the BEV feature, whereas prior methods like PersFormer use IPM. The paper asserts that "LSS predicts depth explicitly and leads to more promising performance" (line 36) but provides **no ablation** that isolates whether the reported gains come from the proposed detection heads or from switching the BEV representation from IPM to LSS. Since LSS is known to improve performance in other BEV tasks, the attribution of the ~14% F1 improvement to the proposed grouping heads and row-wise classification is not cleanly separable. An ablation holding the BEV transformation fixed (e.g., GroupLane with IPM, or PersFormer with LSS) is needed to determine how much of the claimed superiority is due to the method contributions versus a better input representation borrowed from prior work. This is the single most important gap in the experimental validation.

### Minor

1. **Channel grouping accuracy benefit is marginal.** Table 5 shows that using group convolution (vs. standard convolution) with the same per-group channel count yields only a 0.43% F1 improvement (57.27 → 57.70), which is within typical run-to-run variance. The paper acknowledges this is "slight" (line 338) and correctly frames the primary role of grouping as enabling end-to-end detection. However, the paper also claims grouping "alleviates the optimization difficulty" — the accuracy evidence for this claim is weak. Testing standard convolution + light NMS as a baseline would help clarify whether the grouping's practical benefit is in accuracy or in simplifying the pipeline.

2. **SOM assignment stability for diagonal/curved lanes is unexamined.** The SOM heuristic assigns each label to the head group (vertical or horizontal) whose direction yields more crossed BEV grids. This is reasonable for axis-aligned lanes, but the paper does not discuss what happens for diagonal lanes or curves that cross similar grid counts in both directions. The assignment could become unstable, and the method's behavior in such cases is unclear. A brief analysis or discussion would strengthen the empirical narrative.

3. **Efficiency comparison uses different backbones.** The efficiency comparison (Table 3) pits GroupLane with lighter backbones (ResNet18/50, ConvNext-Base) against PersFormer with EfficientNet-B7. The paper transparently notes that EfficientNet-B7 cannot fit on their GPUs (line 275), which is a practical limitation. However, some of the reported speed and FLOPs gains inevitably come from backbone choice rather than architectural innovation. A comparison with GroupLane using a more comparable backbone (or PersFormer with a lighter backbone) would better isolate the architectural contribution to efficiency.

### Trivial
None.

## Nice-to-Haves

- **Epoch-by-epoch F1 after convergence.** Fig. 2 evaluates every 2 epochs and shows convergence by epoch 4. Reporting per-epoch results would give a finer-grained picture of when training is truly done.
- **Failure case analysis.** The limitation discussion (line 377) focuses on depth estimation error. A brief analysis of when GroupLane underperforms (e.g., heavy occlusion, distant lanes, extreme curves) would strengthen the empirical narrative.
- **IPM variant of GroupLane.** If an IPM-based GroupLane variant cannot be run due to architectural incompatibility, a discussion of why would be a useful addition.

## Removed Points

- **"The paper does not frame grouping as enabling end-to-end detection."** — Removed because the paper clearly frames grouping this way: "how the channel grouping strategy realizes end-to-end 3D lane detection" (Fig. 4 caption, line 95) and "In this way, we realize end-to-end 3D lane detection without troublesome post-processing" (line 100). The paper frames grouping as serving *both* purposes, and the accuracy benefit is acknowledged as slight. The critic's claim that the paper "does not frame it that way" is incorrect.

- **The critic's softened language about backbone differences.** — The paper already transparently discloses the GPU limitation (line 275) and explains why EfficientNet-B7 cannot be used. The critic's observation is fair but the paper's handling is adequate; moved here from Major to Minor.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's strengths and the main weakness (BEV confound), without raising genuinely novel observations about the work.

## Suggestions

1. **Add an ablation isolating the BEV transformation.** This is the most important experiment for validating contribution attribution. If LSS→IPM replacement causes a large drop, the paper should reframe its contributions accordingly; if the drop is small, the claims are strengthened. Even if IPM is architecturally incompatible with the pipeline, discussing *why* and quantifying the likely effect would help.

2. **Compare standard convolution + NMS as a baseline against the grouping strategy.** This would clarify whether the grouping's primary benefit is accuracy (weak evidence) or the elimination of post-processing (stronger claim).

3. **Add a discussion of SOM behavior for near-diagonal lanes.** Even a brief paragraph acknowledging the edge case and noting that empirical performance on mixed datasets (e.g., OpenLane-Huawei) suggests the heuristic is adequate would address the concern.

## Score and Decision

**Originality:** Good — first to bring row-wise classification to BEV for 3D lane detection, and the channel-grouping-as-queries design is a clean architectural insight.  
**Importance of research question:** High — efficiency in 3D lane detection is practically important for deployment.  
**Claims supported:** Mostly yes, but the BEV confound weakens attribution of the main accuracy results.  
**Soundness:** The experiments are well-designed except for the missing BEV ablation. Ablations are otherwise thorough.  
**Clarity:** Clear writing with good motivation and exposition.  
**Value to community:** Significant — the approach is simple, fast, and achieves strong results, making it a useful reference for future work.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>