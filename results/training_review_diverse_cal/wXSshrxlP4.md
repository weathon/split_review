Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper proposes GOPS, a two-stage pipeline for 3D instance segmentation from point clouds without scene-level human labels. In the first stage, an object-centric network learns generative object priors (via VAE or diffusion) and orientation estimation from single-object datasets like ShapeNet. In the second stage, a multi-object estimation network uses reinforcement learning with rewards from the frozen object-centric network to discover objects in scenes, producing pseudo masks that train a Mask3D-style segmentation branch. The method is evaluated on ScanNet, S3DIS (chair category), and a synthetic dataset with six object categories, outperforming existing unsupervised methods by substantial margins.

## Strengths

- **Novel two-stage pipeline decoupling object-prior learning from scene-level segmentation**: The paper introduces a clean design where generative object priors are first learned from single-object datasets, and then a separate multi-object network learns to discover objects in scenes by querying the frozen priors via RL — without any scene-level human labels. This is a principled departure from earlier heuristic-based approaches (e.g., EFEM). (Section 3.1–3.3)

- **Significantly outperforms state-of-the-art unsupervised methods on the evaluated setting**: On ScanNet chair evaluation, GOPS (VAE) achieves 38.8 AP@0.25 vs. EFEM's 6.8, Unscene3D's 3.9, and Part2Object's 1.3 (Table 1). On the hidden ScanNet test set, GOPS scores 20.9 AP@0.25 vs. EFEM's 1.7 (Table 2). Cross-dataset evaluation on S3DIS and the synthetic dataset show similar advantages (Tables 4 & 5).

- **Reinforcement learning formulation for object discovery using pretrained object-centric rewards**: The insight of treating object discovery as an RL problem where a dynamic container agent moves and resizes to find objects, receiving rewards based on Chamfer distance between cropped points and reconstructed shapes from the frozen generative prior, is a genuine technical novelty. This is a meaningful advance over EFEM's heuristic search. (Section 3.3, Figure 5)

- **Comprehensive ablation study validates each component**: The ablations (Table 6) show that replacing the generative prior with a deterministic autoencoder drops AP@0.25 from 38.8 to 10.2, removing the orientation module drops it to 17.0, and removing either the RL discovery or segmentation branches causes significant performance drops. This provides clear evidence that each module is necessary.

- **Multi-class capability demonstrated on synthetic data**: Despite real-world evaluation being limited to chairs, the synthetic dataset experiment (Section 4.3) shows that a single object-centric network trained on six ShapeNet categories can segment objects from all categories in synthetic rooms, achieving 61.1 AP@0.25 vs. 15.4 for EFEM (Table 5). This provides initial evidence for the method's cross-category potential.

- **Inference-time efficiency**: The RL-based discovery branch is discarded after training; inference only requires the backbone and the segmentation branch (following the efficient Mask3D architecture). This is a practical advantage over methods that require online search during testing.

## Weaknesses

### Fatal

None.

### Major

- **Real-world evaluation scope severely limits the claimed generality**: The paper's title, abstract, and introduction frame GOPS as a *general* approach to unsupervised 3D instance segmentation. Yet the real-world evaluation (ScanNet, S3DIS) is conducted exclusively on the chair category. The paper states this is "for fair comparisons with baselines" (Section 4.3), and the synthetic multi-class experiment provides supporting evidence. However, synthetic scenes with 4–8 cleanly placed objects from known ShapeNet categories do not substitute for real-world evaluation on additional categories (e.g., tables, sofas, beds) in cluttered scans with occlusions and domain shift. The claim that the method is "agnostic to any object categories" (line 171) is therefore plausible but unsubstantiated on real data. This gap between the breadth of the claims and the narrowness of the real-world evidence is the paper's most significant weakness.

### Minor

- **"Unsupervised" framing overstates the method's autonomy**: The paper uses "unsupervised" in the title and throughout, contrasting with methods that require "human labels of 3D scenes." While this is true at the scene level, the first stage trains on ShapeNet with full supervision (canonical poses, class labels, complete shapes). Methods like Unscene3D, which use only pretrained 2D features with no 3D object-level training, are unsupervised in a stronger sense. The paper should position itself more precisely — e.g., "using supervised object priors to enable unsupervised scene-level segmentation" — to avoid misleading readers about what supervision is required.

- **Cylinder container assumption is unexamined**: The RL agent's container is defined as a cylinder (xy-center and diameter, unconstrained height) "for simplicity" (line 75), but this geometric prior is not analyzed or ablated. Many real-world objects (tables, sofas, long cabinets, narrow floor lamps) do not fit a cylinder shape well. The paper does not study how this assumption affects which objects can be discovered, nor does it compare with alternative geometries (e.g., cuboid containers). Given that the entire RL discovery branch depends on this design choice, an ablation or analysis is needed.

- **RL training dynamics and computational cost are not discussed**: The paper does not report training curves, convergence behavior, or variance across runs for the RL-based discovery branch. The reward is binary (+10 or -1), which with sparse rewards and a complex action space raises stability concerns. Additionally, the method requires Marching Cubes at each RL step to compute Chamfer distance for the reward, and up to 600 trajectories per scene are used — yet runtime or computational complexity is never discussed. The paper mentions dividing scenes into smaller blocks for parallel exploration (line 114) but provides no quantitative efficiency analysis.

