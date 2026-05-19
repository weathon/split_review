- Decision: Reject
- Avg Score: 5.25
- Scores: 3, 6, 6, 6
Now I have all the information needed. Let me compose the consolidated review.

## Summary

This paper proposes 3DGraphLLM, a method that explicitly incorporates semantic relationship features between objects (via a 3D scene graph encoded by VL-SAT) into an LLM-based pipeline for 3D vision-language tasks. The scene graph is flattened into a token sequence where each object is represented by its identifier plus triplets from its k nearest neighbors. The approach is evaluated across six benchmarks (ScanRefer, RioRefer, Multi3DRefer, ScanQA, SQA3D, Scan2Cap) and shows consistent improvements over a zero-neighbor baseline across grounding, captioning, and QA tasks. A two-stage training strategy (GT segmentation pre-training then predicted segmentation fine-tuning) handles realistic noisy inputs.

## Strengths

1. **Controlled ablation isolates the benefit of semantic edges.** Table 3 directly compares the zero-neighbor variant (no semantic relations) with the two-neighbor variant under the same LLM and training pipeline. On ScanRefer Acc@0.25 with LLAMA3-8B-Instruct, adding semantic edges raises accuracy from 52.46 to 55.01, providing clean evidence for the core thesis.

2. **Two-stage training strategy addresses a real practical challenge.** Section 3.3 describes a pipeline that pre-trains on GT instance segmentation then fine-tunes on noisy predicted segmentation. Table 3 confirms this improves grounding accuracy (e.g., LLAMA3 ScanRefer Acc@0.25 from 54.35 to 55.01) and question answering (SQA3D EM from 55.14 to 55.92), showing the method works under realistic conditions where GT segmentation is unavailable.

3. **Token-efficiency analysis with practical guidance.** Section 3.2 and Figure 4 demonstrate that k=2 nearest neighbors reduces the token count from 29,900 (complete graph, 100 objects) to 800, while still improving accuracy over the no-graph baseline. The explicit trade-off plot between inference speed and accuracy is useful for practitioners.

4. **Robustness to noisy segmentation studied through filtering techniques.** Table 4 shows that NMS and minimum-distance (1 cm) filters compensate for spurious neighbor relations introduced by Mask3D predictions, improving RioRefer grounding accuracy from 29.57 to 35.04. This analysis addresses a concrete failure mode of the approach in realistic settings.

5. **Cross-domain transfer demonstrated.** VL-SAT requires only 3D point coordinates for inference and transfers across scene domains (ScanNet → 3RScan). The positive results on RioRefer (3RScan scenes) in Table 2 confirm that the relation encoder generalizes beyond its training domain without retraining.

## Weaknesses

### Fatal
None.

### Major
None. The core claim — that explicitly encoding semantic relationships improves LLM-based 3D scene understanding — is well-supported by the controlled ablation across tasks and model variants.

### Minor

1. **Imprecise baseline equivalence claim.** The paper states (line 104) that the zero-neighbor variant 3DGraphLLM-0 is "equivalent to the Chat-Scene approach." Without a precise specification of what Chat-Scene includes (e.g., whether it also uses spatial relation tokens from bounding-box coordinates), this claim is not fully verifiable from the text. The paper's own spatial-relation experiment (Table 5) partially mitigates this concern by showing that adding spatial relations does not improve performance, but the description should be more precise about what aspects of Chat-Scene are matched.

2. **No variance estimates for key results.** All reported numbers are point estimates from a single run. The improvements from adding semantic edges (e.g., +3.07 pp on ScanRefer Acc@0.25 for LLAMA3) are consistent across tasks and model variants, which partially addresses this concern, but the absence of error bars or multi-seed statistics makes it impossible for the reader to assess whether gains are stable or within optimization noise.

3. **DINOv2 feature aggregation method unspecified.** Line 43 states that DINOv2 features are "obtained by aggregating features from the masked multi-view images" but does not specify the aggregation operation (average, max, attention-pooled, or other). This is a minor reproducibility gap.

