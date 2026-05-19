- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 8, 5, 6, 6
Here is my verified synthesis:

## Summary

This paper introduces SeTok, a dynamic vision tokenizer that groups patch-level visual features into a variable number of semantic-equivalent tokens via density-peak-based clustering, and builds Setokim, an MLLM that uses these tokens for unified understanding, generation, segmentation, and editing. The core idea — that vision tokens should correspond to semantic units rather than fixed patches — is well-motivated, and the paper demonstrates competitive or state-of-the-art results across multiple task families.

## Strengths

- **Dynamic token count adapts to image complexity and improves over fixed-token baselines.** Table 7 (tab:cluster-mechanism) shows that dynamic hard-clustering (avg. 25 tokens) outperforms all fixed token counts (8, 32, 64, 256) on Flickr30K (86.9 vs. ≤85.1) and OK-VQA (60.2 vs. ≤53.6), while using fewer TFLOPs (8.3 vs. 8.0–15.7). This provides a concrete quantitative advantage over prior fixed-token approaches.

- **Concept-level contrastive loss is empirically essential.** The ablation study (Table 6 / tab:ablation) shows that removing ℒ_{citc} causes dramatic degradation: VQA$^{v2}$ accuracy drops from 78.5→65.8, GQA from 65.6→49.7, and Flickr30K CIDEr from 86.9→78.1. This directly supports the claim that semantic alignment via this loss is central to the method's success.

- **Unified architecture achieves strong results across four task types.** Setokim is evaluated on understanding (Table 1: 89.1 POPE, 1537.8 MME, 45.2 MM-Vet), generation/editing (Table 4: best L1 on MagicBrush, MA5K, EVR), and segmentation (Table 5: best cIoU on RefCOCOg/+/Reaseg). Showing one tokenizer supporting all these tasks is a genuine contribution.

- **Interpretable token clusters align with semantic concepts.** Visualizations (Figure 10 / fig:visualTokens) show clusters corresponding to meaningful objects (giraffe, grass, tree, person, head, legs) and adapting granularity. This provides qualitative support for the semantic-equivalence claim.

- **Token merger components are ablated individually.** Table 6 isolates the contribution of positional encoding, inner-cluster Transformer, inter-cluster Transformer, and the merger itself, with each removal causing measurable degradation (e.g., rFID 2.07→6.25 without inner-cluster, 2.07→8.64 without merger).

## Weaknesses

### Fatal
None.

### Major

- **OK-VQA comparison is unfair due to training data exposure.** The paper marks OK-VQA with * (training data observed), and *only* Setokim has this mark on OK-VQA in Table 1. All baselines (Emu: 43.4, NExT-GPT: 52.1, LaVIT: 54.6) did *not* train on OK-VQA, so Setokim's reported 60.2 advantage is uninterpretable as a measure of the method's quality. The paper should retrain baselines on OK-VQA or remove this comparison. *(Note: this issue is limited to OK-VQA — the critic's broader claim that VQA$^{v2}$ and GQA results are invalidated is factually wrong, as Qwen-VL-Chat, LLaVA-1.5, and Unified-IO-2 also have asterisks on those benchmarks.)*

### Minor

- **Non-differentiability of hard clustering is not addressed.** The iterative density-peak clustering involves argmax operations (selecting the highest-score location) and iterative assignment, yet the paper never discusses how gradients flow through these non-differentiable steps. The soft-clustering variant (Table 7) achieves nearly identical performance (86.7 vs. 86.9 on Flickr30K), suggesting a relaxation could be used during training, but the paper does not state this. This is a methodological gap that should be clarified.

- **Stopping condition for clustering is underspecified.** Lines 99 and 121 refer to a "stopping condition" / "stopping criterion" without defining it. Since the token count (and thus model behavior) depends critically on this detail, reproducibility is harmed. The paper should specify the condition.

- **K for K-nearest neighbors in density computation is not specified.** Equation (1) uses KNN but never states the value of K or studies its sensitivity. This is a missing hyperparameter that affects clustering behavior.

- **Distance kernel uses C (final cluster count) in a way that could be circular.** The distance kernel φ(u, v) = exp(-‖u - v‖² · C·ln2) depends on C, the number of clusters, which is the *output* of the clustering process. If C is not known until after clustering completes, the kernel depends on the quantity it helps determine. The paper should clarify whether C is treated as the current running count during iteration or the final count.

- **Segmentation mask decoder training data is ambiguous.** Line 188 says the mask decoder is trained on "segmentation datasets, like MSCOCO." It is unclear whether this includes the referring expression datasets (RefCOCOg/+) used for evaluation, which would affect whether the comparison to LISA, PixelLM, etc. is apples-to-apples.

### Trivial
None.

## Nice-to-Haves

- A controlled experiment where SeTok is replaced with a fixed-grid tokenizer (same vision encoder, matched average token count, same data) to directly isolate the benefit of semantic grouping.
- A quantitative measure of token-cluster semantic consistency (e.g., mIoU against ground-truth object segments on COCO panoptic).
- A comparison of FLOPs or wall-clock time between SeTok and fixed-token baselines at inference to contextualize the reported TFLOPs savings.

## Removed Points

- **"Central experimental evidence invalidated" (for VQA$^{v2}$ and GQA):** Removed because it is factually incorrect. Table 1 shows Qwen-VL-Chat, LLaVA-1.5, and/or Unified-IO-2 also have asterisks on VQA$^{v2}$ and GQA, meaning those comparisons *are* controlled for training data overlap. The sweeping claim does not hold.
- **"Token merger is computationally expensive / large parameter count":** Removed because the 12/8 layer counts are standard for transformer-based aggregation and are clearly stated; the paper reports TFLOPs showing SeTok is competitive.
- **"Large-scale data mix — no ablation isolates SeTok effect":** Removed because Table 6 does ablate SeTok components while keeping the data mix fixed, which *does* isolate the effect.
- **"Fixed baseline poorly described" (Table 7):** Removed because the table and surrounding text ("When employing a fixed number of clusters") sufficiently clarify this.
- **Missing related works / missing appendix content / formatting nitpicks:** Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface a new perspective on the work that the paper itself does not already articulate.

## Suggestions

1. Specify the stopping condition for clustering and the K value for KNN explicitly in the methodology section.
2. Clarify how gradients are handled for the hard clustering (e.g., soft clustering during training with hard clusterization at inference, or a straight-through estimator).
3. Address the C·ln2 circular dependency in the distance kernel by stating whether C is the current running cluster count.
4. Either remove the OK-VQA comparison or re-evaluate under controlled training data conditions, or clearly caveat the result as incomparable.
5. Clarify whether the mask decoder was trained on RefCOCO datasets or only MSCOCO, and if the latter, add a note about it being zero-shot for referring segmentation.