- **No discussion of pseudo-mask quality or error propagation**: The pipeline's segmentation branch is trained on pseudo labels generated by the RL discovery branch. The paper does not analyze the accuracy of these pseudo masks, nor how errors in pseudo labels propagate to the final segmentation performance. This is a missing analysis for a pipeline where the second stage's supervision depends entirely on the first stage's outputs.

- **Missing limitations section**: The conclusion (Section 5) implies the method is broadly effective without acknowledging its limitations (category-specific object-centric network, geometric assumptions on the container, computational cost of RL training, domain gap on the hidden test set, etc.). A dedicated discussion of limitations would strengthen the paper's scientific rigor.

### Trivial

- **Inconsistent citation**: The EFEM reference appears as both "Lei et al., 2023" (lines 25, 60, 131, 147) and "Lai et al., 2023" (lines 129, 149). The correct citation should be used consistently.

## Nice-to-Haves

- A quantitative analysis of pseudo-mask quality (e.g., precision/recall of RL-discovered masks against ground truth) would strengthen confidence in the pipeline.
- Reporting training curves and variance across multiple RL training runs would help assess the method's stability.
- A runtime comparison (e.g., seconds per scene for training and inference) against baselines would contextualize the computational cost.

## Removed Points

These points from the harsh critic are removed with justification:

1. **"Comparison with unsupervised baselines is fundamentally unfair"** — Removed as factually incorrect. The paper evaluates category-specific AP (chair) by filtering baselines' predictions to the chair class and comparing against GOPS's chair predictions. This is standard category-specific evaluation — non-chair predictions from baselines are irrelevant to chair AP. The criticism confuses category-specific evaluation with an unfair comparison protocol. The underlying concern (narrow scope) is already addressed in the Major weakness above.

2. **"Table 6 values are not legible"** — Removed as a parser artifact. The table exists in the original submission as an image; the textual description of results (lines 220–221) is verifiable and clearly describes the ablation findings.

3. **"The synthetic experiment does not approximate real clutter"** — While true that synthetic scenes are cleaner than real ones, this criticism is downgraded from the evaluation discussion. The synthetic experiment is explicitly presented as supporting evidence, not a replacement for real-world multi-class evaluation. The paper's framing is transparent about its purpose.

## Novel Insights

The reviews surface an interesting tension: the paper's strongest evidence of generality (the synthetic multi-class experiment, Table 5) comes from a setup where the object-centric network is trained on multiple categories simultaneously and evaluated on clean synthetic scenes. But in real-world settings, the paper trains per-category object-centric networks and evaluates only chairs. This raises a question the paper does not address: does the object-centric network trained on multiple categories generalize better or worse to real-world domain shift than a category-specific one? The synthetic experiment suggests the multi-category variant works well in clean conditions, but the real-world evaluation protocol (single category) provides no data on whether multi-category training would help or hurt on real scans. This gap between the two evaluation modes is worth exploring in future work.

## Suggestions

1. **Expand real-world evaluation to at least 2–3 additional categories** (e.g., tables, sofas) on ScanNet, training separate object-centric networks per category and aggregating results, to substantiate the generality claims.

2. **Add a class-agnostic evaluation** (treating all object instances equally) alongside the category-specific chair evaluation, so readers can assess overall scene segmentation quality rather than just per-category performance.

3. **Ablate the cylinder container assumption** by comparing with a cuboid container or a learned bounding box parameterization, and discuss failure cases of the cylinder geometry.

4. **Tone down the generality claims** in the title, abstract, and conclusion to match the real-world evidence, or explicitly acknowledge the category-specific limitation and the need for per-category object-centric networks.

5. **Report RL training curves and variance** (across at least 3 random seeds) to demonstrate training stability, and provide a brief runtime analysis.

6. **Add a limitations section** discussing the scope constraints (category-specificity, geometric assumption, domain gap, computational cost).

## Score and Decision

The paper presents a genuinely novel approach that marries generative object priors with RL-based discovery for unsupervised 3D instance segmentation. The core ideas are creative, the ablations are thorough, and the performance on the evaluated setting (chairs) is impressive. However, the paper's claims significantly outpace its real-world evidence: the method is positioned as a general unsupervised segmentation framework, but real-world experiments are limited to a single object category. The synthetic multi-class experiment is a step in the right direction but does not close this gap. These issues are addressable — the architecture itself is category-agnostic in principle — but as presented, the evaluation does not fully support the scope of the claims. The paper is borderline; revision with broader real-world evaluation could make it a strong contribution.

**Originality**: 7/10 — The two-stage pipeline with generative priors + RL discovery is novel.
**Quality**: 6/10 — Experiments are well-executed within their scope but the scope is too narrow.
**Clarity**: 7/10 — Well-written and well-structured.
**Significance**: 6/10 — The idea is important, but the paper does not yet demonstrate the impact it claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>