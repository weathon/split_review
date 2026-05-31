## Summary
This paper introduces CORE-3D, a training-free pipeline for open-vocabulary 3D scene understanding. It improves 2D mask generation by progressively combining multiple granularity levels from SemanticSAM, encodes each mask with a context-aware CLIP strategy (multiple crops with weighted averaging and negative subtraction of surroundings), and enforces multi-view consistency in 3D via a symmetric volumetric overlap criterion. The pipeline is extended to natural-language object retrieval by parsing queries with an LLM, mining candidates via CLIP similarity, verifying with a VLM, and reasoning over spatial relations. Experiments on Replica and ScanNet for semantic segmentation and on Sr3D+ for object retrieval show improvements over prior zero-shot and training-based methods.

## Strengths
- **Addresses an important and timely problem:** open-vocabulary 3D perception without 3D supervision is highly relevant for embodied AI and robotics.
- **Comprehensive pipeline with several technically sound components:** progressive granularity masks, multi-crop CLIP encoding with contrastive surroundings, and symmetric IoV merging are well-motivated and ablated.
- **Strong empirical results on multiple benchmarks:** the method achieves the best reported numbers on both segmentation (Replica, ScanNet) and retrieval (Sr3D+) among compared zero-shot approaches.
- **Ablation studies confirm the contribution of each major component:** tables 3-5 isolate the effect of granularity strategy, context-aware encoding, and extension mechanism.

## Weaknesses
### Fatal
- **The VLM and LLM models used for object retrieval are not specified.** The main text only states they are “accessed through external APIs” but never names the models (e.g., GPT-4, GPT-4V, Gemini, etc.). Since the retrieval pipeline relies critically on these components for parsing, verification, and reasoning, the reported results are not reproducible and the comparison to baselines is confounded by unknown model capability. This invalidates the central retrieval contribution.

### Major
- **The improvement in 3D semantic segmentation over the strongest zero-shot baseline (BBQ-CLIP) is modest.** On Replica, mIoU improves from 0.27 to 0.29; on ScanNet, from 0.34 to 0.36. The gains are incremental, and the method’s mAcc on Replica ties BBQ-CLIP at 0.38.
- **The method relies on several hand-tuned hyperparameters** (granularity thresholds, overlap thresholds τ_k, IoV thresholds γ and δ, CLIP crop weights, DBSCAN parameters, top-K retrieval, etc.). While ablation studies are provided, the sensitivity to these choices is not thoroughly analysed, and the “empirically tuned” weights raise concerns about generalizability to new scenes.

### Minor
- **Evaluation is conducted on a small subset of scenes** (8 per dataset for segmentation, 661 instructions for retrieval). While this follows prior work, the lack of larger-scale evaluation or error bars reduces confidence.
- **The retrieval pipeline is complex and uses multiple calls to external models** (LLM for parsing, VLM for verification and orientation, LLM for final reasoning). The computational cost and dependency on proprietary APIs are not discussed.

### Trivial
- The paper sometimes uses the term “training-free” but the method still requires access to pre-trained models (SemanticSAM, CLIP, VLM, LLM) and their inference. This is a minor terminology nuance.

## Nice-to-Haves
- Release the complete code and specify the exact versions of VLM/LLM (or provide open-source alternatives) to enable reproduction.
- Include confidence intervals or variance estimates for the segmentation results.
- Analyse the sensitivity of the retrieval accuracy to the choice of VLM/LLM.

## Novel Insights
None beyond the paper’s own contributions. The combination of progressive granularity masks and contextual CLIP encoding with a negative-surroundings term is a practical engineering contribution, but the core ideas (multi-crop, VLM verification, LLM reasoning) are already established in the literature. The symmetric IoV merging criterion is a useful heuristic but not theoretically novel.

## Suggestions
- **Immediately specify the VLM/LLM models used in the retrieval experiments.** Without this, the main claim of superior retrieval performance is not interpretable.
- Conduct a sensitivity analysis on the key hyperparameters, especially the CLIP crop weights and the overlap thresholds, to demonstrate robustness.
- Evaluate on the full ScanNet and Replica sets (or at least report statistical significance) to strengthen the segmentation claims.
- Consider replacing the proprietary VLM/LLM with open-weight models (e.g., LLaVA, Mistral) to improve reproducibility.

## Score and Decision
MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>