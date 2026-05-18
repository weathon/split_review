Now I have all the evidence needed. Let me produce the final consolidated review.

## Summary

This paper introduces SparseDFF, a framework for one-shot dexterous manipulation that constructs view-consistent 3D dense feature fields from sparse RGBD observations (4 fixed cameras). The method back-projects DINO features onto a point cloud, refines them with a lightweight per-point MLP trained via contrastive loss on a single demonstration, and applies point pruning for feature continuity. The resulting feature field is used to optimize a 24-DoF dexterous hand pose by minimizing feature discrepancies between demonstration and target scenes. Real-world experiments with a Shadow Dexterous Hand show strong cross-category generalization (e.g., 80% Bowl→Mug, 90% Bowl→BeerBarrel), significantly outperforming both a DFF baseline and the simulation-based UniDexGrasp++.

## Strengths

- **Sparse-view DFF removes the dense-view bottleneck for real-world dexterous manipulation.** Unlike prior NeRF-based DFF methods requiring dense camera sweeps (Shen et al., Rashid et al.), this method operates with only four fixed Azure Kinect sensors and achieves effective 24-DoF hand pose optimization. The approach back-projects DINO features from sparse RGBD views onto a point cloud and propagates them into a continuous field, making it practical for fixed-camera manipulation setups (Section 4, "Environment").

- **One-shot cross-category generalization validated in real-world experiments with strong quantitative results.** The method achieves high success rates on challenging transfers: 80% from Bowl to Mug, 90% from Bowl to BeerBarrel (Table 1), and 60% from Monkey to SmallBear (Table 2). These dramatically outperform the DFF baseline (0% on Bowl→Mug, 0% on Monkey→SmallBear) and the simulation-based UniDexGrasp++ (24.7% on Mug), demonstrating genuine category-level generalization from a single demonstration without any fine-tuning on target scenes.

- **Feature refinement network and point pruning mechanism demonstrably improve feature consistency.** The ablation visualizations (Figures 5 and 6) show that the contrastively trained per-point MLP and Hough-vote-style pruning produce more focused low-energy regions for hand optimization, addressing the core challenge of DINO feature inconsistency across sparse views. The refinement network trains in ~300 seconds on a single source scene and transfers zero-shot to target scenes (Section 4).

## Weaknesses

### Major

- **Ablation studies are purely qualitative, weakening support for the individual design choices.** The paper shows energy field visualizations and hand poses (Figures 5, 6) but does not report success rates for ablated versions. The DFF baseline in Tables 1 and 2 serves as a coarse ablation (no refinement, no pruning), but finer ablations are missing: (a) refinement only without pruning, (b) pruning only without refinement. Without success-rate tables for these conditions, the reader cannot assess whether both components are necessary or whether one dominates. Given the method's modest complexity, these ablations are straightforward to run, and their absence weakens the empirical justification for the two core design choices.

- **The "beyond grasping" results (head caressing, butt patting) lack any quantitative evaluation.** The paper presents these as evidence that the framework generalizes to non-grasping interactions, yet provides only two cropped figure panels (Fig. 7) with no success criteria, no trial counts, and no success rates. This is anecdotal evidence at best. Since the paper's title and abstract frame the contribution around "dexterous manipulations," the claim of generality beyond grasping would benefit from even minimal quantification. However, this is a secondary extension rather than a core contribution — the three enumerated contributions in the introduction do not specifically claim beyond-grasping results.

### Minor

- **The demonstration setup is manual (MeshLab positioning), creating a framing mismatch with the introduction's human-centric language.** The paper is transparent about this (Section 4: "a demonstration is set up within a virtual environment... by manually positioning a dexterous hand model... using MeshLab"), but the introduction uses language like "learning to hold a cat by watching someone do so" that implies a human-in-the-loop pipeline. The "one-shot" label is appropriate for the transfer (the network is trained on one source scene and applied zero-shot), but the demonstration acquisition itself is offline and manual. The paper would benefit from clarifying this distinction and discussing how the pipeline could be extended to teleoperated human demonstrations.

- **The comparison to UniDexGrasp++ is conducted under different conditions (simulation with perfect geometries vs. real-world noisy point clouds).** The paper acknowledges that UniDexGrasp++'s vision model is unstable with their noisy real-world point clouds and therefore evaluates its state-based model in simulation (Section 4, "Baselines"). This makes the comparison informative rather than directly competitive. The paper would be strengthened by quantifying the sim-to-real gap for UniDexGrasp++ under a controlled setting, or by more explicitly stating that this baseline is not a true real-world comparison.