4. **Training epochs per stage not reported.** The paper states (line 88) a total of 3 training epochs but does not specify the per-stage allocation between the GT pre-training and the predicted-segmentation fine-tuning phases described in Section 3.3.

5. **SOTA claim in conclusion is stronger than justified by inspectable evidence.** The conclusion (line 139) states the method "demonstrated state-of-the-art quality on popular ScanRefer, Multi3DRefer, and Scan2Cap datasets." Without the full contents of Table 2 being verifiable in the extracted text, and given that Table 2's comparison set cannot be assessed, a more measured claim such as "competitive with state-of-the-art LLM-based methods" would be more appropriate.

### Trivial

- The DINOv2 feature description has a double period at line 43 ("point cloud..").
- "uwph teor et" appears to be garbled text at line 75, likely a parser artifact.

## Nice-to-Haves

- **Qualitative analysis.** A figure showing example predictions where semantic relations resolve ambiguity (e.g., two objects of the same class distinguished only by their relationship to a third object) would make the contribution more concrete.
- **Ablation on types of semantic relations.** A post-hoc analysis of which relations (e.g., "on", "near", "larger") contribute most would deepen understanding of what the edge features encode.
- **Training cost comparison.** Reporting training time and GPU memory relative to the zero-neighbor baseline would help practitioners assess the accuracy–resource trade-off.
- **Failure case discussion.** Characterizing scenes or queries where adding semantic edges does not help (e.g., very sparse scenes) would provide a more complete picture.

## Removed Points

- **"Table 2 not visible" criticism.** Both critiques about the SOTA claim that were rooted in Table 2 being unreadable in the extracted text are removed. The table exists in the original submission as a figure; the extraction format is a parser artifact, not an author error. The underlying concern about claim strength is retained as Minor #5 above, but demoted from "evidential" severity.
- **Criticism about missing comparison with specific recent methods (Chat3D-v2, Grounded 3D-LLM, LLA3D).** The reviewer speculated that Table 2 might not include these baselines. Since the table's contents cannot be inspected, this is speculative and removed.
- **Speculative claim that the 1 cm distance filter improvement "could easily be within variance."** This is a hypothetical scenario asserted without evidence. The concern about missing variance estimates is retained as Minor #2; the speculation about a specific result is removed.
- **Criticism about related work not clarifying the relationship between Chat3D-v2 and Chat-Scene.** These are cited as separate prior works; the paper is not required to explain relationships between external methods.
- **The "Significant increase in resource consumption" is mentioned by the paper itself as a limitation (line 141).** The reviewer's discussion of this as a weakness is duplicative of the paper's own acknowledged limitation.

## Novel Insights

The most instructive observation from the reviews is that the paper's own spatial-relation ablation (Table 5), which found no benefit from adding spatial coordinates, actually *strengthens* the core claim about semantic relations. If spatial information were driving the gains, adding explicit spatial tokens on top of semantic edges would improve results further — but it does not. This suggests the semantic edge features from VL-SAT may already encode spatial cues (e.g., "above," "next to") that subsume raw coordinate information, making the method's representation more efficient than alternatives that require both spatial and semantic processing. The reviews did not surface this interpretation, but it is a natural synthesis of the paper's null result.

## Suggestions

1. Clarify the baseline equivalence: either (a) add spatial relation tokens to 3DGraphLLM-0 to make it a true Chat-Scene replica, or (b) revise the text to say "adopts the same training pipeline and object representation as Chat-Scene, omitting spatial relation tokens" and note that Table 5 shows spatial tokens do not change the conclusions.

2. Add multi-seed variance estimates for the two or three most critical ablation comparisons (e.g., the 0-NN vs. 2-NN comparison in Table 3 for ScanRefer Acc@0.25).

3. Specify the aggregation method used for DINOv2 multi-view features and the per-stage epoch allocation for the two-stage training.

4. Tone down the SOTA claim in the conclusion to "competitive with state-of-the-art LLM-based methods" or "achieves strong results on popular benchmarks," consistent with the evidence presented.

5. Add at least one qualitative example (prediction visualization) showing where the graph representation corrects an error made by the zero-neighbor baseline.