- **Numerical values for the point-pruning radius \(r\) and threshold \(\delta\) are not specified.** These parameters are defined (Eq. 5) but never given numeric values or stated to be tuned per-scene vs. fixed. Without this information, the method is not fully reproducible, and the reader cannot assess the sensitivity of the pruning mechanism.

- **No failure analysis or discussion of failure modes.** The paper reports no common failure cases (e.g., occlusions, thin structures, objects with uniform appearance). A brief discussion of where and why the method fails would help readers understand its practical limitations.

### Trivial

- None beyond what is addressed in other sections.

## Nice-to-Haves

- A sensitivity analysis of the pruning parameters \(r\) and \(\delta\) would be useful but is not expected for a conference publication.
- A discussion of whether the contrastive learning's 1 cm correspondence threshold (used for positive pairs) creates false positives near occlusion boundaries or specular surfaces would add nuance but does not affect the paper's conclusions.
- A discussion of what limits the feature refinement network's generalization (e.g., extreme appearance gaps or rigid→deformable transfer) would be informative.

## Removed Points

- **Strength: "Versatility beyond grasping to diverse hand-object interactions"** — This strength conflicts with the verified weakness that the beyond-grasping results are purely qualitative and lack quantitative support. Per the rule that when a strength and weakness disagree, the weakness wins, this strength is removed.
- **Criticism about the contrastive learning 1 cm threshold producing false positives** — This is a standard implementation detail that does not constitute a real weakness; it is speculative without evidence of actual problems in the method's operation.
- **Formatting/style complaints and missing appendix references** — These are parser artifacts, not author errors.
- **Demands for additional tasks/domains beyond the paper's scope** — The paper focuses on grasping with a brief qualitative extension to other interactions; demanding full quantitative evaluation of non-grasping tasks at the same level as the core grasping experiments is scope creep.

## Novel Insights

The harsh critic's observation that the DFF baseline already serves as a coarse ablation (no refinement, no pruning) is useful: it means the core comparison is not as hollow as a pure qualitative ablation might suggest. The critic also correctly identifies that the strongest experimental contribution is the cross-category and cross-deformability generalization (Bowl→Mug at 80%, Monkey→SmallBear at 60%), which is genuinely impressive for a method trained on a single demonstration with no target-scene fine-tuning. The tension between the method's simplicity (per-point MLP + pruning) and the breadth of its generalization is the paper's most interesting aspect, and the reviews converge on the idea that this simplicity makes the missing ablations more, not less, noticeable.

## Suggestions

1. **Add success-rate tables for ablation variants** — run the rigid-object and deformable-object experiments with (a) refinement only without pruning, (b) pruning only without refinement, and (c) the full method. Report success rates alongside the existing DFF baseline. This is the single most impactful fix.
2. **For the beyond-grasping results, either add at least one quantitative experiment** (e.g., 10+ trials per scenario with a clear success criterion) **or explicitly scope the claim** to "qualitative demonstration" rather than general "dexterous manipulations."
3. **Specify the numeric values of \(r\) and \(\delta\)** used in the pruning mechanism, or clarify if they are tuned per scene.
4. **Add a brief failure analysis paragraph** discussing common failure modes observed during experiments.
5. **Adjust the introduction's framing** to distinguish between the (manual) virtual demonstration setup and the (automatic) one-shot transfer, to avoid misleading readers about the human-in-the-loop aspect.

## Score and Decision

**Originality:** Good — the combination of sparse-view DFF with contrastive refinement and point pruning for dexterous manipulation is novel relative to prior DFF work that required dense views or focused on gripper-only interactions.  
**Importance of research question:** High — one-shot dexterous manipulation with generalization to novel objects is a significant and practical problem in robotics.  
**Claims well supported:** Mostly — the core grasping claims are well-supported by real-world success rates with multiple baselines. The ablation and beyond-grasping claims are less well-supported (qualitative only).  
**Soundness:** The methodology is sound; the experiments are appropriate for a real-world robotics paper despite lacking some ablations.  
**Clarity:** The paper is clearly written and well-structured.  
**Value to community:** High — the method is practical, uses widely available sensors, and achieves strong results that could serve as a baseline for future work.

The paper makes a genuine contribution with real-world validation and compelling cross-category generalization results. The two significant weaknesses (qualitative ablations, qualitative beyond-grasping) do not invalidate the core grasping claims and are addressable in a revision. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>